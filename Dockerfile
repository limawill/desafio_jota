FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download pt_core_news_sm 
COPY . .
COPY wait-for-it.sh .
RUN chmod +x wait-for-it.sh
RUN chmod +x entrypoint.sh
CMD ["./wait-for-it.sh", "db:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:5746"]