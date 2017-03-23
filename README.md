[![Unix Build Status][travis-image]][travis-link]
![License: GPL v3][license-image]

# Wp-Bench
WP-Bench is a package for Sublime Text 3 which provides function completion, snippets and Codex tooltips. All this information is readly available offline.

The popups are archieved using [sublime-markdown-popups](https://raw.githubusercontent.com/facelessuser/sublime-markdown-popups) by [facelessuser](https://raw.githubusercontent.com/facelessuser)

Screenshot not available for the moment.

**Still in development.**

## Features

- Can take Markdown or HTML and create nice looking popup tooltips and phantoms.
- Dynamically creates popup and phantom themes from your current Sublime color scheme.
- Can create syntax highlighed code blocks easily using either Pygments or the built-in Sublime Text syntax highlighter automatically in the Markdown environment or outside via API calls.
- Can create color preview boxes via API calls.
- A CSS template environment that allows users to override and tweak the overall look of the tooltip and phantom themes to better fit their preferred look.  Using the template filters, users can generically access color scheme colors and manipulate them.
- Plugins can extend the current CSS to inject plugin specific class styling.  Extended CSS will be run through the template environment.

# Documentation

None at the moment.

# License
Released under GPL-v3.

© Ivo Santos — 2017

[travis-image]: https://img.shields.io/travis/psiico/WP-Bench/master.svg
[travis-link]: https://travis-ci.org/psiico/WP-Bench
[license-image]:https://img.shields.io/badge/License-GPL%20v2-blue.svg