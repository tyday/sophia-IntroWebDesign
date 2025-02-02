# Bloom Valley Nursery Website

Welcome to the Bloom Valley Nursery Website project! This project is a multi-page website built as part of an introduction to web design course. It showcases a simple, responsive site with a focus on client branding, product display, customer testimonials, and a contact form.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Installation & Usage](#installation--usage)
- [Templating & Build Process](#templating--build-process)
- [Future Improvements](#future-improvements)
- [License](#license)

## Project Overview

Bloom Valley Nursery is a fictional client website designed to showcase products, gallery images, customer testimonials, and contact information. The site consists of the following pages:

- **Home Page (`index.html`)**: Features the client logo, a hero image, promotional content, and a product showcase.
- **Gallery Page (`gallery_page.html`)**: Displays product images with descriptions and "Add to Cart" buttons arranged in a table layout, optimized for both desktop and mobile.
- **About Us Page (`about_us_page.html`)**: Provides company information, business hours, and a contact form for customer feedback.
- **Other Page (`other_page.html`)**: Showcases customer testimonials and a spotlight on satisfied customers.

## Features

- **Responsive Design**: The layout is structured to support both mobile and desktop views.
- **Accessible Navigation**: The header and footer include navigation menus with proper ARIA attributes.
- **Dynamic Templating**: Utilizes Jinja2 templating to manage common components (header, footer, product cards) and dynamic content.
- **Semantic HTML**: Uses proper semantic elements like `<section>`, `<article>`, and `<blockquote>` to structure content.
- **Interactive Forms**: Includes a newsletter subscription form and a contact form with client-side validation.

## Folder Structure
```plaintext
introtowebdesign/
├── assets/                  # Images and other static assets
├── templates/
│   ├── components/
│   │   ├── footer.html      # Shared footer component
│   │   ├── header.html      # Shared header component
│   │   ├── product_card.html
│   │   └── product_card_gallery.html
│   └── pages/
│       ├── index.html
│       ├── gallery_page.html
│       ├── about_us_page.html
│       └── other_page.html
├── renders/                 # Output directory for built HTML files
├── styles.css               # Main stylesheet
├── script.js                # Main JavaScript file
├── jinja_build.py           # Python script for building the site with Jinja2
├── products.json            # JSON file with product data
└── testimonials.json        # JSON file with testimonial data
```


## Installation & Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/bloom-valley-nursery.git
   cd bloom-valley-nursery
   ```

2. **Install Dependencies:**

This project uses Jinja2 for templating. Install it via pip if you haven’t already:
```bash
pip install jinja2
```

3. **Build the Site:**

    Run the build script to render the HTML files from the templates:
    ```bash
    python jinja_build.py
    ```

4. **Serve the Site Locally:**

    You can use Live Server in VS Code for live reloading.
    To change the Live Server root directory for this workspace, add the following to your workspace’s .vscode/settings.json:
    ```bash
    {
        "liveServer.settings.root": "/renders"
    }
    ```
5. **View the Site:**

    Open your browser and navigate to the address provided by Live Server (usually http://127.0.0.1:5500/).

## Templating & Build Process

* Jinja2 Templating:
    The site uses Jinja2 templates to manage common components (e.g., header, footer, product cards). The build script (jinja_build.py) loads product and testimonial data from JSON files and renders each page template.

* Navigation Management:
    Navigation links are centralized in the build process so that changes to links are reflected across the entire site.