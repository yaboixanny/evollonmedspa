(() => {
  const form = document.querySelector('#lead-form');
  const result = document.querySelector('#form-result');
  const dialog = document.querySelector('#thanks-dialog');
  const closeDialog = document.querySelector('#thanks-close');

  if (form && result && dialog) {
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      result.hidden = true;
      const button = form.querySelector('button[type="submit"]');
      button.disabled = true;
      try {
        const response = await fetch(window.location.pathname, {
          method: 'POST',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          body: new URLSearchParams(new FormData(form)).toString(),
        });
        if (!response.ok) {
          throw new Error('Submission was not accepted.');
        }
        const treatment = form.elements.treatment?.value || 'Consultation';
        if (document.body.dataset.treatment === 'aesthetics') {
          window.dataLayer = window.dataLayer || [];
          window.dataLayer.push({
            event: 'form_submit',
            form_name: form.getAttribute('name') || 'aesthetics-lead',
            treatment,
            page_path: window.location.pathname,
          });
        }
        form.reset();
        dialog.showModal();
        if (typeof window.fbq === 'function') {
          try {
            window.fbq('track', 'Lead', {
              content_name: treatment,
              content_category: 'Consultation Request',
            });
          } catch (_trackingError) {
            // A blocked analytics request should not affect the form confirmation.
          }
        }
      } catch (_error) {
        const phoneLink = document.body.dataset.treatment === 'aesthetics'
          ? '<a href="tel:+13477409508" onclick="gtag(\'event\',\'conversion\',{\'send_to\':\'AW-18426796196/Zl9KCL3qyaIdEKSxytJE\'})">(347) 740-9508</a>'
          : '<a href="tel:+13477409508">347-740-9508</a>';
        result.innerHTML = `Your request could not be sent. Please try again or call ${phoneLink}.`;
        result.hidden = false;
      } finally {
        button.disabled = false;
      }
    });
    closeDialog?.addEventListener('click', () => dialog.close());
  }

  const sticky = document.querySelector('#sticky-cta');
  const heroCta = document.querySelector('.hero-primary-cta');
  if (sticky && heroCta && form) {
    const update = () => {
      const heroCtaPassed = heroCta.getBoundingClientRect().bottom < 0;
      const isMobile = window.matchMedia('(max-width: 700px)').matches;
      const stickyTop = window.innerHeight - (sticky.offsetHeight || 70);
      const controlOverlapsSticky = [...form.querySelectorAll('input, button')].some((control) => {
        const rect = control.getBoundingClientRect();
        return rect.top < window.innerHeight && rect.bottom > stickyTop;
      });
      const formHasFocus = form.contains(document.activeElement);
      sticky.classList.toggle(
        'is-hidden',
        !isMobile || !heroCtaPassed || controlOverlapsSticky || formHasFocus,
      );
    };
    update();
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    form.addEventListener('focusin', update);
    form.addEventListener('focusout', update);
  }
})();
