import g4f.client
from g4f.client import Client

gpt_client = Client()
def gpt3(prompt):
  try:
    response = gpt_client.chat.completions.create(model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': prompt}])
    if response.choices[0].message.content == "当前地区当日额度已消耗完, 请尝试更换网络环境":
        return "Maaf sedang terjadi kesalahan pada sistem ai kami, silakan coba lagi"
    else:
        return response.choices[0].message.content + "\n\n\n[Powered by OpenAI]"
  except Exception as e:
    return "Terjadi kesalahan: {}".format(e)

def gpt4(prompt):
  try:
    response = gpt_client.chat.completions.create(model='gpt-4-turbo', messages=[{'role': 'user', 'content': prompt}])
    return response.choices[0].message.content + "\n\n\n[Powered by OpenAI 4]"
  except Exception as e:
    return "Terjadi kesalahan: {}".format(e)

def gpt(model, prompt):
  try:
    response = gpt_client.chat.completions.create(model=model, messages=[{'role': 'user', 'content': prompt}])
    return response.choices[0].message.content + "\n\n\n[Powered by OpenAI]"
  except Exception as e:
    return "Terjadi kesalahan: {}".format(e)
