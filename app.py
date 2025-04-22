from flask import Flask
import threading
import time
import requests

# Replitの .repl.co URL をここに！
REPLIT_URL = "https://yourusername.projectname.repl.co"

app = Flask(__name__)

@app.route('/')
def home():
    return "Render keep-alive server is running!"

# 5分おきにReplitにPingを送る処理
def ping_replit():
    while True:
        try:
            res = requests.get(REPLIT_URL)
            print(f"[PING] Replit status: {res.status_code}")
        except Exception as e:
            print(f"[ERROR] {e}")
        time.sleep(300)  # 5分ごとに実行

# 起動時にPingスレッドもスタート
if __name__ == '__main__':
    threading.Thread(target=ping_replit).start()
    app.run(host='0.0.0.0', port=10000)
