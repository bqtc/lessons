from flask import Flask, render_template
app = Flask(__name__)

@app.route('/assets/<path:filename>')
def assets(filename):
    return app.send_static_file('assets/' + filename)

@app.route('/images/<path:filename>')
def images(filename):
    return app.send_static_file('images/' + filename)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ ==  '__main__':
    app.run()
