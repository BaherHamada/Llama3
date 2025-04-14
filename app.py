import os
from transformers import AutoTokenizer, AutoModelForCausalLM

token = os.getenv("HUGGINGFACE_TOKEN")
model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=token)
model = AutoModelForCausalLM.from_pretrained(model_id, use_auth_token=token)
