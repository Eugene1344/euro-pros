#!/usr/bin/env python3
"""Content for every interior page. Run: python3 build_pages.py"""
from gen_site import page, write, cta_banner, icon

# ============================================================== SERVICES ===
services_body = f"""  <section class="hero hero--sm">
    <div class="hero__media"><img src="images/services-hero.svg" alt="Bathroom remodeling project" /></div>
    <div class="hero__overlay"></div>
    <div class="container">
      <div class="hero__content">
        <h1 class="hero__title hero__title--h2">Our Remodeling &amp; Construction Services</h1>
        <p class="hero__subtitle">From individual renovations to complete home transformations and new home construction, Euro Pros manages your project from start to finish.</p>
        <div class="hero__actions">
          <a class="btn btn--white" href="contact.html">Get an Estimate</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <h2>What We Remodel &amp; Build</h2>
      </div>

      <div class="service-tile-grid">
        <a href="bathroom-remodeling.html" class="service-tile">
          <img src="images/work-bathroom.svg" alt="Bathroom remodeling project" loading="lazy" />
          <div class="service-tile__body">
            <h3 class="service-tile__title">Bathroom Remodeling</h3>
            <p class="service-tile__text">Create a beautiful, functional bathroom designed around your lifestyle.</p>
            <span class="service-tile__link">Learn More &rarr;</span>
          </div>
        </a>
        <a href="basement-remodeling.html" class="service-tile">
          <img src="images/work-basement.svg" alt="Basement remodeling project" loading="lazy" />
          <div class="service-tile__body">
            <h3 class="service-tile__title">Basement Remodeling</h3>
            <p class="service-tile__text">Turn your basement into comfortable, versatile living space.</p>
            <span class="service-tile__link">Learn More &rarr;</span>
          </div>
        </a>
        <a href="kitchen-remodeling.html" class="service-tile">
          <img src="images/work-kitchen.svg" alt="Kitchen remodeling project" loading="lazy" />
          <div class="service-tile__body">
            <h3 class="service-tile__title">Kitchen Remodeling</h3>
            <p class="service-tile__text">Modern kitchens built for everyday living and effortless entertaining.</p>
            <span class="service-tile__link">Learn More &rarr;</span>
          </div>
        </a>
        <a href="whole-home-remodeling.html" class="service-tile">
          <img src="images/work-whole-home.svg" alt="Whole-home remodeling project" loading="lazy" />
          <div class="service-tile__body">
            <h3 class="service-tile__title">Whole-Home Remodeling</h3>
            <p class="service-tile__text">Reimagine your entire home with cohesive design and quality craftsmanship.</p>
            <span class="service-tile__link">Learn More &rarr;</span>
          </div>
        </a>
        <a href="new-home-construction.html" class="service-tile">
          <img src="images/work-new-construction.svg" alt="New home construction project" loading="lazy" />
          <div class="service-tile__body">
            <h3 class="service-tile__title">New Home Construction</h3>
            <p class="service-tile__text">Custom homes built with integrity, attention to detail, and lasting quality.</p>
            <span class="service-tile__link">Learn More &rarr;</span>
          </div>
        </a>
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container">
      <div class="section-head">
        <h2>What to Expect When You Work With Euro Pros</h2>
      </div>
    </div>
    <div class="process-steps process-steps--5 process-steps--full">
      <div class="process-step">
        <p class="process-step__index">01</p>
        <p class="process-step__title">Consultation</p>
        <p class="process-step__text">On-site consultation to understand your goals and scope.</p>
      </div>
      <div class="process-step">
        <p class="process-step__index">02</p>
        <p class="process-step__title">Detailed Estimate</p>
        <p class="process-step__text">Clear written estimate based on the agreed scope of work.</p>
      </div>
      <div class="process-step">
        <p class="process-step__index">03</p>
        <p class="process-step__title">Project Planning</p>
        <p class="process-step__text">Scheduling, materials, permits and project coordination.</p>
      </div>
      <div class="process-step">
        <p class="process-step__index">04</p>
        <p class="process-step__title">Construction &amp; Communication</p>
        <p class="process-step__text">Project management and regular communication throughout the construction.</p>
      </div>
      <div class="process-step">
        <p class="process-step__index">05</p>
        <p class="process-step__title">Final Walkthrough</p>
        <p class="process-step__text">Review of the completed project with the client.</p>
      </div>
    </div>
  </section>

  <section class="section section--navy">
    <div class="container">
      <div class="section-head section-head--light">
        <h2>Why Work With Euro Pros?</h2>
      </div>
      <div class="icon-list icon-list--light icon-list--5 icon-list--center">
        <div class="icon-list__item">
          {icon('shield', 'icon-list__icon icon-list__icon--light')}
          <div>
            <p class="icon-list__title">Licensed General Contractor</p>
            <p class="icon-list__text">Fully licensed to build, remodel, and manage your project.</p>
          </div>
        </div>
        <div class="icon-list__item">
          {icon('clipboard', 'icon-list__icon icon-list__icon--light')}
          <div>
            <p class="icon-list__title">Licensed &amp; Insured</p>
            <p class="icon-list__text">We carry the proper licenses and insurance for your protection.</p>
          </div>
        </div>
        <div class="icon-list__item">
          {icon('hardhat', 'icon-list__icon icon-list__icon--light')}
          <div>
            <p class="icon-list__title">Construction Experience</p>
            <p class="icon-list__text">Skilled craftsmanship and proven processes from start to finish.</p>
          </div>
        </div>
        <div class="icon-list__item">
          {icon('chat', 'icon-list__icon icon-list__icon--light')}
          <div>
            <p class="icon-list__title">Clear Communication</p>
            <p class="icon-list__text">Honest updates and timelines so you always know what to expect.</p>
          </div>
        </div>
        <div class="icon-list__item">
          {icon('tools', 'icon-list__icon icon-list__icon--light')}
          <div>
            <p class="icon-list__title">Professional Project Management</p>
            <p class="icon-list__text">One team managing every detail to keep your project on track.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <h2>Frequently Asked Questions</h2>
      </div>
      <div class="faq">
        <div class="faq-item">
          <button class="faq-item__question" type="button">
            <span>How much does a remodeling project cost?</span>
            <span class="faq-item__icon"></span>
          </button>
          <div class="faq-item__answer"><p>Costs vary by project type and scope. As a starting point: Bathroom Remodeling starts at $12,000+, Basement Remodeling at $25,000+, Kitchen Remodeling at $35,000+, and Whole-Home Remodeling at $75,000+. We'll provide a detailed, written estimate once we understand your specific project.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-item__question" type="button">
            <span>How long does a remodeling project take?</span>
            <span class="faq-item__icon"></span>
          </button>
          <div class="faq-item__answer"><p>Timelines depend on scope &mdash; a bathroom remodel typically takes 3&ndash;6 weeks, a kitchen 6&ndash;12 weeks, and whole-home or new construction projects several months. We'll walk through a realistic schedule during your consultation.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-item__question" type="button">
            <span>Do you provide materials?</span>
            <span class="faq-item__icon"></span>
          </button>
          <div class="faq-item__answer"><p>Yes. We can source and supply all materials, or work with materials you've already selected &mdash; whichever fits your project best.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-item__question" type="button">
            <span>Do you handle plumbing and electrical work?</span>
            <span class="faq-item__icon"></span>
          </button>
          <div class="faq-item__answer"><p>Yes, our team manages plumbing and electrical work as part of your project, coordinated under one contract and one schedule.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-item__question" type="button">
            <span>Do I need permits?</span>
            <span class="faq-item__icon"></span>
          </button>
          <div class="faq-item__answer"><p>Many remodeling projects require permits, especially when plumbing, electrical, or structural changes are involved. We handle the permitting process for you as part of our project management.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-item__question" type="button">
            <span>What areas do you serve?</span>
            <span class="faq-item__icon"></span>
          </button>
          <div class="faq-item__answer"><p>We proudly serve the Chicago suburbs, including Naperville, Arlington Heights, Glenview, Wheaton, Downers Grove, Elmhurst, Aurora, Hinsdale, Oak Brook, St. Charles, and surrounding communities.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-item__question" type="button">
            <span>Do you offer a warranty?</span>
            <span class="faq-item__icon"></span>
          </button>
          <div class="faq-item__answer"><p>Yes. Every project is backed by our 2-year workmanship warranty, with check-ins at 1 month and 1 year after completion.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="experience-full">
    <div class="experience-full__media">
      <img src="images/experience-kitchen.svg" alt="Finished kitchen remodel" loading="lazy" />
      <div class="experience-full__overlay"></div>
    </div>
    <div class="container">
      <div class="experience-full__content">
        <h2 class="experience-full__title">Have a Project in Mind?</h2>
        <p class="experience-full__text">Let's talk about your ideas and how we can bring them to life.</p>
        <a class="btn btn--white" href="contact.html">Get an Estimate</a>
      </div>
    </div>
  </section>
"""

write("services.html", page(
    title="Remodeling &amp; Construction Services | Euro Pros",
    description="Bathroom, basement, kitchen, and whole-home remodeling plus new home construction — explore Euro Pros' full range of services in the Chicago suburbs.",
    active="services",
    body=services_body,
))


# ==================================================== SERVICE DETAIL TEMPLATE
def what_we_do_item(icon_name, title, text):
    return f"""        <div class="icon-list__item">
          {icon(icon_name, 'icon-list__icon')}
          <div>
            <p class="icon-list__title">{title}</p>
            <p class="icon-list__text">{text}</p>
          </div>
        </div>"""


def faq_item(question, answer):
    return f"""      <div class="faq-item">
        <button class="faq-item__question" type="button">
          <span>{question}</span>
          <span class="faq-item__icon"></span>
        </button>
        <div class="faq-item__answer"><p>{answer}</p></div>
      </div>"""


WHY_CHOOSE_ITEMS = [
    ("shield", "One General Contractor", "Single point of accountability from start to finish."),
    ("clipboard", "Clear Scope &amp; Pricing", "Detailed estimates and no surprise add-ons."),
    ("clock", "Professional Project Management", "On-time, on-budget, and organized."),
    ("chat", "Clear Communication", "You'll always know what's happening and why."),
    ("tools", "Quality Craftsmanship", "Skilled trades and premium materials."),
]

PROCESS_STEPS = [
    ("01", "Consultation", "We listen, learn, and understand your goals."),
    ("02", "Planning &amp; Estimate", "We create a plan and provide a detailed estimate."),
    ("03", "Construction", "Skilled craftsmanship and clear communication."),
    ("04", "Final Walkthrough", "We review every detail with you."),
    ("05", "Project Complete", "Beautiful results, built to last."),
]


def service_page(slug, name, tagline, hero_img, intro_title, intro_text, detail_img,
                  what_we_do, price, price_note, project_imgs, faqs, meta_desc,
                  timeline, scope_summary):
    why_choose_html = "\n".join(
        f"""        <div class="feature-grid__item">
          {icon(i, 'feature-grid__icon')}
          <p class="feature-grid__title">{t}</p>
          <p class="feature-grid__text">{d}</p>
        </div>""" for i, t, d in WHY_CHOOSE_ITEMS
    )

    process_html = "\n".join(
        f"""        <div class="process-step">
          <p class="process-step__index">{n}</p>
          <p class="process-step__title">{t}</p>
          <p class="process-step__text">{d}</p>
        </div>""" for n, t, d in PROCESS_STEPS
    )

    what_we_do_html = "\n".join(
        what_we_do_item(i, t, d) for i, t, d in what_we_do
    )

    portfolio_html = "\n".join(
        f"""      <a href="our-work.html" class="portfolio-strip__item">
        <img src="images/{img}.svg" alt="{caption}" loading="lazy" />
        <span class="portfolio-strip__caption">{caption}</span>
      </a>""" for img, caption in project_imgs
    )

    faq_html = "\n".join(faq_item(q, a) for q, a in faqs)

    body = f"""  <section class="hero hero--sm">
    <div class="hero__media"><img src="images/{hero_img}.svg" alt="{name} project" /></div>
    <div class="hero__overlay"></div>
    <div class="container">
      <div class="hero__content">
        <h1 class="hero__title hero__title--h2">{name}</h1>
        <p class="hero__subtitle">{tagline}</p>
        <div class="hero__actions">
          <a class="btn btn--white" href="contact.html">Get an Estimate</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container">
      <div class="section-head">
        <h2>What We Do</h2>
      </div>
      <div class="icon-list icon-list--4">
{what_we_do_html}
      </div>
    </div>
  </section>

  <section class="experience-full">
    <div class="experience-full__media">
      <img src="images/{detail_img}.svg" alt="{name} detail photo" loading="lazy" />
      <div class="experience-full__overlay"></div>
    </div>
    <div class="container">
      <div class="experience-full__content">
        <h2 class="experience-full__title">{intro_title}</h2>
        <p class="experience-full__text">{intro_text}</p>
        <p class="experience-full__text">As a licensed General Contractor, we handle every detail from start to finish with clear communication and dependable execution.</p>
      </div>
    </div>
  </section>

  <section class="section section--navy">
    <div class="container">
      <div class="section-head section-head--light">
        <h2>Why Choose Euro Pros</h2>
      </div>
      <div class="feature-grid feature-grid--5 feature-grid--light">
{why_choose_html}
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container">
      <div class="section-head">
        <h2>Our Process</h2>
      </div>
      <div class="process-steps process-steps--5">
{process_html}
      </div>
    </div>
  </section>

  <section class="portfolio-strip">
    <div class="container">
      <div class="portfolio-strip__head">
        <div>
          <p class="eyebrow-link" style="color:var(--color-text-on-dark-muted);">Portfolio</p>
          <h2 class="portfolio-strip__title">Real {name.split(' ')[0]} Projects</h2>
        </div>
        <p class="portfolio-strip__lead">See how homeowners like you transformed their space with Euro Pros.</p>
      </div>
    </div>
    <div class="portfolio-strip__grid">
{portfolio_html}
    </div>
    <div class="container">
      <div class="portfolio-strip__footer">
        <a href="our-work.html" class="btn btn--outline-light">View All Projects</a>
        <span class="portfolio-strip__tagline">Every project &mdash; real craftsmanship.</span>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="pricing-strip">
        <div class="pricing-strip__main">
          {icon('house', 'pricing-strip__icon')}
          <div>
            <p class="pricing-strip__label">{name} &mdash; Starting at</p>
            <p class="pricing-strip__value">{price}</p>
            <p class="pricing-strip__note">{price_note}</p>
          </div>
        </div>
        <div class="pricing-strip__details">
          <div class="pricing-strip__detail">
            <p class="pricing-strip__detail-label">Typical Timeline</p>
            <p class="pricing-strip__detail-value">{timeline}</p>
          </div>
          <div class="pricing-strip__detail">
            <p class="pricing-strip__detail-label">Warranty</p>
            <p class="pricing-strip__detail-value">2-Year Workmanship Warranty</p>
          </div>
          <div class="pricing-strip__detail">
            <p class="pricing-strip__detail-label">What We Handle</p>
            <p class="pricing-strip__detail-value">{scope_summary}</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container">
      <div class="section-head">
        <h2>Frequently Asked Questions</h2>
      </div>
      <div class="faq">
{faq_html}
      </div>
    </div>
  </section>

  {cta_banner("Ready to Start Your Project?", "Talk to Euro Pros about your " + name.lower() + " project.")}
"""

    write(f"{slug}.html", page(
        title=f"{name} | Euro Pros Construction &amp; Remodeling",
        description=meta_desc,
        active="services",
        body=body,
    ))


service_page(
    slug="bathroom-remodeling",
    name="Bathroom Remodeling",
    tagline="Transform your bathroom into a space you'll love.",
    hero_img="service-bathroom-hero",
    intro_title="Beautiful. Functional. Built to Last.",
    intro_text="Your bathroom should be more than just a functional space — it should be a daily retreat. We combine smart design, quality materials, and expert craftsmanship to create bathrooms that are comfortable, stylish, and built for the way you live.",
    detail_img="service-bathroom-detail",
    what_we_do=[
        ("bathtub", "Bathroom Renovations", "Complete bathroom remodels designed around your needs."),
        ("shower", "Shower Remodeling", "Custom showers with beautiful tile, glass, and fixtures."),
        ("bathtub", "Bathtub Replacement", "Upgrade to a freestanding tub or modern tub/shower."),
        ("tile", "Tile Installation", "Expert tile work for walls, floors, and showers."),
        ("shield", "Waterproofing", "Protect your home with proper moisture control."),
        ("cabinets", "Vanities &amp; Cabinets", "Custom and semi-custom storage solutions."),
        ("flooring", "Flooring", "Durable, water-resistant flooring options."),
        ("lightbulb", "Lighting", "Layered lighting for function and ambiance."),
        ("plumbing", "Plumbing", "Fixture upgrades and plumbing repositioning."),
        ("electrical", "Electrical", "Safe, code-compliant electrical updates."),
        ("paint", "Finishes", "Paint, trim, hardware, and the final details."),
    ],
    price="$12,000+",
    price_note="Starting prices vary depending on project size, existing conditions, materials and scope of work.",
    project_imgs=[
        ("naperville-gallery-2", "Double Vanity &mdash; Naperville, IL"),
        ("naperville-gallery-3", "Freestanding Tub &mdash; Naperville, IL"),
        ("naperville-gallery-1", "Walk-In Shower &mdash; Naperville, IL"),
    ],
    faqs=[
        ("How long does a bathroom remodel take?", "A typical full bathroom remodel takes 3&ndash;6 weeks depending on the scope of work, material availability, and whether plumbing or layout changes are involved."),
        ("What's included in your bathroom remodeling service?", "We handle design, permitting (when required), demolition, plumbing and electrical work, tile and finish installation, and a final walkthrough &mdash; all under one contract."),
        ("Do I need to move out during the remodel?", "Most homeowners stay in their home during a bathroom remodel, especially if you have a second bathroom. We'll walk you through what to expect for your specific project."),
        ("How do I get started?", "Request an estimate, and we'll schedule a consultation to discuss your goals, walk your space, and provide a detailed plan and pricing."),
        ("Are you licensed and insured?", "Yes. Euro Pros is a licensed General Contractor and fully insured for your protection."),
        ("Do you offer a warranty?", "Yes. Every bathroom remodel is backed by our 2-year workmanship warranty, with check-ins at 1 month and 1 year after completion."),
        ("Do I need a permit for a bathroom remodel?", "Permits are typically required when plumbing, electrical, or layout changes are involved. We handle the permitting process for you as part of our project management."),
    ],
    meta_desc="Bathroom remodeling in the Chicago suburbs. Licensed General Contractor, starting at $12,000+. Get a free estimate from Euro Pros.",
    timeline="3&ndash;6 Weeks",
    scope_summary="Design, permits, demolition, plumbing &amp; electrical, tile and finishes &mdash; all under one contract.",
)

service_page(
    slug="basement-remodeling",
    name="Basement Remodeling",
    tagline="Turn your basement into comfortable, versatile living space.",
    hero_img="service-basement-hero",
    intro_title="More Living Space, Built Right.",
    intro_text="A finished basement adds real, everyday living space to your home &mdash; a family room, home office, gym, or guest suite. We handle framing, moisture control, egress, and finishes so your new space is comfortable, code-compliant, and built to last.",
    detail_img="service-basement-detail",
    what_we_do=[
        ("house", "Basement Finishing", "Full basement remodels designed around how you'll use the space."),
        ("shield", "Waterproofing &amp; Moisture Control", "Proper drainage and vapor barriers to protect your investment."),
        ("layout", "Framing &amp; Layout", "Smart layouts for family rooms, offices, gyms, and more."),
        ("drywall", "Drywall &amp; Ceilings", "Clean, finished walls and ceilings, including drop ceilings."),
        ("flooring", "Flooring", "Moisture-resistant flooring built for below-grade spaces."),
        ("lightbulb", "Lighting", "Recessed and layered lighting for a bright, inviting space."),
        ("plumbing", "Plumbing", "Wet bars, bathrooms, and utility rework."),
        ("electrical", "Electrical", "Outlets, circuits, and fixtures to code."),
        ("window", "Egress Windows", "Code-compliant egress for bedrooms and safety."),
        ("hvac", "HVAC Extensions", "Comfortable heating and cooling for the new space."),
        ("paint", "Finishes", "Trim, paint, and the final details that make it feel like home."),
    ],
    price="$25,000+",
    price_note="Starting prices vary depending on project size, existing conditions, materials and scope of work.",
    project_imgs=[
        ("project-basement-retreat", "Family Room &mdash; Wheaton, IL"),
        ("project-basement-entertainment", "Entertainment Space &mdash; Glenview, IL"),
        ("work-basement", "Basement Remodel &mdash; Chicago Suburbs"),
    ],
    faqs=[
        ("How long does a basement remodel take?", "Most basement remodels take 6&ndash;10 weeks depending on size, layout complexity, and whether a bathroom is included."),
        ("Do I need a permit to finish my basement?", "In most Chicago suburbs, yes. We handle the permitting process for you, including egress requirements for any bedrooms."),
        ("Can you add a bathroom or wet bar?", "Yes &mdash; plumbing rough-in for a bathroom or wet bar is one of the most popular basement upgrades we install."),
        ("What about moisture or past water issues?", "We assess drainage and moisture conditions before finishing and recommend waterproofing steps so your new space stays dry."),
        ("How do I get started?", "Request an estimate and we'll schedule a walkthrough to discuss layout options, budget, and timeline."),
        ("Are you licensed and insured?", "Yes. Euro Pros is a licensed General Contractor and fully insured for your protection."),
        ("Do you offer a warranty?", "Yes. Every basement remodel is backed by our 2-year workmanship warranty, with check-ins at 1 month and 1 year after completion."),
    ],
    meta_desc="Basement remodeling in the Chicago suburbs. Licensed General Contractor, starting at $25,000+. Get a free estimate from Euro Pros.",
    timeline="6&ndash;10 Weeks",
    scope_summary="Framing, waterproofing, electrical, plumbing rough-in, drywall, flooring and finishes &mdash; all under one contract.",
)

service_page(
    slug="kitchen-remodeling",
    name="Kitchen Remodeling",
    tagline="Modern kitchens built for everyday living and effortless entertaining.",
    hero_img="service-kitchen-hero",
    intro_title="The Heart of Your Home, Reimagined.",
    intro_text="Whether it's a full layout change or a refresh of cabinets, counters, and finishes, we design kitchens that work for how your family actually lives &mdash; then build them with quality materials and skilled craftsmanship.",
    detail_img="service-kitchen-detail",
    what_we_do=[
        ("house", "Full Kitchen Remodels", "Layout changes, islands, and complete transformations."),
        ("cabinets", "Cabinetry", "Custom and semi-custom cabinets built to fit your space."),
        ("tile", "Countertops &amp; Backsplash", "Quartz, stone, and tile surfaces built to last."),
        ("flooring", "Flooring", "Durable flooring options for high-traffic kitchens."),
        ("lightbulb", "Lighting", "Task, ambient, and accent lighting layered for function."),
        ("plumbing", "Plumbing", "Sink, faucet, and appliance plumbing updates."),
        ("electrical", "Electrical", "Circuits and outlets for modern kitchen appliances."),
        ("layout", "Layout &amp; Islands", "Open-concept layouts and functional islands."),
        ("paint", "Finishes", "Paint, trim, and hardware for a cohesive look."),
    ],
    price="$35,000+",
    price_note="Starting prices vary depending on project size, existing conditions, materials and scope of work.",
    project_imgs=[
        ("work-kitchen", "Kitchen Island &mdash; Chicago Suburbs"),
        ("project-transitional-kitchen", "Transitional Kitchen &mdash; Elmhurst, IL"),
        ("project-timeless-kitchen", "Timeless Kitchen &mdash; Westmont, IL"),
    ],
    faqs=[
        ("How long does a kitchen remodel take?", "Most kitchen remodels take 6&ndash;12 weeks depending on scope, whether the layout is changing, and material lead times."),
        ("Can you change my kitchen layout?", "Yes &mdash; we regularly move walls, relocate plumbing and electrical, and reconfigure layouts to open up the space."),
        ("What's included in your kitchen remodeling service?", "Design, cabinetry, countertops, plumbing and electrical, flooring, and finishes &mdash; all managed under one contract."),
        ("Do you help choose materials and finishes?", "Yes, our team can guide you through cabinet, countertop, and finish selections that fit your style and budget."),
        ("How do I get started?", "Request an estimate and we'll schedule a consultation to talk through your goals and provide a detailed plan."),
        ("Are you licensed and insured?", "Yes. Euro Pros is a licensed General Contractor and fully insured for your protection."),
        ("Do you offer a warranty?", "Yes. Every kitchen remodel is backed by our 2-year workmanship warranty, with check-ins at 1 month and 1 year after completion."),
    ],
    meta_desc="Kitchen remodeling in the Chicago suburbs. Licensed General Contractor, starting at $35,000+. Get a free estimate from Euro Pros.",
    timeline="6&ndash;12 Weeks",
    scope_summary="Design, cabinetry, countertops, plumbing &amp; electrical, flooring and finishes &mdash; all under one contract.",
)

service_page(
    slug="whole-home-remodeling",
    name="Whole-Home Remodeling",
    tagline="Reimagine your entire home with cohesive design and quality craftsmanship.",
    hero_img="service-whole-home-hero",
    intro_title="One Contractor for Your Entire Home.",
    intro_text="From multiple rooms to a full-home transformation, we coordinate every trade and phase under one team &mdash; so your project stays organized, on schedule, and cohesive from room to room.",
    detail_img="service-whole-home-detail",
    what_we_do=[
        ("house", "Whole-Home Renovations", "Multi-room and full-home remodeling under one contract."),
        ("layout", "Layout Changes", "Open-concept living, additions, and reconfigured floor plans."),
        ("cabinets", "Kitchens &amp; Baths", "Coordinated kitchen and bathroom remodeling."),
        ("flooring", "Flooring", "Consistent, durable flooring throughout your home."),
        ("lightbulb", "Lighting", "Whole-home lighting design and updates."),
        ("plumbing", "Plumbing", "Full plumbing updates and repositioning."),
        ("electrical", "Electrical", "Panel upgrades and whole-home electrical work."),
        ("hvac", "HVAC", "Heating and cooling updates for your renovated space."),
        ("paint", "Finishes", "Cohesive paint, trim, and hardware throughout."),
    ],
    price="$75,000+",
    price_note="Starting prices vary depending on project size, existing conditions, materials and scope of work.",
    project_imgs=[
        ("work-whole-home", "Living Room &mdash; Chicago Suburbs"),
        ("project-downers", "Whole-Home Remodel &mdash; Downers Grove, IL"),
        ("downers-gallery-1", "Open-Concept Living &mdash; Downers Grove, IL"),
    ],
    faqs=[
        ("How long does a whole-home remodel take?", "Whole-home projects typically take 4&ndash;9 months depending on square footage, scope, and whether structural changes are involved."),
        ("Can you manage a project with multiple rooms at once?", "Yes &mdash; this is exactly what whole-home remodeling is built for. One team, one schedule, one point of contact for every trade."),
        ("Do you handle additions and structural changes?", "Yes, we manage structural changes, additions, and permitting as part of whole-home projects."),
        ("Can I stay in my home during the remodel?", "It depends on the scope. We'll walk you through what to expect and can phase work to minimize disruption where possible."),
        ("How do I get started?", "Request an estimate and we'll schedule a consultation to understand your goals across the whole home."),
        ("Are you licensed and insured?", "Yes. Euro Pros is a licensed General Contractor and fully insured for your protection."),
        ("Do you offer a warranty?", "Yes. Every whole-home project is backed by our 2-year workmanship warranty, with check-ins at 1 month and 1 year after completion."),
    ],
    meta_desc="Whole-home remodeling in the Chicago suburbs. Licensed General Contractor, starting at $75,000+. Get a free estimate from Euro Pros.",
    timeline="4&ndash;9 Months",
    scope_summary="Design, structural changes, and every trade and finish across your home &mdash; coordinated under one contractor.",
)


# ==================================================== NEW HOME CONSTRUCTION
NC_WHY = [
    ("person", "Your General Contractor", "We are a licensed General Contractor with the experience and resources to build beautiful, lasting homes."),
    ("house", "Construction Experience", "Years of hands-on experience building custom homes throughout the Chicago suburbs."),
    ("clipboard", "Clear Project Management", "Proactive planning, transparent timelines, and consistent communication keep your project on track."),
    ("contact", "One Point of Contact", "One contractor. One team. One dedicated point of contact from start to finish."),
]

NC_STEPS = [
    ("1", "Plans &amp;<br />Pre-Construction", "step-plans"),
    ("2", "Permits", "step-permits"),
    ("3", "Site Work", "step-sitework"),
    ("4", "Foundation", "step-foundation"),
    ("5", "Framing", "step-framing"),
    ("6", "Plumbing,<br />Electrical &amp; HVAC", "step-mep"),
    ("7", "Insulation &amp;<br />Drywall", "step-insulation"),
    ("8", "Interior<br />Finishes", "step-interior"),
    ("9", "Final<br />Inspections &amp;<br />Completion", "step-final"),
]

NC_COORDINATE = [
    ("excavation", "Excavation", "Safe, precise excavation and grading."),
    ("foundation", "Foundation", "Strong, code-compliant foundations built to last."),
    ("framing", "Framing", "Expert framing for structural integrity."),
    ("roof", "Roofing", "Quality roof systems that protect your home."),
    ("window", "Windows &amp; Exterior", "High-performance windows and beautiful exteriors."),
    ("plumbing", "Plumbing", "Rough-in and trim plumbing installed to code."),
    ("electrical", "Electrical", "Complete electrical systems for safety and performance."),
    ("hvac", "HVAC", "Efficient heating and cooling designed for your home."),
    ("insulation", "Insulation", "Energy-efficient insulation for year-round comfort."),
    ("drywall", "Drywall", "Smooth, professional drywall installation and finishing."),
    ("flooring", "Flooring", "Durable, beautiful flooring installed with care."),
    ("cabinets", "Cabinets", "Custom and semi-custom cabinetry solutions."),
    ("tile", "Tile", "Precision tile work in kitchens, baths, and beyond."),
    ("paint", "Painting", "Clean, detailed painting throughout your home."),
    ("trim", "Trim &amp; Finish Work", "Crown, baseboards, doors, and custom millwork."),
]

NC_FAQ = [
    ("How long does it take to build a new home?", "Most custom homes take 9&ndash;14 months from groundbreaking to completion, depending on size, design complexity, and permitting timelines."),
    ("What areas do you serve?", "We build throughout the Chicago suburbs, including Naperville, Arlington Heights, Glenview, Wheaton, Downers Grove, Elmhurst, and surrounding communities."),
    ("Can you build from our plans?", "Yes &mdash; we can build from your architect's plans, or work with our design partners to develop plans for your new home."),
    ("Do you help with permits and approvals?", "Yes, we manage the permitting and approval process with local municipalities as part of every new construction project."),
    ("How do you keep my project on schedule and on budget?", "We provide a detailed schedule and budget up front, assign a dedicated project manager, and give you regular updates throughout construction."),
    ("What is included in your pricing?", "Our estimates cover site work, materials, labor, permits, and project management. We'll walk through exactly what's included during your consultation."),
]

nc_why_html = "\n".join(
    f"""        <div class="feature-grid__item">
          {icon(i, 'feature-grid__icon')}
          <p class="feature-grid__title">{t}</p>
          <p class="feature-grid__text">{d}</p>
        </div>""" for i, t, d in NC_WHY
)

nc_steps_row = "\n".join(
    f"""        <div class="step-row__step">
          <div class="step-row__circle">{n}</div>
          <span class="step-row__label">{label}</span>
        </div>""" for n, label, _img in NC_STEPS
)

nc_steps_photos = "\n".join(
    f'        <img src="images/{img}.svg" alt="{label.replace("<br />", " ")} construction phase" loading="lazy" />'
    for _n, label, img in NC_STEPS
)

nc_coordinate_html = "\n".join(
    f"""        <div class="icon-list__item">
          {icon(i, 'icon-list__icon')}
          <div>
            <p class="icon-list__title">{t}</p>
            <p class="icon-list__text">{d}</p>
          </div>
        </div>""" for i, t, d in NC_COORDINATE
)

nc_faq_html = "\n".join(faq_item(q, a) for q, a in NC_FAQ)

new_construction_body = f"""  <section class="hero hero--sm">
    <div class="hero__media"><img src="images/new-construction-hero.svg" alt="Custom new home construction" /></div>
    <div class="hero__overlay"></div>
    <div class="container">
      <div class="hero__content">
        <h1 class="hero__title hero__title--h2">New Home Construction</h1>
        <p class="hero__subtitle">From plans to completion, Euro Pros manages your new home construction project.</p>
        <div class="hero__actions">
          <a class="btn btn--outline-light" href="contact.html">Discuss Your Project</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <h2>Why Choose Euro Pros for New Construction</h2>
      </div>
      <div class="feature-grid">
{nc_why_html}
      </div>
    </div>
  </section>

  <section class="section section--navy">
    <div class="container">
      <div class="section-head">
        <h2 style="color:#fff;">Our New Home Construction Process</h2>
      </div>
      <div class="step-row">
{nc_steps_row}
      </div>
      <div class="step-photos">
{nc_steps_photos}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="why-us">
        <div class="why-us__content">
          <h2 class="why-us__title">One Contractor. One Point of Contact. Total Accountability.</h2>
          <p style="color:var(--color-text-muted);margin-top:var(--space-md);max-width:46ch;">We manage every detail of your new home from start to finish. You'll work with a dedicated project manager who coordinates our team, our trade partners, and the schedule &mdash; so you always know what's happening and what's next.</p>
        </div>
        <div class="why-us__media">
          <img src="images/experience-kitchen.svg" alt="Finished new home kitchen" loading="lazy" />
        </div>
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container">
      <div class="section-head">
        <h2>What We Coordinate</h2>
      </div>
      <div class="icon-list">
{nc_coordinate_html}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <h2>New Home Construction FAQ</h2>
      </div>
      <div class="faq">
{nc_faq_html}
      </div>
    </div>
  </section>

  {cta_banner("Planning to Build a New Home?", "Let's bring your vision to life &mdash; on time and built to last.", button_label="Discuss Your Project")}
"""

write("new-home-construction.html", page(
    title="New Home Construction | Euro Pros Construction &amp; Remodeling",
    description="Custom new home construction in the Chicago suburbs. Euro Pros manages plans, permits, site work, and every phase of your build.",
    active="services",
    body=new_construction_body,
))


# ============================================================== OUR WORK ===
PROJECTS = [
    dict(slug="project-naperville-bathroom-remodel", title="Modern Spa Bathroom", h1="Naperville Bathroom Remodel",
         category="Bathrooms", cat_value="bathrooms", location="Naperville, IL", card_img="project-naperville"),
    dict(slug="project-wheaton-basement-retreat", title="Finished Basement Retreat", h1="Finished Basement Retreat",
         category="Basements", cat_value="basements", location="Wheaton, IL", card_img="project-basement-retreat"),
    dict(slug="project-elmhurst-transitional-kitchen", title="Transitional Kitchen", h1="Transitional Kitchen",
         category="Kitchens", cat_value="kitchens", location="Elmhurst, IL", card_img="project-transitional-kitchen"),
    dict(slug="project-downers-grove-whole-home", title="Whole-Home Remodel", h1="Whole-Home Remodel",
         category="Whole-Home", cat_value="whole-home", location="Downers Grove, IL", card_img="project-downers"),
    dict(slug="project-barrington-custom-new-home", title="Custom New Home", h1="Custom New Home",
         category="New Construction", cat_value="new-construction", location="Barrington, IL", card_img="project-custom-new-home"),
    dict(slug="project-oak-brook-classic-bathroom", title="Classic Bathroom Renovation", h1="Classic Bathroom Renovation",
         category="Bathrooms", cat_value="bathrooms", location="Oak Brook, IL", card_img="project-classic-bathroom"),
    dict(slug="project-glenview-basement-entertainment", title="Basement Entertainment Space", h1="Basement Entertainment Space",
         category="Basements", cat_value="basements", location="Glenview, IL", card_img="project-basement-entertainment"),
    dict(slug="project-westmont-timeless-kitchen", title="Timeless Kitchen Remodel", h1="Timeless Kitchen Remodel",
         category="Kitchens", cat_value="kitchens", location="Westmont, IL", card_img="project-timeless-kitchen"),
]

FILTER_TABS = [
    ("all", "All"),
    ("bathrooms", "Bathrooms"),
    ("basements", "Basements"),
    ("kitchens", "Kitchens"),
    ("whole-home", "Whole-Home"),
    ("new-construction", "New Construction"),
]

tabs_html = "\n".join(
    f'        <a href="#" data-filter="{val}" class="{"is-active" if val == "all" else ""}">{label}</a>'
    for val, label in FILTER_TABS
)

project_cards_html = "\n".join(f"""        <a href="{p['slug']}.html" class="project-card" data-category="{p['cat_value']}" data-filter-target="work">
          <div class="project-card__media">
            <img src="images/{p['card_img']}.svg" alt="{p['title']}" loading="lazy" />
          </div>
          <h3 class="project-card__title">{p['title']}</h3>
          <div class="project-card__meta">
            <p class="project-card__location">{p['category']}<br />{p['location']}</p>
            <span class="project-card__view">View Project &rarr;</span>
          </div>
        </a>""" for p in PROJECTS)

pagination_html = """      <div class="pagination">
        <a href="#" class="is-active">1</a>
        <a href="#">2</a>
        <a href="#">3</a>
        <span>&hellip;</span>
        <a href="#">10</a>
        <a href="#">Next &rarr;</a>
      </div>
      <p style="text-align:center;margin-top:var(--space-lg);">
        <a class="btn btn--outline-dark" href="#">Load More</a>
      </p>"""

our_work_body = f"""  <section class="hero hero--sm">
    <div class="hero__media"><img src="images/our-work-hero-photo.svg" alt="Euro Pros finished kitchen remodel" /></div>
    <div class="hero__overlay"></div>
    <div class="container">
      <div class="hero__content">
        <h1 class="hero__title hero__title--h2">Our Work</h1>
        <p class="hero__subtitle">Real projects. Real results.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="tabs-row" data-filter-group="work">
{tabs_html}
      </div>

      <p class="gallery-note">Replace with verified Euro Pros project photography.</p>

      <div class="projects-grid projects-grid--gallery">
{project_cards_html}
      </div>

{pagination_html}
    </div>
  </section>

  <section class="final-cta section--navy">
    <div class="container">
      <h2 class="final-cta__title">Have a Similar Project?</h2>
      <div class="final-cta__actions">
        <a class="btn btn--white" href="contact.html">Get an Estimate</a>
      </div>
    </div>
  </section>
"""

write("our-work.html", page(
    title="Our Work | Euro Pros Construction &amp; Remodeling",
    description="Browse bathroom, basement, kitchen, whole-home, and new construction projects by Euro Pros in the Chicago suburbs.",
    active="work",
    body=our_work_body,
))


# ========================================================= PROJECT DETAIL ===
def project_overview_row(location, ptype, scope):
    return f"""      <div class="project-overview">
        <div class="project-overview__item">
          {icon('pin', 'project-overview__icon')}
          <span class="project-overview__label">Location</span>
          <span class="project-overview__value">{location}</span>
        </div>
        <div class="project-overview__item">
          {icon('house', 'project-overview__icon')}
          <span class="project-overview__label">Project Type</span>
          <span class="project-overview__value">{ptype}</span>
        </div>
        <div class="project-overview__item">
          {icon('checklist', 'project-overview__icon')}
          <span class="project-overview__label">Scope</span>
          <span class="project-overview__value">{scope}</span>
        </div>
      </div>"""


def project_detail_full(p):
    """Rich template used for the fully-detailed Naperville example."""
    body = f"""  <section class="hero hero--sm">
    <div class="hero__media"><img src="images/naperville-hero.svg" alt="{p['h1']}" /></div>
    <div class="hero__overlay"></div>
    <div class="container">
      <div class="hero__content">
        <h1 class="hero__title hero__title--h2">{p['h1']}</h1>
        <p class="hero__meta">Bathroom Remodeling &nbsp;|&nbsp; {p['location']}</p>
      </div>
    </div>
  </section>

  <section class="section" style="padding-bottom:0;">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow" style="display:block;">Project Overview</span>
      </div>
{project_overview_row(p['location'], 'Bathroom Remodeling', 'Full bathroom renovation')}
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="challenge-solution">
        <div>
          <p class="challenge-solution__label">The Challenge</p>
          <img src="images/naperville-challenge.svg" alt="Before photo of outdated bathroom" />
          <p>The existing bathroom was outdated, cramped, and lacked functionality. Dark finishes, an inefficient layout, and minimal storage made the space feel smaller and didn't meet the homeowners' needs for comfort or style.</p>
        </div>
        <div>
          <p class="challenge-solution__label">Our Solution</p>
          <p style="margin-bottom:var(--space-md);">We completely reimagined the space with a bright, open layout and high-quality finishes. A custom vanity, spacious walk-in shower, and thoughtful storage solutions create a bathroom that is both beautiful and functional.</p>
          <ul class="challenge-solution__checklist">
            <li>{icon('check-circle')} Improved layout for better flow and functionality</li>
            <li>{icon('check-circle')} Premium finishes for a timeless, modern look</li>
            <li>{icon('check-circle')} Custom vanity with ample storage</li>
            <li>{icon('check-circle')} Walk-in shower with niche and glass enclosure</li>
            <li>{icon('check-circle')} Upgraded plumbing and efficient fixtures</li>
            <li>{icon('check-circle')} Bright, neutral design for a clean, spa-like feel</li>
          </ul>
        </div>
      </div>

      <div class="section-head">
        <span class="eyebrow" style="display:block;">Before &amp; After</span>
      </div>
      <div class="before-after">
        <div class="before-after__item">
          <span class="before-after__tag">Before</span>
          <img src="images/process-before.svg" alt="Bathroom before remodel" />
        </div>
        <div class="before-after__item">
          <span class="before-after__tag">After</span>
          <img src="images/process-after.svg" alt="Bathroom after remodel" />
        </div>
      </div>

      <div class="section-head">
        <span class="eyebrow" style="display:block;">Project Gallery</span>
      </div>
      <div class="gallery-grid">
        <img src="images/naperville-gallery-1.svg" alt="Walk-in shower" loading="lazy" />
        <img src="images/naperville-gallery-2.svg" alt="Double vanity" loading="lazy" />
        <img src="images/naperville-gallery-3.svg" alt="Freestanding tub" loading="lazy" />
        <img src="images/naperville-gallery-4.svg" alt="Tiled niche" loading="lazy" />
        <img src="images/naperville-gallery-5.svg" alt="Matte black fixtures" loading="lazy" />
        <img src="images/naperville-gallery-6.svg" alt="Custom linen cabinet" loading="lazy" />
      </div>

      <div class="section-head">
        <span class="eyebrow" style="display:block;">Client Review</span>
      </div>
      <div class="review-placeholder">
        {icon('star')}
        <p>Verified client review to be added.</p>
      </div>
    </div>
  </section>

  {cta_banner("Planning a Similar Project?", "Let's bring your vision to life with expert planning and craftsmanship.")}
"""
    write(f"{p['slug']}.html", page(
        title=f"{p['h1']} | Euro Pros Construction &amp; Remodeling",
        description=f"{p['h1']} in {p['location']} by Euro Pros &mdash; a licensed General Contractor serving the Chicago suburbs.",
        active="work",
        body=body,
    ))


SIMPLE_PROJECT_DETAILS = {
    "project-wheaton-basement-retreat": dict(
        ptype="Basement Remodeling", scope="Full basement finish", hero="wheaton-hero",
        challenge="This unfinished basement was cold, dark storage space with exposed framing and no real function beyond utility access.",
        solution="We finished the space into a warm family retreat with a built-in entertainment wall, durable flooring, and layered lighting &mdash; built to stay comfortable and dry year-round.",
        bullets=["Custom built-in entertainment center", "Moisture-resistant flooring throughout", "Recessed and accent lighting", "Egress window for natural light and safety"],
        gallery=["project-basement-retreat", "work-basement", "downers-gallery-1"],
    ),
    "project-elmhurst-transitional-kitchen": dict(
        ptype="Kitchen Remodeling", scope="Full kitchen renovation", hero="elmhurst-hero",
        challenge="A closed-off, dated kitchen with limited counter space made everyday cooking and entertaining difficult for this growing family.",
        solution="We opened the layout, added a large island, and installed transitional cabinetry and finishes that balance classic and modern style.",
        bullets=["Open-concept layout with new island", "Custom cabinetry to the ceiling", "Quartz countertops and tile backsplash", "Upgraded lighting and electrical"],
        gallery=["project-transitional-kitchen", "work-kitchen", "project-timeless-kitchen"],
    ),
    "project-barrington-custom-new-home": dict(
        ptype="New Home Construction", scope="Custom new home build", hero="barrington-hero",
        challenge="The homeowners wanted a custom home built from the ground up on their Barrington lot &mdash; with one contractor managing the entire process.",
        solution="Euro Pros managed the project from plans and permits through final inspection, coordinating every trade under one dedicated project manager.",
        bullets=["Custom floor plan built to the homeowners' goals", "One point of contact through every phase", "Energy-efficient systems and finishes", "On-time, on-budget delivery"],
        gallery=["project-custom-new-home", "work-new-construction", "why-framing"],
    ),
    "project-oak-brook-classic-bathroom": dict(
        ptype="Bathroom Remodeling", scope="Full bathroom renovation", hero="oakbrook-hero",
        challenge="A dated, dimly-lit bathroom with worn finishes no longer matched the rest of this Oak Brook home.",
        solution="We reimagined the space with a classic, timeless palette, updated fixtures, and a spa-inspired walk-in shower.",
        bullets=["Classic tile and finish palette", "New walk-in shower with glass enclosure", "Updated vanity and lighting", "Improved layout and storage"],
        gallery=["project-classic-bathroom", "naperville-gallery-2", "naperville-gallery-5"],
    ),
    "project-glenview-basement-entertainment": dict(
        ptype="Basement Remodeling", scope="Basement entertainment space", hero="glenview-basement-hero",
        challenge="This basement had potential but no real design &mdash; just unused open space beneath the main living areas.",
        solution="We built out a dedicated entertainment space with a media wall, wet bar rough-in, and durable, stylish finishes for everyday use.",
        bullets=["Media wall with built-in shelving", "Wet bar plumbing rough-in", "Durable, low-maintenance flooring", "Layered lighting for movie nights and gatherings"],
        gallery=["project-basement-entertainment", "project-basement-retreat", "work-basement"],
    ),
    "project-westmont-timeless-kitchen": dict(
        ptype="Kitchen Remodeling", scope="Full kitchen renovation", hero="westmont-hero",
        challenge="An outdated kitchen layout with limited storage and dated finishes didn't fit how this family cooks and entertains.",
        solution="We redesigned the layout for better flow, added custom cabinetry, and selected timeless finishes that will hold up for years to come.",
        bullets=["Redesigned layout for better flow", "Custom cabinetry with expanded storage", "Timeless stone countertops", "New lighting and updated electrical"],
        gallery=["project-timeless-kitchen", "work-kitchen", "project-transitional-kitchen"],
    ),
}


def project_detail_simple(p):
    d = SIMPLE_PROJECT_DETAILS[p["slug"]]
    bullets_html = "\n".join(f"            <li>{icon('check-circle')} {b}</li>" for b in d["bullets"])
    p_title = p["h1"]
    gallery_html = "\n".join(
        f'        <img src="images/{img}.svg" alt="{p_title} gallery photo" loading="lazy" />' for img in d["gallery"]
    )
    body = f"""  <section class="hero hero--sm">
    <div class="hero__media"><img src="images/{d['hero']}.svg" alt="{p['h1']}" /></div>
    <div class="hero__overlay"></div>
    <div class="container">
      <div class="hero__content">
        <h1 class="hero__title hero__title--h2">{p['h1']}</h1>
        <p class="hero__meta">{d['ptype']} &nbsp;|&nbsp; {p['location']}</p>
      </div>
    </div>
  </section>

  <section class="section" style="padding-bottom:0;">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow" style="display:block;">Project Overview</span>
      </div>
{project_overview_row(p['location'], d['ptype'], d['scope'])}
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="challenge-solution">
        <div>
          <p class="challenge-solution__label">The Challenge</p>
          <p>{d['challenge']}</p>
        </div>
        <div>
          <p class="challenge-solution__label">Our Solution</p>
          <p style="margin-bottom:var(--space-md);">{d['solution']}</p>
          <ul class="challenge-solution__checklist">
{bullets_html}
          </ul>
        </div>
      </div>

      <div class="section-head">
        <span class="eyebrow" style="display:block;">Project Gallery</span>
      </div>
      <div class="gallery-grid">
{gallery_html}
      </div>

      <div class="review-placeholder">
        {icon('star')}
        <p>Verified client review to be added.</p>
      </div>
    </div>
  </section>

  {cta_banner("Planning a Similar Project?", "Let's bring your vision to life with expert planning and craftsmanship.")}
"""
    write(f"{p['slug']}.html", page(
        title=f"{p['h1']} | Euro Pros Construction &amp; Remodeling",
        description=f"{p['h1']} in {p['location']} by Euro Pros &mdash; a licensed General Contractor serving the Chicago suburbs.",
        active="work",
        body=body,
    ))


for _p in PROJECTS:
    if _p["slug"] == "project-naperville-bathroom-remodel":
        project_detail_full(_p)
    elif _p["slug"] == "project-downers-grove-whole-home":
        pass  # built separately below with its own richer content
    else:
        project_detail_simple(_p)

# Downers Grove gets a slightly richer template (before/after) since it's reused from the home page
downers = next(p for p in PROJECTS if p["slug"] == "project-downers-grove-whole-home")
downers_body = f"""  <section class="hero hero--sm">
    <div class="hero__media"><img src="images/downers-hero.svg" alt="{downers['h1']}" /></div>
    <div class="hero__overlay"></div>
    <div class="container">
      <div class="hero__content">
        <h1 class="hero__title hero__title--h2">{downers['h1']}</h1>
        <p class="hero__meta">Whole-Home Remodeling &nbsp;|&nbsp; {downers['location']}</p>
      </div>
    </div>
  </section>

  <section class="section" style="padding-bottom:0;">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow" style="display:block;">Project Overview</span>
      </div>
{project_overview_row(downers['location'], 'Whole-Home Remodeling', 'Multi-room whole-home renovation')}
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="challenge-solution">
        <div>
          <p class="challenge-solution__label">The Challenge</p>
          <img src="images/downers-challenge.svg" alt="Before photo of closed-off layout" />
          <p>A choppy, closed-off floor plan separated the kitchen, dining, and living areas, making the home feel smaller and less functional for a growing family.</p>
        </div>
        <div>
          <p class="challenge-solution__label">Our Solution</p>
          <p style="margin-bottom:var(--space-md);">We opened the main floor into a cohesive, open-concept layout and refreshed the kitchen, living spaces, and primary suite with consistent, elevated finishes throughout.</p>
          <ul class="challenge-solution__checklist">
            <li>{icon('check-circle')} Open-concept kitchen, dining, and living layout</li>
            <li>{icon('check-circle')} New kitchen island and custom cabinetry</li>
            <li>{icon('check-circle')} Refreshed primary suite</li>
            <li>{icon('check-circle')} Consistent flooring and finishes throughout</li>
            <li>{icon('check-circle')} Updated lighting and electrical</li>
            <li>{icon('check-circle')} One contractor managing every trade</li>
          </ul>
        </div>
      </div>

      <div class="section-head">
        <span class="eyebrow" style="display:block;">Project Gallery</span>
      </div>
      <div class="gallery-grid">
        <img src="images/downers-gallery-1.svg" alt="Open-concept living space" loading="lazy" />
        <img src="images/downers-gallery-2.svg" alt="Kitchen island" loading="lazy" />
        <img src="images/downers-gallery-3.svg" alt="Primary suite" loading="lazy" />
      </div>

      <div class="review-placeholder">
        {icon('star')}
        <p>Verified client review to be added.</p>
      </div>
    </div>
  </section>

  {cta_banner("Planning a Similar Project?", "Let's bring your vision to life with expert planning and craftsmanship.")}
"""
write("project-downers-grove-whole-home.html", page(
    title=f"{downers['h1']} | Euro Pros Construction &amp; Remodeling",
    description=f"{downers['h1']} in {downers['location']} by Euro Pros &mdash; a licensed General Contractor serving the Chicago suburbs.",
    active="work",
    body=downers_body,
))


# ============================================================ OUR PROCESS ===
PROCESS_ROWS = [
    ("01", "Consultation", "We learn about your goals, budget, and timeline. We walk your space, answer questions, and discuss possibilities.", "process-consultation", "media-first"),
    ("02", "Planning &amp; Estimate", "We develop a plan tailored to your project and provide a detailed, transparent estimate so you know exactly what to expect.", "process-planning", "content-first"),
    ("03", "Scheduling &amp; Preparation", "We finalize the schedule, order materials, secure permits, and prepare your home for a smooth start.", "process-scheduling", "media-first"),
    ("04", "Construction", "Our team gets to work. We manage daily progress, maintain a clean job site, and keep you informed every step of the way.", "process-construction", "content-first"),
    ("05", "Final Walkthrough", "We review every detail with you to ensure you're 100% satisfied. We don't consider the job complete until you are.", "process-walkthrough", "media-first"),
]

TIMELINE_STEPS = [
    ("clipboard", "Scope"),
    ("checklist", "Contract"),
    ("clock", "Schedule"),
    ("shield", "Permits"),
    ("hardhat", "Construction"),
    ("check-circle", "Inspections"),
    ("house", "Completion"),
]

process_rows_html = []
for n, title, text, img, order in PROCESS_ROWS:
    media_html = f'<div class="process-row__media"><img src="images/{img}.svg" alt="{title.replace("&amp;", "and")}" loading="lazy" /></div>'
    content_html = f"""<div class="process-row__content">
          <p class="process-row__index">{n}</p>
          <h3 class="process-row__title">{title}</h3>
          <p class="process-row__text">{text}</p>
        </div>"""
    if order == "media-first":
        process_rows_html.append(f'      <div class="process-row">\n        {media_html}\n        {content_html}\n      </div>')
    else:
        process_rows_html.append(f'      <div class="process-row">\n        {content_html}\n        {media_html}\n      </div>')
process_rows_html = "\n".join(process_rows_html)

timeline_html = []
for i, (icon_name, label) in enumerate(TIMELINE_STEPS):
    if i > 0:
        timeline_html.append('        <div class="icon-timeline__connector"></div>')
    timeline_html.append(f"""        <div class="icon-timeline__step">
          <div class="icon-timeline__circle">{icon(icon_name)}</div>
          <span class="icon-timeline__label">{label}</span>
        </div>""")
timeline_html = "\n".join(timeline_html)

our_process_body = f"""  <section class="hero hero--sm">
    <div class="hero__media"><img src="images/service-kitchen-hero.svg" alt="Bathroom remodeling in progress" /></div>
    <div class="hero__overlay"></div>
    <div class="container">
      <div class="hero__content">
        <h1 class="hero__title hero__title--h2">Our Process</h1>
        <p class="hero__subtitle">A clear, organized process from the first consultation to the final walkthrough.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="process-rows">
{process_rows_html}
      </div>
    </div>
  </section>

  <section class="section section--navy">
    <div class="container">
      <p class="eyebrow eyebrow--on-dark" style="text-align:center;">For Larger Projects</p>
      <div class="icon-timeline">
{timeline_html}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="why-us">
        <div class="why-us__content">
          <h2 class="why-us__title">Clear Communication From Start to Finish</h2>
          <p style="color:var(--color-text-muted);margin-top:var(--space-md);max-width:44ch;">We believe great projects start with great communication. You'll have a dedicated point of contact and regular updates so you always know what's happening.</p>
        </div>
        <div class="why-us__media">
          <img src="images/process-communication.svg" alt="Euro Pros team discussing a project" loading="lazy" />
        </div>
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container" style="display:flex;gap:var(--space-md);align-items:flex-start;justify-content:center;text-align:left;max-width:820px;margin-inline:auto;">
      {icon('info', 'note-box__icon')}
      <div>
        <h3 style="margin-bottom:var(--space-2xs);">Changes &amp; Unexpected Conditions</h3>
        <p style="color:var(--color-text-muted);">In construction, unexpected conditions can happen. If anything arises that impacts the scope, cost, or timeline, we will discuss it with you before proceeding so you can make an informed decision.</p>
      </div>
    </div>
  </section>

  {cta_banner("Ready to Discuss Your Project?", "We're here to help bring your vision to life with a process you can trust.")}
"""

write("our-process.html", page(
    title="Our Process | Euro Pros Construction &amp; Remodeling",
    description="From consultation to final walkthrough &mdash; see the clear, organized process Euro Pros follows on every remodeling and construction project.",
    active="process",
    body=our_process_body,
))


# ============================================================== ABOUT US ===
WHO_WE_ARE = [
    ("Family-Owned Company", "We treat every project like it's for our own family."),
    ("Licensed General Contractor", "Fully licensed to build, remodel, and manage projects from start to finish."),
    ("Licensed &amp; Insured", "We meet all state requirements and carry proper insurance for your protection."),
    ("Residential Remodeling", "Kitchens, bathrooms, basements, additions, and more."),
    ("New Home Construction", "Custom homes built with care, from the ground up."),
    ("Professional Project Management", "One dedicated team, clear communication, and a smooth process from start to finish."),
]

OUR_APPROACH = [
    ("Quality", "We use quality materials and proven methods to deliver results that last."),
    ("Communication", "We keep you informed at every step and make sure your questions are always answered."),
    ("Accountability", "We do what we say we'll do and stand behind our work from start to finish."),
    ("Craftsmanship", "Our team takes pride in the details that make your home beautiful and built to last."),
    ("Integrity", "We believe in honest pricing, realistic timelines, and earning your trust every day."),
]

WHO_WE_ARE_ICONS = ["person", "hardhat", "shield", "house", "framing", "clipboard"]

who_we_are_html = "\n".join(f"""        <div class="icon-list__item">
          {icon(i, 'icon-list__icon')}
          <div>
            <p class="icon-list__title">{t}</p>
            <p class="icon-list__text">{d}</p>
          </div>
        </div>""" for i, (t, d) in zip(WHO_WE_ARE_ICONS, WHO_WE_ARE))

approach_html = "\n".join(f"""        <div class="feature-grid__item" style="text-align:left;">
          <p class="feature-grid__title" style="border-top:2px solid var(--color-navy-800);padding-top:var(--space-sm);">{t}</p>
          <p class="feature-grid__text">{d}</p>
        </div>""" for t, d in OUR_APPROACH)

about_body = f"""  <section class="hero hero--sm">
    <div class="hero__media"><img src="images/about-hero.svg" alt="Euro Pros team member on a construction site" /></div>
    <div class="hero__overlay"></div>
    <div class="container">
      <div class="hero__content">
        <h1 class="hero__title hero__title--h2">Built on Real Construction Experience</h1>
        <p class="hero__subtitle">Euro Pros brings hands-on construction experience and professional project management to homeowners throughout the Chicago suburbs.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="why-us why-us--top">
        <div class="why-us__media">
          <img src="images/experience-kitchen.svg" alt="Finished kitchen remodel" loading="lazy" />
        </div>
        <div class="why-us__content">
          <h2 class="why-us__title">Construction Experience Since 2010</h2>
          <p style="color:var(--color-text-muted);margin-top:var(--space-md);max-width:44ch;">Our team's construction experience dates back to 2010, with a foundation built on hands-on work, proven processes, and a commitment to doing things right.</p>
          <div class="pull-quote" style="margin-top:var(--space-lg);max-width:44ch;">Euro Pros Construction &amp; Remodeling has proudly served homeowners as a company for nearly 5 years.</div>
        </div>
      </div>

      <div class="note-box" style="max-width:760px;margin:var(--space-xl) auto 0;">
        {icon('info', 'note-box__icon')}
        <p>&ldquo;Since 2010&rdquo; refers to the hands-on construction experience of our team and leadership. Euro Pros Construction &amp; Remodeling, LLC is a distinct, newer company built on that experience &mdash; not a business that has legally operated since 2010.</p>
      </div>
    </div>
  </section>

  <section class="section section--soft" id="who-we-are">
    <div class="container">
      <div class="why-us why-us--top">
        <div class="why-us__content">
          <span class="eyebrow">Who We Are</span>
          <h2 class="why-us__title">A Local Team Built on Real Construction Experience</h2>
          <p style="color:var(--color-text-muted);margin-top:var(--space-sm);max-width:48ch;">Every project is backed by a licensed, insured team that treats your home like our own &mdash; from the first walkthrough to the final coat of paint.</p>
        </div>
        <div class="why-us__media">
          <img src="images/about-consultation.svg" alt="Euro Pros team member consulting with a homeowner" loading="lazy" />
        </div>
      </div>
      <div class="icon-list" style="margin-top:var(--space-2xl);">
{who_we_are_html}
      </div>
    </div>
  </section>

  <section class="section" id="why-euro-pros">
    <div class="container">
      <div class="section-head">
        <h2>Our Approach</h2>
      </div>
      <div class="feature-grid feature-grid--5">
{approach_html}
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container">
      <div class="section-head">
        <h2>Meet Our Team</h2>
        <div class="section-divider">
          <span class="section-divider__line"></span>
          {icon('house', 'section-divider__icon')}
          <span class="section-divider__line"></span>
        </div>
      </div>
      <div class="team-grid">
        <div class="team-card">
          <img src="images/team-gleb.jpg" alt="Gleb Starostin" loading="lazy" />
          <div class="team-card__info">
            <p class="team-card__name">Gleb Starostin</p>
            <p class="team-card__role">Owner</p>
          </div>
        </div>
        <div class="team-card">
          <img src="images/team-alec.jpg" alt="Alec Starastsin" loading="lazy" />
          <div class="team-card__info">
            <p class="team-card__name">Alec Starastsin</p>
            <p class="team-card__role">Owner</p>
          </div>
        </div>
        <div class="team-card">
          <img src="images/team-kiryl.jpg" alt="Kiryl Starastsin" loading="lazy" />
          <div class="team-card__info">
            <p class="team-card__name">Kiryl Starastsin</p>
            <p class="team-card__role">Owner</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  {cta_banner("Let's Talk About Your Project", "We're here to listen, answer your questions, and help you take the next step with confidence.")}
"""

write("about-us.html", page(
    title="About Us | Euro Pros Construction &amp; Remodeling",
    description="Euro Pros is a licensed General Contractor serving the Chicago suburbs, built on hands-on construction experience and a commitment to quality.",
    active="about",
    body=about_body,
))


# ==================================================================== BLOG ===
CATEGORIES = [
    ("all", "All Articles"),
    ("bathroom-remodeling", "Bathroom Remodeling"),
    ("basement-remodeling", "Basement Remodeling"),
    ("kitchen-remodeling", "Kitchen Remodeling"),
    ("home-remodeling", "Home Remodeling"),
    ("new-home-construction", "New Home Construction"),
    ("remodeling-tips", "Remodeling Tips"),
]

ARTICLES = [
    dict(slug="blog-bathroom-remodeling-how-to-plan-your-project", title="Bathroom Remodeling: How to Plan Your Project",
         category="Bathroom Remodeling", cat_value="bathroom-remodeling", date="May 24, 2025", img="blog-bathroom-ideas",
         excerpt="A well-planned bathroom remodel delivers comfort, style, and lasting value. Use this step-by-step guide to plan with clarity and confidence."),
    dict(slug="blog-kitchen-remodeling-planning-your-project", title="Kitchen Remodeling: Planning Your Project the Right Way",
         category="Kitchen Remodeling", cat_value="kitchen-remodeling", date="May 15, 2025", img="blog-featured",
         excerpt="A successful kitchen remodel starts with clear goals, a realistic budget, and a solid plan. Learn the key steps to guide your project from concept to completion."),
    dict(slug="blog-how-to-budget-for-a-home-remodel", title="How to Budget for a Home Remodel",
         category="Remodeling Tips", cat_value="remodeling-tips", date="May 1, 2025", img="blog-budget",
         excerpt="Understand the real costs involved in a remodel and how to create a budget that keeps your project on track."),
    dict(slug="blog-bathroom-remodel-ideas-that-add-value", title="Bathroom Remodel Ideas That Add Value",
         category="Bathroom Remodeling", cat_value="bathroom-remodeling", date="Apr 24, 2025", img="naperville-gallery-2",
         excerpt="Explore timeless design choices and smart upgrades that improve comfort and boost your home's value."),
    dict(slug="blog-understanding-the-remodeling-process", title="Understanding the Remodeling Process: Step by Step",
         category="Home Remodeling", cat_value="home-remodeling", date="Apr 10, 2025", img="blog-process",
         excerpt="From consultation to final walkthrough, here's what you can expect when you work with Euro Pros."),
    dict(slug="blog-do-you-need-a-permit-for-your-remodel", title="Do You Need a Permit for Your Remodel?",
         category="Remodeling Tips", cat_value="remodeling-tips", date="Mar 27, 2025", img="blog-permit",
         excerpt="When permits are required, how the process works, and why it protects your investment."),
    dict(slug="blog-basement-remodeling-ideas", title="Basement Remodeling Ideas for More Living Space",
         category="Basement Remodeling", cat_value="basement-remodeling", date="Mar 13, 2025", img="blog-basement-ideas",
         excerpt="Turn your basement into a functional, beautiful space your family will love with these practical ideas."),
    dict(slug="blog-building-a-new-home-what-to-consider", title="Building a New Home: What to Consider",
         category="New Home Construction", cat_value="new-home-construction", date="Feb 27, 2025", img="blog-new-home",
         excerpt="Key factors to think about before breaking ground on your custom home project."),
]

tabs_blog_html = "\n".join(
    f'        <a href="#" data-filter="{val}" class="{"is-active" if val == "all" else ""}">{label}</a>'
    for val, label in CATEGORIES
)

featured = next(a for a in ARTICLES if a["slug"] == "blog-kitchen-remodeling-planning-your-project")
grid_articles = [a for a in ARTICLES if a["slug"] != featured["slug"]]

blog_grid_html = "\n".join(f"""        <a href="{a['slug']}.html" class="blog-card" data-category="{a['cat_value']}" data-filter-target="blog">
          <div class="blog-card__media"><img src="images/{a['img']}.svg" alt="{a['title']}" loading="lazy" /></div>
          <div class="blog-card__body">
            <span class="blog-card__category">{a['category']}</span>
            <h3 class="blog-card__title">{a['title']}</h3>
            <p class="blog-card__excerpt">{a['excerpt']}</p>
            <div class="blog-card__meta">
              <span>{a['date']}</span>
              <span>Read Article &rarr;</span>
            </div>
          </div>
        </a>""" for a in grid_articles)

blog_body = f"""  <section class="hero hero--sm">
    <div class="hero__media"><img src="images/blog-hero.svg" alt="Bathroom remodel" /></div>
    <div class="hero__overlay"></div>
    <div class="container">
      <div class="hero__content">
        <h1 class="hero__title hero__title--h2">Home Remodeling &amp; Construction Insights</h1>
        <p class="hero__subtitle">Helpful information from Euro Pros for homeowners planning their next project.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="tabs-row" data-filter-group="blog">
{tabs_blog_html}
      </div>

      <a href="{featured['slug']}.html" class="blog-featured" data-category="{featured['cat_value']}" data-filter-target="blog">
        <div class="blog-featured__media"><img src="images/{featured['img']}.svg" alt="{featured['title']}" loading="lazy" /></div>
        <div class="blog-featured__body">
          <span class="blog-featured__category">{featured['category']}</span>
          <h2 class="blog-featured__title">{featured['title']}</h2>
          <p class="blog-featured__excerpt">{featured['excerpt']}</p>
          <div class="blog-card__meta blog-featured__meta">
            <span>{featured['date']}</span>
            <span>Read Article &rarr;</span>
          </div>
        </div>
      </a>

      <div class="blog-grid">
{blog_grid_html}
      </div>

      <div class="pagination">
        <a href="#" class="is-active">1</a>
        <a href="#">2</a>
        <a href="#">3</a>
        <span>&hellip;</span>
        <a href="#">8</a>
        <a href="#">Next &rarr;</a>
      </div>
    </div>
  </section>

  {cta_banner("Planning a Remodeling Project?", "Talk to Euro Pros about your project.")}
"""

write("blog.html", page(
    title="Home Remodeling &amp; Construction Blog | Euro Pros",
    description="Helpful guides on bathroom, basement, kitchen, and whole-home remodeling plus new home construction from Euro Pros, a licensed Chicago-suburbs General Contractor.",
    active="blog",
    body=blog_body,
))


def related_articles_html(current_slug, count=3):
    others = [a for a in ARTICLES if a["slug"] != current_slug][:count]
    return "\n".join(f"""        <a href="{a['slug']}.html" class="blog-card">
          <div class="blog-card__media"><img src="images/{a['img']}.svg" alt="{a['title']}" loading="lazy" /></div>
          <div class="blog-card__body">
            <span class="blog-card__category">{a['category']}</span>
            <h3 class="blog-card__title">{a['title']}</h3>
            <p class="blog-card__excerpt">{a['excerpt']}</p>
            <div class="blog-card__meta">
              <span>{a['date']}</span>
              <span>Read Article &rarr;</span>
            </div>
          </div>
        </a>""" for a in others)


# ------------------------------------------------- Full article (Bathroom) ---
bathroom_article = next(a for a in ARTICLES if a["slug"] == "blog-bathroom-remodeling-how-to-plan-your-project")

toc_items = [
    ("start-with-your-goals", "Start With Your Goals"),
    ("define-the-scope", "Define the Scope"),
    ("plan-your-budget", "Plan Your Budget"),
    ("choose-materials", "Choose Materials"),
    ("understand-the-timeline", "Understand the Timeline"),
    ("work-with-a-general-contractor", "Work With a General Contractor"),
    ("final-thoughts", "Final Thoughts"),
]
toc_html = "\n".join(f'          <a href="#{anchor}">{label}</a>' for anchor, label in toc_items)

article_body = f"""  <section class="hero hero--sm">
    <div class="hero__media"><img src="images/blog-article-hero.svg" alt="{bathroom_article['title']}" /></div>
    <div class="hero__overlay"></div>
    <div class="container">
      <div class="hero__content">
        <span class="eyebrow-link" style="color:var(--color-text-on-dark-muted);">Bathroom Remodeling</span>
        <h1 class="hero__title hero__title--h2">{bathroom_article['title']}</h1>
        <p class="hero__date">{bathroom_article['date']}</p>
        <p class="hero__subtitle">{bathroom_article['excerpt']}</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="article-layout">
        <aside class="article-sidebar">
          <nav class="toc" aria-label="On this page">
            <p class="toc__title">On This Page</p>
{toc_html}
          </nav>
          <div class="note-box">
            {icon('info', 'note-box__icon')}
            <p>Costs and timelines vary based on the size, materials, and scope of your project.</p>
          </div>
        </aside>

        <div class="article-body">
          <p>A successful bathroom remodel starts long before demo day. With thoughtful planning and the right team, you can create a space that looks beautiful, functions better, and adds value to your home. Here's how to plan your bathroom remodel the right way.</p>

          <h2 id="start-with-your-goals">1. Start With Your Goals</h2>
          <p>Think about how you use your bathroom and what you want to improve. Are you looking for more storage, a better layout, or a spa-like retreat? Clear goals will guide every decision.</p>
          <p>Common goals include:</p>
          <ul>
            <li>Improve functionality and flow</li>
            <li>Update outdated finishes</li>
            <li>Increase storage</li>
            <li>Enhance comfort and relaxation</li>
            <li>Add value before selling</li>
          </ul>

          <h2 id="define-the-scope">2. Define the Scope</h2>
          <p>Decide what will change in your space. A cosmetic update might include new fixtures and finishes, while a full remodel could involve reconfiguring the layout, moving plumbing, or replacing everything.</p>
          <p><strong>Tip:</strong> Be realistic about what's possible based on your space, structure, and budget.</p>

          <h2 id="plan-your-budget">3. Plan Your Budget</h2>
          <p>Set a budget range early and account for both essentials and extras. Include allowances for materials, labor, permits, and a contingency for unexpected issues.</p>
          <p><strong>Keep in mind:</strong> Costs and timelines vary depending on the size of your bathroom, materials selected, and scope of work.</p>

          <h2 id="choose-materials">4. Choose Materials</h2>
          <p>Materials impact both the look and durability of your bathroom. Invest in quality where it matters most &mdash; like tile, fixtures, and waterproofing.</p>
          <p>Popular choices include:</p>
          <ul>
            <li>Porcelain or ceramic tile</li>
            <li>Quartz or natural stone countertops</li>
            <li>Solid wood or moisture-resistant cabinetry</li>
            <li>Water-efficient fixtures</li>
            <li>Glass shower enclosures</li>
          </ul>

          <div class="article-figure">
            <div>
              <h2 id="understand-the-timeline">5. Understand the Timeline</h2>
              <p>A typical bathroom remodel can take several weeks, depending on scope and availability of materials. Your contractor should provide a clear schedule and keep you informed as the project progresses.</p>
            </div>
            <figure>
              <img src="images/blog-article-materials.svg" alt="Well-chosen bathroom materials" loading="lazy" />
              <figcaption>Well-chosen materials create a polished, lasting result.</figcaption>
            </figure>
          </div>

          <div class="pull-quote">Good planning prevents surprises and keeps your project moving forward smoothly.</div>

          <div class="article-figure">
            <div>
              <h2 id="work-with-a-general-contractor">6. Work With a General Contractor</h2>
              <p>A trusted contractor brings experience, manages the details, and helps you avoid costly mistakes. Look for clear communication, a proven process, and quality craftsmanship.</p>
              <p>Explore <a href="our-process.html">our process</a> to see how we keep your project organized from start to finish.</p>
            </div>
            <figure>
              <img src="images/blog-article-layout.svg" alt="Smart bathroom layout planning" loading="lazy" />
              <figcaption>Smart layout planning improves comfort and everyday function.</figcaption>
            </figure>
          </div>

          <h2 id="final-thoughts">Final Thoughts</h2>
          <p>Bathroom remodeling is an investment in your home and your daily life. With the right plan and the right partner, you'll enjoy a space that's both beautiful and built to last.</p>
          <p>Ready to get started? <a href="contact.html">Contact Euro Pros</a> for a consultation and estimate.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container">
      <div class="section-head">
        <h2>Related Articles</h2>
      </div>
      <div class="blog-grid">
{related_articles_html(bathroom_article['slug'])}
      </div>
    </div>
  </section>

  {cta_banner("Planning a Remodeling Project?", "Talk to Euro Pros about your project.")}
"""

write(f"{bathroom_article['slug']}.html", page(
    title=f"{bathroom_article['title']} | Euro Pros Blog",
    description=bathroom_article["excerpt"],
    active="blog",
    body=article_body,
))


# ---------------------------------------------- Simple articles (the rest) ---
SIMPLE_ARTICLES = {
    "blog-kitchen-remodeling-planning-your-project": [
        ("Set Clear Goals First", ["Before you look at a single cabinet sample, define how you actually use your kitchen. Do you need more counter space, better storage, or a layout that opens to your living area? Clear goals keep every design decision focused."]),
        ("Establish a Realistic Budget", ["Kitchen remodels vary widely in cost depending on layout changes, cabinetry, and countertop materials. Build in a contingency of 10&ndash;15% for unexpected conditions once walls and plumbing are opened up."]),
        ("Think Through the Layout", ["The classic \"work triangle\" between the sink, stove, and refrigerator is still a useful starting point, but islands, open shelving, and multi-cook layouts have changed how many families use their kitchens. Consider how you'll move through the space daily."]),
        ("Choose Durable Materials", ["Countertops and flooring take the most daily wear in a kitchen. Quartz, durable hardwood, and water-resistant flooring options are worth the investment for a space that gets used every day."]),
        ("Partner With an Experienced Contractor", ["A kitchen remodel touches plumbing, electrical, and often structural elements. Working with a licensed General Contractor keeps every trade coordinated under one schedule and one point of contact."]),
    ],
    "blog-how-to-budget-for-a-home-remodel": [
        ("Start With Your Must-Haves", ["List the changes that matter most to you before you get attached to finishes and extras. This helps you protect budget for the elements that will make the biggest difference in how your home functions."]),
        ("Understand Where the Money Goes", ["Labor, materials, permits, and project management all factor into a remodeling budget. Larger scope changes &mdash; like moving plumbing or walls &mdash; typically cost more than cosmetic updates."]),
        ("Build in a Contingency", ["Set aside 10&ndash;15% of your budget for unexpected conditions, especially in older homes where issues can be hidden behind walls or under flooring until demolition begins."]),
        ("Get a Detailed, Transparent Estimate", ["A trustworthy contractor will walk you through exactly what's included in your estimate &mdash; and what could change your final cost &mdash; before work begins."]),
    ],
    "blog-bathroom-remodel-ideas-that-add-value": [
        ("Walk-In Showers", ["Replacing an underused tub with a spacious, glass-enclosed walk-in shower is one of the most popular upgrades homeowners make &mdash; and one of the best for everyday comfort."]),
        ("Double Vanities", ["Adding a second sink to a shared bathroom improves your morning routine and is a feature buyers consistently look for."]),
        ("Timeless Tile and Finishes", ["Neutral tile palettes with warm metal fixtures tend to stay in style far longer than trend-driven choices, which protects your investment over time."]),
        ("Smart Storage", ["Custom vanities, built-in niches, and linen storage keep a bathroom functional and clutter-free without sacrificing style."]),
    ],
    "blog-understanding-the-remodeling-process": [
        ("Consultation", ["We start by learning about your goals, budget, and timeline, and walking your space to understand what's possible."]),
        ("Planning &amp; Estimate", ["We develop a plan and provide a detailed, transparent estimate so you know what to expect before any work begins."]),
        ("Scheduling &amp; Preparation", ["Once you approve the plan, we finalize the schedule, order materials, and secure any required permits."]),
        ("Construction", ["Our team manages daily progress, keeps your job site clean, and keeps you informed throughout construction."]),
        ("Final Walkthrough", ["We review every detail with you before considering the project complete &mdash; see our full <a href=\"our-process.html\">process</a> for more detail."]),
    ],
    "blog-do-you-need-a-permit-for-your-remodel": [
        ("When Permits Are Typically Required", ["Most municipalities require permits for work involving plumbing, electrical, structural changes, or additions &mdash; even if the work happens inside an existing wall."]),
        ("Why Permits Protect You", ["Permitted work is inspected, which helps confirm it meets code and was done safely. This matters for insurance claims and when you eventually sell your home."]),
        ("How the Process Works", ["We handle the permitting process for you, including submitting plans and coordinating inspections, so you don't have to navigate local requirements yourself."]),
        ("What Happens Without a Permit", ["Unpermitted work can create problems during a home sale or insurance claim, and may need to be redone to bring it up to code."]),
    ],
    "blog-basement-remodeling-ideas": [
        ("Family &amp; Media Rooms", ["An unfinished basement is often the easiest place to add real square footage for a family room, home theater, or play space."]),
        ("Home Offices &amp; Gyms", ["Basements offer a quiet, separate space that works well for a dedicated home office or workout area."]),
        ("Guest Suites", ["Adding a bedroom and bathroom below grade &mdash; with proper egress &mdash; creates flexible space for guests or multigenerational living."]),
        ("Wet Bars &amp; Entertainment Spaces", ["A basement is a natural place for a wet bar or entertainment-focused layout, especially when paired with durable, moisture-resistant finishes."]),
    ],
    "blog-building-a-new-home-what-to-consider": [
        ("Lot &amp; Site Conditions", ["Soil conditions, grading, and utility access all affect what's possible on your lot and should be assessed early in planning."]),
        ("Budget &amp; Timeline", ["Custom homes typically take 9&ndash;14 months from groundbreaking to completion. Build a realistic budget that includes site work, permits, and finishes &mdash; not just construction labor."]),
        ("Working With One General Contractor", ["Coordinating excavation, foundation, framing, and every trade after under one contractor keeps your project accountable and on schedule."]),
        ("Permits &amp; Approvals", ["New construction requires coordination with local municipalities on permits and approvals &mdash; something an experienced contractor manages on your behalf."]),
    ],
}


def article_page_simple(a):
    sections = SIMPLE_ARTICLES[a["slug"]]
    sections_html = "\n".join(f"          <h2>{h}</h2>\n" + "\n".join(f"          <p>{p}</p>" for p in paras) for h, paras in sections)
    body = f"""  <section class="hero hero--sm">
    <div class="hero__media"><img src="images/{a['img']}.svg" alt="{a['title']}" /></div>
    <div class="hero__overlay"></div>
    <div class="container">
      <div class="hero__content">
        <span class="eyebrow-link" style="color:var(--color-text-on-dark-muted);">{a['category']}</span>
        <h1 class="hero__title hero__title--h2">{a['title']}</h1>
        <p class="hero__date">{a['date']}</p>
        <p class="hero__subtitle">{a['excerpt']}</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="article-body" style="max-width:760px;margin-inline:auto;">
{sections_html}
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container">
      <div class="section-head">
        <h2>Related Articles</h2>
      </div>
      <div class="blog-grid">
{related_articles_html(a['slug'])}
      </div>
    </div>
  </section>

  {cta_banner("Planning a Remodeling Project?", "Talk to Euro Pros about your project.")}
"""
    write(f"{a['slug']}.html", page(
        title=f"{a['title']} | Euro Pros Blog",
        description=a["excerpt"],
        active="blog",
        body=body,
    ))


for _a in ARTICLES:
    if _a["slug"] != bathroom_article["slug"]:
        article_page_simple(_a)


# ================================================================ CONTACT ===
NEXT_STEPS = [
    ("We Review Your Request", "Our team will review your details and follow up within one business day."),
    ("We Schedule a Consultation", "We'll schedule a convenient time to discuss your project and answer any questions."),
    ("We Plan Your Project", "Together we'll create a plan, provide an estimate, and guide you through the next steps."),
]

TRUST_ICONS = [
    ("shield", "Licensed &amp; Insured", "Fully licensed and insured for your protection."),
    ("hardhat", "General Contractor", "Full-service design, planning, and construction."),
    ("chat", "Clear Communication", "You'll always know what's happening."),
    ("clipboard", "2-Year Workmanship Warranty", "Quality work backed by our workmanship warranty."),
]

next_steps_html = "\n".join(f"""          <div class="step-list__item">
            <div class="step-list__circle">{i + 1}</div>
            <div>
              <p class="step-list__title">{t}</p>
              <p class="step-list__text">{d}</p>
            </div>
          </div>""" for i, (t, d) in enumerate(NEXT_STEPS))

trust_icons_html = "\n".join(f"""        <div>
          {icon(i, 'trust-icons__icon')}
          <p class="trust-icons__title">{t}</p>
          <p class="trust-icons__text">{d}</p>
        </div>""" for i, t, d in TRUST_ICONS)

PROJECT_TYPES = ["Bathroom Remodeling", "Basement Remodeling", "Kitchen Remodeling", "Whole-Home Remodeling", "New Home Construction", "Other"]
project_type_options = "\n".join(f'                <option>{t}</option>' for t in PROJECT_TYPES)
BUDGET_RANGES = ["Under $25,000", "$25,000 &ndash; $50,000", "$50,000 &ndash; $100,000", "$100,000 &ndash; $250,000", "$250,000+"]
budget_options = "\n".join(f'                <option>{b}</option>' for b in BUDGET_RANGES)

contact_body = f"""  <section class="hero hero--sm">
    <div class="hero__media"><img src="images/contact-hero.svg" alt="Bathroom vanity" /></div>
    <div class="hero__overlay"></div>
    <div class="container">
      <div class="hero__content">
        <h1 class="hero__title hero__title--h2">Tell Us About Your Project</h1>
        <p class="hero__subtitle">Tell us what you're planning and we'll help determine the next step.</p>
      </div>
    </div>
  </section>

  <section class="section" id="get-estimate">
    <div class="container">
      <div class="form-grid">
        <div class="form-card">
          <form class="project-form" novalidate>
            <div class="field">
              <label>Name <span class="required">*</span></label>
              <div class="field-row">
                <input type="text" name="first_name" placeholder="First Name" required />
                <input type="text" name="last_name" placeholder="Last Name" required />
              </div>
            </div>

            <div class="field">
              <label>Phone <span class="required">*</span></label>
              <input type="tel" name="phone" placeholder="(123) 456-7890" required />
            </div>

            <div class="field">
              <label>Email <span class="required">*</span></label>
              <input type="email" name="email" placeholder="name@email.com" required />
            </div>

            <div class="field">
              <label>Project Address <span class="required">*</span></label>
              <input type="text" name="address" placeholder="Street Address" required style="margin-bottom:var(--space-sm);" />
              <div class="field-row">
                <input type="text" name="city" placeholder="City" />
                <input type="text" name="zip" placeholder="ZIP Code" />
              </div>
            </div>

            <div class="field">
              <label>Project Type <span class="required">*</span></label>
              <select name="project_type" required>
                <option value="" selected disabled>Select a project type</option>
{project_type_options}
              </select>
            </div>

            <div class="field">
              <label>Approximate Budget</label>
              <select name="budget">
                <option value="" selected disabled>Select a budget range</option>
{budget_options}
              </select>
            </div>

            <div class="field">
              <label>Preferred Start Date</label>
              <input type="text" name="start_date" placeholder="Select a timeframe" />
            </div>

            <div class="field">
              <label>Project Description <span class="required">*</span></label>
              <textarea name="description" placeholder="Tell us about your project goals, must-haves, and any other details that will help us understand." required></textarea>
            </div>

            <div class="field">
              <label>Upload Photos (Optional)</label>
              <div class="upload-box">
                {icon('upload')}
                <p>Drag and drop files here or click to browse</p>
                <p>JPG, PNG up to 10MB each</p>
              </div>
            </div>

            <button type="submit" class="btn btn--primary btn--block">Submit Project Request</button>

            <p class="form-note">
              {icon('shield')}
              <span>Your information is secure and will never be shared. We will only use it to contact you about your project.</span>
            </p>
          </form>

          <div class="form-success">
            {icon('check-circle')}
            <h3>Thanks &mdash; your request is on its way.</h3>
            <p style="color:var(--color-text-muted);">A member of our team will follow up within one business day.</p>
          </div>
        </div>

        <div>
          <div class="contact-info-card">
            <h3>Contact Information</h3>
            <div class="contact-info-card__item">
              <div class="contact-info-card__icon">{icon('phone')}</div>
              <div>
                <p class="contact-info-card__title">(847) 888-1919</p>
                <p class="contact-info-card__text">Call us today</p>
              </div>
            </div>
            <div class="contact-info-card__item">
              <div class="contact-info-card__icon">{icon('mail')}</div>
              <div>
                <p class="contact-info-card__title">info@europrosremodeling.com</p>
                <p class="contact-info-card__text">We reply within one business day</p>
              </div>
            </div>
            <div class="contact-info-card__item">
              <div class="contact-info-card__icon">{icon('pin')}</div>
              <div>
                <p class="contact-info-card__title">Serving Chicagoland</p>
                <p class="contact-info-card__text">Cook, DuPage &amp; surrounding counties</p>
              </div>
            </div>

            <hr class="divider" />
            <h3>Business Hours</h3>
            <div class="contact-info-card__item" style="border-bottom:none;">
              <div class="contact-info-card__icon">{icon('clock')}</div>
              <div>
                <p class="contact-info-card__text">Monday &ndash; Friday: 8:00am &ndash; 5:00pm</p>
                <p class="contact-info-card__text">Saturday &ndash; Sunday: Closed</p>
              </div>
            </div>

            <hr class="divider" />
            <h3>What Happens Next?</h3>
            <div class="step-list" style="margin-top:var(--space-sm);">
{next_steps_html}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container">
      <div class="trust-icons">
{trust_icons_html}
      </div>
    </div>
  </section>

  <section class="final-cta section--navy">
    <div class="container">
      <div>
        <h2 class="final-cta__title">Ready to Discuss Your Project?</h2>
        <p style="color:var(--color-text-on-dark-muted);margin-top:var(--space-2xs);">We're here to help bring your vision to life with a process you can trust.</p>
      </div>
      <div class="final-cta__actions">
        <a class="btn btn--outline-light" href="#get-estimate">Get an Estimate</a>
      </div>
    </div>
  </section>
"""

write("contact.html", page(
    title="Get an Estimate | Euro Pros Construction &amp; Remodeling",
    description="Tell Euro Pros about your remodeling or new construction project and request a free estimate. Serving the Chicago suburbs.",
    active="contact",
    body=contact_body,
))
