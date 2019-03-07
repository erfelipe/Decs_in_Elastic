
# python3.7 -m venv venv 
# source venv/bin/activate 
import flask
from flask import Flask
from flask import render_template
import controler
import json

app = Flask(__name__)

@app.route("/") 
def inicio(): 
    return render_template('index.html') 

@app.route("/pesquisa/")
def semPesquisa():
    return "Informe um termo para ser pesquisado."

@app.route("/pesquisa/<termo>/") 
def pesquisa(termo):  
    #encontra o termo em Es panhol
    termoEsp = "ofrecer"
    #encontra o termo em En glish
    termoEng = "meaning"
    
    res = controler.getDadosPeloDeCS(tBr=termo, tEs=termoEsp, tEn=termoEng) 
    return json.dumps(res)

if __name__ == "__main__":
    app.run(debug=True) 

#app.run(use_reloader=True)