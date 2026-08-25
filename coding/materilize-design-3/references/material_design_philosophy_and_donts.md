# Material Design Philosophy and Don'ts

Use this reference for decisions that are not purely technical (layout, priority, interaction behavior).

## Philosophy rules

1. Prioritize clarity over decoration.
- Users should immediately understand what is primary, secondary, and informational.

2. Make actions obvious and intentional.
- Emphasize a single primary action per context.
- Keep secondary actions available but visually subordinate.

3. Design for meaning, not color cosmetics.
- Color, shape, and elevation should communicate role/state.
- Keep state semantics consistent across screens.

4. Minimize cognitive load.
- Reduce unnecessary choices and repeated decisions.
- Keep labels concise and action-oriented.

5. Preserve continuity through motion.
- Use small, purposeful transitions to explain state change.
- Avoid decorative or long animations that slow interaction.

6. Accessibility is non-negotiable.
- Maintain keyboard access, visible focus, sufficient contrast, and clear labels.
- Ensure interactive target sizes are practical on touch and desktop.

7. Build adaptive consistency.
- Keep component behavior consistent across breakpoints.
- Adapt layout density without changing core interaction patterns.

## MD3 don'ts

- Do not create multiple high-emphasis CTAs in a single action cluster.
- Do not rely on color alone for errors, warnings, or success states.
- Do not remove built-in affordances (focus ring, pressed/hover states) without valid replacements.
- Do not force custom visual overrides when a first-party Material Web component variant already exists.
- Do not mix spacing scales or typography systems across neighboring sections.
- Do not use one-off hex values when system tokens can express the same intent.
- Do not break component semantics by replacing labels with ambiguous icons only.
- Do not introduce motion that delays task completion or obscures state.

## Quick compliance pass

Before handoff, verify:
- One clear primary action per region.
- Tokenized color/type/spacing usage.
- Keyboard and focus behavior preserved.
- Error, disabled, and selected states visually and semantically clear.
- No listed don'ts violated in touched surfaces.

