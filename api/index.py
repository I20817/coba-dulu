from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Halo! Python berhasil jalan di Vercel!</h1>"
