import g4f.client
from g4f.client import Client

gpt_client = Client()
def gpt3(prompt):
  try:
    response = gpt_client.chat.completions.create(model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': prompt}])
    return response.choices[0].message.content
  except Exception as e:
    return "Terjadi kesalahan: {}".format(e)

def gpt4(prompt):
  try:
    response = gpt_client.chat.completions.create(model='gpt-4-turbo', messages=[{'role': 'user', 'content': prompt}])
    return response.choices[0].message.content
  except Exception as e:
    return "Terjadi kesalahan: {}".format(e)

def gpt(model, prompt):
  try:
    response = gpt_client.chat.completions.create(model=model, messages=[{'role': 'user', 'content': prompt}])
    return response.choices[0].message.content
  except Exception as e:
    return "Terjadi kesalahan: {}".format(e)
