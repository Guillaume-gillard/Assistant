import requests
import json

#define the source of json file
API_KEY = "tFk6HLU6dTGt"
PROJECT_TOKEN = "tPiKwEOYxsL1"
RUN_TOKEN = "tApMbr8NMnTV"

class Data:
  def __init__(self, api_key, project_token):
    self.api_key = api_key
    self.project_token = project_token
    self.params = {
        "api_key": self.api_key
    }
    self.get_data()


  def get_data(self):
    response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={"api_key":API_KEY})
    self.data = json.loads(response.text)

  def get_day(self):
    data = self.data['Day']
    for content in data:      
      if content['name'] == "name":
        return content['name']
  
  def get_temperature(self):
    data = self.data['Day']
    for content in data:      
      if content['name'] == "temperature":
        return content['temperature']

  def get_precipitation(self):
    data = self.data['Day']
    for content in data:      
      if content['name'] == "Precipitation":
        return content['Precipitation']

def get_precipitation():
  text = ""
  for word in text:
    if word == "pleuvoir" or "pluie" or "faire beau":
      if word == "demain":
        print(data)