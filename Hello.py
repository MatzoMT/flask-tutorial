from flask import Flask
app = Flask(__name__)

"""
@app.route('/')
def hello_world():
   return 'Hello World'
"""

@app.route('/deutsch')
def hello_deutsch():
    return 'Hallo Welt'

@app.route('/suomi')
def hello_suomi():
    return 'Hei maailma'

def hello_wada():
   return 'Hola mundo'
# Below is alternative to route decorator to define routes
app.add_url_rule('/espanol', 'espanol', hello_wada)

def hello_world():
    return 'Hello world'
app.add_url_rule('/', 'hello', hello_world)

if __name__ == '__main__':
   app.run(debug = True)