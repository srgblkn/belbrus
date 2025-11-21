FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt bot.py .env ./
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "bot.py"]