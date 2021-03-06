# BB&A Course Website

This repository holds the BB&A course website.

## Setup

To make changes to the course website, use the Terminal to get to where you want the repository and
run the following commands on Linux, Mac, or Windows Subsystem for Linux. Make sure you already have
a GitHub account that has permission to access the repo.

    git clone --recurse-submodules https://github.com/cproctor/bba
    cd bba
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    pelican -s settings.local.py
    cd output_local
    python -m http.server
    open http://localhost:8000

The last command should have opened your local build of the current website in a browser.

## Editing

Generally, you will only need to change files in the `content` directory. These are plain old text
files you can edit with any text editor. They are in a simple langauge called
[Markdown](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf);
you can basically just write text. Before you start editing, run `git pull` to make sure you
have the most recent version of the site.
While editing, it is helpful to use the `-r` flag to tell Pelican to rebuilt the site whenever there's a
change:

    pelican -r -s settings.local.py

Here's a quick tour of the site's content:

- `pages` appear on the main navigation menu.
- `announcements` are automatically displayed on the homepage, in date order. Use the `index` metadata property to control the order.
- `assignments`, `curriculum`, `logistics`, and `modules` are normal content you can link to or view by category.
- `slides` is for slides. Have a look at the [example slideshow](http://beyondbitsandatoms.org/slides-example.html) for details.
- `images` and `resources` are for static assets like images, readings, design files, bibtex refs, etc.

Assigned readings are not stored as part of this repository, because they are large files and due to copyright restrictions.
They are maintained separately; you can link to readings using the `READINGS_URL` defined in settings.

## Publishing changes

Once you are happy with your changes, you need to commit your work back to the repository,
build the site for publication, and push it to the production server. Before you can do this,
you'll need to add the server credentials to `upload.sh`; they are not included in this repository
because they are not public. Read `upload.sh` for setup instructions.

    git status
    git add [whichever files you changed]
    git commit -m "A message explaining what I changed"
    git push
    pelican -s settings.published.py
    ./upload.sh

## More details

The site is built by a Python library called Pelican. It has [great documentation](http://docs.getpelican.com/en/stable/index.html).
