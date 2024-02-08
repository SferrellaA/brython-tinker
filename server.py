from bottle import route, run
#        <script type=<"text/javascript" src="/brython.js"></script>

x = '''\
<html>
    <head>
        <meta charset="utf-8">
        <script src="https://cdn.jsdelivr.net/npm/brython@3.12.1/brython.min.js"></script>
        <title>{title}</title>
    </head>
    <body onload="brython()">
        <script type="text/python">
{script}
        </script
    </body>
</html>\
'''


@route('/index.py')
def hello():
    return x.format(title="index.py", script=open("index.py").read())

run(host='localhost', port=8080, debug=True)