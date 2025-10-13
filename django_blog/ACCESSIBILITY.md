# Accessibility Notes (WCAG 2.2)


- **Landmarks**: `<nav>` and `<main>` present; skip link to `#main`.
- **Focus**: Visible focus outline via CSS; keyboard-only navigation tested.
- **Labels**: Forms use `<label>` elements; HTMX updates wrapped in `aria-live="polite"`.
- **Color/Contrast**: Bootstrap 5 defaults; avoid overriding with low-contrast colors.
- **Dynamic Updates**: HTMX swaps target containers with live regions to announce updates.
