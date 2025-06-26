FROM python:3.11-slim

RUN useradd -m user

ENV PYTHONUNBUFFERED=1
ENV HF_HOME=/home/user/huggingface
ENV NUMBA_CACHE_DIR=/home/user/numba_cache
ENV TTS_CACHE_DIR=/home/user/tts_cache
ENV MPLCONFIGDIR=/home/user/.config/matplotlib

RUN mkdir -p /home/user/huggingface /home/user/numba_cache /home/user/.local/share/tts /home/user/.config/matplotlib /app/audio && \
    chown -R user:user /home/user && \
    chmod -R 777 /home/user /app/audio

USER user

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

RUN mkdir -p /app/audio

EXPOSE 7860

CMD ["python", "clone-new.py"]