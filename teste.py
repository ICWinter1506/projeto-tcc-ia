import os
from dotenv import load_dotenv
import ollama

load_dotenv() # Carrega o IP do arquivo .env
client = ollama.Client(host=os.getenv('OLLAMA_HOST'))