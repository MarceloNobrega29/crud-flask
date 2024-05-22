from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")

def ola_mundo():
    titulo = "Gestão de Usúarios"
    usuarios = [
        {"nome": "Guilherme", "membro_ativo": True},
        {"nome": "Gabriel", "membro_ativo": False},
        {"nome": "joão", "membro_ativo": False},
    ] 
    
    return render_template ("index.html", titulo=titulo, usuarios=usuarios)

@app.route("/menu")
def pagina_menu():
    return """""
        <b>OlaMundo</b>: link do video
        <a href="https://www.youtube.com/watch?v=fkXlSyWiXVg">Canal no yt</a>
    """
        
app.run(debug=True)

