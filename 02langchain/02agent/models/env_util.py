import os
from dotenv import load_dotenv

#
load_dotenv(override=True)

ALI_API_KEY = os.getenv("ALI_API_KEY")
ALI_BASE_URL = os.getenv("ALI_BASE_URL")

ALI_API_OPENAI_KEY = os.getenv("ALI_API_OPENAI_KEY")
ALI_ANTHROPIC_URL = os.getenv("ALI_ANTHROPIC_URL")

