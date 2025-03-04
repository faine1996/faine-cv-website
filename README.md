# Static Site Generator

## Overview
A simple static site generator that converts Markdown files into HTML. It consists of a shell script (`main.sh`) that processes Markdown files, applies user-defined HTML templates, and outputs a structured static website. The generator is lightweight, efficient, and ideal for documentation and blogs.

## Features
Converts Markdown files to HTML, supports customizable templates, and is designed to be lightweight and fast. The processing flow scans the project directory for `.md` files, converts Markdown content into HTML using predefined templates, and outputs the generated HTML files to a specified directory.

## Running Locally
To set up and run the project, clone the repository using `git clone https://github.com/faine1996/static-site-generator.git`, navigate into the project directory with `cd static-site-generator`, ensure the main script has execution permissions by running `chmod +x main.sh`, and execute `./main.sh` to generate the static site.

## Troubleshooting
If you get a **"Permission denied"** error when running `./main.sh`, ensure that execution permissions are properly set using `chmod +x main.sh` before retrying. If issues persist, verify that the Markdown files are correctly formatted and located in the expected directory. If the script requires external tools like `pandoc` or `python`, install them using `sudo apt install pandoc` (for Debian-based systems).

## Contributing
To contribute to the project, fork the repository, create a feature branch using `git checkout -b feature-branch`, make your changes, commit them with `git commit -m "Describe your changes"`, push to your fork, and open a Pull Request on GitHub.