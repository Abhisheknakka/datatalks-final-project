FROM python: 3.12-slim

WORKDIR /app

COPY dataset/main_faq_database.json
COPY ["Pipfile","Pipfile.lock","./"]