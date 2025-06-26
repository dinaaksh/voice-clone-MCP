import asyncio
import os
import logging
from dotenv import load_dotenv
load_dotenv()
os.environ['TTS_CACHE_DIR'] = '/home/user/tts_cache'

tts=None
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

async def load_model_async():
    global tts
    def load():
        from TTS.api import TTS
        return TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC",gpu=False)
    
    logger.info("Loading TTS model asynchronously...")
    tts=await asyncio.to_thread(load)
    logger.info("Model loaded successfully")

async def get_voice_clone(text: str, speaker_wav: str)->str:
    if tts is None:
        return "Model not loaded yet, please wait."

    if not os.path.isfile(speaker_wav):
        return f"Error: Speaker file '{speaker_wav}' not found."

    # output_path="output.wav"
    output_path="/app/audio/output.wav"

    def synthesize():
        tts.tts_to_file(
            text=text,
            file_path=output_path,
            speaker_wav=[speaker_wav],
            language="en",
            split_sentences=False
        )

    try:
        await asyncio.to_thread(synthesize)
        return f"Audio saved at: {output_path}"
    except Exception as e:
        return f"Error: {e}"