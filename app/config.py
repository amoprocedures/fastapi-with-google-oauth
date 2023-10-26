import os
from dotenv import load_dotenv


load_dotenv()

CLIENT_ID = os.environ.get('client-id', None)
CLIENT_SECRET = os.environ.get('client-secret', None)
