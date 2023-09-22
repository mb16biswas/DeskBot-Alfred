from transformers import   GPT2Tokenizer, pipeline, GPT2LMHeadModel
from Utils.Config.config import GPT_PATH

loaded_model = GPT2LMHeadModel.from_pretrained(GPT_PATH)


tokenizer_gpt = GPT2Tokenizer.from_pretrained('gpt2')

tokenizer_gpt.pad_token = tokenizer_gpt.eos_token

generator = pipeline('text-generation', model=loaded_model, tokenizer=tokenizer_gpt )