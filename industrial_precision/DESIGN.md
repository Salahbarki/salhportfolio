---
name: Industrial Precision
colors:
  surface: '#f8fafa'
  surface-dim: '#d8dada'
  surface-bright: '#f8fafa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f4'
  surface-container: '#eceeee'
  surface-container-high: '#e6e8e8'
  surface-container-highest: '#e1e3e3'
  on-surface: '#191c1d'
  on-surface-variant: '#41474e'
  inverse-surface: '#2e3131'
  inverse-on-surface: '#eff1f1'
  outline: '#72787f'
  outline-variant: '#c1c7cf'
  surface-tint: '#326286'
  primary: '#003857'
  on-primary: '#ffffff'
  primary-container: '#1b4f72'
  on-primary-container: '#92c0e9'
  inverse-primary: '#9dcbf4'
  secondary: '#a23f00'
  on-secondary: '#ffffff'
  secondary-container: '#fc7127'
  on-secondary-container: '#5c2000'
  tertiary: '#283643'
  on-tertiary: '#ffffff'
  tertiary-container: '#3e4d5a'
  on-tertiary-container: '#aebdcd'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cce5ff'
  primary-fixed-dim: '#9dcbf4'
  on-primary-fixed: '#001e31'
  on-primary-fixed-variant: '#154b6d'
  secondary-fixed: '#ffdbcd'
  secondary-fixed-dim: '#ffb595'
  on-secondary-fixed: '#351000'
  on-secondary-fixed-variant: '#7c2e00'
  tertiary-fixed: '#d5e4f5'
  tertiary-fixed-dim: '#b9c8d8'
  on-tertiary-fixed: '#0e1d29'
  on-tertiary-fixed-variant: '#3a4856'
  background: '#f8fafa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e3'
typography:
  h1:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 40px
  container-max: 1200px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

This design system is built for the maintenance professional who operates at the intersection of heavy industry and high-tech precision. The brand personality is rooted in reliability, structural integrity, and meticulous organization. It avoids decorative fluff in favor of utilitarian clarity, drawing inspiration from technical blueprints and industrial control interfaces.

The aesthetic follows a **Modern Industrial** style—a hybrid of Corporate and Minimalism. It emphasizes high-contrast information density and structural grids, ensuring that technical certifications, machine logs, and project case studies are presented with absolute authority. The interface should feel as sturdy as a steel beam and as precise as a micrometer.

## Colors

The palette is anchored by **Industrial Blue (#1B4F72)**, conveying stability and professional depth. **Safety Orange (#D35400)** is used sparingly but strategically for call-to-action elements, status indicators, and critical highlights, mimicking its use in industrial environments for high visibility.

Neutral Grays provide the structural scaffolding of the UI. Backgrounds use a clean white or ultra-light gray to ensure a "modern" feel, while darker grays define borders and secondary text. This high-contrast approach ensures readability in various lighting conditions, reflecting the practical needs of a technician.

## Typography

This design system utilizes **Inter** for its neutral, systematic, and utilitarian character. It provides exceptional legibility for technical descriptions and documentation. **Work Sans** is introduced for labels and metadata to provide a slightly more grounded, architectural feel.

Headlines are tight and bold, mimicking the headers found in technical manuals. Body text is optimized for long-form reading of project reports. A "data-mono" style is included, utilizing Inter’s tabular numbers feature to ensure that technical specs, measurements, and dates align perfectly in vertical lists.

## Layout & Spacing

The layout utilizes a **Fixed Grid** model based on a 12-column system. This creates a predictable structure that implies organization and discipline. Content should be grouped into clear "modules" or sections that align strictly to the grid.

A 4px baseline rhythm ensures all elements—from icons to text blocks—are mathematically aligned. Generous margins (40px) prevent the industrial aesthetic from feeling cluttered, maintaining the "modern" aspect of the brief. Use stacked spacing to separate technical specifications from descriptive text, ensuring clear information hierarchy.

## Elevation & Depth

To maintain the precise, industrial feel, this design system avoids soft, atmospheric shadows. Instead, it uses **Tonal Layers** and **Low-Contrast Outlines**.

Depth is communicated through:
1.  **Surface Tiering:** Using slightly different shades of gray (#F2F4F4 vs #FFFFFF) to differentiate between the background and interactive cards.
2.  **Hairline Borders:** 1px solid borders in a medium gray (#D5DBDB) are used to define element boundaries, mimicking the clean lines of a blueprint.
3.  **Inset Accents:** On active states (like a pressed button), a slight inner shadow or a color shift to a darker tone can be used to simulate physical mechanical movement.

## Shapes

The shape language is primarily rectangular and rigid. A "Soft" roundedness (0.25rem) is applied to prevent the UI from feeling hostile or dated, but it remains sharp enough to feel engineered. 

Interactive elements like buttons and input fields should maintain this 4px corner radius. Larger containers (cards) can use the same radius to maintain a consistent "machined" look. Icons should follow a stroke-based, geometric style with square terminals rather than rounded ones.

## Components

### Buttons
Primary buttons use the Industrial Blue background with white text. Secondary buttons use a 1px border of the primary color. The "Danger" or "Critical" action uses Safety Orange. Buttons are rectangular with a 4px radius and should feel "heavy" and substantial.

### Technical Chips
Used for listing skills (e.g., "PLC Programming," "Hydraulics"). These use a light gray background with Industrial Blue text and a 1px border. They are not rounded pills; they are rectangles to maintain the structural theme.

### Data Tables
Maintenance logs and equipment lists should use clean, bordered tables. Header rows are Industrial Blue with white "label-caps" typography. Alternate rows use a subtle zebra-stripe (#F8F9F9) for legibility.

### Cards
Portfolio pieces are housed in cards with a 1px border. The top of the card may feature a "Status Bar" using a thin 4px strip of Safety Orange to draw the eye to active or high-priority projects.

### Status Indicators
Small, geometric indicators (squares or diamonds) using Safety Orange for "Active/In-Progress" and Industrial Blue for "Certified/Completed." Avoid soft circles to maintain the technical aesthetic.

### Input Fields
Strictly rectangular with a 1px gray border. On focus, the border thickens to 2px and changes to Industrial Blue. Labels are always positioned above the field in "label-caps" style.