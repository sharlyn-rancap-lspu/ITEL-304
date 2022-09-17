from flask import Flask, request

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return """<html><body>
                    <h1>Hello!</h1>
                    <form action='/greet'>
                        How are you today? <input type='text' name='name'><br>
                        <input type='submit' value='Submit'>
              </body></html>
           """

@app.route('/greet')
def greet():
    name = request.args.get('name')
    if name == '':
        msg = 'Cheer Up, Everything will be alright.'
    else:
        msg = name

    return """
        <html><body>
                    <h2>Good thing! {0}<h2>
              </body></html>
           """.format(name, msg)


# It will launch the Flask dev server
app.run(host="localhost", debug=True)
