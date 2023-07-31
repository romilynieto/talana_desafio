FROM python:3

WORKDIR /app

COPY main.py /app
COPY requirements.txt /app
COPY common /app/common
COPY player /app/player
COPY game /app/game

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]