
from transformers import BertModel
from torch import nn
import torch
from Utils.Config.config import MODEL_NAME, DEVICE, BERT_PATH, FLAG



class SentimentClassifier(nn.Module):

    # Constructor class
    def __init__(self, n_classes = 5):
        super(SentimentClassifier, self).__init__()
        self.bert = BertModel.from_pretrained(MODEL_NAME)
        self.drop = nn.Dropout(p=0.3)
        self.out = nn.Linear(self.bert.config.hidden_size, n_classes)


    def forward(self, input_ids, attention_mask):
        _, pooled_output = self.bert(
          input_ids=input_ids,
          attention_mask=attention_mask,
          return_dict=False
        )
        #  Add a dropout layer
        output = self.drop(pooled_output)
        return self.out(output)
    




model_trained = SentimentClassifier()




if FLAG == 0:

    print("Cuda not available")
    model_trained.load_state_dict(torch.load(BERT_PATH,map_location=torch.device('cpu')))

else:

    print("Cuda available")
    model_trained.load_state_dict(torch.load(BERT_PATH))


model_trained = model_trained.to(DEVICE)