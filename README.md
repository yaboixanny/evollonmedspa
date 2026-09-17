# Evollon landing pages

- `index.html` is the Botox page.
- `lip-filler.html` is the lip filler page.

Both pages use `styles.css` and `site.js`. The forms use Netlify Forms and show a thank-you dialog after a successful submission. Enable form detection in Netlify and redeploy. Submissions appear in the Netlify dashboard; to receive emails, configure Forms → Submission notifications. Forms only submit on the deployed site, not when the HTML files are opened directly from disk. There is no booking or payment backend connected.

## Add offer pricing

Edit the relevant treatment in `OFFERS` inside `build_pages.py`, including the pricing FAQ and offer copy, then run:

```sh
python3 build_pages.py
```

The Botox page currently shows $249 for the first 30 units, $100 off the normal price. The Lip Filler page shows full lip enhancement for $375 (normally $500), a $125 saving for new clients through September 30.

## Preview locally

```sh
python3 -m http.server 8765
```

Open `http://localhost:8765/` for Botox and `http://localhost:8765/lip-filler.html` for lip filler.
