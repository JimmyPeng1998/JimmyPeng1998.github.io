# Renfeng Peng's academic website

Personal website built with Jekyll and jekyll-scholar, based on the Dumbarton theme. The original theme license is retained in LICENSE.txt.

## Update content

- `index.md`: biography.
- `_layouts/home.html`: portrait caption, Updates, presentations, awards, and thesis links.
- `_config.yml`: email, postal address, author, and social preview image.
- `_bibliography/papers.bib`: publications shared by the homepage and `/publications.html`. Store DOI identifiers as `10.…`; full DOI URLs are also supported. Only add code links to the relevant repository.
- `_data/projects.yml`: software projects.
- `_data/education.yml`: education.
- `assets/pdf/Renfeng_CV.pdf`: public CV download. Replace this file after compiling the CV locally.

The CV source directory `assets/pdf/Renfeng_CV/` is excluded from the published website. Its tracked source files remain visible in the Git repository. Generated LaTeX files and `.DS_Store` files are ignored. Historical copies remain in Git history.

Template About, Blog, Tags, and example posts are excluded from publication. `/contact.html` uses the configured address and email; the email link opens the visitor's email application. There is no server-side contact form.

## Build and preview

Install the Ruby version in `.ruby-version` using your preferred Ruby version manager, then run:

```sh
bundle install
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py _site
bundle exec jekyll serve
```

Open http://127.0.0.1:4000 for the local preview. Dependencies are locked in `Gemfile.lock`; include that file when committing dependency updates. Do not commit `_site`, `vendor`, or local build caches.

## Deploy

GitHub Pages must use **GitHub Actions** as its publishing source. The workflow in `.github/workflows/jekyll.yml` reads `.ruby-version`, installs the locked dependencies, builds the site, checks the generated output, and deploys on pushes to `master`. It can also be run manually in GitHub Actions.

Before committing, review `git status` and `git diff`, including any CV changes. Build and run the checks above, commit the intended files, then push to `master`. Confirm that the build and deployment jobs finish successfully in GitHub Actions.

## Appearance

The homepage uses an obsidian background and mint accents. Color tokens and responsive layout rules are in `css/main.css`; font loading is in `_includes/head.html`. Headings use Space Grotesk, body text uses Inter, and dates use IBM Plex Mono, with system font fallbacks.

`_includes/geometry.html` contains the decorative SVG. Its subtle animation respects reduced-motion preferences. `assets/js/site.js` handles the research tabs, including keyboard navigation and direct links such as `/#projects`. Without JavaScript, all research sections remain readable. Older homepage updates are kept in an expandable section in `_layouts/home.html`.
