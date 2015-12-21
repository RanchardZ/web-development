import cgi

table = dict(zip(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'),\
				 list('nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM')))

def rot13(words):
	new_words = []
	for char in words.strip():
		if table.has_key(char):
			new_words.append(table[char])
		else:
			new_words.append(char)
	new_words.append('\n')
	return ''.join(new_words)

def escape(words):
	return cgi.escape(words, quote=True)