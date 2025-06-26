FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV HF_HOME=/home/user/huggingface
ENV NUMBA_CACHE_DIR=/home/user/numba_cache

RUN mkdir -p /home/user/huggingface /home/user/numba_cache && chmod -R 777 /home/user/huggingface /home/user/numba_cache

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

RUN mkdir -p /app/audio

EXPOSE 7860

CMD ["python", "clone-new.py"]