import helper
helper.create_title("# Main Title")
helper.create_paragraph("This is the main introduction to the test page")
helper.create_title("## Sub Title One")
helper.create_paragraph("This is my sectional paragraph, with an &")
helper.create_paragraph("""And a 
	multiline secondary paragraph 
	for that one""")
helper.create_paragraph("This `is` a\n `code` test")
helper.create_title("## Codeblock Test")
helper.create_codeblock("""1---5---10---15---20---25---30---35---40---45---50---55---60---65---70---75---80---85---90---95--100--105--110--115--120--125--130--135--140--145--150--155--160--165--170--175--180--185--190--195--200--205--210--215--220--225--230--235--240--245--250--255--260--265--270--275--280--285--290--295--300
	printf(\"hello world\")
	test with &
""")
helper.create_title("##blockquote test")
helper.create_paragraph("Here's the conclusion")
helper.create_blockquote("This is a blockquote")
helper.create_blockquote("This is a really long block quote. \nIn a moment I'm just going to copy/paste a lorem ipsum or something because I don't really want to type all this out. Or maybe I will - it'll be a good thing for me to practive doing.")
helper.create_title("##image test")
helper.create_image('https://i.imgur.com/UrJrpo1.png')
helper.create_image('https://i.imgur.com/UrJrpo1.png', "this is my alt text")
helper.create_image('https://i.imgur.com/UrJrpo1.png', "the alt text", "the figure caption\n`testtesttest`")
