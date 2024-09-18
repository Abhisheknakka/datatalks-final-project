import streamlit as st
import time
from dotenv import load_dotenv
import os
import openai  # Fix the import statement
from groq import Groq
import minsearch
import json

# Load environment variables
load_dotenv()

# Setup the OpenAI client to use either Groq, OpenAI.com, or Ollama API
API_HOST = os.getenv("API_HOST")

if API_HOST == "groq":
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    MODEL_NAME = os.getenv("GROQ_MODEL")
elif API_HOST == "ollama":
    client = openai.OpenAI(
        base_url=os.getenv("OLLAMA_ENDPOINT"),
        api_key="nokeyneeded",
    )
    MODEL_NAME = os.getenv("OLLAMA_MODEL")
elif API_HOST == "github":
    client = openai.OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.getenv("GITHUB_TOKEN")
    )
    MODEL_NAME = os.getenv("GITHUB_MODEL")
else:
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    MODEL_NAME = os.getenv("OPENAI_MODEL")

# Load dataset
base_folder = 'D:/Projects/AI-Restaurent-Chat-bot/'
input_data_folder = base_folder + 'dataset/'

with open(input_data_folder + 'main_faq_database.json', 'rt') as f_in:
    data = json.load(f_in)

# Prepare documents for search index
documents = []
for dish in data['dishes']:
    dish_name = dish['dish name']
    for doc in dish['documents']:
        doc['dish_name'] = dish_name  # Add dish_name to each document
        documents.append(doc)

# Initialize the search index
index = minsearch.Index(
    text_fields=['id', 'question', 'section', 'text', 'dish_name'],
    keyword_fields=['dish_name']
)
index.fit(documents)

# Search function using minsearch
def minsearch(query):
    return index.search(query)

# Prompt building function
def build_prompt(query, search_results):
    prompt_template = """
    You are a highly trained professional and helpful assistant that answers questions about food based off a menu dataset.
    You must use the dataset to answer the questions, you should not provide any info that is not in the provided sources.
    Answer the questions which user asks based on the CONTEXT.
    QUESTION :{question}
    CONTEXT : {context}
    """.strip()
    
    # Create context from search results
    context = ""
    for doc in search_results:
        context += f"section: {doc['section']}\nquestion: {doc['question']}\nanswer: {doc['text']}\n\n"
    
    prompt = prompt_template.format(question=query, context=context).strip()
    return prompt

# Function to interact with LLM
def llm(prompt):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# RAG function
def rag(query):
    # Get search results
    search_results = minsearch(query)
    
    # Check if search results are valid
    if not search_results:
        return "I couldn't find any relevant information in the dataset."

    # Build prompt based on search results
    prompt = build_prompt(query, search_results)
    
    # Get answer from LLM
    answer = llm(prompt)
    return answer

# Main app function
def main():
    st.title("Jack's Chat Application")
    user_input = st.text_input("Chatbot is ready to help with the menu. Ask your questions:")

    if st.button("Ask"):
        with st.spinner('Processing...'):
            output = rag(user_input)
            st.success("Completed!")
            st.write(output)

if __name__ == "__main__":
    main()

