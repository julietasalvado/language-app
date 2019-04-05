from bottle import Bottle, run, template, debug, static_file


import os
import sys

dirname = os.path.dirname(sys.argv[0])
app = Bottle()
debug(True)


@app.route('/static/<filename:re:.*\.css>')
def send_css(filename):
	return static_file(filename, root=dirname+'/static/asset/css')


@app.route('/static/<filename:re:.*\.js>')
def send_js(filename):
	return static_file(filename, root=dirname+'/static/asset/js')


@app.route('/')
def index():
	data = {"developer_name":"Ahmedur Rahman Shovon",
			"developer_organization":"Datamate Web Solutions"}
	return template('index', data = data)


#@app.route('/')
#@app.route('/hello/<name>')
#def add_picture_word_card(name='Stranger'):
    # return template('<b>Hello {{name}}</b>!', name=name)
    # return '''
    #         <form action="/login" method="post">
    #             Word: <input name="word" type="text" />
    #             Picture: <input name="picture" type="text" />
    #             <input value="Add card" type="submit" />
    #         </form>
    #     '''


# def check_login(word, picture):
#     pass


# @app.route('/', method='POST')
# def do_add_picture_word_card():
#     word = request.forms.get('word')
#     picture = request.forms.get('picture')
#     if check_login(word, picture):
#         return "<p>Your login information was correct.</p>"
#     else:
#         return "<p>Login failed.</p>"


@app.error(404)
def error404(error):
    return 'Nothing here, sorry'


run(app, host='localhost', port=8080)


