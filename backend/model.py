import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import json

class ChatModel():
  def __init__(self):
      self.initialize()

  def initialize(self, ):
      from sentence_transformers import SentenceTransformer
      self.model = SentenceTransformer('jhgan/ko-sroberta-multitask')
		
      self.file_name = "wellness_dataset.csv" #your data file name
      self.df = pd.read_csv(self.file_name)
      self.df['embedding'] = self.df['embedding'].apply(json.loads)

  def get_answer(self, user_input):
      similarity_arr = []
      embedding = self.model.encode(user_input)
      similarity_arr = self.df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
      answer = self.df.loc[similarity_arr.idxmax()] 
      return answer['chatbot']