# frontend

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VS Code](https://code.visualstudio.com/) + [Vue (Official)](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Recommended Browser Setup

- Chromium-based browsers (Chrome, Edge, Brave, etc.):
  - [Vue.js devtools](https://chromewebstore.google.com/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd) 
  - [Turn on Custom Object Formatter in Chrome DevTools](http://bit.ly/object-formatters)
- Firefox:
  - [Vue.js devtools](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/)
  - [Turn on Custom Object Formatter in Firefox DevTools](https://fxdx.dev/firefox-devtools-custom-object-formatters/)

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```

## Email Verification Flow

- Frontend route: `/verify-email/:token?`
- Accepts token via either path param (`:token`) or query (`?token=...` or `?t=...`). Optionally supports `uid` via `?uid=` or `?u=` if your backend requires both.
- The page will call `${VITE_API_URL}security/verify-email/` using POST with JSON `{ token, uid }`. If POST is not supported, it falls back to GET with query params.
- On success, a success message is shown with a quick link to the login page.

Update your backend to redirect verification emails to one of the following URLs:

- `https://<your-frontend-domain>/verify-email/<token>`
- or `https://<your-frontend-domain>/verify-email?token=<token>[&uid=<uid>]`
