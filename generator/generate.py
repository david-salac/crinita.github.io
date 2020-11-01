import shutil
from pathlib import Path

import crinita as cr

homepage = cr.Page(
    title="Project",
    url_alias=None,  # Homepage
    content="""Python application for generating static websites like a blog or simple static pages. Creates HTML files based on inputs (without requiring to run any script languages on the server-side).""",
    menu_position=0,
    description="""Python application for generating static websites like a blog or simple static pages. Creates HTML files based on inputs (without requiring to run any script languages).""",
    keywords="Crinita, static websites, generator, free, open-source",
    large_image_path=None
)
license_page = cr.Page(
    title="License",
    url_alias='license',
    content="""MIT License
<p>
Copyright (c) 2020 David Salac
</p><p>
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
</p><p>
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
</p><p>
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.</p>""",
    menu_position=5,
    large_image_path=None
)

# Template path
cr.Config.templates_path = Path('templates')
# Append menu
cr.Config.append_to_menu = (
    {
        'title': "GitHub Project",
        'url': "https://github.com/david-salac/crinita",
        'menu_position': 10
    },
)
# Change config
cr.Config.site_logo_text = "Crinita"
cr.Config.site_title = "Crinita"
cr.Config.default_meta_description = """Python application for generating static websites like a blog or simple static pages. Creates HTML files based on inputs (without requiring to run any script languages)."""
cr.Config.default_meta_keywords = "Crinita, static websites, generator, free, open-source"
cr.Config.text_sections_in_right_menu = (
    {
        "header": "About",
        "content": f'The description and documentation of Crinita application.<p>Generated using <a href="http://www.crinita.com/">Crinita</a> version {cr.__version__}</p>'
    },)
cr.Config.default_meta_meta_author = "Crinita team"
cr.Config.site_home_url = "/"

generator = cr.Sites(
    list_of_articles=[], list_of_pages=[homepage, license_page]
)
output_directory_path: Path = Path('../')
generator.generate_pages(output_directory_path)


# TODO: REWRITE IN SMARTER WAY
# Postprocessing scripts
shutil.copy(Path('resources/root/style.css'), Path(output_directory_path, 'style.css'))
Path(output_directory_path, 'images').mkdir(exist_ok=True)
shutil.copy(Path('resources/images/logo.png'), Path(output_directory_path, 'images', 'logo.png'))