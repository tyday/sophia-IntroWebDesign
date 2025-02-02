import json
from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('templates'))

templates = [
    {'env': env.get_template('pages/index.html'),
     'name': 'index.html'
     },
     {'env': env.get_template('pages/gallery_page.html'),
     'name': 'gallery_page.html'
     },
     {'env': env.get_template('pages/about_us_page.html'),
     'name': 'about_us_page.html'
     },
     {'env': env.get_template('pages/other_page.html'),
     'name': 'other_page.html'
     }
    ]

with open("products.json") as f:
    products = json.load(f)
with open("testimonials.json") as f:
    testimonials = json.load(f)
for template in templates:
    with open("renders/" + template['name'], 'w') as f:
        print(template['env'].render(products = products, testimonials = testimonials), file = f)
# with open("renders/index.html", 'w') as f:
#     print(template.render(products = products), file = f)