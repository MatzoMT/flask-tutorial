from flask import Flask, redirect, url_for
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

# url_for() function is very useful for dynamically building a URL for a specific function
# The function accepts the name of a function as first argument, and one or more keyword arguments,
# each corresponding to the variable part of URL.
@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

# redirect will change the url 
@app.route('/language/<language>')
def set_language(language):
    if language =='finnish':
        return redirect(url_for('hello_suomi'))
    elif language == 'german':
       return redirect(url_for('hello_deutsch'))
    else:
        return redirect(url_for('hello_guest',guest = language))

if __name__ == '__main__':
   app.run(debug = True)
