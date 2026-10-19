"""Generate brand-neutral, service-specific Evollon landing pages."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).parent

SERVICES = {
    "filler-dissolving": {
        "name": "Filler Dissolving",
        "eyebrow": "Careful assessment before treatment",
        "intro": "Concerned about existing facial filler? Evollon offers consultations for dissolving certain hyaluronic acid fillers when treatment is appropriate for your needs.",
        "bullets": [
            "Personalized assessment of your concerns and filler history",
            "Discuss unwanted volume, asymmetry, or possible migration",
            "Clear explanation of suitability, risks, and aftercare",
            "Convenient Forest Hills, Queens location",
        ],
        "description": "Filler dissolving uses an enzyme-based injectable treatment to break down certain hyaluronic acid fillers. Not every filler can be dissolved this way, and not every concern requires treatment. Your provider will assess the area, review what was previously injected, and explain appropriate options.",
        "steps": [
            ("01", "Review your filler history", "Share what was treated, when it was injected, and what concerns you now."),
            ("02", "Assess the treatment area", "Your provider will examine the area and discuss whether dissolving may be appropriate."),
            ("03", "Understand the plan", "Review timing, possible swelling or bruising, risks, aftercare, and whether more than one visit may be needed."),
        ],
        "faqs": [
            ("What is filler dissolving?", "It is an injectable treatment that may break down certain fillers made with hyaluronic acid. Your provider must first confirm that the existing filler and your concern are appropriate for this approach."),
            ("Can every type of filler be dissolved?", "No. Enzyme-based dissolving treatment works on certain hyaluronic acid fillers, not every injectable product. If you do not know what was used, tell your provider everything you know about the previous treatment."),
            ("How quickly will I see a change?", "Timing varies by product, treatment area, and amount used. Swelling can temporarily affect what you see, and some people may need reassessment or additional treatment."),
            ("Are there risks?", "Possible effects include discomfort, swelling, redness, bruising, and allergic reaction. There can also be uncommon but serious risks. Your provider will review these before treatment."),
        ],
    },
    "wrinkle-relaxers": {
        "name": "Wrinkle Relaxers",
        "eyebrow": "Softer expression lines, personalized to you",
        "intro": "Explore wrinkle-relaxing injectable treatments at Evollon Med Spa & Wellness. Your consultation is tailored to the areas you want to discuss and the movement you want to preserve.",
        "bullets": [
            "Personalized consultation and facial assessment",
            "Options for selected expression lines and facial areas",
            "Discuss natural-looking goals, timing, and aftercare",
            "Convenient Forest Hills, Queens location",
        ],
        "description": "Wrinkle relaxers are injectable treatments that temporarily reduce movement in selected muscles. They may soften the appearance of certain expression lines for a limited time. Your provider will discuss the areas you want treated, your health history, and whether treatment is appropriate.",
        "steps": [
            ("01", "Choose the areas to discuss", "Point out the expression lines or facial movement you would like your provider to assess."),
            ("02", "Plan for your preferences", "Discuss how much movement you want to keep and what a realistic result may look like."),
            ("03", "Review safety and timing", "Learn about the procedure, onset, duration, aftercare, possible side effects, and important risks."),
        ],
        "faqs": [
            ("What can wrinkle relaxers help with?", "They may temporarily soften selected expression lines caused by repeated muscle movement. The appropriate areas and treatment plan depend on your anatomy and provider assessment."),
            ("Will I still look like myself?", "Your provider can discuss a plan based on your goals and how much movement you want to preserve. Results vary, and no specific outcome can be guaranteed."),
            ("How long do results last?", "Results are temporary. Timing varies by person, treatment area, and treatment plan. Your provider can explain when people commonly notice changes and when reassessment may make sense."),
            ("Is there downtime or risk?", "Many people return to usual activities soon afterward, but redness, swelling, bruising, headache, or other side effects can occur. There are also important uncommon risks that your provider will review."),
        ],
    },
    "lip-filler-consultation": {
        "name": "Lip Filler",
        "eyebrow": "Shape and definition, on your terms",
        "intro": "Explore lip filler at Evollon Med Spa & Wellness in Forest Hills. Discuss the shape, definition, balance, or fullness you want with an experienced aesthetic provider.",
        "bullets": [
            "Personalized consultation and lip assessment",
            "Discuss shape, border definition, balance, or volume",
            "Treatment planning focused on your individual features",
            "Convenient Forest Hills, Queens location",
        ],
        "description": "Lip filler is an injectable treatment used to add fullness or definition to the lips. The right amount and approach depend on your anatomy, goals, previous treatment, and provider assessment. Your consultation is the time to discuss the look you want and understand the benefits and risks.",
        "steps": [
            ("01", "Share your lip goals", "Talk about the shape, definition, symmetry, or fullness you have in mind."),
            ("02", "Plan for facial balance", "Your provider can recommend an amount and approach based on your features and treatment history."),
            ("03", "Prepare for treatment", "Review the procedure, swelling, bruising, aftercare, possible side effects, and serious risks before deciding."),
        ],
        "faqs": [
            ("What can lip filler change?", "Lip filler may add shape, border definition, balance, or fullness. Your provider can explain what may be realistic for your anatomy and goals."),
            ("Can lip filler look natural?", "A subtle result may be possible depending on your starting features, the treatment plan, and how your body responds. Explain the look you prefer during consultation."),
            ("What should I expect afterward?", "Tenderness, swelling, firmness, and bruising are common after treatment and usually improve with time. Your provider will explain aftercare and when to seek urgent help."),
            ("How long does lip filler last?", "Duration varies by person, product type, amount, and metabolism. Your provider can explain expected timing without guaranteeing a specific duration."),
        ],
    },
    "cheek-jawline-filler": {
        "name": "Cheek & Jawline Filler",
        "eyebrow": "Facial contour with your features in mind",
        "intro": "Explore cheek and jawline filler at Evollon Med Spa & Wellness. Your provider can assess facial balance and discuss options for contour, structure, or definition.",
        "bullets": [
            "Personalized facial profile and symmetry assessment",
            "Discuss cheek support, jawline definition, or contour",
            "Treatment planning based on your anatomy and goals",
            "Convenient Forest Hills, Queens location",
        ],
        "description": "Cheek and jawline fillers are injectable treatments used to add volume, support, or definition in selected facial areas. Treatment is individualized because the right placement and amount depend on your features, goals, and provider assessment.",
        "steps": [
            ("01", "Assess facial balance", "Discuss the angles, contours, or areas you would like your provider to evaluate."),
            ("02", "Map a personalized plan", "Your provider can explain possible placement, amount, and whether treating one or both areas makes sense."),
            ("03", "Review expectations", "Understand temporary swelling, bruising, aftercare, possible side effects, serious risks, and expected duration."),
        ],
        "faqs": [
            ("What can cheek filler help with?", "Cheek filler may add volume, support, or contour in selected areas. Your provider will assess how treatment could affect overall facial balance."),
            ("What can jawline filler help with?", "Jawline filler may add definition or structure in selected areas. Suitability depends on your anatomy, goals, and whether another approach may be more appropriate."),
            ("Can cheek and jawline filler be done together?", "Sometimes, but not everyone needs both areas treated. Your provider can explain whether a combined or staged plan better fits your goals."),
            ("What are the risks?", "Swelling, tenderness, bruising, lumps, or asymmetry can occur. Fillers also carry rare but serious risks, including blood-vessel complications. Your provider will review warning signs and aftercare."),
        ],
    },
    "under-eye-filler": {
        "name": "Under-Eye Filler",
        "eyebrow": "A careful approach to the under-eye area",
        "intro": "Explore an under-eye filler consultation at Evollon Med Spa & Wellness. A provider can assess hollows, facial structure, skin quality, and whether filler is appropriate for your concerns.",
        "bullets": [
            "Detailed under-eye and midface assessment",
            "Discuss hollowness, shadows, balance, and alternatives",
            "Conservative planning for a delicate treatment area",
            "Convenient Forest Hills, Queens location",
        ],
        "description": "Under-eye filler may be used to add support in selected areas beneath the eyes, but it is not appropriate for every concern or every person. Puffiness, skin laxity, pigmentation, and facial structure can affect whether filler is likely to help. A careful in-person assessment is essential.",
        "steps": [
            ("01", "Identify what creates the shadow", "Your provider will assess hollowness, puffiness, skin quality, and the relationship between the under-eye and cheek."),
            ("02", "Compare appropriate options", "Learn whether filler, another treatment, or no treatment is the safest match for your concern."),
            ("03", "Understand the risks", "Review swelling, bruising, prolonged puffiness, contour changes, aftercare, and rare but serious vascular complications."),
        ],
        "faqs": [
            ("What can under-eye filler help with?", "It may help selected cases of under-eye hollowing or support-related shadowing. It does not directly treat every cause of dark circles or puffiness."),
            ("Who may not be a good candidate?", "People with prominent under-eye bags, certain skin or medical conditions, or concerns unlikely to improve with filler may need a different approach. Only an in-person assessment can determine suitability."),
            ("Will it remove dark circles?", "Dark circles can have several causes, including pigmentation, visible vessels, shadowing, or skin quality. Filler may only help when hollowing or structure contributes to the appearance."),
            ("What are the risks?", "Swelling, bruising, lumps, asymmetry, or prolonged puffiness can occur. Fillers also have rare but serious blood-vessel and vision-related risks. Your provider will review these carefully."),
        ],
    },
    "smile-lines-filler": {
        "name": "Smile Lines Filler",
        "eyebrow": "Support and balance around the smile",
        "intro": "Explore filler for smile lines at Evollon Med Spa & Wellness. Your provider can assess the folds around the nose and mouth, nearby facial support, and the treatment options that may fit your goals.",
        "bullets": [
            "Personalized assessment of facial folds and support",
            "Discuss direct treatment and nearby areas that affect balance",
            "Conservative planning based on your facial movement",
            "Convenient Forest Hills, Queens location",
        ],
        "description": "Smile lines, also called nasolabial folds, are the creases that extend from the sides of the nose toward the corners of the mouth. Filler may soften their appearance in selected cases, but the best plan may also consider cheek support, facial movement, and overall balance.",
        "steps": [
            ("01", "Assess the full area", "Your provider will look at the folds, nearby volume, facial movement, and what you would like to change."),
            ("02", "Choose a balanced approach", "Discuss whether direct treatment, support in another area, or a different option may fit your features."),
            ("03", "Plan for recovery", "Review swelling, bruising, aftercare, possible side effects, serious risks, and realistic expectations."),
        ],
        "faqs": [
            ("What are smile lines?", "Smile lines are the folds that run from the sides of the nose toward the corners of the mouth. They are a normal facial feature and may become more noticeable over time."),
            ("Can filler soften smile lines?", "Filler may soften selected folds by adding support or volume, but results depend on anatomy and the cause of the crease. Your provider will assess the surrounding face before recommending treatment."),
            ("Will my smile still look natural?", "The goal and amount of change are part of your consultation. Your provider can discuss a conservative plan designed around your facial movement and preferences."),
            ("What are the risks?", "Possible effects include tenderness, swelling, bruising, lumps, or asymmetry. Rare but serious blood-vessel complications can occur. Your provider will explain warning signs and aftercare."),
        ],
    },
    "collagen-stimulator": {
        "name": "Collagen Stimulator",
        "eyebrow": "Gradual-looking support, personalized to you",
        "intro": "Explore collagen-stimulating injectable treatments at Evollon Med Spa & Wellness. Your provider can explain how these treatments differ from traditional fillers and whether they fit your goals.",
        "bullets": [
            "Personalized facial and skin-quality assessment",
            "Discuss gradual changes, treatment areas, and timing",
            "Understand the treatment series, aftercare, and risks",
            "Convenient Forest Hills, Queens location",
        ],
        "description": "Collagen stimulators are injectable treatments intended to encourage gradual collagen production in treated areas. They work differently from fillers that create an immediate volume change. Results develop over time and may require a planned series of treatments.",
        "steps": [
            ("01", "Clarify your goals", "Discuss facial support, contour, or skin-quality concerns and the pace of change you prefer."),
            ("02", "Build a treatment timeline", "Your provider can explain possible treatment areas, number of sessions, and when changes may become noticeable."),
            ("03", "Review aftercare and risk", "Learn about temporary swelling or bruising, massage instructions when applicable, nodules, and other possible complications."),
        ],
        "faqs": [
            ("How is a collagen stimulator different from filler?", "Traditional fillers may create a more immediate volume change. Collagen stimulators are intended to support gradual collagen production, so changes generally develop over time."),
            ("When will I see results?", "Timing varies and results are not immediate. Your provider can explain the expected progression, treatment schedule, and when reassessment may be appropriate."),
            ("How many treatments might I need?", "The number of sessions depends on the treatment plan, area, and your goals. Some people may be advised to complete a series rather than a single visit."),
            ("What are the risks?", "Tenderness, swelling, bruising, asymmetry, or nodules can occur, along with uncommon but serious complications. Follow all aftercare instructions and contact the practice with concerns."),
        ],
    },
}

RELATED = {
    "filler-dissolving": [("Explore all med spa services", "../aesthetics/"), ("Learn about lip filler", "../lip-filler-consultation/")],
    "wrinkle-relaxers": [("Explore all med spa services", "../aesthetics/"), ("Learn about collagen stimulators", "../collagen-stimulator/")],
    "lip-filler-consultation": [("View the current lip filler offer", "../lip-filler.html"), ("Learn about cheek & jawline filler", "../cheek-jawline-filler/")],
    "cheek-jawline-filler": [("Learn about lip filler", "../lip-filler-consultation/"), ("Learn about collagen stimulators", "../collagen-stimulator/")],
    "under-eye-filler": [("Explore all med spa services", "../aesthetics/"), ("Learn about smile lines filler", "../smile-lines-filler/")],
    "smile-lines-filler": [("Learn about under-eye filler", "../under-eye-filler/"), ("Learn about cheek & jawline filler", "../cheek-jawline-filler/")],
    "collagen-stimulator": [("Explore all med spa services", "../aesthetics/"), ("Learn about cheek & jawline filler", "../cheek-jawline-filler/")],
}


def render(slug, service):
    name = service["name"]
    bullets = "\n".join(f"            <li>{escape(item)}</li>" for item in service["bullets"])
    steps = "\n".join(
        f'        <article class="step"><span>{number}</span><h3>{escape(title)}</h3><p>{escape(copy)}</p></article>'
        for number, title, copy in service["steps"]
    )
    faqs = "\n".join(
        f'        <details><summary>{escape(question)}</summary><div class="answer">{escape(answer)}</div></details>'
        for question, answer in service["faqs"]
    )
    related = "".join(f'<a class="button button-outline" href="{href}">{escape(label)}</a>' for label, href in RELATED[slug])
    canonical = f"https://evollon.onlynearyou.com/{slug}/"
    form_name = f"search-{slug}-lead"
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f8f2ee">
  <meta name="description" content="Explore {escape(name)} at Evollon Med Spa &amp; Wellness in Forest Hills, Queens. Request a personalized consultation.">
  <link rel="canonical" href="{canonical}">
  <title>{escape(name)} in Forest Hills, Queens | Evollon Med Spa</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;0,700;1,400;1,700&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css">
  <script src="../site.js" defer></script>
  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
  new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  }})(window,document,'script','dataLayer','GTM-W4987RVB');</script>
  <!-- End Google Tag Manager -->
  <!-- Meta Pixel Code -->
  <script>
  !function(f,b,e,v,n,t,s)
  {{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)}};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}}(window,document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init','1474880180835813');
  fbq('track','PageView');
  </script>
  <noscript><img height="1" width="1" style="display:none" alt="" src="https://www.facebook.com/tr?id=1474880180835813&amp;ev=PageView&amp;noscript=1"></noscript>
  <!-- End Meta Pixel Code -->
</head>
<body data-treatment="aesthetics" data-page="service">
  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-W4987RVB" height="0" width="0" style="display:none;visibility:hidden" title="Google Tag Manager"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->
  <div class="announcement">{escape(name)} Consultations in Forest Hills, Queens</div>
  <header class="site-header wrap"><div class="wordmark">Evollon Med Spa &amp; Wellness</div><div class="header-address">105-09 Metropolitan Ave, Ste 2, Forest Hills, NY 11375</div></header>
  <main>
    <section class="hero aesthetics-hero"><div class="hero-inner wrap"><div class="hero-copy">
      <div class="eyebrow"><span class="line"></span> {escape(service['eyebrow'])}</div>
      <h1><em>{escape(name)}</em> in Forest Hills, Queens</h1>
      <p class="intro">{escape(service['intro'])}</p>
      <ul class="check-list">
{bullets}
      </ul>
      <div class="hero-actions"><a class="button button-primary" href="#lead-form">Request a consultation</a></div>
    </div></div></section>

    <section class="consult-section" id="consultation"><div class="wrap consult-grid"><div class="consult-copy"><div class="eyebrow">LET'S TALK</div><h2>Start with a <em>personal consultation.</em></h2><p>Tell us what you would like to discuss. An Evollon team member will follow up about your goals and consultation options.</p><div class="contact-line"><span aria-hidden="true">⌖</span><div><strong>Visit us in Forest Hills</strong><br>105-09 Metropolitan Ave, Ste 2<br>Forest Hills, NY 11375<br><a href="tel:+13477409508">347-740-9508</a> · <a href="mailto:info@evollon.com">info@evollon.com</a></div></div></div>
      <form class="form-card" id="lead-form" name="{form_name}" method="POST" data-netlify="true" aria-label="Request a {escape(name)} consultation">
        <input type="hidden" name="form-name" value="{form_name}"><input type="hidden" name="treatment" value="{escape(name)} Consultation">
        <div class="form-title">Request a consultation<span>We'll help you take the next step.</span></div>
        <label for="full-name">Full name <span class="required">*</span></label><input id="full-name" name="name" autocomplete="name" required placeholder="Full name">
        <label for="email">Email <span class="optional">(optional)</span></label><input id="email" name="email" type="email" autocomplete="email" placeholder="Email">
        <label for="phone">Phone <span class="required">*</span></label><input id="phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required placeholder="Phone">
        <label class="consent-option" for="contact-consent"><input id="contact-consent" name="contact-consent" type="checkbox" value="Agreed" required><span>I agree that Evollon may call or text me at the number provided about this request and appointment scheduling. Message and data rates may apply. Reply STOP to opt out. Consent is not a condition of purchase. <span class="required">*</span></span></label>
        <label class="consent-option" for="marketing-consent"><input id="marketing-consent" name="marketing-consent" type="checkbox" value="Agreed"><span>Yes, I would also like to receive occasional promotional texts and emails from Evollon. This is optional, and I can unsubscribe at any time.</span></label>
        <button class="button button-primary submit" type="submit">Request my {escape(name)} consultation</button>
        <p class="form-fine">Evollon uses your information to respond to this request. Read the <a href="https://evollon.com/privacy-policy/" target="_blank" rel="noopener noreferrer">Privacy Policy</a> to learn what is collected, how it is used, who may receive it, and how to contact Evollon about your data.</p><div class="form-result" id="form-result" role="alert" hidden></div>
      </form>
    </div></section>

    <section class="content-section service-focus wrap"><div class="section-heading"><div class="eyebrow">ABOUT THE TREATMENT</div><h2>A plan built around <em>your goals.</em></h2><p>{escape(service['description'])}</p></div><div class="steps">
{steps}
    </div></section>

    <section class="trust-section"><div class="wrap trust-wrap"><div class="trust-heading"><div class="eyebrow">THE EVOLLON EXPERIENCE</div><h2>Why choose Evollon Med Spa?</h2><div class="google-profile"><div class="google-profile-top"><strong>Evollon Medspa &amp; Wellness</strong></div><div><span class="google-g" aria-label="Google">G</span><b>5.0</b> <span class="stars" aria-label="5 out of 5 stars">★★★★★</span> <span>48 Google reviews</span></div><small>Medical spa in New York</small></div></div><div class="review-grid"><article class="review-card"><div class="review-head"><span class="review-avatar blue">M</span><div><strong>Moon</strong><small>4 reviews · 1 photo</small></div></div><div class="review-meta"><span class="stars" aria-label="5 out of 5 stars">★★★★★</span><span>a week ago</span><b>New</b></div><p>“Nadia did a phenomenal job with my lips. I didn’t feel pain, she has the most gentle hands, and she took her time to explain everything. She is so sweet and welcoming.”</p></article><article class="review-card"><div class="review-head"><span class="review-avatar blue">S</span><div><strong>Stella Mullayev</strong><small>10 reviews</small></div></div><div class="review-meta"><span class="stars" aria-label="5 out of 5 stars">★★★★★</span><span>2 months ago</span></div><p>“Nadia was wonderful. She made me feel comfortable from the start, answered all of my questions, and explained everything thoroughly. Her professionalism and genuine care really stood out.”</p></article></div></div></section>

    <section class="evollon-gallery" aria-label="Evollon Med Spa treatment experience"><div class="wrap gallery-wrap"><img src="../assets/evollon-treatment.webp" alt="Evollon Med Spa provider providing an aesthetic treatment" width="1100" height="629" loading="lazy"><img src="../assets/evollon-wellness.webp" alt="Evollon Med Spa provider attending to a client in a treatment room" width="1100" height="629" loading="lazy"></div></section>

    <section class="faq-section wrap"><div class="section-heading"><div class="eyebrow">GOOD TO KNOW</div><h2>{escape(name)} questions, <em>answered.</em></h2></div><div class="faq-list">
{faqs}
    </div></section>

    <section class="visit-section"><div class="wrap visit-grid"><div><div class="eyebrow">COME SEE US</div><h2>Your Forest Hills <em>med spa.</em></h2><p>Evollon Med Spa &amp; Wellness<br>105-09 Metropolitan Ave, Ste 2<br>Forest Hills, NY 11375</p></div><div class="map-frame"><iframe title="Map to Evollon Med Spa in Forest Hills" src="https://www.google.com/maps?q=105-09%20Metropolitan%20Ave%20Ste%202%2C%20Forest%20Hills%2C%20NY%2011375&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div></section>

    <section class="other-treatment related-services wrap"><div><div class="eyebrow">RELATED SERVICES</div><h2>Continue exploring your options.</h2></div><div class="related-links">{related}</div></section>
  </main>
  <footer><div class="wrap footer-inner"><div><span class="wordmark">EVOLLON <small>MED SPA &amp; WELLNESS</small></span><p>105-09 Metropolitan Ave, Ste 2, Forest Hills, NY 11375<br><a href="tel:+13477409508">347-740-9508</a> · <a href="mailto:info@evollon.com">info@evollon.com</a></p></div></div><div class="wrap footer-bottom"><a href="https://evollon.com/privacy-policy/" target="_blank" rel="noopener noreferrer">Privacy Policy</a><br>© Evollon Med Spa &amp; Wellness. Treatment suitability and results vary. Consultation information does not replace medical advice.</div></footer>
  <dialog class="thanks-dialog" id="thanks-dialog" aria-labelledby="thanks-title" aria-describedby="thanks-message"><h2 id="thanks-title">Thanks—your request has been received.</h2><p id="thanks-message">An Evollon team member will call or text you, usually within one business day. For immediate assistance, call <a href="tel:+13477409508">347-740-9508</a>.</p><button class="button button-primary" id="thanks-close" type="button">Close</button></dialog>
  <div class="sticky-cta is-hidden" id="sticky-cta"><a class="sticky-offer" href="#lead-form"><b>Request a {escape(name)} Consultation</b><small>Personalized care in Forest Hills, Queens</small></a></div>
</body>
</html>'''


for slug, service in SERVICES.items():
    directory = ROOT / slug
    directory.mkdir(exist_ok=True)
    (directory / "index.html").write_text(render(slug, service), encoding="utf-8")
    print(f"Wrote {slug}/index.html")
