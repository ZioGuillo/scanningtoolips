from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Set the template folder to "templates" in the current directory
app.template_folder = 'templates'

def is_root_directory_enabled(url):
    try:
        response = requests.get(url)
        if response.status_code // 100 == 2:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a')]
            return '/' in links  # Check if '/' (root directory) link is present
    except requests.exceptions.RequestException:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-headers')
def get_server_headers():
    url = request.args.get('url')

    try:
        response = requests.get(url)
        response_headers = dict(response.headers)
        return jsonify(response_headers), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/check-root-directory')
def check_root_directory():
    url = request.args.get('url')
    is_enabled = is_root_directory_enabled(url)

    if is_enabled:
        return "Root Directory is Enabled"
    else:
        return "Root Directory is Disabled"

if __name__ == '__main__':
    app.run()
