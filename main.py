import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def api_funcionando():

    #resultado = subprocess.run(['python', 'input.py'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    resultado = subprocess.run(['python', 'test.py'], capture_output=True, text=True)

    return f'API Running! {resultado}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')