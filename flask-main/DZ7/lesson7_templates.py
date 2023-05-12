from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Jerry"
    fruit = "flask"
    x, y = 5, 6 
    template_context = {
        'name': name,
        'fruit': fruit,
        'x': x,
        'y': y
    }
    return render_template('const.html', **template_context)

@app.route('/html')
def index_html():
    return render_template('const.html')

if __name__ == "__main__":
    app.run(debug=True)
