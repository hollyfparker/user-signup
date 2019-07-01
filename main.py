from flask import Flask, request 
app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}

        </style>
    </head>
    <body>
      <form method="post">
        <label>
         Rotate by:   
            <input type="text" name="Username"/>
            <input type="password" name="Password"/>
            <input type="password" name="Verify Password"/>
            <input type="text" name="Email (optional)"/>
        
            
        </label>
        <input type="submit"/>
    </form>
    </body>
</html>
"""
