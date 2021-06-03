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

# suomi will route correctly with/wo trailing slash
@app.route('/suomi/')
def hello_suomi():
    return 'Hei maailma'

def hello_wada():
   return 'Hola mundo'
# Below is alternative to route decorator to define routes
app.add_url_rule('/espanol', 'espanol', hello_wada)

def hello_world():
    return 'Hello world'
app.add_url_rule('/', 'hello', hello_world)

# Below routes anything not mentioned above to say 'Hey var'! Good for error handling?
@app.route('/<var>')
def hello_var(var):
   return 'Hey %s!' % var

@app.route('/goodbye/<var>')
def goodbye_var(var):
   return 'Goodbye %s!' % var

# floatvar must be in floating point form (having a decimal point)
@app.route('/float/<float:floatvar>')
def show_float(floatvar):
    return 'Float is %f' % floatvar

if __name__ == '__main__':
   app.run(debug = True)

if __name__ == '__main__':
   app.run(debug = True)