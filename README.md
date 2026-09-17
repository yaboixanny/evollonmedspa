# Evollon landing pages

- `index.html` is the Botox page.
- `lip-filler.html` is the lip filler page.

Both pages use `styles.css` and `site.js`. The pages use the image-free, centered funnel layout of the supplied reference. The form opens a prefilled SMS draft to **(347) 740-9508**; visitors must send the text themselves. There is no booking, payment, or lead storage backend connected.

## Add offer pricing

Edit the relevant treatment in `OFFERS` inside `build_pages.py`, including the pricing FAQ and offer copy, then run:

```sh
python3 build_pages.py
```

The Botox page currently shows $249 for the first 30 units, with $100 off already applied. The Lip Filler page shows full lip enhancement for $375 (normally $500), a $125 saving for new clients through September 30.

## Preview locally

```sh
python3 -m http.server 8765
```

Open `http://localhost:8765/` for Botox and `http://localhost:8765/lip-filler.html` for lip filler.
