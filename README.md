# Lootnika Sphinx Theme

Sphinx theme created as Vue.js SPA with responsive design support.

Based on [sphinx_press_theme](https://github.com/schettino72/sphinx_press_theme) by schettino72.

**This is beta version!**



## Usage

First install the theme:

```shell
py -m pip install --upgrade build
py -m build
pip install dist\sphinx_lootnika_theme-0.2.3b0-py2.py3-none-any.whl
```

To use the theme, set the theme name to `sphinx_lootnika_theme` in your sphinx project's `conf.py`:

```python
html_theme = "sphinx_lootnika_theme"
```



To use without installing copy `sphinx_lootnika_theme` path local.

Add path that contain `sphinx_lootnika_theme` path in your sphinx project's `conf.py`:

```python
html_theme = "sphinx_lootnika_theme"
html_path = ["."]
```

For more information, see the [Sphinx theming docs](http://www.sphinx-doc.org/en/master/theming.html#using-a-theme).



## Using

* [Vue.js 2.5](http://vuejs.org)
* [Vue Router 1.4](https://router.vuejs.org/)
* [vue-scrollto 2.19](https://github.com/rigor789/vue-scrollto)
* [http-vue-loader 1.4](https://github.com/FranckFreiburger/http-vue-loader)
* [Font Awesome 5.15](http://fortawesome.github.com/Font-Awesome/)



## Requirement

- Python 3.6 or later.
- Sphinx 3.x or later.

Tested on Python 3.8.7 and Sphinx  3.3.1
