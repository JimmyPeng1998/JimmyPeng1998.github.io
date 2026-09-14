"""Check the actual Jekyll output before publishing it."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site')
errors = []

class Links(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name not in ('href', 'src') or not value:
                continue
            url = urlsplit(value)
            if url.scheme or url.netloc or not url.path:
                continue
            target = root / unquote(url.path).lstrip('/') if url.path.startswith('/') else self.page.parent / unquote(url.path)
            if not target.exists():
                errors.append(f'{self.page}: missing local resource {value}')

for page in root.rglob('*.html'):
    parser = Links()
    parser.page = page
    parser.feed(page.read_text())

for name in ('index.html', 'publications.html', 'contact.html', 'assets/pdf/Renfeng_CV.pdf'):
    if not (root / name).is_file():
        errors.append(f'Missing required output: {name}')
for name in ('about.html', 'blog.html', 'tags.html', 'assets/pdf/Renfeng_CV', 'scripts'):
    if (root / name).exists():
        errors.append(f'Unexpected published content: {name}')
for path in root.rglob('*'):
    if path.is_file() and (path.name == '.DS_Store' or path.suffix in ('.tex', '.aux', '.log', '.bcf', '.blg', '.synctex')):
        errors.append(f'Unexpected published source/build file: {path}')
for name in ('index.html', 'publications.html'):
    text = (root / name).read_text() if (root / name).exists() else ''
    for required in ('Quotient geometry of tensor ring decomposition', 'https://arxiv.org/abs/2601.21874', 'https://doi.org/10.1137/24M1643773', 'https://github.com/JimmyPeng1998/GeomNTT'):
        if required not in text:
            errors.append(f'{name}: missing {required}')
for name in ('index.html', 'contact.html'):
    text = (root / name).read_text() if (root / name).exists() else ''
    for required in ('Workstation 7, Room 215, Innovation Centre, 72 Tat Chee Avenue', 'renfpeng (a.t.) cityu.edu.hk'):
        if required not in text:
            errors.append(f'{name}: missing contact information {required}')
    for unwanted in ('mailto:', 'pengrenfeng@lsec.cc.ac.cn', 'renfpeng@cityu.edu.hk', 'LanBai', 'John Doe', 'data-netlify', 'BEGIN PGP', 'jquery-3.3.1', 'gitalk.min.js', 'googletagmanager.com'):
        if unwanted in text:
            errors.append(f'{name}: unexpected {unwanted}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('Site checks passed: required pages, contact details, publications, local links, and publication exclusions.')
