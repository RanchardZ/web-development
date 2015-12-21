import webapp2
from util import *

form =  """
		<form method="post">
			<h1>Signup</h1>
			<br>

			<label>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Username
				<input type='text' name='username' value=%(username)s>
				<span style="color: red">%(username_error)s</span>
			</label>			
			<br>
			<label>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Password&nbsp;
				<input type='password' name='password' value=%(password)s>
				<span style="color: red">%(password_error)s</span>
			</label>			
			<br>
			<label>
				Verify Password
				<input type='password' name='vpassword' value=%(vpassword)s>
				<span style="color: red">%(vpassword_error)s</span>
			</label>

			<br>
			<label>
				Email (optional)
				<input type='text' name='email' value=%(email)s>
				<span style="color: red">%(email_error)s</span>
			</label>	
			<br>
			<input type='submit'>

		</form>
		"""

class MainPage(webapp2.RequestHandler):
	def write_form(self, username='', password='', vpassword='', email='',\
				   username_error='', password_error='', vpassword_error='', email_error=''):
		self.response.out.write(form % {"username": username,
										"password": password,
										"vpassword": vpassword,
										"email": email,
										"username_error": username_error,
										"password_error": password_error,
										"vpassword_error": vpassword_error,
										"email_error": email_error})

	def get(self):
		self.write_form()

	def post(self):
		username 		= self.request.get('username')
		password 		= self.request.get('password')
		vpassword 		= self.request.get('vpassword')
		email 			= self.request.get('email')

		uname, uname_error 	= valid_username(username)
		pswrd, paswd_error 	= valid_password(password)
		vpwrd, vpwrd_error 	= valid_vpassword(password, vpassword)
		email, email_error 	= valid_email(email)

		if (uname_error or paswd_error or vpwrd_error or email_error):
			self.write_form(username = uname, password = pswrd, vpassword = vpwrd, email = email,\
							username_error = uname_error, password_error = paswd_error,\
							vpassword_error = vpwrd_error, email_error = email_error)

		else:
			self.redirect("/welcome")

class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("welcome!")

app = webapp2.WSGIApplication([('/', MainPage), ('/welcome', WelcomeHandler)], debug=True)

