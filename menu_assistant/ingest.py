import json
import os
import minsearch
from tqdm import tqdm
import config

# Setup project paths
base_folder = 'D:/Projects/AI-Restaurent-Chat-bot/'
input_data_folder = base_folder + 'dataset/'

def load_index(data_path=input_data_folder + "main_faq_database.json"):
    # Load the JSON file
    with open(data_path, 'r') as f:
        data = json.load(f)

    # Prepare documents for indexing
    documents = []
    
    # Iterate through the dataset to gather documents with dish names
    for dish in data['dishes']:
        dish_name = dish['dish name']  # Extract dish name from each dish
        for doc in dish['documents']:
            doc['dish_name'] = dish_name  # Add dish_name to each document
            documents.append(doc)  # Append modified document to the list

    # Initialize the search index
    index = minsearch.Index(
        text_fields=['id', 'question', 'section', 'text', 'dish_name'],
        keyword_fields=['dish_name']
    )

    # Fit the index with the prepared documents
    index.fit(documents)
    
    return index

# Example usage
if __name__ == "__main__":
    index = load_index()
    print("Index loaded successfully!")
