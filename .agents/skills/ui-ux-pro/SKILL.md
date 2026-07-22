---
name: ui-ux-pro
description: Professional UI/UX design and frontend development guidelines for building visually stunning, modern, responsive, and accessible web interfaces. Use this skill whenever designing, building, refactoring, or polishing web application user interfaces, CSS design systems, or HTML components.
---

# 🎨 UI/UX Pro Design System & Guidelines

This skill provides comprehensive, production-grade UI/UX design and frontend architecture standards. Apply these principles to create high-impact, modern, and intuitive user interfaces.

---

## 🏛️ 1. Design System & Design Tokens

### Color Palette Architecture
- **Avoid Generic Default Colors**: Never use raw `#ff0000` red, `#00ff00` green, or plain `#0000ff` blue. Use tailored HSL/Hex colors.
- **Dark Mode Palette**:
  - Background Base: `#050811` or `#0a0f1d`
  - Surface Cards: `#0c1322` or `#111827`
  - Inner Containers: `#070d19` or `#1f2937`
  - Text Primary: `#ffffff`
  - Text Secondary: `#cbd5e1` / `#94a3b8`
  - Muted Text: `#64748b`
- **Gradients & Accents**: Use sleek linear/radial gradients (e.g. `linear-gradient(135deg, #2563eb 0%, #06b6d4 100%)`).

### Elevation, Depth & Glassmorphism
- **Depth Shadows**: Use multi-layered elevation shadows:
  ```css
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8), 0 0 30px rgba(37, 99, 235, 0.15);
  ```
- **Glassmorphism Effect**: Combine semi-transparent backgrounds with backdrop blur:
  ```css
  background: rgba(12, 19, 34, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  ```

### Typography Hierarchy
- **Font Pairings**: Combine a strong display font for headings with a clean sans-serif for body text:
  - Headings: `'Outfit'`, `'Plus Jakarta Sans'`, or `'Poppins'`
  - Body & UI: `'Inter'`, `'Roboto'`, or system font stacks
- **Fluid Typography**: Use `clamp()` for responsive text scaling without breakpoint jumps:
  ```css
  font-size: clamp(1.5rem, 4vw + 1rem, 2.5rem);
  ```

---

## 📐 2. Layout, Structure & Responsiveness

### Semantic HTML5
- Always wrap page structures in semantic HTML elements: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`.
- Maintain a strict heading order (`<h1>` ➔ `<h2>` ➔ `<h3>`). Only one `<h1>` per page.

### Grid & Flexbox Containers
- Use CSS Grid for overall page layouts and multi-card grids:
  ```css
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  ```
- Use Flexbox for aligned component items, control bars, and toolbars.

### Touch Targets & Spacing Scale
- Ensure all interactive elements (buttons, links, inputs) have a minimum touch target size of `44px x 44px`.
- Use a consistent 8-point spacing grid: `4px`, `8px`, `12px`, `16px`, `24px`, `32px`, `48px`, `64px`.

---

## ⚡ 3. Motion Design & Micro-Interactions

### Smooth Transitions
- Apply timing functions to hover, focus, and state transitions:
  ```css
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  ```

### Hover & Active Feedback
- Add micro-animations on hover and click:
  - Lift Effect: `transform: translateY(-2px);`
  - Glow Expansion: `box-shadow: 0 0 20px rgba(6, 182, 212, 0.4);`
  - Active Press: `transform: translateY(0) scale(0.98);`

### Keyframe Animations
- Use subtle entry animations for cards, modals, and toasts:
  ```css
  @keyframes fadeInSlide {
      from { opacity: 0; transform: translateY(12px); }
      to { opacity: 1; transform: translateY(0); }
  }
  ```

---

## ♿ 4. Accessibility (a11y) & UX Best Practices

### Contrast & State Clarity
- Ensure contrast ratio meets WCAG AA standards (minimum 4.5:1 for normal text).
- Visible focus rings for keyboard navigation:
  ```css
  :focus-visible {
      outline: 2px solid var(--primary-cyan);
      outline-offset: 2px;
  }
  ```

### ARIA & Inputs
- Add descriptive `aria-label` attributes to icon-only buttons.
- Styled dropdown `<option>` elements must explicitly set background and text colors to prevent white-on-white browser bugs in Windows Chrome/Edge.

### Visual State Feedback
- Provide immediate visual feedback for all user actions:
  - Loading states (spinners, skeletons, pulse dots)
  - Success / Warning / Error toast notifications
  - Helpful empty states (never leave blank unstyled screens)
