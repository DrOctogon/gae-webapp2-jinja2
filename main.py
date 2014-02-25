__author__ = 'AppScale Systems'

import os
import jinja2
import webapp2


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class IndexPage(webapp2.RequestHandler):
  """ The API Checker dashboard home page. """
  def get(self):
    temp_val = {}
    template = jinja_env.get_template('templates/index.html')
    self.response.out.write(template.render(temp_val))


app = webapp2.WSGIApplication([
  ('/', IndexPage),
  ])