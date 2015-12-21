import webapp2
'''
form 	= """
		<form action='http://www.google.com/search'>
			<input name='q'>
			<input type='submit'>
		</form>
		"""
'''
'''
form 	= """
		<form method='post' action='/testform'>
			<input name='q'>
			<input type='submit'>
		</form>
		"""
'''
'''
form 	= """
		<form>
			<input type= 'checkbox' name='q'>
			<input type= 'checkbox' name='r'>
			<input type= 'checkbox' name='s'>
			<br>
			<input type='submit'>
		</form>
		"""
'''
'''
form 	= """
		<form>
			<input type= 'radio' name='q' value='one'>
			<input type= 'radio' name='q' value='two'>
			<input type= 'radio' name='q' value='three'>
			<br>
			<input type='submit'>
		</form>
		"""
'''
form 	= """
		<form>
			<label>
				pig
				<input type= 'radio' name='q' value='one'>
			</label>
			<label>
				dog
				<input type= 'radio' name='q' value='two'>
			</label>
			<label>
				chick
				<input type= 'radio' name='q' value='three'>
			</label>
			<br>
			<input type='submit'>
		</form>
		"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/html'
        #self.response.write('Hello, World!')
        self.response.write(form)

class TestHandler(webapp2.RequestHandler):
	#def get(self):
	def post(self):
		#q = self.request.get("q")
		#self.response.out.write(q)
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write(self.request)


app = webapp2.WSGIApplication([
    ('/', MainPage), ('/testform', TestHandler)
], debug=True)