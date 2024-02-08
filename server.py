from bottle import route, run
from pathlib import Path

brython = open("brython.js").read()
@route('/brython.js')
def serveBrython():
    return brython

html = '''\
<html>
    <head>
        <meta charset="utf-8">
        <script src="/brython.js"></script>
        <title>{title}</title>
    </head>
    <body onload="brython()">{content}</body>
</html>\
'''

def getPath(path):
    p = Path(path)
    if p.is_file():
        return open(path).read()
    if p.is_dir():
        if path[-1] != '/':
            path += '/'
        if Path(path + "index.html").is_file():
            return open(path + "index.html").read()
        if Path(path + "index.py").is_file():
            return open(path + "index.py").read()
    else:
        return "Not Found"

def enscript(script):
    return f"<script type=\"text/python\">{getPath(script)}</script>"

def call(script):
    return f"<script type=\"text/python\" src=\"{script}\"></script>"

'''
@route('/index.py')
def hello():
    return x.format(title="index.py", script=open("index.py").read())
'''

x = "/index.py"
@route(x)
def main():
    return html.format(title=x, content=call(x))

run(host='localhost', port=8080, debug=True)



