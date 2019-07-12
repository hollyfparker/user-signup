from flask import Flask, request, redirect, render_template
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/", methods=['POST'])

def psw_verify():
    password = request.form['password']
    verify_password = request.form['verify']
    username = request.form['username']
    password_error = 'Passwords must match!'
    if password == verify_password:
          
        return render_template('welcome.html', username=username)   

    else:
           
        return render_template('index.html', password_error=password_error)    

  
app.run()