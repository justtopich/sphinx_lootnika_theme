from os import path
import re

from docutils import nodes
from sphinx.environment.collectors import EnvironmentCollector
from sphinx import addnodes, __version__ as spinxVersion
from sphinx.util.osutil import relative_uri
from bs4 import BeautifulSoup

# from sphinx.ext import viewcode
# viewcode.collect_pages = collect_pages


__version__ = (0, 2, 2)


class SimpleTocTreeCollector(EnvironmentCollector):
    """A TocTree collector that saves toctrees in a simple dict.

    sphinx.environment.collectors.toctree.TocTreeCollector saves
    TocTree as docutils.nodes which are hard to work with...

    Executed once per document/page, at sphinx's "read" phase.

    Saved data example:
    >>> {
    >>>  'sections': [{'title': 'Demo', 'href': '#demo'}],
    >>>  'toctrees': [<toctree: >]
    >>> }
    """
    def enable(self, app):
        super().enable(app)
        # env is populated from cache, if not cache create/initalize attibute
        if not hasattr(app.env, 'toc_dict'):
            app.env.toc_dict = {}

    def clear_doc(self, app, env, docname):
        env.toc_dict.pop(docname, None)

    def merge_other(self, app, env, docnames, other):
        for docname in docnames:
            env.toc_dict[docname] = other.toc_dict[docname]


    def process_doc(self, app, doctree):
        docname = app.env.docname # sphinx mutates this, ouch!!!

        # print(f"================ Collector\n{docname}\n============\n")
        # get 1 level document toc (sections)
        section_nodes = [s for s in doctree if isinstance(s, nodes.section)]
        # if first level is a single section,
        # ignore it and use second level of sections
        if len(section_nodes) == 1:
            section2_nodes = [s for s in section_nodes[0]
                              if isinstance(s, nodes.section)]
            if section2_nodes: # do not replace with level-2 sections if None
                section_nodes = section2_nodes

        sections = []
        for node in section_nodes:
            sections.append({
                'title': node[0].astext(),
                'href': '#{}'.format(node['ids'][0]),
            })

        app.env.toc_dict[docname] = {
            'sections': sections,
            'toctrees': doctree.traverse(addnodes.toctree)
        }


def parse_index(app, templatename, context, doctree):
    """
    split index.rst into two different documents:
        * index.html - layout with all elements that will be at all pages (sidebar, navbar, js e.t.c) and routes
        * index.vue - page content.

    app.env.toctree_includes - cсылки на другие rst
    По дефолту всегда содержит index с ссылками на заголовки  .. toctree::
    """

    def order_nav_tree(nav_tree, name):
        # for saving navigation header order as source
        for toctree in headers[name]:
            if toctree in headers:
                nav_tree[toctree] = headers[toctree]
                order_nav_tree(nav_tree, toctree)
        return nav_tree

    if templatename == 'page.html':
        app.builder.config.nav_tree = nav_tree = {'index': app.env.toctree_includes['index']}
        app.builder.config.nav_titles = nav_titles = {'index': app.env.toctree_includes['index']}

        headers = app.env.toctree_includes.copy()

        # index is entry point
        app.builder.config.nav_tree = order_nav_tree(nav_tree, 'index')

        toc_dict = app.env.toc_dict
        for page, v in app.env.titles.items():
            name = "".join([str(i) for i in v.children])
            name = name.replace('<title_reference>', '<cite>', -1).replace('</title_reference>', '</cite>', -1)

            nav_titles[page] = {'name': name}
            if page in toc_dict and toc_dict[page]['sections'][0]['href'] != "#id1":
                nav_titles[page]['sections'] = app.env.toc_dict[page]['sections']

        app.builder.out_suffix = '.vue'
    else:
        app.builder.out_suffix = '.html'

    context['nav_tree'] = app.builder.config.nav_tree
    context['nav_titles'] = app.builder.config.nav_titles
    context['spinx_version'] = spinxVersion

    if hasattr(app.builder.env, '_viewcode_modules'):
        # add source pages to vue router
        for modname in app.builder.env._viewcode_modules:
            pagename = '_modules/' + modname.replace('.', '/')
            context['nav_tree'][f"{pagename}"] = []
            context['nav_titles'][f"{pagename}"] = modname
    return


def body_update(body: str, includes: dict, includes_val: set, modules_url: set):
    def link_vuezer(link):
        """
        If linked to another page - used router-link
        Else - enough v-scroll-to

        :param link: html link
        :return: vue link
        """

        def find_parent(page: str):
            for parent, ls in includes.items():
                if page in ls:
                    return f"{find_parent(parent)}/{page}"
            return page

        href = link.get('href')
        anchor = None
        sourced = False

        if href.startswith('#'):
            link1 = body.new_tag('a')
            href = href.replace('.', "-", -1)
        else:
            if '.html#' in href:
                # get page and position on page of element
                href = href.split('#')
                anchor = href[1].replace('.', "-", -1)
                href = href[0]

            if 'viewcode-back' in link['class']:
                # links fot internal assets that will be in root directory
                idx = href.rfind('../') + 3
                href = f"/index/{href[idx:]}"

            if href.endswith('.html'):
                # routed to another pages
                cur = href[:-5]
                link1 = body.new_tag('router-link')

                # find full url to the page
                if any(cur in ls for ls in [includes_val, includes]):
                    href = f"/{find_parent(cur)}"
                elif cur.startswith('../_'):
                    # links fot internal assets that will be in root directory
                    href = cur[2:]
                elif cur in modules_url:
                    href = cur
                    if not href.startswith('/'):
                        href = f"/{href}"
                else:
                    href = cur

                link1['to'] = href
                if anchor is not None:
                    link1['v-scroll-to'] = f"'{href}#{anchor}'"
                    link1['to'] += f"#{anchor}"
            else:
                if href.startswith('../_'):
                    # links fot internal assets that will be in root directory
                    href = href[3:]
                link1 = body.new_tag('a')

        link1.contents = link.contents
        link1['class'] = link['class']
        link1['href'] = href
        # if 'config/config_syntax' in str(link1):
        #     print(99)
        return link1

    body = BeautifulSoup(body, features="lxml")

    for img in body.findAll('img'):
        # links fot internal assets that will be in root directory
        if img.has_attr('src'):
            img['src'] = img['src'][3:]

    for i in body.select('a.internal'):
        if i.has_attr('href'):
            link1 = link_vuezer(i)
            i.insert_after(link1)
            i.extract()

    for i in body.select('a.viewcode-back'):
        # becouse vue-router know root as index
        if i.has_attr('href'):
            link1 = link_vuezer(i)
            i.insert_after(link1)
            i.extract()

    for i in body.select('a.toc-backref'):
        text = i.text
        i.insert_after(text)
        i.extract()

    for i in body.findAll(True,{'id': True}):
        # fix id because vue-scrollto don't work if id have dots
        i['id'] = i['id'].replace('.', "-", -1)

    return str(body)[12:-15]


def add_toctree_data(app, pagename, templatename, context, doctree):
    """Create toctree_data, used to build sidebar navigation

    :param pagename: The name of the page
    :type pagename: str
    :param templatename: The name of the templatename
    :type templatename: str
    :param context: The context
    :type context: dict
    :param doctree: A doctree
    :type doctree: docutils.nodes.document

    Add to `toctree_data` to `context` that will be available on templates.
    Although data is "global", it is called once per page because current
    page is "highlighted", and some part of TOC might be collapsed.

    :return: None
    """
    # print(f"---------- Context\n{pagename}\n-------------\n")

    # start from master_doc
    master = app.env.get_doctree(app.env.config.master_doc)

    # each toctree will create navigation section
    res = [] # list of top level toctrees in master_doc
    for tree in master.traverse(addnodes.toctree):

        # special case for toctree that includes a single item
        # that contains a nested toctree.
        # In this case, just use the referenced toctree directly
        if len(tree['entries']) == 1:
            entry_docname = tree['entries'][0][1]
            toctrees = app.env.toc_dict[entry_docname]['toctrees']

            if toctrees:
                # FIXME
                assert len(toctrees) == 1, "Press: Not supported more then one toctree on nested toctree"
                tree = toctrees[0]
        current0 = False # same page might have multiple tocs

        # add toc tree items, expand one more level if toctree is current page
        entries = []
        for title, name in tree['entries']:
            if not title:
                title = app.env.titles[name].astext()

            current1 = (pagename == name)
            children = []
            if current1:
                current0 = True
                # if current, add another level
                children = app.env.toc_dict[name]['sections']
            # add page_toc for current page

            entries.append({
                'name': name,
                'title': title,
                'current': current1,
                'children': children,
            })

        toc_docname = tree['parent'] # docname where this toc appears
        title = tree['caption']

        # Anchor element is the section containing the toc,
        # as the toc itself does not contain ID.
        anchor_id = ''

        # tree.parent is the parent docutils node.
        # First parent is "compound" node toctree-wrapper,
        # second parent is the section containing the toctree
        toc_section = tree.parent.parent
        if toc_section['ids']: # no id means toc actually not in a section
            # TODO: should we be strict about toc being inside a section
            anchor_id = toc_section['ids'][0]
            if not title:
                title = toc_section['names'][0]

        # sphinx `pathto` does not play nice with anchors when
        # `allow_sharp_as_current_path` is True
        baseuri = app.builder.get_target_uri(pagename).rsplit('#', 1)[0]
        toc_uri = app.builder.get_target_uri(toc_docname).rsplit('#', 1)[0]
        toc_href = f'{relative_uri(baseuri, toc_uri)}#{anchor_id}'
        res.append({
            'docname': toc_docname,
            'href': toc_href,
            'title': title,
            'current': current0,
            'entries': entries,
        })

    context['toctree_data'] = res
    context["theme_route_base"] = context["theme_route_base"][1:-1]

    if not hasattr(app.env, 'toctree_includes_val'):
        # need for creating vue href
        includes_val = []
        for v in app.env.toctree_includes.values():
            includes_val.extend(v)
        app.env.toctree_includes_val = set(includes_val)

    if hasattr(app.builder.env, '_viewcode_modules') and not hasattr(app.builder.env, 'modules_url'):
        # add source pages to vue router
        app.env.modules_url = []
        for modname in app.builder.env._viewcode_modules:
            pagename = '_modules/' + modname.replace('.', '/')
            app.env.modules_url.append(pagename)
        app.env.modules_url = set(app.env.modules_url)

    if pagename == 'index':
        parse_index(app, templatename, context, doctree)
    else:
        app.builder.out_suffix = '.vue'

    if 'body' in context:
        if hasattr(app.builder.env, "modules_url"):
            modules_url = app.env.modules_url
        else:
            modules_url = {}

        context['body'] = body_update(
            context['body'],
            app.env.toctree_includes,
            app.env.toctree_includes_val,
            modules_url)
    return


def setup(app):
    app.add_env_collector(SimpleTocTreeCollector)
    app.connect('html-page-context', add_toctree_data)
    app.add_html_theme('sphinx_lootnika_theme', path.abspath(path.dirname(__file__)))
    app.builder.config.html_additional_pages = {**{"index": "index.html"}, **app.builder.config.html_additional_pages}
