from flask import Flask
import subprocess
import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    username = subprocess.getoutput('whoami')
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    top_output = subprocess.getoutput('top -b -n 1')

    response = f"""Name: Rani
user: {username}
Server Time (IST): {server_time}
TOP output:
{top_output}"""
    
    return response, 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)