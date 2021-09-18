#Para executar este scrip, digitar o comando "py run.py" no terminal do mesmo, e abrir o endereço " http://127.0.0.1:5000/ " no navegador google chrome.
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from src.triangulo import defineFormato, imagemDoFormato

app = Flask(__name__, template_folder='./templates')

@app.route('/', methods=["GET"])
def renderizaTemplate():
    return render_template('template.html')


@app.route('/', methods=["POST"])
def trataDoTriangulo():
    lado1 = float(request.form.get('vertice-1'))
    lado2 = float(request.form.get('vertice-2'))
    lado3 = float(request.form.get('vertice-3'))
    
    formato = defineFormato(lado1, lado2, lado3)

    if formato == 'Não é um triângulo':
        return render_template('template.html', exibe="erro")
    else:
        return render_template(
            'template.html',
            exibe="triangulo",
            formato=formato,
            formatoUrl=imagemDoFormato(formato),
            vertice1=lado1,
            vertice2=lado2,
            vertice3=lado3
        )


if __name__ == '__main__':
    app.run(debug=True)
