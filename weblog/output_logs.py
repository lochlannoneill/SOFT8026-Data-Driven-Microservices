from flask import Flask

import redis

app = Flask(__name__)

@app.route('/')
def print_logs():
    logs = []
    try:
        conn = redis.StrictRedis(host='redis', port=6379)
        for key in conn.scan_iter("log.*"):
            value = str(conn.get(key), 'utf-8')
            logs.append(value)
    except Exception as ex:
        logs.append('Error:' + str(ex))
    return '<br>'.join(logs)
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

