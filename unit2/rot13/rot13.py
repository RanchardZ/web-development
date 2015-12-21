import webapp2
from util import rot13, escape

form = 	"""
		<h2> Enter some text to ROT13:</h2>
		<form method="post">
			<textarea type = "text" name="words" style="height: 100px; width: 400px;">%(words)s</textarea>
			<br>
			<div style="color: red">%(error)s</div>
			<br>
			<input type="submit">
		</form>
		"""


class MainPage(webapp2.RequestHandler):
	def write_form(self, words = '', error = ''):
		self.response.out.write(form % {"words": words,
										"error": error})
	def get(self):
		self.write_form()

	def post(self):
		user_words = self.request.get('words')
		ecpt_words = rot13(user_words)
		self.write_form(words = escape(ecpt_words))



app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

