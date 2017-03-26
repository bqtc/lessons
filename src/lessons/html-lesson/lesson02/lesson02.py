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
    template_options = {
        'page_title': 'Example page',
        'body_title': 'Best Example Ever',
        'body_paragraph': 'This is literally the best'
    }
    return render_template('lesson02_template.html', **template_options)

if __name__ ==  '__main__':
    app.run()
