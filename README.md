# Evollon landing pages

- `index.html` is the Botox page.
- `lip-filler.html` is the lip filler page.

Both pages use `styles.css` and `site.js`. The pages use the image-free, centered funnel layout of the supplied reference. The form opens a prefilled SMS draft to **(347) 740-9508**; visitors must send the text themselves. There is no booking, payment, or lead storage backend connected.

## Add offer pricing

Edit the relevant treatment in `OFFERS` inside `build_pages.py`, including the pricing FAQ and offer copy, then run:

```sh
python3 build_pages.py
```

The current pages intentionally say “Offer details coming soon.” Keep pricing, quantities, deadlines, and guarantees off the page until they are confirmed by Evollon.

## Preview locally

```sh
python3 -m http.server 8765
```

Open `http://localhost:8765/` for Botox and `http://localhost:8765/lip-filler.html` for lip filler.
