import os
import json
from jinja2 import Environment, FileSystemLoader

# Set up Jinja environment
env = Environment(loader=FileSystemLoader('templates'))

# Navigation links (shared across all templates)
nav_links = [
    {'href': 'index.html', 'text': 'Home', 'page': 'index.html'},
    {'href': 'gallery_page.html', 'text': 'Gallery', 'page': 'gallery_page.html'},
    {'href': 'about_us_page.html', 'text': 'About Us', 'page': 'about_us_page.html'},
    {'href': 'other_page.html', 'text': 'Other page', 'page': 'other_page.html'}
]

# List of templates to process
templates = [
    {'template': 'pages/index.html', 'output': 'index.html'},
    {'template': 'pages/gallery_page.html', 'output': 'gallery_page.html'},
    {'template': 'pages/about_us_page.html', 'output': 'about_us_page.html'},
    {'template': 'pages/other_page.html', 'output': 'other_page.html'}
]

# Ensure 'renders/' directory exists
os.makedirs('renders', exist_ok=True)

# Load data files
with open("products.json") as f:
    products = json.load(f)
with open("testimonials.json") as f:
    testimonials = json.load(f)

# Render and save each template
for item in templates:
    template = env.get_template(item['template'])
    output_path = os.path.join('renders', item['output'])

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template.render(
            products=products,
            testimonials=testimonials,
            current_page=item['output'],
            nav_links=nav_links  # Pass the navigation links to all templates
        ))

print("✔ Jinja templates compiled successfully into 'renders/'")

# Copy static files to 'renders/' directory
import shutil
shutil.copytree('static', 'renders/static', dirs_exist_ok=True)
print("✔ Static files copied to 'renders/static/'")

