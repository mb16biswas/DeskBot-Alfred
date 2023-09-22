import torch 
MODEL_NAME = 'bert-base-cased'
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
FLAG = 1 if torch.cuda.is_available() else 0
RANDOM_SEED = 16
MAX_LEN = 50
CLASSES = ['Quary' , 'Email', 'Random' , 'Task' , 'Youtube'  ]
BERT_PATH =  "Bert_Finetuned_Model\Bert_model.pth"
GPT_PATH = "Gpt_2_Finetuned_Model"
CONVERSION_PROMPT = "Q&A\n"
CONVERSION_TOKEN = "Answer: "

