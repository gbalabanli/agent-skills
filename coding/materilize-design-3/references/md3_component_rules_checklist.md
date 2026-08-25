# MD3 Component Rules Checklist

Use this checklist when applying `materilize-design-3`.

## Action hierarchy
- Use one primary action per view section (`md-filled-button`).
- Use outlined buttons for secondary actions.
- Keep low-emphasis actions as text-style buttons.
- Do not style random elements to look like buttons when MD3 button components exist.

## Form and input consistency
- Prefer MD3 inputs (`md-outlined-text-field`, `md-checkbox`, `md-radio`, `md-switch`) over custom controls.
- Ensure each field has a visible label.
- Keep validation, disabled, and focus states visible.

## Layout and spacing
- Use consistent spacing scale across grouped controls.
- Keep alignment predictable in forms and action rows.
- Avoid pixel-by-pixel ad hoc spacing on each component.

## Tokens and theme
- Define colors via MD3 system tokens (`--md-sys-color-*`) at root/theme scope.
- Avoid hard-coded accent colors where tokenized roles exist.
- Keep typography consistent with MD type scale classes or a documented equivalent.

## Accessibility
- Ensure all controls are keyboard reachable.
- Ensure focus indication is visible.
- Ensure contrast is acceptable for text and controls against surfaces.

## Migration guardrails
- Replace legacy custom controls incrementally by surface.
- Avoid mixing conflicting visual systems in the same flow.
- Track remaining non-MD3 components in handoff notes.

