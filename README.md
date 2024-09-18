# Restaurant Chatbot Project

## Description

This repository contains the code for a Streamlit-based application that acts as a chatbot for restaurant inquiries. This chatbot leverages a Retrieval Augmented Generation (RAG) framework with a comprehensive knowledge base about restaurant menus, allowing it to provide helpful and informative responses to user questions. This chatbot was developed as part of a project for the LLM Zoomcamp course.

## Features

- **Natural Language Interaction**: Communicate with the chatbot in natural language, asking questions about the restaurant menu, dishes, ingredients, and more.
- **Comprehensive Knowledge Base**: The chatbot's knowledge base covers a wide range of menu items and dish details.
- **Streamlit UI**: An intuitive and user-friendly Streamlit interface provides an interactive chat experience.
- **RAG-Powered**: The chatbot utilizes the power of Retrieval Augmented Generation to provide relevant and accurate information tailored to user queries.

## Dataset

In this project, we used the following dataset:
- **Restaurant Menu Dataset**: Available in the `dataset` folder as `main_faq_database.json`.

## Data Ingestion

Before running the application, you need to perform data ingestion. Run the Python script `menu_assistant/data_ingestion.py` to load the data into the knowledge base.

```bash
cd datatalks-final-project/menu_assistant
python data_ingestion.py
```

## How to Use
Initialize the Streamlit application

```bash
cd datatalks-final-project/menu_assistant
streamlit run app.py
```


## Disclaimer
This chatbot is for informational purposes only and was created as a project for the LLM Zoomcamp course. The first draft has been submitted, and further work including dashboard and database integration will be completed before the next attempt.