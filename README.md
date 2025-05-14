# My Favorite Reads & Musings - A Static Site

This project is a personal website and blog, statically generated using a Python-based site generator. It's a place to share thoughts on favorite books, fitness journeys, and tech insights.

## Features

*   **Static Site Generation**: Built with a custom Python script that converts Markdown content into HTML pages.
*   **Markdown-based Content**: Easy to write and manage content using Markdown.
*   **Themed Design**: Styled with a custom "epic dark mode" theme inspired by epic fantasy.
*   **Blog Functionality**: Includes sections for book reviews, fitness articles, and potentially other topics.

## Project Origin

The foundational static site generator script was developed as part of the "Build a Static Site Generator in Python" course on [Boot.dev](https://www.boot.dev). This project extends and customizes that base to create a personalized website.

Thanks to Boot.dev for the excellent course and a great starting point!

## Running Locally

1.  Ensure you have Python 3 installed.
2.  To run the development server (which uses a `/` basepath):
    ```bash
    python3 src/main.py
    cd docs
    python3 -m http.server 8888
    ```
    Then open `http://localhost:8888` in your browser.

3.  To build for production (e.g., for GitHub Pages):
    ```bash
    ./build.sh
    ```
    This will build the site into the `docs/` directory with the basepath specified in `build.sh`. 