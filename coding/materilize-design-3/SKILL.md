---
name: materilize-design-3
description: Implement UI using Material Design 3 with Material Web (`@material/web`) based on the official quick-start flow. Use when building or migrating interfaces to MD3 components, tokens, and interaction rules with production-ready import/build setup.
---

# Materilize Design 3

Use this skill to apply Material Design 3 using Material Web components with a predictable implementation workflow.

## When to use
- Creating a new UI with MD3 components
- Migrating custom or legacy UI to MD3 primitives
- Standardizing forms, buttons, fields, and selection controls
- Building a quick prototype first, then hardening for production

## Workflow

1. Run intake and scope.
- Capture target surface (page, flow, component set), platform constraints, and existing stack.
- Identify if this is `prototype` or `production`.

2. Choose integration mode.
- `prototype` mode: CDN + import map.
- `production` mode: install from NPM and bundle.
- If user does not choose, default to `production`.

3. Apply Material Web quick-start setup.
- Install: `npm install @material/web`
- Import only needed component definitions from `@material/web/<component>/<variant>.js`.
- Add typography styles (`md-typescale-styles`) when using MD3 type scale classes.
- Use `<md-*>` tags in markup.

4. Resolve module loading for production.
- If the project does not already resolve bare module specifiers, bundle with Rollup quick start:
  - `npm install rollup @rollup/plugin-node-resolve`
  - `npx rollup -p @rollup/plugin-node-resolve index.js -o bundle.js`

5. Apply MD3 component rules.
- Use semantic button hierarchy:
  - primary CTA: `md-filled-button`
  - secondary actions: `md-outlined-button`
  - low-emphasis actions: text variant
- Use MD3 input controls for stateful input: checkbox, radio, text field, switch.
- Keep form spacing and alignment consistent with a tokenized spacing scale.

6. Apply Material Design philosophy rules.
- Build clear visual hierarchy first, then decoration.
- Keep interaction predictable and reduce user effort at each step.
- Use color and shape to communicate meaning, not just style.
- Preserve accessibility as a core requirement, not a post-step.
- Keep motion purposeful and short; motion should explain state change.

7. Apply MD3 design-token rules.
- Configure color tokens at `:root` (or app theme scope) using `--md-sys-color-*` custom properties.
- Configure typography via MD type scale classes (e.g. `md-typescale-*`) or component-level styles.
- Avoid hard-coded one-off colors when a system token exists.

8. Enforce MD3 don'ts.
- Do not mix multiple design systems in one flow unless explicitly required.
- Do not override component internals with brittle deep selectors.
- Do not use multiple competing primary CTAs in the same action group.
- Do not remove focus styles or shrink hit targets below usable size.
- Do not use color alone as the only status/error signal.
- Do not hard-code spacing, colors, and type values when tokens exist.

9. Validate accessibility and behavior.
- Ensure controls have labels and focus visibility.
- Validate keyboard navigation for all interactive elements.
- Confirm disabled, error, and selected states are visually distinct.

10. Report and handoff.
- Summarize installed packages, imported components, and files changed.
- Provide exact next command to run/build/test.

## Output Rules
- Always state which mode was used (`prototype` or `production`).
- Always list imported Material components explicitly.
- If build tooling was introduced, include build command and output file path.
- If migration is partial, list remaining non-MD3 components.
- Always include a short "philosophy and don'ts compliance" note.

## Defaults
- Default mode: `production`
- Default typography: MD3 type scale enabled
- Default build fallback: Rollup quick start when unresolved module specifiers appear

## References

- [material_web_quick_start_mapping.md](references/material_web_quick_start_mapping.md)
- [md3_component_rules_checklist.md](references/md3_component_rules_checklist.md)
- [material_design_philosophy_and_donts.md](references/material_design_philosophy_and_donts.md)
