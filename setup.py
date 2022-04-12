from setuptools import setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.readlines()

setup(
    name='sphinx_lootnika_theme',
    version='0.2.3-beta.0',
    description='A Sphinx-doc theme created as Vue.js SPA',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Alex Whiteeyes',
    author_email='alex1.beloglazov@yandex.ru',
    url='https://github.com/justtopich/sphinx_lootnika_theme/',
    packages=['sphinx_lootnika_theme'],
    package_data={
        "sphinx_lootnika_theme": [
            "theme.conf",
            "../requirements.txt",
            "*.html",
            "util/*.html",
            "static/**/*",
        ]
    },
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'sphinx_lootnika_theme = sphinx_lootnika_theme',
        ]
    },
    install_requires=requirements,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Theme",
    ],
    python_requires=">=3.6",
    keywords="sphinx doc theme vue.js",
)
