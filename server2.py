from bottle import route, run
#        <script type=<"text/javascript" src="/brython.js"></script>

x = '''\
<html lang="en">
    <head>
        <meta charset="utf-8">
        <script src="https://cdn.jsdelivr.net/npm/brython@3.12.1/brython.min.js"></script>
        <title>{title}</title>
    </head>
    <body onload="brython()">
        <script type="text/python" src="{script}"></script
    </body>
</html>\
'''


@route('/index.py')
def index():
    return open("index.py").read()

@route('/')
def hello():
    return x.format(title="index.py", script="index.py")


run(host='localhost', port=8080, debug=True)