"""Build the two static Evollon treatment pages. Edit OFFERS to change pricing."""

from html import escape
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
CURRENT_MONTH = date.today().strftime("%B")
OFFERS = {
    "botox": {
        "file": "index.html",
        "name": "Botox",
        "eyebrow": "A more rested look, still entirely you",
        "headline": "Get Our <em>Botox Beauty Package</em> With <em>$100 Off</em> This Month!",
        "intro": "Your first 30 units of Botox are $249 this month—that’s $100 OFF our normal price. The package also includes a personalized treatment plan with our specialist.",
        "bullets": ["Personalized consultation and treatment plan", "Designed to soften fine lines, wrinkles, and expression lines", "No downtime, non-invasive treatment, and no surgery", "Convenient Forest Hills, Queens location"],
        "description": "Botox is an injectable treatment that temporarily relaxes certain facial muscles. During your consultation, you can discuss the areas that concern you, your health history, and whether treatment is appropriate for you.",
        "benefits": [
            ("01", "Start with a conversation", "Share the expressions and lines you would like to discuss."),
            ("02", "Make it personal", "Your provider can explain treatment options and an approach suited to your goals."),
            ("03", "Know what to expect", "Ask about the procedure, aftercare, timing, and possible side effects before deciding."),
        ],
        "faq": [
            ("What can Botox help with?", "Botox can help soften some facial lines and wrinkles for a limited time. At your visit, your provider will talk with you about the areas you want to treat."),
            ("Will I still look like myself?", "That is up to you and your provider. Tell them how much movement you want to keep. Your results may be different from someone else’s."),
            ("Is there downtime or any risk?", "Many people return to their usual day soon after treatment. You may have redness, swelling, or bruising where you were treated. Botox also has important risks. Your provider will review them with you before treatment."),
            ("How much does it cost?", "Your first 30 units of Botox are $249 this month. That’s $100 off our normal price. Ask your provider about the cost of any extra units before treatment."),
        ],
    },
    "lip-filler": {
        "file": "lip-filler.html",
        "name": "Lip Filler",
        "eyebrow": "Shape and definition, on your terms",
        "headline": "Get Our <em>Lip Filler Package</em> With <em>$125 Off</em> This Month!",
        "intro": "Full lip enhancement for $375 (normally $500)—save $125. We focus on natural shape and definition for a refined, balanced look.",
        "bullets": ["Personalized consultation and treatment plan", "Natural shape and definition—refined, never exaggerated", "Professional injectors and careful technique", "New clients only · Offer ends September 30"],
        "description": "Lip filler is an injectable treatment used to add fullness or definition to the lips. Your consultation is the time to talk through the look you want, the product your provider recommends, and the benefits and risks.",
        "benefits": [
            ("01", "Bring your inspiration", "Talk about the shape, definition, or volume you have in mind."),
            ("02", "Plan for balance", "Your provider can recommend an approach based on your features and goals."),
            ("03", "Feel informed", "Review the treatment process, recovery, and possible risks before deciding."),
        ],
        "faq": [
            ("What does lip filler do?", "Lip filler can add shape or fullness to your lips. Your provider can explain which option may fit your goals."),
            ("Can the result look natural?", "Yes. You can ask for a soft, natural look. Talk with your provider about the shape and amount of fullness you want."),
            ("What should I expect afterward?", "Your lips may feel tender, swollen, or bruised after treatment. These effects often improve in a few days or weeks. There are also rare but serious risks. Your provider will explain them before treatment."),
            ("How much does it cost?", "Full lip enhancement is $375, down from $500. You save $125. This offer is for new clients and ends September 30."),
        ],
    },
}


def render(key, d):
    title = f"{d['name']} Consultation | Evollon Med Spa"
    bullets = "\n".join(f"<li>{escape(x)}</li>" for x in d["bullets"])
    benefits = "\n".join(f'<article class="step"><span>{n}</span><h3>{escape(h)}</h3><p>{escape(p)}</p></article>' for n, h, p in d["benefits"])
    faqs = "\n".join(f'<details><summary>{escape(q)}</summary><div class="answer">{escape(a)}</div></details>' for q, a in d["faq"])
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f8f2ee">
  <meta name="description" content="Explore {escape(d['name'])} at Evollon Med Spa in Forest Hills, NY and request a personalized consultation.">
  <title>{escape(title)}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;0,700;1,400;1,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
  <script src="site.js" defer></script>
</head>
<body data-treatment="{escape(key)}">
  <div class="announcement">{'$100 OFF Botox This Month' if key == 'botox' else '$125 OFF Lip Filler This Month'}</div>
  <header class="site-header wrap">
    <div class="wordmark">Evollon Med Spa &amp; Wellness</div>
    <div class="header-address">105-09 Metropolitan Ave, Ste 2, Forest Hills, NY 11375</div>
  </header>
  <main>
    <section class="hero">
      <div class="hero-inner wrap">
        <div class="hero-copy">
          <div class="eyebrow"><span class="line"></span> {escape(d['eyebrow'])}</div>
          <h1>{d['headline']}</h1>
          <p class="intro">{escape(d['intro'])}</p>
          <ul class="check-list">{bullets}</ul>
        </div>
      </div>
    </section>
    <section class="intro-strip"><div class="wrap strip-inner"><span>PERSONALIZED CARE</span><i></i><span>NATURAL LOOKING GOALS</span><i></i><span>FOREST HILLS, NEW YORK</span></div></section>
    <section class="content-section wrap" id="about"><div class="section-heading"><div class="eyebrow">THE EVOLLON APPROACH</div><h2>Beauty that begins <em>with you.</em></h2><p>{escape(d['description'])}</p></div><div class="steps">{benefits}</div></section>
    <section class="consult-section" id="consultation"><div class="wrap consult-grid"><div class="consult-copy"><div class="eyebrow">LET'S TALK</div><h2>Your next step starts <em>here.</em></h2><p>Have a question about {escape(d['name'])}? Share your details and Evollon will be in touch.</p><div class="contact-line"><span aria-hidden="true">⌖</span><div><strong>Visit us in Forest Hills</strong><br>105-09 Metropolitan Ave, Ste 2<br>Forest Hills, NY 11375</div></div></div><form class="form-card" id="lead-form" name="{'botox-lead' if key == 'botox' else 'lip-filler-lead'}" method="POST" data-netlify="true" aria-label="Ask about {escape(d['name'])}"><input type="hidden" name="form-name" value="{'botox-lead' if key == 'botox' else 'lip-filler-lead'}"><input type="hidden" name="treatment" value="{escape(d['name'])}"><input type="hidden" name="offer" value="{'First 30 units for $249 ($100 off)' if key == 'botox' else 'Full lip enhancement for $375 ($125 off)'}"><div class="form-title">Ask about {escape(d['name'])}<span>We'll help you take the next step.</span></div><label for="full-name">Full name <span class="required">*</span></label><input id="full-name" name="name" autocomplete="name" required placeholder="Full name"><label for="email">Email <span class="required">*</span></label><input id="email" name="email" type="email" autocomplete="email" required placeholder="Email"><label for="phone">Phone <span class="required">*</span></label><input id="phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required placeholder="Phone"><button class="button button-primary submit" type="submit">{'I want $100 off.' if key == 'botox' else 'I want $125 off.'}</button><p class="form-fine">When you submit the form, you agree that Evollon may contact you by phone, text or email about your appointment and this offer.</p><div class="form-result" id="form-result" role="alert" hidden></div></form></div></section>
    <section class="trust-section"><div class="wrap trust-wrap"><div class="trust-heading"><div class="eyebrow">THE EVOLLON EXPERIENCE</div><h2>Why Evollon?</h2><div class="google-profile"><div class="google-profile-top"><strong>Evollon Medspa &amp; Wellness</strong></div><div><span class="google-g" aria-label="Google">G</span><b>5.0</b> <span class="stars" aria-label="5 out of 5 stars">★★★★★</span> <span>48 Google reviews</span></div><small>Medical spa in New York</small></div></div><div class="review-grid"><article class="review-card"><div class="review-head"><span class="review-avatar blue">M</span><div><strong>Moon</strong><small>4 reviews · 1 photo</small></div></div><div class="review-meta"><span class="stars" aria-label="5 out of 5 stars">★★★★★</span><span>a week ago</span><b>New</b></div><p>“Nadia did a phenomenal job with my lips. I didn’t feel pain, she has the most gentle hands, and she took her time to explain everything. She is so sweet and welcoming.”</p></article><article class="review-card"><div class="review-head"><span class="review-avatar green">J</span><div><strong>Jose Caba</strong><small>3 reviews</small></div></div><div class="review-meta"><span class="stars" aria-label="5 out of 5 stars">★★★★★</span><span>3 weeks ago</span><b>New</b></div><p>“Beautiful experience for my mother on her birthday for Botox treatment. Nadia was amazing, and my mom left very happy. Highly recommended!”</p></article><article class="review-card"><div class="review-head"><span class="review-avatar blue">S</span><div><strong>Stella Mullayev</strong><small>10 reviews</small></div></div><div class="review-meta"><span class="stars" aria-label="5 out of 5 stars">★★★★★</span><span>2 months ago</span></div><p>“Nadia was wonderful. She made me feel comfortable from the start, answered all of my questions, and explained everything thoroughly. Her professionalism and genuine care really stood out.”</p></article></div></div></section>
    <section class="evollon-gallery" aria-label="Evollon Med Spa treatment experience"><div class="wrap gallery-wrap"><img src="assets/evollon-treatment.webp" alt="Evollon Med Spa provider providing a facial treatment" width="1100" height="629" loading="lazy"><img src="assets/evollon-wellness.webp" alt="Evollon Med Spa provider attending to a client in a treatment room" width="1100" height="629" loading="lazy"></div></section>
    <section class="faq-section wrap"><div class="section-heading"><div class="eyebrow">GOOD TO KNOW</div><h2>Questions? <em>Let's talk.</em></h2></div><div class="faq-list">{faqs}</div></section>
    <section class="visit-section"><div class="wrap visit-grid"><div><div class="eyebrow">COME SEE US</div><h2>Close to home. <em>Here for you.</em></h2><p>Evollon Med Spa &amp; Wellness<br>105-09 Metropolitan Ave, Ste 2<br>Forest Hills, NY 11375</p></div><div class="map-frame"><iframe title="Map to Evollon Med Spa in Forest Hills" src="https://www.google.com/maps?q=105-09%20Metropolitan%20Ave%20Ste%202%2C%20Forest%20Hills%2C%20NY%2011375&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div></section>
  </main>
  <footer><div class="wrap footer-inner"><div><span class="wordmark">EVOLLON <small>MED SPA &amp; WELLNESS</small></span><p>105-09 Metropolitan Ave, Ste 2, Forest Hills, NY 11375</p></div></div><div class="wrap footer-bottom">© Evollon Med Spa &amp; Wellness. Treatment suitability and results vary. Consultation information does not replace medical advice.</div></footer>
  <dialog class="thanks-dialog" id="thanks-dialog" aria-labelledby="thanks-title"><h2 id="thanks-title">Thanks. We'll be in touch with you shortly.</h2><button class="button button-primary" id="thanks-close" type="button">Close</button></dialog>
  <div class="sticky-cta" id="sticky-cta">{'<a class="sticky-offer" href="#consultation"><b>Get $100 OFF Botox</b><small>Only For the Month of ' + CURRENT_MONTH + '</small></a>' if key == 'botox' else '<a class="sticky-offer" href="#consultation"><b>Get $125 OFF Lip Filler</b><small>New clients only · Ends September 30</small></a>'}</div>
</body>
</html>'''


for key, offer in OFFERS.items():
    (ROOT / offer["file"]).write_text(render(key, offer), encoding="utf-8")
    print(f"Wrote {offer['file']}")
