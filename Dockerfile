FROM python: 3.12-slim

WORKDIR /app

RUN pip install pipenv

COPY dataset/main_faq_database.json
COPY ["Pipfile", "Pipfile.lock", "./"]

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pipenv install --deploy --ignore-pipfile --system

COPY menu_assistant .
# Expose port for Streamlit
EXPOSE 8501

# Run the streamlit app
CMD ["streamlit", "run", "menu_assistant/app.py"]
