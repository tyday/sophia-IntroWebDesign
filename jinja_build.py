import json
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

# Define a single navigation variable to be used in all templates
nav_links = [
    {'href': '/', 'text': 'Home', 'page': 'index.html'},
    {'href': '/gallery_page.html', 'text': 'Gallery', 'page': 'gallery_page.html'},
    {'href': '/about_us_page.html', 'text': 'About Us', 'page': 'about_us_page.html'},
    {'href': '/other_page.html', 'text': 'Other page', 'page': 'other_page.html'}
]

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
        print(
            template['env'].render(
                products=products,
                testimonials=testimonials,
                current_page=template['name'],
                nav_links=nav_links  # Pass the navigation links to every template
            ),
            file=f
        )
