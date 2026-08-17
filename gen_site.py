#!/usr/bin/env python3
"""
Site generator for the Euro Pros Remodeling static site.

This is a dev-only helper (not part of the deployed site). It exists so the
header, footer, and CTA banner are defined ONCE and stamped identically
across every page, instead of hand-copied into 14+ files. Re-run it after
editing HEADER_HTML / FOOTER_HTML / cta_banner() to propagate changes.

Usage: python3 gen_site.py
"""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

# Until real Euro Pros photography is supplied, every generated placeholder
# photo collapses onto one of these two real stock/reference photos: hero
# sections get hero.jpg, every other content photo gets placeholder.jpg.
# Remove this substitution once per-image real photos are ready.
_IMG_PATTERN = re.compile(r'src="images/([A-Za-z0-9_.-]+)\.svg"')


def _substitute_placeholder_images(html):
    def repl(match):
        filename = match.group(1)
        target = "hero.jpg" if "hero" in filename.lower() else "placeholder.jpg"
        return f'src="images/{target}"'
    return _IMG_PATTERN.sub(repl, html)

NAV_ITEMS = [
    ("services", "services.html", "Services"),
    ("work", "our-work.html", "Our Work"),
    ("process", "our-process.html", "Our Process"),
    ("about", "about-us.html", "About Us"),
    ("blog", "blog.html", "Blog"),
    ("contact", "contact.html", "Contact"),
]


def nav_links(active):
    out = []
    for key, href, label in NAV_ITEMS:
        cls = ' class="is-active"' if key == active else ""
        out.append(f'        <a href="{href}"{cls}>{label}</a>')
    return "\n".join(out)


SOCIAL_LINKS = [
    ("facebook", "https://www.facebook.com/Euro.Pros.Incorp/", "Euro Pros on Facebook"),
    ("instagram", "https://www.instagram.com/euro_pros_inc/", "Euro Pros on Instagram"),
    ("youtube", "https://www.youtube.com/@europrosremodeling", "Euro Pros on YouTube"),
]


def social_icons_html(cls, icon_cls="social-icon__glyph"):
    items = []
    for key, href, label in SOCIAL_LINKS:
        items.append(
            f'        <a href="{href}" class="{cls}" target="_blank" rel="noopener" aria-label="{label}">{icon(key, icon_cls)}</a>'
        )
    return "\n".join(items)


def header_html(active=""):
    return f"""  <header class="site-header">
    <div class="container">
      <a href="index.html" class="logo">
        <img src="images/logo.png" alt="Euro Pros Construction &amp; Remodeling" width="201" height="100" />
      </a>

      <nav class="main-nav" id="primary-nav" aria-label="Primary">
{nav_links(active)}
        <a class="main-nav__phone" href="tel:+18478881919">(847) 888-1919</a>
        <div class="main-nav__social">
{social_icons_html("main-nav__social-link")}
        </div>
      </nav>

      <div class="header-social">
{social_icons_html("header-social__link")}
      </div>

      <div class="header-actions">
        <a class="header-call" href="tel:+18478881919" aria-label="Call Euro Pros">{icon('phone')}</a>
        <a class="btn btn--primary" href="contact.html">Get an Estimate</a>
      </div>

      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="primary-nav">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>"""


def footer_html():
    return f"""  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="logo">
            <img src="images/logo-white.png" alt="Euro Pros Construction &amp; Remodeling" width="201" height="100" />
          </a>
          <p class="footer-brand__tagline">Licensed &middot; Insured &middot; General Contractor</p>
          <div class="footer-social">
{social_icons_html("footer-social__link")}
          </div>
        </div>

        <div class="footer-col">
          <p class="footer-heading">Services</p>
          <ul class="footer-links">
            <li><a href="bathroom-remodeling.html">Bathroom Remodeling</a></li>
            <li><a href="basement-remodeling.html">Basement Remodeling</a></li>
            <li><a href="kitchen-remodeling.html">Kitchen Remodeling</a></li>
            <li><a href="whole-home-remodeling.html">Whole-Home Remodeling</a></li>
            <li><a href="new-home-construction.html">New Home Construction</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <p class="footer-heading">Company</p>
          <ul class="footer-links">
            <li><a href="about-us.html">About Us</a></li>
            <li><a href="about-us.html#why-euro-pros">Why Euro Pros</a></li>
            <li><a href="our-work.html">Reviews</a></li>
            <li><a href="blog.html">Blog</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <p class="footer-heading">Contact</p>
          <ul class="footer-links">
            <li><a href="tel:+18478881919">(847) 888-1919</a></li>
            <li><a href="mailto:info@europrosremodeling.com">info@europrosremodeling.com</a></li>
            <li><a href="contact.html">Get an Estimate</a></li>
            <li class="footer-links__map">
              <span class="footer-links__map-label">Map</span>
              <a href="https://www.google.com/maps/search/?api=1&amp;query=1753+Fredericksburg+Ln%2C+Aurora%2C+IL+60503" target="_blank" rel="noopener">Euro Pros Inc</a>
            </li>
          </ul>
        </div>

        <div class="footer-actions">
          <a class="btn btn--white btn--block" href="contact.html">Get an Estimate</a>
          <a class="btn btn--outline-light btn--block" href="tel:+18478881919">Call Us (847) 888-1919</a>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2026 Euro Pros Remodeling. All rights reserved.</p>
      </div>
    </div>
  </footer>"""


def cta_banner(title, text, button_label="Get an Estimate", button_href="contact.html", secondary=None):
    secondary_html = ""
    if secondary:
        secondary_html = f'\n        <a class="btn btn--outline-light" href="{secondary[1]}">{secondary[0]}</a>'
    return f"""  <section class="cta-banner section--navy">
    <div class="container cta-banner__grid">
      <div class="cta-banner__content">
        <h2 class="cta-banner__title">{title}</h2>
        <p class="cta-banner__text">{text}</p>
        <div class="cta-banner__actions">
          <a class="btn btn--white" href="{button_href}">{button_label}</a>{secondary_html}
        </div>
      </div>
      <div class="cta-banner__media" aria-hidden="true">
        <img src="images/blueprint-house.png" alt="" />
      </div>
    </div>
  </section>"""


BLUEPRINT_SVG = """<svg viewBox="0 0 480 360" fill="none" xmlns="http://www.w3.org/2000/svg">
          <g stroke="rgba(255,255,255,0.55)" stroke-width="1.3" fill="none" stroke-linejoin="round">
            <!-- roof -->
            <path d="M70 150L245 55l175 95" />
            <path d="M245 55v-18" stroke-dasharray="3 4" />
            <path d="M95 150h300" />
            <!-- chimney -->
            <path d="M300 70v45h-26V95" />
            <!-- main walls -->
            <path d="M95 150v170h300V150" />
            <!-- garage / lean-to wing -->
            <path d="M395 210l55-28v138h-55" />
            <path d="M450 182v-10" stroke-dasharray="3 4" />
            <!-- upper windows -->
            <path d="M130 180h50v40h-50z" />
            <path d="M155 180v40M130 200h50" />
            <path d="M300 180h50v40h-50z" />
            <path d="M325 180v40M300 200h50" />
            <!-- door -->
            <path d="M212 245h56v75h-56z" />
            <path d="M240 245v75" />
            <circle cx="256" cy="285" r="1.6" fill="rgba(255,255,255,0.55)" stroke="none" />
            <!-- lower side window -->
            <path d="M130 260h50v40h-50z" />
            <path d="M155 260v40M130 280h50" />
            <!-- garage door -->
            <path d="M410 250h70v70h-70z" />
            <path d="M410 265h70M410 280h70M410 295h70" />
            <!-- foundation hatch -->
            <path d="M70 320h410M78 320l10 14M108 320l10 14M138 320l10 14M168 320l10 14M198 320l10 14M228 320l10 14M258 320l10 14M288 320l10 14M318 320l10 14M348 320l10 14M378 320l10 14M408 320l10 14M438 320l10 14" stroke-width="1" />
            <!-- width dimension -->
            <path d="M70 30h380" stroke-width="1" />
            <path d="M70 24v12M450 24v12" stroke-width="1" />
            <path d="M70 30l10-4v8zM450 30l-10-4v8z" fill="rgba(255,255,255,0.55)" stroke="none" />
            <text x="260" y="22" fill="rgba(255,255,255,0.6)" font-family="Arial, sans-serif" font-size="13" text-anchor="middle">42'-0&quot;</text>
            <!-- height dimension -->
            <path d="M30 55v265" stroke-width="1" />
            <path d="M24 55h12M24 320h12" stroke-width="1" />
            <path d="M30 55l-4 10h8zM30 320l-4-10h8z" fill="rgba(255,255,255,0.55)" stroke="none" />
            <text x="20" y="190" fill="rgba(255,255,255,0.6)" font-family="Arial, sans-serif" font-size="13" text-anchor="middle" transform="rotate(-90 20 190)">24'-0&quot;</text>
            <!-- north arrow -->
            <g transform="translate(440,40)">
              <circle cx="0" cy="0" r="18" stroke-width="1" />
              <path d="M0 -12L5 6H-5z" fill="rgba(255,255,255,0.55)" stroke="none" />
              <text x="0" y="-22" fill="rgba(255,255,255,0.6)" font-family="Arial, sans-serif" font-size="11" text-anchor="middle">N</text>
            </g>
          </g>
        </svg>"""


def page(title, description, active, body, extra_head="", favicon_emoji=None):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="icon" type="image/png" href="favicon.png" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />

  <link rel="stylesheet" href="css/variables.css" />
  <link rel="stylesheet" href="css/main.css" />
  <link rel="stylesheet" href="css/components.css" />
{extra_head}</head>
<body>

{header_html(active)}

  <main>

{body}

  </main>

{footer_html()}

{EXIT_POPUP_HTML}

  <script src="js/main.js"></script>
</body>
</html>
"""


EXIT_POPUP_HTML = """  <div class="exit-popup-overlay" id="exitPopupOverlay">
    <div class="exit-popup" role="dialog" aria-modal="true" aria-labelledby="exitPopupTitle">
      <button class="exit-popup__close" type="button" aria-label="Close">&times;</button>
      <p class="exit-popup__eyebrow">&mdash; Before You Go &mdash;</p>
      <h3 class="exit-popup__title" id="exitPopupTitle">Leave with a number,<br />not a guess.</h3>
      <p class="exit-popup__text">The consultation is free, and the estimate you receive is detailed and in writing &mdash; most homeowners have it within 48 hours.</p>
      <div class="exit-popup__actions">
        <a class="btn btn--primary" href="contact.html">Request My Free Estimate &rarr;</a>
        <a class="exit-popup__call" href="tel:+18478881919">or call (847) 888-1919</a>
      </div>
    </div>
  </div>"""


def icon(name, cls=""):
    """Minimal 24x24 stroke icon set, colored via CSS currentColor."""
    paths = {
        "shield": '<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/>',
        "hardhat": '<path d="M4 15a8 8 0 0116 0"/><path d="M2 15h20"/><path d="M11 5v3"/><path d="M6 15v-2a6 6 0 0112 0v2"/>',
        "clipboard": '<rect x="6" y="4" width="12" height="17" rx="1.5"/><rect x="9" y="2.5" width="6" height="3" rx="1"/><path d="M9 11h6M9 15h6"/>',
        "chat": '<path d="M4 5h16v11H9l-4 4V5z"/><path d="M8 9h8M8 12h5"/>',
        "person": '<circle cx="12" cy="8" r="3.2"/><path d="M5 20c1.5-4 4-6 7-6s5.5 2 7 6"/>',
        "house": '<path d="M4 11l8-7 8 7"/><path d="M6 10v10h12V10"/><path d="M10 20v-6h4v6"/>',
        "tools": '<path d="M14.5 6.5l3 3-8 8-3-3 8-8z"/><path d="M17 4l3 3-1.5 1.5-3-3z"/><path d="M4 20l3.5-1 .5-3"/>',
        "contact": '<circle cx="12" cy="12" r="9"/><path d="M8 13c1 1 2 1.5 4 1.5s3-.5 4-1.5"/><path d="M9 9.5h.01M15 9.5h.01"/>',
        "check-circle": '<circle cx="12" cy="12" r="9"/><path d="M8 12.3l2.6 2.6L16.5 9"/>',
        "phone": '<path d="M6 3h3l1.5 4-2 1.5a12 12 0 006 6l1.5-2 4 1.5v3a2 2 0 01-2.2 2A17 17 0 015 5.2 2 2 0 016 3z"/>',
        "mail": '<rect x="3" y="5" width="18" height="14" rx="1.5"/><path d="M3.5 6.5l8.5 6 8.5-6"/>',
        "pin": '<path d="M12 21s7-6.5 7-12a7 7 0 10-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
        "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>',
        "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6"/><circle cx="12" cy="8" r="0.4" fill="currentColor" stroke="none"/>',
        "excavation": '<path d="M3 20l6-6M9 14l4 4M13 18l7-7M17 14l3-3"/><circle cx="18" cy="9" r="2"/>',
        "foundation": '<rect x="4" y="16" width="16" height="4"/><path d="M6 16v-3h12v3"/>',
        "framing": '<path d="M4 20V6l8-3 8 3v14"/><path d="M4 12h16M12 3v17"/>',
        "roof": '<path d="M3 12l9-7 9 7"/><path d="M6 11v9h12v-9"/>',
        "window": '<rect x="5" y="4" width="14" height="16" rx="1"/><path d="M12 4v16M5 12h14"/>',
        "plumbing": '<path d="M7 3v6a3 3 0 003 3h1v9"/><path d="M17 3v6a3 3 0 01-3 3"/><circle cx="11" cy="19" r="2"/>',
        "electrical": '<path d="M13 2L4 14h7l-1 8 9-12h-7l1-8z"/>',
        "hvac": '<circle cx="12" cy="12" r="9"/><path d="M12 5v3M12 16v3M5 12h3M16 12h3M7 7l2 2M15 15l2 2M17 7l-2 2M9 15l-2 2"/>',
        "insulation": '<path d="M3 8c2-2 4-2 6 0s4 2 6 0 4-2 6 0"/><path d="M3 14c2-2 4-2 6 0s4 2 6 0 4-2 6 0"/><path d="M3 20c2-2 4-2 6 0s4 2 6 0 4-2 6 0"/>',
        "drywall": '<rect x="4" y="4" width="16" height="16" rx="1"/><path d="M4 10h16M4 15h16M9 4v16M15 4v16"/>',
        "flooring": '<path d="M3 8l6-4 6 4-6 4-6-4z"/><path d="M9 12l6-4 6 4-6 4-6-4z"/>',
        "cabinets": '<rect x="4" y="4" width="16" height="16" rx="1"/><path d="M12 4v16"/><circle cx="9" cy="12" r="0.6" fill="currentColor" stroke="none"/><circle cx="15" cy="12" r="0.6" fill="currentColor" stroke="none"/>',
        "tile": '<rect x="4" y="4" width="7" height="7"/><rect x="13" y="4" width="7" height="7"/><rect x="4" y="13" width="7" height="7"/><rect x="13" y="13" width="7" height="7"/>',
        "paint": '<path d="M6 3h9v6l-2 2v8a2.5 2.5 0 01-5 0v-8L6 9V3z"/>',
        "trim": '<path d="M4 6h16M4 12h16M4 18h10"/>',
        "quote": '<path d="M7 8c-2 0-3 1.5-3 3.5S5 15 7 15v3H4v-3c0-4 2-7 6-7z"/><path d="M17 8c-2 0-3 1.5-3 3.5s1 3.5 3 3.5v3h-3v-3c0-4 2-7 6-7z"/>',
        "star": '<path d="M12 3l2.6 5.6 6.1.6-4.6 4.1 1.3 6-5.4-3-5.4 3 1.3-6-4.6-4.1 6.1-.6z" fill="currentColor" stroke="none"/>',
        "upload": '<path d="M12 15V4M8 8l4-4 4 4"/><path d="M4 15v3a2 2 0 002 2h12a2 2 0 002-2v-3"/>',
        "location-pin": '<path d="M12 21s7-6.5 7-12a7 7 0 10-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
        "layout": '<rect x="3" y="4" width="18" height="16" rx="1.5"/><path d="M9 4v16"/>',
        "shower": '<path d="M6 8V5a2 2 0 012-2h3" /><circle cx="17" cy="4" r="1.5"/><path d="M17 6.5V9M6 9h14" /><path d="M8 13v.01M12 13v.01M16 13v.01M8 17v.01M12 17v.01M16 17v.01M8 21v.01M12 21v.01M16 21v.01" />',
        "bathtub": '<path d="M3 12h18v3a4 4 0 01-4 4H7a4 4 0 01-4-4v-3z"/><path d="M5 12V7a2 2 0 012-2 2 2 0 012 2" /><path d="M2 12h1M21 12h1M6 19v2M16 19v2" />',
        "lightbulb": '<path d="M9 18h6M10 21h4" /><path d="M12 3a6 6 0 00-3.5 10.9c.5.4.8 1 .8 1.7v.4h5.4v-.4c0-.7.3-1.3.8-1.7A6 6 0 0012 3z" />',
        "sink": '<path d="M4 12h16" /><ellipse cx="12" cy="12" rx="8" ry="3" /><path d="M6 15v1a6 6 0 0012 0v-1" /><path d="M12 5v3M9 4l1.5 2M15 4l-1.5 2" />',
        "checklist": '<path d="M9 6h11M9 12h11M9 18h11"/><path d="M4 6l1 1 2-2M4 12l1 1 2-2M4 18l1 1 2-2"/>',
        "facebook": '<circle cx="12" cy="12" r="9"/><path d="M13.5 8.5h1.5V6h-1.7c-1.6 0-2.6 1-2.6 2.7V11H9v2.5h1.7V18h2.5v-4.5h1.7l.3-2.5h-2V9c0-.4.2-.5.5-.5z" fill="currentColor" stroke="none"/>',
        "instagram": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="0.6" fill="currentColor" stroke="none"/>',
        "youtube": '<rect x="2" y="5" width="20" height="14" rx="4"/><path d="M10 9.5v5l4.5-2.5z" fill="currentColor" stroke="none"/>',
    }
    d = paths.get(name, "")
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'


def write(filename, html):
    html = _substitute_placeholder_images(html)
    path = os.path.join(ROOT, filename)
    with open(path, "w") as f:
        f.write(html)
    print("wrote", filename)
