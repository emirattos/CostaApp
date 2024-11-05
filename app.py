from flask import Flask, render_template, request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    modified_html = ""
    if request.method == 'POST':
        html_content = request.form['html_content']
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Encuentra la imagen, el bold y el párrafo
        image = soup.find('img')
        bold_text = soup.find(['b', 'strong'])  # Busca tanto <b> como <strong>
        paragraph = soup.find('p')

        # Comprobar si se encontraron todos los elementos requeridos
        if image and bold_text and paragraph:
            # Construir el nuevo HTML
            modified_html = f'''
<div class="flex-content-blog">
    <div class="image-container">
        <img src="{image['src']}" alt="{image.get('alt', 'Descripción de la imagen')}">
    </div>
    <div class="text-container">
        <h2>{bold_text.text}</h2>
        <p>{paragraph.text}</p>
    </div>
</div>
            '''
        else:
            modified_html = "<p>No se encontraron todos los elementos requeridos. Asegúrate de incluir una imagen, un texto en negrita y un párrafo.</p>"

    return render_template('index.html', modified_html=modified_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
