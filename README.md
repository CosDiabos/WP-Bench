[![Unix Build Status][travis-image]][travis-link]
![License: GPL v3][license-image]

# Wp-Bench
WP-Bench is a package for Sublime Text 3(ST3) which provides an integration with Wordpress core functions based on the Codex reference website. All this information is readly available offline.


https://github.com/psiico/WP-Bench/assets/14842802/636038b0-ed55-4faa-b13d-7573fd2cb03b



## Motivation

Lately most of my work consists on working with Wordpress CMS so I thought about trying to increase my productivity with this package for ST3.

## Process

The file [scrapper-funcs.py](scrapper-funcs.py) takes a first pass to get all the available functions into a local file (Scrapper/wp_all_funcs.txt) and then [scrapper.py](scrapper.py) takes care of the scrapping and writting of each function into snippets' files to Snippets/ folder, which is read and processed by ST3.

## Requirements

Scrappers require Python 3 + [lxml](https://pypi.org/project/lxml/) installed to properly work.


## Install

Clone the repository into your Package folder inside ST3 folder. To find your ST3 folder go to “Preferences -> Browse Packages”.


## Features

- Functions auto-complete;
- Functions snippets;
- Popup with function documentation based on WP Codex;
- Creates basic folder and file scaffold for themes and plugins;
- Customizable scaffold by JSON;
- Scrappes WP reference documentation to keep snippets up-to-date.


## Folder Structure

```
.
├── Snippets/
│   └── [...].sublime-snippet      # All generated snippets
├── Scrapper/
│   ├── scrapper_funcs.py      # Scrapper for all functions generates 'wp_all_funcs.txt'
│   ├── scrapper.py      # Info scrapper for each function, generates each 'function.sublime-snippet'
│   └── wp_all_funcs.txt      # Collection of all codex functions, CSV style.
└── WP--bench.py
```

## Settings

(0 = Off, 1 = On, \* = default)

ShowOnOver = 1\*\|0 :: On hover tooltip

PluginOverwriteFiles = 1|0\* :: Overwrite existing files when creating folder/file structure

ThemeOverwriteFiles = 1|0\* :: Overwrite existing files when creating folder/file structure


To change the default snippets folder, edit ```snippets_dirname``` var on [WP-Bench.py](WP-Bench.py)

## Customize the default theme or plugin structure

Edit ThemeBase.json or PluginBase.json to add or remove files from the default structure.

ThemeBase.json
```
.
├── assets (dir)/
│   ├── css (dir)/
│   │   └── index.php
│   ├── images (dir)/
│   │   └── index.php
│   └── js (dir)/
│       └── index.php
├── inc (dir)/
│   └── index.php
├── template-parts (dir)/
│   └── index.php
├── 404.php
├── archive.php
├── comments.php
├── footer.php
├── front-page.php
├── functions.php
├── header.php
├── index.php
├── page.php
├── README.txt
├── rtl.css
├── screenshot.png
├── search.php
├── searchform.php
├── sidebar.php
├── single.php
└── style.css
```

PluginBase.json
```
.
└── plugin-name/
    ├── /languages/
    │   └── index.php
    ├── /includes/
    │   └── index.php
    ├── /admin/
    │   ├── /js/
    │   │   └── index.php
    │   ├── /css/
    │   │   └── index.php
    │   └── /images/
    │       └── index.php
    ├── /public/
    │   ├── /js
    │   ├── /css
    │   └── /images
    ├── plugin-name.php
    └── uninstall.php
```

## Documentation

None at the moment.

## License
Released under GPL-v3.

© Jéssica Pereira — 2017

[travis-image]: https://img.shields.io/travis/psiico/WP-Bench/master.svg
[travis-link]: https://travis-ci.org/psiico/WP-Bench
[license-image]:https://img.shields.io/badge/License-GPL%20v2-blue.svg
