from pathlib import Path
import shutil
from typing import List, Union
import pkgutil
from os import listdir

import crinita as cr

# Iterate through all entities
ENTITIES: List[Union[cr.Page, cr.Article]] = []
for single_file in pkgutil.walk_packages(['.']):
    try:
        if single_file.name == 'generate':
            continue
        pack = __import__(single_file.name)
        ENTITIES.append(pack.ENTITY)
    except:  # noqa
        continue

sites = cr.Sites(ENTITIES)
# ========= CONFIGURATION =========
# Path to outputs
output_directory: Path = Path('../')
# Resource directory
resource_directory: Path = Path('RESOURCES')

# Add template path:
cr.Config.templates_path = Path('templates')
# Configure blog name
cr.Config.site_logo_text = "Crinita"
cr.Config.site_title = "Crinita"
cr.Config.append_to_menu = (
    {
        'title': "GitHub Project",
        'url': "https://github.com/david-salac/crinita",
        'menu_position': 30
    },
)
cr.Config.text_sections_in_right_menu = (
    {
        "header": "Recommended links",
        "content": """
        <ul>
        <li><a href="https://itblog.uk/">IT Blog</a></li>
        <li><a href="https://portable-spreadsheet.com/">Portable Spreadsheet</a></li>
        </ul>"""
    },
    {
        "header": "What is Crinita",
        "content": f'Python application for generating static websites like a blog or simple static pages. Creates HTML files based on inputs (without requiring to run any script languages).<p>Generated using <a href="http://www.crinita.com/">Crinita</a> version {cr.__version__}</p>'
    },
)
cr.Config.default_meta_description = "Python application for generating static websites like a blog or simple static pages. Creates HTML files based on inputs (without any script languages)."
cr.Config.default_meta_meta_author = "Crinita team"
cr.Config.default_meta_keywords = "Crinita, Static Website Generator, Blog, Pages, Websites"
cr.Config.site_home_url = "/"
cr.Config.site_map_url_prefix = "https://crinita.com/"
cr.Config.robots_txt = """User-agent: *
Allow: /
Sitemap: https://crinita.com/sitemap.xml"""
# =================================

# Remove existing content
if output_directory.exists():
    if output_directory.joinpath('images').exists():
        shutil.rmtree(output_directory.joinpath('images'))
    if output_directory.joinpath('styles.css').exists():
        shutil.rmtree(output_directory.joinpath('styles.css'))
    onlyfiles = [f for f in listdir(output_directory) if output_directory.joinpath(f).is_file() and cr.Config.site_file_suffix in f]
    for file in onlyfiles:
        output_directory.joinpath(file).unlink()
    if output_directory.joinpath("robots.txt").exists():
        output_directory.joinpath("robots.txt").unlink()
    if output_directory.joinpath("sitemap.xml").exists():
        output_directory.joinpath("sitemap.xml").unlink()
    if output_directory.joinpath("style.css").exists():
        output_directory.joinpath("style.css").unlink()

# Generate sites
sites.generate_pages(output_directory)

# Add resources
shutil.copytree(resource_directory, output_directory, dirs_exist_ok=True)
