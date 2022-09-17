from flask import Flask, request

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <form action='/greet'>
    <html><body style="margin:20%;">
            <h1>Welcome! Dear User!</h1>
            <form action='/greet'>
            May I have your full name? <br> <input type='text' name='name'><br>
            <input type='submit' value='Submit'>
            </body></html>
            """

@app.route('/greet')
def greet():
    name = request.args.get('name')
    time = str(datetime.now())
    return """
        <html><body style="margin:20%;">
                    <h2>Ma'am/Sir, ! {0} </h2> 
                    <h3>The date and time is {1} </h3>
                    
              </body></html>
           """.format(name, time)


# It will launch the Flask dev server
app.run(host="localhost", debug=True)
