# GitHub hosting for Crinita project websites
Author: David Salac <https://github.com/david-salac>

This is the hosting repo for websites <https://crinita.salispace.com/>

Sites are generated using Crinita system.

## How to change content
In the `generator` folder, there are two types of files: `page_` and
`article_` (representing single static page or article in the blog).
To add a new page or article just follow the logic of remaining files.

Resources (pictures and style files) are in the `generator/RESOURCES`
folder. All resources are copied to the target directory.

## How to generate sites
Sites are generated using Crinita system. All the content is in the
`generator` folder.

To generate sites use the logic:
```
python generate.py
```

To install requirements:
```
pip install -r requirements.txt
```

HTML files are located in the folder
```
/
```
they have to be in the root folder (because of GitHub configuration).
