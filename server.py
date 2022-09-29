from flask import Flask
app = Flask(__name__)

# Route Statements
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hi(name):
    name = name.capitalize()
    print(name)
    return f'Hi {name}!'

@app.route('/repeat/<int:num>/<phrase>')
def phrase_multiplier(num, phrase):
    return num * phrase


# End Main Statement
if __name__=="__main__":
    app.run(debug=True)