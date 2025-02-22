**Cocktail Advisor**
This project is a FastAPI-based web application that allows users to search for cocktails by ingredients or save their favorite ingredients for later use. 
It uses the SentenceTransformer model for semantic search and FAISS to efficiently find similar cocktails in the database.

**Technologies**
FastAPI: A web framework for creating APIs.
SentenceTransformer (“all-MiniLM-L6-v2”): A model for creating textual embeddings for search.
FAISS: A library for fast similarity search in vector space.
Pandas: Processing of cocktail data.
Jinja2: HTML template rendering.
Python 3.8+: The main programming language.

**Project structure**
cocktail-advisor/
├── app/
│ └── main.py # Main file with FastAPI logic
├── templates/
│ └── index.html # HTML interface with one input field and a button
├── data/ │ └── final.html
│ └── final_cocktails.csv # CSV file with data about cocktails (name, ingredients)
├── requirements.txt # File with project dependencies
└── README.md # This file

**Set the dependencies from requirements.txt:**
pip install -r requirements.txt
