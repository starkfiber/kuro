# Kuro browser workspace

The first SFE Kit integration is at https://starkfiber.my/kit/tools . It runs in the browser with Canvas; no uploads, inference API or account is needed.

Included: local JPEG/PNG/WebP input, bounded canvas sizing, contain/cover, crop positioning, 90-degree rotation, horizontal flip, brightness/contrast, background colour, PNG/JPEG/WebP export. Input limit 20MB / 24 megapixels; output up to 4096px per edge. Browser codec support may fall back to PNG; the extension follows the actual blob format.

`kuro.tsx`, `kuro.module.css`, `kuro-geometry.ts` are a React 19 + TypeScript component module. Copy them together and render the named `Kuro` component in a Next.js client route. The Python/OpenCV tools remain available separately. `kuro-geometry.test.ts` runs with Vitest. This repository does not include SFE account or payment source.

Validation: geometry tests, SFE lint/typecheck and production build, responsive 320/390/768/1440 layouts, real file upload/rotation/portrait-size PNG download with checked output dimensions. No universal browser codec compatibility claim. Future work: vertical flip, presets that follow manual dimensions, richer non-destructive adjustments and keyboard shortcuts.
