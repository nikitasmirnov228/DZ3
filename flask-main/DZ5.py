from flask import Flask, make_response

app = Flask(__name__)
#заголовок
@app.route('/')
def render_markdown():
    response = make_response("## Heading")
    response.status_code = 200
    response.headers['Content-Type'] = 'text/markdown'
    return response
#возвращение ошибки 404 с помощью make_response
@app.route('/error404')
def http_404_handler():
    response = make_response("404 Error")
    response.status_code = 404
    return response
#Функция представления вернет ошибку HTTP 500 Internal Server Error.
@app.route('/error500')
def http_500_handler():
    response = make_response("500 Error")
    response.status_code = 500
    return response

@app.route('/books/<genre>/')
def books(genre):
    response = make_response("All Books in {} category".format(genre))
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Server'] = 'Foobar'
    return response

@app.route('/set-cookie')
def set_cookie():
    response = make_response("Cookie setter")
    response.set_cookie("favorite-color", "skyblue", max_age=60*60*24*15)
    response.set_cookie("favorite-font", "sans-serif", max_age=60*60*24*15)
    return response

@app.route('/transfer')
def transfer():
    return "", 302, {'location': 'https://localhost:5000/login'}

if __name__ == '__main__':
    app.run(debug=True)
