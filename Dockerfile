FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install uv

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

RUN mkdir -p /app/audio

EXPOSE 7860

CMD ["uv", "run", "clone-new.py"]