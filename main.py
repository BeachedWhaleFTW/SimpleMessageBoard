from models.greetings import Greetings
import webapp2
import os
import jinja2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		results = Greetings.query().order(-Greetings.timestamp).fetch()

		results_dict = {'greetings': results}

		template_dir = os.path.join(os.path.dirname(__file__), 'templates')

		jinja_env = jinja2.Environment(
			loader=jinja2.FileSystemLoader(template_dir)
		)

		template = jinja_env.get_template('home.html')
		rendered_template = template.render(results_dict)

		self.response.write(rendered_template)

class GreetHandler(webapp2.RequestHandler):
	def post(self):
		user_name = self.request.get('user_name')
		message = self.request.get('message')

		Greetings(name=user_name, message=message).put()

		self.redirect('/')