
import re
import cgi
USER_NAME_RE 	= re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
USER_PAWD_RE 	= re.compile(r"^.{3,20}$")
EMAIL_RE		= re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
	if not username:
		return "", "That's not a valid username."
	elif ' ' in username:
		return username, "That's not a valid username"
	else:
		return username, ""

def valid_password(password):
	if len(password)<3 or len(password)>20:
		return "", "That wasn't a valid password"
	else:
		return "", ""

def valid_vpassword(password, vpassword):
	if password != vpassword:
		return "", "Your passwords didn't match"
	else:
		return "", ""

def valid_email(email):
	if not email or '@' in email:
		return email, ""
	else:
		return email, "That's not a valid email"
		

def escape(words):
	return cgi.escape(words, quote=True)
