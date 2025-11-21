FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt bot.py ./
RUN pip install -r requirements.txt
# ENV TOKEN='ВРОДЕ БЫ НАДО УБИРАТЬ ТОКЕН'
ENTRYPOINT ["python", "bot.py"]