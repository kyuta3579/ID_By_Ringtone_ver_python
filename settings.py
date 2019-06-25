import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DIS_TOKEN = os.environ.get("DIS_TOKEN")
NOS_TEXT = os.environ.get("NOS_TEXT")
NOS_VOICE = os.environ.get("NOS_VOICE")
TNS_VOICE = os.environ.get("TNS_VOICE") # 環境変数の値をAPに代入