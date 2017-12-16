# BB&A Course Website

This repository holds the BB&A course website. 

## Setup

To make changes to the course website, use the Terminal to get to where you want the repository and 
run the following commands on linux or mac. Make sure you already have a GitHub account that has
permission to access the repo.

    git clone https://github.com/cproctor/bba
    cd bba
    python3 -m venv env
    source env/bin/activate
    pip install pelican markdown
    pelican -s settings.local.py
    cd output_local
    python -m pelican.server

Now you can open the site locally at [http://localhost:8000](http://localhost:8000).

## Editing

Generally, you will only need to change files in the `content` directory. These are plain old text 
files you can edit with any text editor. They are in a simple langauge called 
[Markdown](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf); 
you can basically just write text. Before you start editing, run `git pull` to make sure you 
have the most recent version of the site.

When you save a file, you need to rebuild the site to see it. Use:

    pelican -s settings.local.py

If you still have the server running, you'll see the new site when you reload it in your browser.

## Publishing changes

Once you are happy with your changes, you need to commit your work back to the repository, 
build the site for publication, and push it to Stanford's servers. Make sure you replace `cproctor`
with your own SUNetID. (You will only be able to do this if you have access to the course directory.)

    git status
    git add [whichever files you changed]
    git commit -m "A message explaining what I changed"
    git push
    pelican -s settings.published.py
    rsync -r output_published/* cproctor@rice.stanford.edu:/afs/.ir.stanford.edu/class/educ211/WWW

## More details

The site is built by a Python library called Pelican. It has [great documentation](http://docs.getpelican.com/en/stable/index.html). 

