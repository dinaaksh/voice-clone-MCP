FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app


COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

RUN mkdir -p /app/audio

EXPOSE 7860

CMD ["python", "clone-new.py"]