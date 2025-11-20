# rotoforge-website
A repository containing introductory documentation relating to the rotoforge project

## How to Add a Page

Mkdocs is configured to automatically index and publish any markdown file in the `source` directory. 

To create a new section, create a directory and place your markdown files in there. An empty folder will not be indexed.

## Building Mkdocs Static Site

You will need `python` and the ability to run Makefiles. 

To initialise the project, run `make venv` followed by `make setup`.

To serve a local copy of the site run `make serve`.

To build the static site in the out directory `docs` please run `make build`. This is also the default option if you just run `make`.