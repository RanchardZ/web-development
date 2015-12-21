import cgi

months = ['January',
		  'February',
		  'March',
		  'April',
		  'May',
		  'June',
		  'July',
		  'August',
		  'September',
		  'October',
		  'November',
		  'December']

month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
	if month:
		short_month = month[:3].lower()
		return month_abbvs.get(short_month)

def valid_day(day):
	if day and day.isdigit():
		day = int(day)
		if day > 0 and day <= 31:
			return day

def valid_year(year):
	if year and year.isdigit():
		year = int(year)
		if year > 1990 and year < 2020:
			return year

def escape_html(s):
	'''
	for (i, o) in (("&", "&amp;"),
				   (">", "&gt;"),
				   ("<", "&lt;"),
				   ('"', "&quote;")):
		s = s.replace(i, o)
	return s
	'''
	return cgi.escape(s, quote = True)

#print valid_month('feb')