import os  
from dotenv import load_dotenv 

# Load environment variables from .env file  
load_dotenv()  

az_client_id = os.getenv("AZURE_CLIENT_ID")
if not az_client_id:  
    raise EnvironmentError("STORAGE_ACCOUNT_BLOB_URL environment variable is not set.")  

print(f"The azure client id being used for auth is: {az_client_id}")  
