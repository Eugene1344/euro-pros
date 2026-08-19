#!/usr/bin/env python3
"""
Assembles index.html from components/<section>/<section>.html partials.

Each component folder may contain <name>.html (required), <name>.css and
<name>.js (optional). This script stitches them into a single static
index.html: <link>/<script> tags are emitted in component order, right
after the shared global assets (variables.css, main.css) and, for scripts,
right before </body>.

This mirrors how the same components will map onto WordPress later --
each folder becomes a template part / ACF flexible-content block, with its
own enqueued style and script.

Usage: python3 build_index.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
COMPONENTS_DIR = os.path.join(ROOT, "components")
ASSET_VERSION = "20260818-4"

# Components rendered inside <header>/<main>/<footer> wrappers, in order.
HEADER_COMPONENTS = ["header"]
MAIN_COMPONENTS = [
    "hero",
    "trust-bar",
    "services",
    "why-us",
    "value-props",
    "work",
    "stats-bar",
    "process-preview",
    "process-steps",
    "reviews",
    "experience",
    "construction-banner",
    "pricing",
    "advantages",
    "faq",
    "service-area",
    "final-cta",
]
FOOTER_COMPONENTS = ["footer"]
OVERLAY_COMPONENTS = ["exit-popup"]

ALL_COMPONENTS = HEADER_COMPONENTS + MAIN_COMPONENTS + FOOTER_COMPONENTS + OVERLAY_COMPONENTS


def read_component(name, ext):
    path = os.path.join(COMPONENTS_DIR, name, f"{name}.{ext}")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return f.read()


def component_html(name):
    html = read_component(name, "html")
    if html is None:
        raise FileNotFoundError(f"components/{name}/{name}.html not found")
    return html.rstrip("\n")


def css_links():
    links = [
        f'  <link rel="stylesheet" href="css/variables.css?v={ASSET_VERSION}" />',
        f'  <link rel="stylesheet" href="css/main.css?v={ASSET_VERSION}" />',
        '  <link rel="stylesheet" href="vendor/swiper/swiper-bundle.min.css" />',
    ]
    for name in ALL_COMPONENTS:
        if read_component(name, "css") is not None:
            links.append(f'  <link rel="stylesheet" href="components/{name}/{name}.css?v={ASSET_VERSION}" />')
    return "\n".join(links)


def js_scripts():
    scripts = ['  <script src="vendor/swiper/swiper-bundle.min.js"></script>']
    for name in ALL_COMPONENTS:
        if read_component(name, "js") is not None:
            scripts.append(f'  <script src="components/{name}/{name}.js?v={ASSET_VERSION}"></script>')
    return "\n".join(scripts)


STRUCTURED_DATA = """  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "GeneralContractor",
    "name": "Euro Pros Remodeling",
    "url": "https://www.europrosremodeling.com/",
    "logo": "https://www.europrosremodeling.com/images/logo.png",
    "image": "https://www.europrosremodeling.com/images/hero.jpg",
    "telephone": "+1-847-888-1919",
    "email": "info@europrosremodeling.com",
    "priceRange": "$$",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "1753 Fredericksburg Ln",
      "addressLocality": "Aurora",
      "addressRegion": "IL",
      "postalCode": "60503",
      "addressCountry": "US"
    },
    "areaServed": [
      "Naperville, IL", "Arlington Heights, IL", "Glenview, IL", "Wheaton, IL",
      "Downers Grove, IL", "Elmhurst, IL", "Aurora, IL", "Hinsdale, IL",
      "Oak Brook, IL", "St. Charles, IL"
    ],
    "sameAs": [
      "https://www.facebook.com/Euro.Pros.Incorp/",
      "https://www.instagram.com/euro_pros_inc/",
      "https://www.youtube.com/@europrosremodeling"
    ],
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "5.0",
      "reviewCount": "24"
    }
  }
  </script>"""


def build():
    header_html = "\n\n".join(component_html(name) for name in HEADER_COMPONENTS)
    main_html = "\n\n".join(component_html(name) for name in MAIN_COMPONENTS)
    footer_html = "\n\n".join(component_html(name) for name in FOOTER_COMPONENTS)
    overlay_html = "\n\n".join(component_html(name) for name in OVERLAY_COMPONENTS)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <script>
    // Applied synchronously, before CSS paints, so a returning visitor's
    // saved theme doesn't flash the wrong palette for a frame.
    (function () {{
      try {{
        var t = localStorage.getItem("epTheme");
        if (t === "dark" || t === "light") document.documentElement.setAttribute("data-theme", t);
      }} catch (e) {{}}
    }})();
  </script>
  <title>Euro Pros Remodeling | Licensed General Contractor in the Chicago Suburbs</title>
  <meta name="description" content="Euro Pros Remodeling is a licensed general contractor serving the Chicago suburbs — bathroom, basement, kitchen, whole-home remodeling and new home construction." />
  <link rel="canonical" href="https://www.europrosremodeling.com/" />
  <link rel="icon" type="image/png" href="favicon.png" />

  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Euro Pros Remodeling" />
  <meta property="og:title" content="Euro Pros Remodeling | Licensed General Contractor in the Chicago Suburbs" />
  <meta property="og:description" content="Bathroom, basement, kitchen, whole-home remodeling and new home construction — a licensed General Contractor serving the Chicago suburbs." />
  <meta property="og:image" content="https://www.europrosremodeling.com/images/hero.jpg" />
  <meta property="og:url" content="https://www.europrosremodeling.com/" />
  <meta name="twitter:card" content="summary_large_image" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />

{css_links()}

{STRUCTURED_DATA}
</head>
<body>

{header_html}

  <main id="main-content">

{main_html}

  </main>

{footer_html}

{overlay_html}

{js_scripts()}
</body>
</html>
"""

    out_path = os.path.join(ROOT, "index.html")
    with open(out_path, "w") as f:
        f.write(html)
    print("wrote index.html from", len(ALL_COMPONENTS), "components")


if __name__ == "__main__":
    build()
