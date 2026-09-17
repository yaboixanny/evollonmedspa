(() => {
  const form = document.querySelector('#lead-form');
  const result = document.querySelector('#form-result');
  const treatment = document.body.dataset.treatment === 'lip-filler' ? 'Lip Filler' : 'Botox';
  const number = '13477409508';

  if (form && result) {
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      const data = new FormData(form);
      const name = String(data.get('name') || '').trim();
      const email = String(data.get('email') || '').trim();
      const phone = String(data.get('phone') || '').trim();
      const offer = treatment === 'Botox' ? 'the first 30 units for $249 with $100 off this month' : 'the current lip filler offer';
      const message = `Hi Evollon, I'd like to ask about ${offer}. My name is ${name}. My phone is ${phone} and my email is ${email}. Please contact me about a consultation.`;
      const smsUrl = `sms:+${number}?body=${encodeURIComponent(message)}`;

      result.hidden = false;
      result.replaceChildren();
      result.append('Your text is ready. If your messaging app did not open, ');
      const textLink = document.createElement('a');
      textLink.href = smsUrl;
      textLink.textContent = 'tap here to open the text';
      result.append(textLink, '. Your request is sent only after you send the message.');
      window.location.href = smsUrl;
    });
  }

  const sticky = document.querySelector('#sticky-cta');
  const consultation = document.querySelector('#consultation');
  const hero = document.querySelector('.hero');
  if (sticky && consultation && hero && 'IntersectionObserver' in window) {
    let heroVisible = true;
    let consultationVisible = false;
    const update = () => sticky.classList.toggle('is-hidden', heroVisible || consultationVisible);
    update();
    new IntersectionObserver(([entry]) => {
      heroVisible = entry.isIntersecting;
      update();
    }, { threshold: 0.08 }).observe(hero);
    new IntersectionObserver(([entry]) => {
      consultationVisible = entry.isIntersecting;
      update();
    }, { threshold: 0.12 }).observe(consultation);
  }
})();
