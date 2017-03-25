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
        'body_description': 'This is literally the best',
        'page_header': 'Here we have a page that is all kinds of good',
        'paragraph_header_one': 'This is a cool paragraph',
        'paragraph_one': 'Look at all of this useful information!',
        'paragraph_header_two': 'This is also a cool paragraph',
        'paragraph_two': 'More useful information here.',
        'paragraph_header_three': 'This is clearly the best paragraph',
        'paragraph_three': 'The most useful information ever.',
        'info_one': 'Pictures here! Yay features!',
        'info_two': 'Refresh here! Yay more features!',
        'info_three': 'Clouds here! OMG clouds!',
        'info_four': 'HTML here! Meh.',
        'info_five': 'Computers here! Burn them all!',
        'closing_header': 'In conclusion, we win the internet',
        'closing_paragraph': 'All of this absurd stuff needs to be replaced by '
            'someone with real stuff to say. Go wild!'
    }
    return render_template('index.html', **template_options)

if __name__ ==  '__main__':
    app.run()
