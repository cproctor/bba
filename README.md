# BB&A Course Website

This repository holds the BB&A course website. 

## Setup

To make changes to the course website, use the Terminal to get to where you want the repository and 
run the following commands on linux or mac. Make sure you already have a GitHub account that has
permission to access the repo.

    git clone https://github.com/cproctor/bba
    cd bba
    python3 -m venv env
    pip install pelican
    pelican content -s settings.local.py
    python -m pelican.server

Now you can open the site locally at [http://localhost:8000](http://localhost:8000).

## Editing

Generally, you will only need to change files in the `content` directory. These are plain old text 
files you can edit with any text editor. They are in a simple langauge called 
[Markdown](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf); 
you can basically just write text. 

When you save a file, you need to rebuild the site to see it. Use:

    pelican content -s settings.local.py

## Publishing changes

Once you are happy with your changes, you need to build the site for publication, push it to Stanford's servers, 
and commit your work into the repository. Use the following commands--though make sure you replace `cproctor`
with your own SUNetID. (You will only be able to do this if you have access to the course directory.)

    git status
    git add [whichever files you changed]
    git commit -m "A message explaining what I changed"
    git push
    rsync -r output/* cproctor@rice.stanford.edu:/afs/.ir.stanford.edu/class/educ211/WWW

