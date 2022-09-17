from flask import Flask, request

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return """
                <html>
                <body style="background: rgb(40,107,131);
                             background: linear-gradient(18deg, rgba(40,107,131,1) 37%, rgba(51,214,204,0.938813025210084) 100%);">
                    
                    <h1 style="color:#fff;text-align:center; 
                    font-family: Brush Script MT, Brush Script Std, cursive; font-size: 100px; margin:10px;">
                    Hello! Dear Client's </h1>
                    
                    <hr>
                    <form action='/greet'>
                        <h4 style="color:#fff;
                        font-size: 20px; 
                        font-family: Courier New;">
                        What is your name?
                        <br><input type='text' name='name'
                        style="width: 100%;
                               padding: 12px 20px;
                               margin: 8px 0;
                               box-sizing: border-box;
                               font-size: 20px; 
                               font-family: Courier New;"></h4><br>
                        
                        <h4 style="color:#fff;
                        font-size: 20px; 
                        font-family: Courier New;">
                        What is your characteristics as a person?
                        <input type='text' name='character'
                        style="width: 100%;
                               padding: 12px 20px;
                               margin: 8px 0;
                               box-sizing: border-box;
                               font-size: 20px; 
                               font-family: Courier New;"></h4><br>
                        
                        <input type='submit' value='Submit'
                        style="width: 100%;
                               padding: 12px 20px;
                               margin: 8px 0;
                               box-sizing: border-box;
                               font-size: 20px; 
                               font-family: Courier New;">
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
        <html><body style="background: rgb(40,107,131);
                    background: linear-gradient(18deg, rgba(40,107,131,1) 37%, rgba(51,214,204,0.938813025210084) 100%);">
                    
                    <h1 style="color:#fff;text-align:center; 
                    font-family: Brush Script MT, Brush Script Std, cursive; font-size: 80px; margin:10px;">
                    We have a new friend!</h1>
                    <hr>
                    
                    <h2 style="color:#fff;
                    text-align:center; 
                    font-family: Courier New; 
                    font-size: 40px; 
                    margin:20px;">
                    {0} is {1}<h2>
                    <input type="button" value="Back" onclick="history.back()"
                    style="width: 100%;
                               padding: 12px 20px;
                               margin: 8px 0;
                               box-sizing: border-box;
                               font-size: 20px; 
                               font-family: Courier New;">
              </body></html>
           """.format(name, msg)


# Launch the Flask dev server
app.run(host="localhost", debug=True)
