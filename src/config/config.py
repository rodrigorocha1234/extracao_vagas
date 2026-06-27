import os
from typing import Final

from dotenv import load_dotenv
load_dotenv()

class Config:
    TOKEN_TELEGRAM: Final[str] = os.environ["TOKEN_TELEGRAM"]
    CHAT_ID_TELEGRAM: Final[str] = os.environ["CHAT_ID_TELEGRAM"]

