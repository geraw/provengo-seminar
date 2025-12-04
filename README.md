
# Provengo Seminar — Slidev Deck

This repository contains a Slidev presentation for the talk:

> **From Behavioral Programming Research to Provengo**  
> Achiya Elyasaf & Gera Weiss, Ben-Gurion University of the Negev

[View Slides Online](https://geraw.github.io/provengo-seminar/) | [Download PDF](https://github.com/geraw/provengo-seminar/actions)


## Local Development

Requirements:

- Node.js 18+ (recommended 20)
- npm (or pnpm / yarn, if you prefer and adapt commands)

Install dependencies:

```bash
npm install
```

Run the slides locally:

```bash
npm run dev
```

Build a static site:

```bash
npm run build
```

Export to PDF (locally):

```bash
npm run export
```

The PDF will be created at `dist/slides.pdf`.

## GitHub Actions — PDF + GitHub Pages

A GitHub Actions workflow is configured in:

- `.github/workflows/build-and-deploy.yml`

On every push to `main`/`master` (and on manual trigger), it will:

1. Install Node + dependencies  
2. Install Playwright Chromium  
3. Run `npm run build` to produce a static site in `dist/`  
4. Run `npm run export` to generate `dist/slides.pdf`  
5. Upload `dist/slides.pdf` as a workflow artifact  
6. Upload `dist/` as a Pages artifact  
7. Deploy it to **GitHub Pages** (source = GitHub Actions)

After the first run, set your repository's **Pages** settings to:

- **Source**: GitHub Actions

GitHub will host your slides as a web page.
