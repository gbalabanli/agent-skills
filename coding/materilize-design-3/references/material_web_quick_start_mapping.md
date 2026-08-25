# Material Web Quick-Start Mapping

Source: <https://github.com/material-components/material-web/blob/main/docs/quick-start.md>

## 1) Prototype path (CDN + import map)

Use this for fast demos and throwaway prototypes.

```html
<head>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
  <script type="importmap">
    {
      "imports": {
        "@material/web/": "https://esm.run/@material/web/"
      }
    }
  </script>
  <script type="module">
    import '@material/web/all.js';
    import {styles as typescaleStyles} from '@material/web/typography/md-typescale-styles.js';
    document.adoptedStyleSheets.push(typescaleStyles.styleSheet);
  </script>
</head>
```

## 2) Production path (NPM)

Install:

```bash
npm install @material/web
```

Import only what you use:

```js
// index.js
import '@material/web/button/filled-button.js';
import '@material/web/button/outlined-button.js';
import '@material/web/checkbox/checkbox.js';
```

Use in HTML:

```html
<script type="module" src="./index.js"></script>

<label>
  Material 3
  <md-checkbox checked></md-checkbox>
</label>

<md-outlined-button>Back</md-outlined-button>
<md-filled-button>Next</md-filled-button>
```

## 3) Build fallback (Rollup quick start)

Use when unresolved bare module specifiers break runtime.

```bash
npm install rollup @rollup/plugin-node-resolve
npx rollup -p @rollup/plugin-node-resolve index.js -o bundle.js
```

Then reference:

```html
<script src="./bundle.js"></script>
```

## 4) Required implementation notes

- Prefer importing specific components rather than `all.js` in production.
- Keep MD3 typography enabled when using `md-typescale-*` utility classes.
- Confirm each used `<md-*>` tag has its corresponding JS import.

