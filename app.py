from urllib.parse import urlparse
from urllib.request import urlopen

from flask import abort, Flask, render_template, render_template_string, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def post_index():
    url = request.form['url']

    return render_template('index.html', result=get_url_content(url))


@app.errorhandler(500)
def internal_server_error(e):
    tmpl = 'Error: {{err}}'
    return render_template_string(tmpl, err=e.description), 500


def get_url_content(url: str) -> str:
    try:
        res = urlopen(url)
        return res.read().decode()
    except Exception as e:
        abort(500, description=e)


if __name__ == '__main__':
    app.run()