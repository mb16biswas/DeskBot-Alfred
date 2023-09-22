from transformers import  BertTokenizer
import torch
from Utils.Config.config import MODEL_NAME, DEVICE, CLASSES, CONVERSION_PROMPT, CONVERSION_TOKEN, FLAG
from Utils.models.gpt2 import generator, tokenizer_gpt
from Utils.models.bert import model_trained




tokenizer_bert_ = BertTokenizer.from_pretrained(MODEL_NAME)

def process_text_bert(s):

    return  tokenizer_bert_.encode_plus(
        s,
        add_special_tokens=True,
        max_length= 50,
        return_token_type_ids=False,
        pad_to_max_length=True,
        return_attention_mask=True,
        return_tensors='pt',
    )


def pred_bert(encoding):

    model_trained_ = model_trained.eval()

    with torch.no_grad():

        input_ids = encoding["input_ids"].to(DEVICE)
        attention_mask = encoding["attention_mask"].to(DEVICE)
        # targets = encoding["intend"].to(device)

        # Get model ouptuts
        outputs = model_trained_(
            input_ids=input_ids,
            attention_mask=attention_mask
        )

        _, preds = torch.max(outputs, dim=1)

        if(FLAG == 0):

            preds_cpu = preds.cpu()

            return CLASSES[preds_cpu]

        else:

            return CLASSES[preds]





def process_text_gpt(t):

    return f'{CONVERSION_PROMPT}Question: {t}\n{CONVERSION_TOKEN}'

def pred_gpt(text):

    res = generator(
        text, temperature=0.5,
        max_length=len(tokenizer_gpt.encode(text)) + 30
    )[0]['generated_text']

    ans_ = res.split("\n")[2][9:] + " . . . "

    return ans_