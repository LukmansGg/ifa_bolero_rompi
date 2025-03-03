import g4f.client
from g4f.client import Client

gpt_client = Client()
def gpt3(prompt):
  try:
    response = gpt_client.chat.completions.create(model='gpt-4o-mini', messages=[{'role': 'user', 'content': prompt + " jelaskan dengan menarik, santai, seru dan sistematis disertai emote"}])
    if response.choices[0].message.content == "当前地区当日额度已消耗完, 请尝试更换网络环境":
        return "Maaf sedang terjadi kesalahan pada sistem ai kami, silakan coba lagi"
    else:
        return response.choices[0].message.content + "\n\n\n[Powered by OpenAI]"
  except Exception as e:
    return "Terjadi kesalahan: {}".format(e)

def gpt4(prompt):
  try:
    response = gpt_client.chat.completions.create(model='gpt-4', messages=[{'role': 'user', 'content': prompt + " jelaskan dengan menarik, santai, seru dan sistematis disertai emote"}])
    return response.choices[0].message.content + "\n\n\n[Powered by OpenAI 4]"
  except Exception as e:
    return "Terjadi kesalahan: {}".format(e)

def gpt(model, prompt):
  try:
    response = gpt_client.chat.completions.create(model='gpt-4o-mini', messages=[{'role': 'user', 'content': prompt + " jelaskan dengan menarik, santai, seru dan sistematis disertai emote"}])
    return response.choices[0].message.content + "\n\n\n[Powered by OpenAI]"
  except Exception as e:
    return "Terjadi kesalahan: {}".format(e)
