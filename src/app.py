from werkzeug.wrappers import Request, Response
import setuptools

def application(env, start_response):
    request = Request(env)
    text = f"Hello, {request.args.get('name', 'World')}!"
    response = Response(text, mimetype='text/plain')
    return response(env, start_response)

def func():
    dev = "dev commit"
    dev2 = 'dev2 commit'
    fix3 = 'fix3'