from flask import Flask, render_template, request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    modified_html = ""
    if request.method == 'POST':
        html_content = request.form['html_content']
        soup = BeautifulSoup(html_content, 'html.parser')

        # Buscar la imagen, bold y párrafo
        images = soup.find_all('img')
        bolds = soup.find_all('b')  # También puedes usar 'strong' si es el caso
        paragraphs = soup.find_all('p')

        if images and bolds and paragraphs:
            # Crear el nuevo contenedor
            flex_content_blog = soup.new_tag('div', **{'class': 'flex-content-blog'})
            # Primer div para la imagen
            image_div = soup.new_tag('div')
            image_div.append(images[0])  # Solo toma la primera imagen
            flex_content_blog.append(image_div)

            # Segundo div para el bold convertido a h2 y el párrafo
            text_div = soup.new_tag('div')
            if bolds:
                h2 = soup.new_tag('h2')
                h2.string = bolds[0].string  # Convertir el primer bold a h2
                text_div.append(h2)

            if paragraphs:
                text_div.append(paragraphs[0])  # Agregar el primer párrafo

            flex_content_blog.append(text_div)

            # Convertir a string
            modified_html = str(flex_content_blog)
    
    return render_template('index.html', modified_html=modified_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

