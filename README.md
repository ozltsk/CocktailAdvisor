# Cocktail Recommender

This project is a **FastAPI-based web application** that allows users to search for cocktails by ingredients or save their favorite ingredients for later use. It leverages *SentenceTransformer* for semantic search and *FAISS* for efficient similarity search within a cocktail dataset.

## Features
- **Cocktail Search**: Enter ingredients or a question (e.g., "What can I make with vodka?") to get a list of matching cocktails.
- **Save Favorite Ingredients**: Input ingredients separated by commas (e.g., "vodka, lime") to store them as favorites.
- **Use Favorites**: Ask "cocktails with my favorites" to find cocktails based on saved ingredients.
- **Simple Interface**: One input field and one button for all interactions.

## Technologies
- **FastAPI**: Web framework for building the API.
- **SentenceTransformer ("all-MiniLM-L6-v2")**: Model for generating text embeddings for search.
- **FAISS**: Library for fast similarity search in vector space.
- **Pandas**: Data processing for cocktail dataset.
- **Jinja2**: HTML template rendering.
- **Python 3.8+**: Core programming language.

## Project Structure
```
cocktail-recommender/
├── app/
│   └── main.py          # Main FastAPI application logic
├── templates/
│   └── index.html       # HTML interface with single input and button
├── data/
│   └── final_cocktails.csv  # CSV file with cocktail data (name, ingredients)
├── requirements.txt     # Project dependencies
└── README.md            # This file
```

## Install Dependencies:
```
pip install -r requirements.txt
```

## Ensure Data Availability:
Place the **data/final_cocktails.csv** file in the data/ directory.
Expected format: columns name (string) and ingredients (string formatted as a list, e.g., ['vodka', 'lime']).

## Running the Application
```
python -m app.main
```
## Open in Browser:
Navigate to
```
http://localhost:8000
```
## Do not forget to set the correct port to run the application in the main file
