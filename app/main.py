from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/consultar', methods=['POST'])
def consultar():
    tipo_documento = request.form['tipo_documento']
    dni = request.form['dni']
    # Llamar a la función de scraping desde api.web_scraper
    #datos = obtener_datos(tipo_documento, dni)
    # return render_template('resultados.html', datos=datos)
    return render_template('resultados.html')


if __name__ == '__main__':
    app.run(debug=True)
