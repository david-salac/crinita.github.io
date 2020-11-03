import crinita as cr

html_code = """Author: David Salac <a href="https://www.github.com/david-salac">https://www.github.com/david-salac</a>
<p>Python application for generating static websites like a blog or
simple static pages. Creates HTML files based on inputs (without
requiring to run any script languages on the server-side).</p>
<h2 id="blog-and-static-website-generator">Blog and static website generator</h2>
<p>Generally speaking, Crinita is a static website generator. That is
an application that generates simple HTML files that cover all the
content of sites from all inputs - composed mainly of the
definition of pages, articles and other entities on websites).
So after running of static websites generator, you have a set of
<code>*.html</code> files (including index.html) that allows you to browse sites.</p>
<p>There are many advantages of using static websites generator rather
than the standard approach using some web framework (like PHP,
Django). Mainly, the result can be simply deployed to production
as you do not need to configure anything on the server-side. There
are many ways how to deploy the outcome; the most popular is
GitHub pages (technically a free place where to host your static
pages). Another significant advantage is the security perspective - it
is almost impossible to hack static websites (what a massive
difference if you consider how vulnerable are websites running on
WordPress or similar technologies). Last but not least advantage is
cost-effectiveness - you do not need to use any expensive technologies
for hosting (like AWS) or pay directly for these services (like Wix,
Medium). </p>
<p>Crinita allows you to generate blog (and/or) websites (blog
or just set of static pages). It includes advanced features like
tags, the possibility to edit meta tags for each entity (article
or page). Interface for using Crinita is simple so you can learn
it quickly. Installation of Crinita is a simple task as it does not
require any system dependencies.</p>
<h2 id="typical-use-cases">Typical use cases</h2>
<p>There are some typical use cases when it is beneficial to use Crinita,
among the most popular are:</p>
<ol>
<li>Need to leave technically weak services like Blogger: There are many
services that allow you to run your blog. One of the most popular is
Blogger. However, the technical quality of these services is notoriously
weak (particularly if it comes to Blogger). It is often hard to use them
for anything even bit more technical (like including articles with
code examples). The resulting page often is also technically weak - no
SEO-friendly output (usually it&#39;s impossible to index article in Google
at all).</li>
<li>Do not want to pay for services like Medium: Many helpful services
can run your blog (or static pages) in a technically suitable way. One
of the reasonably good services is Medium. Although it is quite good,
it is also quite expensive - which can demotivate many potentials bloggers.</li>
<li>Afraid of security vulnerabilities of WordPress: if people want to
run their blog on their infrastructure, the typical first choice is
WordPress. It is simple, quick to install and easy to use. Unfortunately,
it is notoriously problematic in the security point of view. Everyone can
find a lot of articles and analysis of these vulnerabilities. It is
mainly the security issue that makes WordPress almost useless for many
cases. Because Crinita works on different principles, it is practically
impossible to hack resulting pages.</li>
<li>Difficulties with back-up and restore procedures: it is often hard
(and sometimes impossible) to back-up your blog (pages) content. So if
your pages are hacked (or destroyed by any other way), you lose all your
work. This is a frequent problem with WordPress - where even if you create
a back-up of your database - restoring it is a fairly difficult task.
Some external services (Blogger, Medium) do not allow backing-up in any
reasonable format at all. Crinita, on the other hand, is backed-up in
principle (because generator files are just simple Python scripts that
can be easily pushed to GitHub).</li>
<li>Simple to use and quick to install: one of the essential quality of
Crinita is that it is simple to install and to use. On the other hand,
it is presumed here, that user is fluent in Python developing and HTML
coding. If this is your case, it just requires to install Crinita from
PyPi archive, download layouts and styles and then just write some content.</li>
<li>Cheap and primitive infrastructure: as you do not need to run any script
on the server-side (like PHP, Ruby, etc.), infrastructure for the Crinita
is fairly simple. Technically the simplest way how to run your websites
is to deploy them through GitHub pages (technically the free hosting
for static websites) - which is a highly recommended approach (as you
can have both generating scripts and content on one place and backed-up).</li>
</ol>
<h2 id="how-to-install-crinita">How to install Crinita</h2>
<p>In order to install Crnita, you need to have prepared your Python (in
version at least 3.8) environment ready first. There are many manuals
on how to install Python on your machine (so there is no reason why
to explain it here again).</p>
<p>To install Crinita, you can use your PIP
directly with a default package manager (PyPi.org). Just write
a command:</p>
<pre class="code"><code>pip <span class="hljs-keyword">install</span> crinita
</code></pre><p>To check if the installation is successful, write in some script:</p>
<pre class="code"><code><span class="hljs-keyword">import</span> crinita <span class="hljs-keyword">as</span> cr
</code></pre><p>If you do not see any error, it looks good.</p>
<h2 id="how-to-use-crinita">How to use Crinita</h2>
<p>The simplest way where to start to generate your own websites
is to use the logic of existing ones:</p>
<ol>
<li>Use <strong><a href="https://github.com/david-salac/itblog.github.io">https://github.com/david-salac/itblog.github.io</a></strong> for the
complex blog (with articles and pages).</li>
<li>Use <strong><a href="https://github.com/david-salac/crinita.github.io">https://github.com/david-salac/crinita.github.io</a></strong> for the
simple static websites.</li>
</ol>
<p>In all these cases, the generating script is in the folder generator.
There is also a definition of pages and articles there.</p>
"""

ENTITY = cr.Page(
    title="About Crinita",
    url_alias=None,  # Is homepage
    large_image_path=None,
    content=html_code,
    menu_position=0
)
