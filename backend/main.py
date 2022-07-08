from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
import tensorflow as tf 
import numpy as np 
import os 
from pydantic import BaseModel
from transformers import BartTokenizer, BartForConditionalGeneration

tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

app = FastAPI()

class input_model(BaseModel) : 
    data : str

origins =  ['http://localhost:3000']
app.add_middleware(
    CORSMiddleware , 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)



@app.post('/predict/') 
def predict(data :dict) : 
    input = dict(data)
    article = input['text']
    inputs = tokenizer([article], max_length=1024, return_tensors="pt")
    summary_ids = model.generate(inputs["input_ids"], num_beams=2, min_length=0, max_length=20)
    return tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
