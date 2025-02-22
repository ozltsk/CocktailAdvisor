import ast
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import faiss
from transformers import pipeline

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class UserInput(BaseModel):
    text: str

class State:
    def __init__(self):
        self.cocktails = None
        self.model = None
        self.index = None
        self.user_favorites = []
        self.chatbot = None

    def initialize(self):
        self.cocktails = pd.read_csv("data/final_cocktails.csv")[["name", "ingredients"]]
        self.cocktails["ingredients"] = self.cocktails["ingredients"].apply(
            lambda x: ", ".join(ast.literal_eval(x)) if isinstance(x, str) else x
        )
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        cocktail_texts = self.cocktails["name"] + " - " + self.cocktails["ingredients"]
        embeddings = self.model.encode(cocktail_texts.tolist(), convert_to_tensor=True)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings.cpu().numpy())
        self.chatbot = pipeline("text-generation", model="gpt2")  # Додаємо GPT-2
        print("Дані та LLM завантажено успішно")

state = State()

@app.on_event("startup")
async def startup_event():
    state.initialize()

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

def search_cocktail(query: str, top_k=5):
    query_embedding = state.model.encode([query], convert_to_tensor=True)
    _, indices = state.index.search(query_embedding.cpu().numpy(), top_k)
    return state.cocktails.iloc[indices[0]].to_dict(orient="records")

@app.post("/submit/")
def submit(input: UserInput):
    text = input.text.lower()

    if "," in text and "what" not in text and "?" not in text:
        state.user_favorites = [i.strip() for i in text.split(",")]
        return {"response": f"Улюблені інгредієнти збережено: {', '.join(state.user_favorites)}"}

    query = text
    if "favorite" in text and state.user_favorites:
        query = " ".join(state.user_favorites)

    cocktails = search_cocktail(query)
    if not cocktails:
        return {"response": "Недостатньо даних для рекомендації коктейлю."}

    # Формуємо контекст для LLM
    context = "\n".join([f"{c['name']} - {c['ingredients']}" for c in cocktails[:5]])
    prompt = (
        f"List these cocktails with their ingredients:\n{context}\n"
        f"Format: 1. Name - Ingredients\n2. Name - Ingredients\n..."
    )
    response = state.chatbot(prompt, max_new_tokens=100, do_sample=False)[0]["generated_text"]
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)