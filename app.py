import sys
from flask import Flask, request

sys.path.append('programs')

sys.path.append('bot_analytics')
import bot_analytics.operator

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, welcome to my Flask app!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

# Loop pemblokiran untuk menjaga kode tetap berjalan
while True:
    pass
  
