import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

env_type = os.getenv("ENVIRONMENT")
crypto_key = os.getenv("SECRET_KEY").encode("utf-8")
to_emails = os.getenv("TO_EMAIL")
