# Pegasus Studio Website

A responsive, static landing page for Pegasus Studio.

## Structure

- `index.html` — main page
- `resources/css/style.css` — all styling
- `resources/js/main.js` — theme toggle, app filtering, scroll effects
- `resources/images/pegasus-studio-banner.jpg` — supplied Pegasus Studio banner
- `resources/images/pegasus-studio-icon.jpg` — supplied Pegasus Studio icon artwork

The app icons are loaded from Google Play's public image CDN so the page reflects the current Play Store branding for the listed apps.

## Deploy

Upload the contents of this folder to the document root for `pegasusstudio.net` (for example `public_html/`). No build step or server-side code is required.

## Customize

Edit the app cards in `index.html` to add, remove or reorder apps. Colors, spacing and typography are controlled through CSS variables at the top of `resources/css/style.css`.
