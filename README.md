# Evollon landing pages

- `index.html` is the Botox page.
- `lip-filler.html` is the lip filler page.
- `aesthetics/index.html` is the broad, brand-neutral med spa services landing page at `/aesthetics/`.
- `build_service_landers.py` generates the focused service pages at `/filler-dissolving/`, `/wrinkle-relaxers/`, `/lip-filler/`, `/cheek-jawline-filler/`, `/under-eye-filler/`, `/smile-lines-filler/`, and `/collagen-stimulator/`.

All pages use `styles.css` and `site.js`. The forms use Netlify Forms and show a thank-you dialog after a successful submission. Enable form detection in Netlify and redeploy. Submissions appear in the Netlify dashboard; to receive emails, configure Forms → Submission notifications. Forms only submit on the deployed site, not when the HTML files are opened directly from disk. There is no booking or payment backend connected.

## Add offer pricing

Edit the relevant treatment in `OFFERS` inside `build_pages.py`, including the pricing FAQ and offer copy, then run:

```sh
python3 build_pages.py
```

The Botox page currently shows 25 units for $175 (normally $300 at $12 per unit), a $125 saving. The Lip Filler page shows a half syringe for $249 (normally $498), a 50% saving.

## Update service landing pages

Edit the relevant entry in `SERVICES` inside `build_service_landers.py`, then run:

```sh
python3 build_service_landers.py
```

## Preview locally

```sh
python3 -m http.server 8765
```

Open `http://localhost:8765/` for Botox, `http://localhost:8765/lip-filler.html` for the lip filler offer, and `http://localhost:8765/aesthetics/` for the broad med spa page. The focused pages use the clean paths listed above.
