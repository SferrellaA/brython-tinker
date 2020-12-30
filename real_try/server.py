from http.server import BaseHTTPRequestHandler, HTTPServer
import ast
from os import path

def read_html(filename):
	imports = []
	filetext = open(filename, 'r').read()

	# Handle the imports 
	for node in ast.iter_child_nodes(ast.parse(filetext)):
		if isinstance(node, ast.ImportFrom):
			imports.append(bytes('<script src="/brython/' + node.module + '.brython.js"></script>', "utf8"))
		elif isinstance(node, ast.Import): 
			imports.append(bytes('<script src="/brython/' + node.names[0].name + '.brython.js"></script>', "utf8"))
	return imports, bytes(filetext, "utf8")

class MyServer(BaseHTTPRequestHandler):
	def do_GET(self):
		filepath = "."+self.path
		if not path.exists(filepath):
			self.send_response(404)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(b'404')
			return
		else:
			self.send_response(200)
			if path.isfile(filepath):
				self.end_headers()
				self.wfile.write(bytes(open(filepath, 'r').read(), "utf8"))
				return
			self.send_header("Content-type", "text/html")
			self.end_headers()
			filepath = path.join(filepath, "index.py")
		script_imports, script_body = read_html(filepath)
		self.wfile.write(b'<script type="text/javascript" src="/brython/brython.js"></script>')
		self.wfile.write(b'<script type="text/javascript" src="/brython/brython_stdlib.js"></script>')
		self.wfile.write(b'<body onload="brython(1)">')
		self.wfile.writelines(script_imports)
		self.wfile.write(b'<script type="text/python">')
		self.wfile.write(script_body)
		self.wfile.write(b'</script>')
		self.wfile.write(b'</body>')

webServer = HTTPServer(("localhost", 8000), MyServer)
try:
	webServer.serve_forever()
except KeyboardInterrupt:
	pass
webServer.server_close()