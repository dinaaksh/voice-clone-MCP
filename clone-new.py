import threading
import asyncio
from mcp.server.fastmcp import FastMCP
import inference
import logging
import os

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

from dotenv import load_dotenv
load_dotenv()
os.environ["COQUI_TOS_AGREED"]="1"

PORT=int(os.environ.get("PORT",7860))
mcp=FastMCP("clone", host="0.0.0.0", port=PORT)

@mcp.tool("clone_voice")
async def speaker_clone(text: str,speaker_wav: str)->str:
    """Get a voice clone of a text.
    Args:
        text: The text to clone
        speaker_wav: The wav file of the speaker
    
    Returns:
        str: The path to the cloned voice
    """
    return await inference.get_voice_clone(text,speaker_wav)

@mcp.tool("ping")
async def test() -> str:
    """Get a ping.
    
    Returns:
        str: responds with a ping
    """
    return "pong"

def model_initalization():
    def run():
        asyncio.run(inference.load_model_async())
    thread=threading.Thread(target=run,daemon=True)
    thread.start()

if __name__=="__main__":
    logger.info(f"Starting MCP server on 0.0.0.0:{PORT}")
    model_initalization()
    mcp.run(transport='streamable-http')