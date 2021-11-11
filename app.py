from flask import Flask, render_template, url_for

app = Flask(__name__)

myself = '''Olá! Sou graduando em sistema de informação pela Unisales. Sou de vitória, ES. 
            Tenho paixão por aprender e adoro continuar sempre me aprimorando em todos meus desafios. 
            Gosto de música, corrida e jogos eletrônicos.'''

@app.route("/")
def index():
    return render_template("home.html", title="Home", myself=myself)

@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects")

@app.route("/experience")
def experience():
    return render_template("experience.html", title="Experience")

if __name__ == "__main__":
 app.run(debug=True)