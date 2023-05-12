from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name,surname,paytronomic, age, street = "Jerry", "Bobikov" ,"Andreevich",31,'Lenina'
    template_context = dict(name=name,surname = surname,paytronomic=paytronomic, age=age, street=street)
    return render_template('index.html', **template_context)

@app.route('/html')
def index_html():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)