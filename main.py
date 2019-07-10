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
    
        return render_template('welcome.html')
  
app.run()