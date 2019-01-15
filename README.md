# BB&A Course Website

This repository holds the BB&A course website. 

## Setup

To make changes to the course website, use the Terminal to get to where you want the repository and 
run the following commands on Linux, Mac, or Windows Subsystem for Linux. Make sure you already have 
a GitHub account that has permission to access the repo.

    git clone https://github.com/cproctor/bba
    git checkout tc # If at TC, you'll want to work on the TC branch
    cd bba
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    pelican -s settings.local.py
    open output_local/index.html

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

Now you can reload the page in your browser to see your changes after every save.

## Publishing changes

Once you are happy with your changes, you need to commit your work back to the repository, 
build the site for publication, and push it to Stanford's servers. Make sure you replace `cproctor`
with your own SUNetID. (You will only be able to do this if you have access to the course directory.)

    git status
    git add [whichever files you changed]
    git commit -m "A message explaining what I changed"
    git push
    pelican -s settings.published.py

Now you can push the built site to the BBA server, using `upload.sh`. See that script for instructions.

## More details

The site is built by a Python library called Pelican. It has [great documentation](http://docs.getpelican.com/en/stable/index.html). 

