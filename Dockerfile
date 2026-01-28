FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
COPY .env .  # Ensure .env is copied if needed
CMD ["python", "main.py"]
