from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    "Mais de 50% das pessoas sentem ansiedade quando ficam longe do celular.",
    "O uso excessivo de telas antes de dormir reduz a produção de melatonina.",
    "Checar o celular constantemente ativa o sistema de recompensa e dopamina no cérebro.",
    "Pausas curtas a cada 45 minutos ajudam a reduzir a fadiga visual e o estresse digital."
]

@app.route("/")
def home():
    return '''
        <h1>Bem-vindo ao ConscientizaTech!</h1>
        <p>Este site foi criado para conscientizar sobre os impactos do uso exagerado da tecnologia no nosso dia a dia.</p>
        <p><a href="/random_fact">Clique aqui para ver um fato aleatório sobre dependência digital!</a></p>
    '''

@app.route("/random_fact")
def random_fact():
    fato = random.choice(facts_list)
    return f'''
        <h2>Fato sobre Dependência Tecnológica</h2>
        <p><strong>{fato}</strong></p>
        <hr>
        <p><a href="/random_fact">Recarregar página (Gerar outro fato)</a></p>
        <p><a href="/">Voltar para a Página Inicial</a></p>
    '''

@app.route("/secret")
def secret():
    resultado = random.choice(["Cara 🪙", "Coroa 👑"])
    return f"""
        <h1>Página Secreta! 🤫</h1>
        <p>Resultado do Cara ou Coroa:</p>
        <h2>{resultado}</h2>
        <br>
        <a href="/secret">Tentar novamente</a> | <a href="/">Voltar ao início</a>
    """

if __name__ == "__main__":
    app.run(debug=True)