# HTMX Explorer

An interactive demo app for learning [htmx](https://htmx.org) — built for the [Alamo Python Group](https://alamopython.com).

Browse 16 concepts from beginner to "I could build a real app", with a live demo and request/response inspector for each one.

![HTMX Explorer](alamo-python-logo.jpg)

## Quick Start

```bash
git clone https://github.com/rchrdgwr/htmx-explorer.git
cd htmx-explorer
python server.py
```

Then open **http://localhost:8765** in your browser.

Python 3.7+ required. No other dependencies.

## What's Inside

| # | Concept | What you learn |
|---|---------|----------------|
| 1 | Basic Request | `hx-get`, server returns HTML not JSON |
| 2 | HTTP Verbs | `hx-get` `hx-post` `hx-put` `hx-delete` |
| 3 | Targeting | `hx-target` with CSS selectors and `closest` |
| 4 | Swap Strategies | `hx-swap` — innerHTML, outerHTML, beforeend… |
| 5 | Triggering | `hx-trigger` — clicks, keyup, hover, polling |
| 6 | Forms | `hx-post` on a form, validation, inline errors |
| 7 | Loading Indicators | Spinners with `hx-on` events |
| 8 | Out-of-Band Swaps | `hx-swap-oob` — one response, many targets |
| 9 | Confirmation | `hx-confirm` before destructive actions |
| 10 | Inline Editing | Click to edit, save returns updated view |
| 11 | Polling | `hx-trigger="every 5s"` |
| 12 | Infinite Scroll | `hx-trigger="revealed"` |
| 13 | hx-boost | Convert links/forms without changing them |
| 14 | hx-push-url | Browser history and bookmarkable URLs |
| 15 | Event System | Custom events, decoupled components |
| 16 | Server-Driven UI | Patterns: CRUD, wizard, dashboard, master/detail |

## How It Works

Each example has two tabs:

- **Concept** — explains the idea with a diagram and code snippet
- **Live Demo** — interactive demo running against the local server

The right panel shows:
- **Page Source** — the body HTML with htmx attributes
- **Response Received** — the actual HTML fragment returned by the server

## Structure

```
htmx_explorer/
├── server.py          # Local dev server (handles GET/POST/PUT/DELETE)
├── index.html         # Explorer shell
├── home.html          # Landing page
├── slides.html        # Intro slide deck (8 slides)
├── concepts/          # Concept explanation pages (one per topic)
└── examples/          # Live demo pages
    └── responses/     # HTML fragments returned by the server
```

## The Big 7

If you only remember seven things, these cover 80–90% of real htmx apps:

```html
hx-get    hx-post    hx-target    hx-swap    hx-trigger    hx-swap-oob
```

And: **the server returns HTML, not JSON.**

## Resources

- [htmx.org](https://htmx.org) — official docs
- [htmx Discord](https://htmx.org/discord) — community
- [Hypermedia Systems](https://hypermedia.systems) — free book by the htmx author
- [django-htmx](https://github.com/adamchainz/django-htmx) — Django integration
- [Flask + htmx](https://github.com/Konfuzzyus/htmx-flask) — Flask integration

## License

MIT
