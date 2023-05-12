from flask import Flask,  redirect, url_for
app = Flask(__name__)
@app.route('/')
def index():
    return redirect(url_for('hello'))
@app.route("/flask8job")
def hello():
    return 'Flask 8 job - completed'
@app.route('/user/<user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)
@app.route('/books/<genre>/')
def books(genre):
    return "All Books in{} category.format(genre)"
if __name__ =='__main__':
    app.run(debug=True)