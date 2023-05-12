from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name, age, profession = "Jerry",31,'Programmist'
    template_context = dict(name=name, age=age, profession = profession)
    return render_template('index.html', **template_context)



if __name__ == "__main__":
    app.run(debug=True)