from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>nico's Nextbots</h1><p>[play] [options] [custom bot] [patch notes].</p>"

if __name__ == '__main__':
    app.run(debug=True)
