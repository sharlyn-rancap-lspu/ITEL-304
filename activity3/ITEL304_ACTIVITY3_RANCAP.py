from flask import Flask, request

from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    return """
                <head>
                <style>
                body
                {background-image: linear-gradient(to right top, #41142d, #422d4e, #394567, #345c76, #3f727d, #447478, #4a7573, #52766f, #436661, #355752, #274844, #1a3937);}

                h1
                {color:#fff;
                text-align:center; 
                font-family: Brush Script MT, Brush Script Std, cursive; 
                font-size: 100px; 
                margin:10px;}

                h2
                {color:#fff;
                text-align:center; 
                ont-family: Courier New; 
                font-size: 40px; 
                margin:20px;}

                h4
                {color:#fff;
                font-size: 20px; 
                font-family: Courier New;}

                input
                {width: 100%;
                padding: 12px 20px;
                margin: 8px 0;
                box-sizing: border-box;
                font-size: 20px; 
                font-family: Courier New;}
                
                .container
                {margin: 50px;
                padding: 50px;
                background: rgba(36, 69, 82, 0.36);
                border-radius: 16px;
                box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(10.5px);
                -webkit-backdrop-filter: blur(10.5px);
                border: 1px solid rgba(36, 69, 82, 0.57);}
                </style>
                </head>

                <html>
                <body>
                    <h1> Hello! Dear Client's </h1>

                    <hr>
                    <form action='/greet'>
                        <div class="container">
                        <h4>What is your name?
                        <br><input type='text' name='name'></h4>
                        <br>

                        <h4>What is your characteristics as a person?
                        <input type='text' name='character' ></h4>
                        <br>

                        <input type='submit' value='Submit'>
                        </div>
              </body></html>
           """


@app.route('/greet')
def greet():
    name = request.args.get('name')
    character = request.args['character']
    if character == '':
        msg = 'might still confuse about his/her self.'
    else:
        msg = character

    return """

        <html><body style="background-image: linear-gradient(to right top, #41142d, #422d4e, #394567, #345c76, #3f727d, #447478, #4a7573, #52766f, #436661, #355752, #274844, #1a3937);">
                    

                    <h1 style="color:#fff;text-align:center; 
                    font-family: Brush Script MT, Brush Script Std, cursive; font-size: 80px; margin:10px;">
                    We have a new friend!</h1>
                    <hr>

                    <div style="margin: 50px; padding: 50px;">
                    <h2 style="color:#fff;
                    text-align:center; 
                    font-family: Courier New; 
                    font-size: 40px; 
                    margin:20px;">
                    {0} is {1}</h2>
                    <input type="button" value="Back" onclick="history.back()"
                    style="width: 100%;
                               padding: 12px 20px;
                               margin: 8px 0;
                               box-sizing: border-box;
                               font-size: 20px; 
                               font-family: Courier New;">
                    </div>
              </body></html>
           """.format(name, msg)


# It will launch the Flask dev server
app.run(host="localhost", debug=True)
