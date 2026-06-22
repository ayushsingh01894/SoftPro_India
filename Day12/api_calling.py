import os

#pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()
demo_key = os.getenv("MY_API")
if (demo_key):
    print("found",demo_key)
else:
    print("not found")

