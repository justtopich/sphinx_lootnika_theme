<template>
  <div>
    
    <h1>Source code for test_py_module.test</h1><div class="highlight"><pre>
<span></span><span class="c1"># -*- coding: utf-8 -*-</span>
<span class="sd">"""Test Module for sphinx_rtd_theme."""</span>


<div class="viewcode-block" id="Foo"><router-link class="viewcode-back" href="/index/demo/api" to="/index/demo/api#test_py_module-test-Foo" v-scroll-to="'/index/demo/api#test_py_module-test-Foo'">[docs]</router-link><span class="k">class</span> <span class="nc">Foo</span><span class="p">:</span>

    <span class="sd">"""Docstring for class Foo.</span>

<span class="sd">    This text tests for the formatting of docstrings generated from output</span>
<span class="sd">    ``sphinx.ext.autodoc``. Which contain reST, but sphinx nests it in the</span>
<span class="sd">    ``&lt;dl&gt;``, and ``&lt;dt&gt;`` tags. Also, ``&lt;tt&gt;`` is used for class, method names</span>
<span class="sd">    and etc, but those will *always* have the ``.descname`` or</span>
<span class="sd">    ``.descclassname`` class.</span>

<span class="sd">    Normal ``&lt;tt&gt;`` (like the &lt;tt&gt; I just wrote here) needs to be shown with</span>
<span class="sd">    the same style as anything else with ````this type of markup````.</span>

<span class="sd">    It's common for programmers to give a code example inside of their</span>
<span class="sd">    docstring::</span>

<span class="sd">        from test_py_module import Foo</span>

<span class="sd">        myclass = Foo()</span>
<span class="sd">        myclass.dothismethod('with this argument')</span>
<span class="sd">        myclass.flush()</span>

<span class="sd">        print(myclass)</span>


<span class="sd">    Here is a link to :py:meth:`capitalize`.</span>
<span class="sd">    Here is a link to :py:meth:`__init__`.</span>

<span class="sd">    """</span>

    <span class="c1">#: Doc comment for class attribute Foo.bar.</span>
    <span class="c1">#: It can have multiple lines.</span>
    <span class="n">bar</span> <span class="o">=</span> <span class="mi">1</span>

    <span class="n">flox</span> <span class="o">=</span> <span class="mf">1.5</span>  <span class="c1">#: Doc comment for Foo.flox. One line only.</span>

    <span class="n">baz</span> <span class="o">=</span> <span class="mi">2</span>
    <span class="sd">"""Docstring for class attribute Foo.baz."""</span>

<div class="viewcode-block" id="Foo-__init__"><router-link class="viewcode-back" href="/index/demo/api" to="/index/demo/api#test_py_module-test-Foo-__init__" v-scroll-to="'/index/demo/api#test_py_module-test-Foo-__init__'">[docs]</router-link>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">qux</span><span class="p">,</span> <span class="n">spam</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
        <span class="sd">"""Start the Foo.</span>

<span class="sd">        :param qux: The first argument to initialize class.</span>
<span class="sd">        :type qux: string</span>
<span class="sd">        :param spam: Spam me yes or no...</span>
<span class="sd">        :type spam: bool</span>

<span class="sd">        """</span>
        <span class="c1">#: Doc comment for instance attribute qux.</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">qux</span> <span class="o">=</span> <span class="mi">3</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">spam</span> <span class="o">=</span> <span class="mi">4</span>
        <span class="sd">"""Docstring for instance attribute spam."""</span></div>

<div class="viewcode-block" id="Foo-add"><router-link class="viewcode-back" href="/index/demo/api" to="/index/demo/api#test_py_module-test-Foo-add" v-scroll-to="'/index/demo/api#test_py_module-test-Foo-add'">[docs]</router-link>    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">val1</span><span class="p">,</span> <span class="n">val2</span><span class="p">):</span>
        <span class="sd">"""Return the added values.</span>

<span class="sd">        :param val1: First number to add.</span>
<span class="sd">        :type val1: int</span>
<span class="sd">        :param val2: Second number to add.</span>
<span class="sd">        :type val2: int</span>
<span class="sd">        :rtype: int</span>

<span class="sd">        """</span>

        <span class="k">return</span> <span class="n">val1</span> <span class="o">+</span> <span class="n">val2</span></div>

<div class="viewcode-block" id="Foo-capitalize"><router-link class="viewcode-back" href="/index/demo/api" to="/index/demo/api#test_py_module-test-Foo-capitalize" v-scroll-to="'/index/demo/api#test_py_module-test-Foo-capitalize'">[docs]</router-link>    <span class="k">def</span> <span class="nf">capitalize</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">myvalue</span><span class="p">):</span>
        <span class="sd">"""Return a string as uppercase.</span>

<span class="sd">        :param myvalue: String to change</span>
<span class="sd">        :type myvalue: string</span>
<span class="sd">        :rtype: string</span>

<span class="sd">        """</span>

        <span class="k">return</span> <span class="n">myvalue</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span></div>

<div class="viewcode-block" id="Foo-another_function"><router-link class="viewcode-back" href="/index/demo/api" to="/index/demo/api#test_py_module-test-Foo-another_function" v-scroll-to="'/index/demo/api#test_py_module-test-Foo-another_function'">[docs]</router-link>    <span class="k">def</span> <span class="nf">another_function</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
        <span class="sd">"""</span>
<span class="sd">        Here is another function.</span>

<span class="sd">        :param a: The number of green hats you own.</span>
<span class="sd">        :type a: int</span>

<span class="sd">        :param b: The number of non-green hats you own.</span>
<span class="sd">        :type b: int</span>

<span class="sd">        :param kwargs: Additional keyword arguments. Each keyword parameter</span>
<span class="sd">                       should specify the name of your favorite cuisine.</span>
<span class="sd">                       The values should be floats, specifying the mean price</span>
<span class="sd">                       of your favorite dish in that cooking style.</span>
<span class="sd">        :type kwargs: float</span>

<span class="sd">        :returns: A 2-tuple.  The first element is the mean price of all dishes</span>
<span class="sd">                  across cuisines.  The second element is the total number of</span>
<span class="sd">                  hats you own: :math:`a + b`.</span>
<span class="sd">        :rtype: tuple</span>

<span class="sd">        :raises ValueError: When ``a`` is not an integer.</span>

<span class="sd">        .. versionadded:: 1.0</span>
<span class="sd">            This was added in 1.0</span>
<span class="sd">        .. versionchanged:: 2.0</span>
<span class="sd">            This was changed in 2.0</span>
<span class="sd">        .. deprecated:: 3.0</span>
<span class="sd">            This is deprecated since 3.0</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="nb">sum</span><span class="p">(</span><span class="n">kwargs</span><span class="o">.</span><span class="n">values</span><span class="p">())</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">kwargs</span><span class="p">),</span> <span class="n">a</span> <span class="o">+</span> <span class="n">b</span></div></div>
</pre></div
    <div></div>
    <div id='vueBottomPage'></div>
    </div>
  </div>
</template>