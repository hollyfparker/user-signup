from flask import Flask, request, render_template
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html')
    
    @app.route("/", methods=['POST'])
def psw_verify():
    password = request.form['password']
    orig_password = request.form['password']
    verify_password = request.form['verify']
    username = request.form['username']
    for password in password:
        if orig_password == verify_password:
            return ("Welcome, " + username + "!")
        else:
            return "Passwords must match!" 
  
app.run()