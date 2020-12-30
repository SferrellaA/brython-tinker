from browser import document

def create_codeblock(text):
	from browser.html import PRE
	code = document.createElement("code")
	code <= text
	document <= PRE(code)

def clean_text(text):
	if '\n' in text:
		text = text.replace('\n', '<br>')
	if '`' in text:
		segments = text.split('`')
		for i in range(0, len(segments)):
			if i % 2 == 1:
				segments[i] = "<code>" + segments[i] + "</code>"
		text = ''.join(segments)
	# TODO - check markdown links, make pictures turn into the thing
	return text

def create_paragraph(text):
	from browser.html import P
	text = clean_text(text)
	document <= P(text)

def create_blockquote(text):
	block = document.createElement("blockquote")
	block <= text
	document <= block

def create_title(raw_text):
	from browser.html import H1
	text = raw_text.lstrip('#')
	size = len(raw_text) - len(text)
	if size <= 1:
		from browser.html import H1 as header
	elif size == 2:
		from browser.html import H2 as header
	elif size == 3:
		from browser.html import H3 as header
	elif size == 4:
		from browser.html import H4 as header
	elif size == 5:
		from browser.html import H5 as header
	else:
		from browser.html import H6 as header
	document <= header(text)

def create_image(source, *args):
	from browser.html import IMG
	altText = ''
	if len(args) > 0:
		altText = args[0]
	image = IMG(src=source, alt=altText, title=altText)
	if len(args) == 2:
		from browser.html import FIGURE, FIGCAPTION
		figure = FIGURE()
		figure <= image
		figure <= FIGCAPTION(clean_text(args[1]))
		document <= figure
	else:
		from browser.html import P
		document <= P(image)