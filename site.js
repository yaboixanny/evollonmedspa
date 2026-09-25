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
        form.reset();
        dialog.showModal();
      } catch (_error) {
        result.innerHTML = 'Your request could not be sent. Please try again or call <a href="tel:+13477409508">347-740-9508</a>.';
        result.hidden = false;
      } finally {
        button.disabled = false;
      }
    });
    closeDialog?.addEventListener('click', () => dialog.close());
  }

  const sticky = document.querySelector('#sticky-cta');
  const experienceLabel = document.querySelector('.trust-heading .eyebrow');
  if (sticky && experienceLabel) {
    const update = () => sticky.classList.toggle(
      'is-hidden',
      experienceLabel.getBoundingClientRect().top > window.innerHeight,
    );
    update();
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
  }
})();
