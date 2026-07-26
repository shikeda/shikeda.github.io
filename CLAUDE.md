# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository is the source for the HDIC project site (https://shikeda.github.io/), a Hugo static
site built with the [hugo-book](https://github.com/alex-shpak/hugo-book) theme (vendored as a git
submodule at `themes/hugo-book`). The site's primary content is the **KRM Documentation**
(`content/docs/krm/`), a bilingual (Japanese/English) reference for the *Ruiju Myōgishō* Database
(KRM), a historical Japanese lexicography resource. `content/posts/` holds a blog-style series of
working notes on related data-integration projects (SBGY phonological data, itaiji inventories,
Hugo/GitHub Actions setup, etc.).

Because the KRM Documentation is scholarly reference material, **this repository is governed by a
document hierarchy that sits above ordinary engineering conventions.** Read the "Governing
Documents" section below before editing anything under `content/docs/krm/`.

## Commands

Hugo (extended) is required; CI pins `v0.152.0` (see `.github/workflows/`), local dev has been
verified against `v0.152.2`.

```bash
# Clone with the theme submodule (required — the theme is not vendored in-tree)
git clone --recurse-submodules https://github.com/shikeda/shikeda.github.io.git
# or, if already cloned without submodules:
git submodule update --init --recursive

# Local dev server with live reload
hugo server

# Production build (matches the CI build; output goes to ./public, which is gitignored)
hugo --minify --baseURL "https://shikeda.github.io/"
```

There is no separate lint/test/typecheck toolchain — validate changes by running `hugo server`
(watch for build warnings/errors in the console, e.g. broken shortcodes or missing front matter)
and spot-checking the rendered pages, especially both language versions of any page you touch.

Deployment is automatic: pushes to `master` trigger `.github/workflows/*.yml`, which builds with
Hugo and publishes `./public` to GitHub Pages. There is no manual deploy step.

## Site Architecture

- **`content/docs/krm/NN-chapter-name/`** — numbered chapters (`01-introduction` through
  `08-case-studies`). Each chapter has a `_index.ja.md` / `_index.en.md` pair (section landing
  page) plus numbered content pages, e.g. `03-01-data-structure.ja.md` /
  `03-01-data-structure.en.md`. The numeric prefix in the filename encodes both ordering and the
  implicit outline position — preserve it when adding or moving pages.
- **Bilingual pages are file-pair based**, not a single file with language front matter: every
  `X.ja.md` is expected to have a corresponding `X.en.md` (see `I18N_POLICY.md` for when this is
  and isn't required). `config.toml` sets `defaultContentLanguage = "ja"` with
  `defaultContentLanguageInSubdir = false`, so Japanese is served at the bare path and English
  under `/en/`.
- **`content/posts/`** — informal dated notes, mixed Japanese/English, not part of the governed
  KRM Documentation hierarchy; lighter editorial standards apply.
- **`layouts/`** — minimal theme overrides on top of `themes/hugo-book`: `_default/baseof.html`,
  `_default/list.html`, `_default/single.html`, and `partials/docs/` overrides
  (`html-head.html`, `footer.html`, `language-switcher.html`). Check here first when a page isn't
  rendering the way the base theme would suggest.
- **`layouts/shortcodes/mermaid.html`** — custom shortcode that lazy-loads Mermaid.js from a CDN
  once per page render; used for diagrams in the documentation.
- **`assets/_custom.scss`** — site-wide style overrides, wired in via `BookCustomCSS` in
  `config.toml`.
- **`static/`** — images and downloadable files served as-is.
- **`public/`** — Hugo build output; gitignored, never edit directly.

## Governing Documents (KRM Documentation work)

Editing anything under `content/docs/krm/` is governed by a stack of project-standard documents,
highest authority first:

1. `PROJECT_CHARTER.md` — mission, phase lifecycle, and the binding **preservation policy**.
2. `ROADMAP.md` — current implementation priorities within the Charter.
3. `AGENTS.md` — shared operating rules for AI assistants in this repo (role boundaries, required
   working method, reporting requirements). **Read this in full before doing KRM Documentation
   work** — it is not summarized here to avoid drift between the two files.
4. `DOCUMENTATION_STYLE_GUIDE.md`, `EDITORIAL_CONVENTIONS.md`, `GLOSSARY_CONVENTIONS.md`,
   `I18N_POLICY.md`, `MAINTENANCE_CONVENTIONS.md` — operational standards for page structure,
   editing authority, terminology, language-version policy, and long-term maintenance,
   respectively.
5. `REVIEW_CHECKLIST.md` — converts the above standards into checklist items for reviewing a
   specific change.
6. `DOCUMENTATION_BLUEPRINT.md` and `CURRENT_STATE_REPORT.md` — planning/analysis references for
   target information architecture, not standards to apply directly.

When these documents conflict, the higher one in this list wins.

The single most important rule, repeated across all of the above: **AI assistants must not alter
scholarly interpretations, bibliography, examples, datasets, encoding rules, identifiers, or
database specifications** unless explicitly instructed. AI assistants may restructure, clarify,
and improve navigation/terminology/discoverability around that content, but not its substance. If
a task seems to require scholarly judgment, stop and ask rather than guessing.

The project is currently in **Phase 4 (Project Standards)** per `PROJECT_CHARTER.md` — large-scale
chapter-level refactoring of `content/docs/krm/` should not begin until the user explicitly
instructs it, even if a gap in the standards is obvious.

## Working Notes

- `content/posts/` and general Hugo/theme/build changes are ordinary engineering work and are
  **not** subject to the preservation policy above — normal judgment applies.
- Known pre-existing navigation issues (stale `/docs/notes/...` paths, `headword_chars` vs
  `headword-chars` inconsistency, leftover `localhost` links) are tracked in `ROADMAP.md`; don't
  "fix" these opportunistically inside an unrelated change without flagging it, since link targets
  in this documentation are sometimes intentionally provisional.
