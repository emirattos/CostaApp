from flask import Flask, render_template, request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    modified_html = ""
    if request.method == 'POST':
        html_content = request.form['html_content']
        soup = BeautifulSoup(html_content, 'html.parser')
        for span in soup.find_all('span'):
            span.name = 'h1'
        modified_html = str(soup)
    
    return render_template('index.html', modified_html=modified_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
