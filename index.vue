<template>
  <div>
    
    <section id="sample-sphinx-documentation">
<h1>Sample Sphinx Documentation<a class="headerlink" href="#sample-sphinx-documentation" title="Permalink to this headline">¶</a></h1>
<p>This is a <em>very</em> rudimentary sample page for Sphinx based documentation.</p>
<p>In case you’re looking for a lot of fairly extensive pages, that stretch the
theme in as many reasonable ways as possible, consider scrolling right to the
end of this page and looking at the Demo Documentation below.</p>
<section id="quick-inline-markup-demo">
<h2>Quick Inline Markup Demo<a class="headerlink" href="#quick-inline-markup-demo" title="Permalink to this headline">¶</a></h2>
<p>Inline markup in reStructuredText is pretty powerful. You can have <em>emphasis</em>,
<strong>strong emphasis</strong>, <code class="docutils literal notranslate"><span class="pre">inline</span> <span class="pre">literals</span></code>, external hyperlinks with embedded
URIs (<a class="reference external" href="http://www.python.org">Python web site</a>) standalone hyperlinks
(<a class="reference external" href="http://www.python.org">http://www.python.org</a>), footnote references <a href="#id4"><span class="problematic" id="id1">[1]_</span></a> and so much more. Sometimes,
you even have some <a href="#id2"><span class="problematic" id="id3">|problematic|</span></a> text that doesn’t do the right things but
Sphinx still builds your page.</p>
<p>Often, you’ll have multiple paragraphs of text in your documentation, possibly
an explanation how stuff works. Here are some explicit interpreted text roles:
a PEP reference (<span class="target" id="index-0"></span><a class="pep reference external" href="https://www.python.org/dev/peps/pep-0287"><strong>PEP 287</strong></a>); a <sub>subscript</sub>; a <sup>superscript</sup>; and
explicit roles for <em>standard</em> <strong>inline</strong> <code class="docutils literal notranslate"><span class="pre">markup</span></code>.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>You may want to know what admonitions look like.</p>
</div>
<div class="admonition important">
<p class="admonition-title">Important</p>
<p>I just wanted to interrupt your very relevant insight, to assert my
importance.</p>
</div>
<p>Or, maybe, you want to present a code block to the user.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="linenos">1</span><span class="sd">"""Just a small code example"""</span>
<span class="linenos">2</span>
<span class="linenos">3</span><span class="k">class</span> <span class="nc">Demo</span><span class="p">:</span>
<span class="linenos">4</span>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="linenos">5</span>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
<span class="hll"><span class="linenos">6</span>        <span class="bp">self</span><span class="o">.</span><span class="n">ready</span> <span class="o">=</span> <span class="kc">True</span>
</span><span class="linenos">7</span>
<span class="linenos">8</span>    <span class="k">def</span> <span class="nf">how_ready_are_we</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="hll"><span class="linenos">9</span>        <span class="k">return</span> <span class="s2">"very"</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">ready</span> <span class="k">else</span> <span class="s2">"not at all"</span>
</span></pre></div>
</div>
<div class="toctree-wrapper compound">
<p class="caption"><span class="caption-text">Demo Documentation</span></p>
<ul>
<li class="toctree-l1"><router-link class="reference internal" href="/index/demo/structure" to="/index/demo/structure">Structural Elements</router-link><ul>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/structure" to="/index/demo/structure#document-section" v-scroll-to="'/index/demo/structure#document-section'">Document Section</router-link></li>
</ul>
</li>
<li class="toctree-l1"><router-link class="reference internal" href="/index/demo/structure" to="/index/demo/structure#structural-elements-2" v-scroll-to="'/index/demo/structure#structural-elements-2'">Structural Elements 2</router-link><ul>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/structure" to="/index/demo/structure#id1" v-scroll-to="'/index/demo/structure#id1'">Document Section</router-link></li>
</ul>
</li>
<li class="toctree-l1"><router-link class="reference internal" href="/index/demo/demo" to="/index/demo/demo">Paragraph Level Markup</router-link><ul>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/demo" to="/index/demo/demo#inline-markup" v-scroll-to="'/index/demo/demo#inline-markup'">Inline Markup</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/demo" to="/index/demo/demo#math" v-scroll-to="'/index/demo/demo#math'">Math</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/demo" to="/index/demo/demo#meta" v-scroll-to="'/index/demo/demo#meta'">Meta</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/demo" to="/index/demo/demo#blocks" v-scroll-to="'/index/demo/demo#blocks'">Blocks</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/demo" to="/index/demo/demo#sidebar" v-scroll-to="'/index/demo/demo#sidebar'">Sidebar</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/demo" to="/index/demo/demo#references" v-scroll-to="'/index/demo/demo#references'">References</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/demo" to="/index/demo/demo#directives" v-scroll-to="'/index/demo/demo#directives'">Directives</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/demo" to="/index/demo/demo#download-links" v-scroll-to="'/index/demo/demo#download-links'">Download Links</router-link></li>
</ul>
</li>
<li class="toctree-l1"><router-link class="reference internal" href="/index/demo/lists_tables" to="/index/demo/lists_tables">Lists &amp; Tables</router-link><ul>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/lists_tables" to="/index/demo/lists_tables#lists" v-scroll-to="'/index/demo/lists_tables#lists'">Lists</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/lists_tables" to="/index/demo/lists_tables#tables" v-scroll-to="'/index/demo/lists_tables#tables'">Tables</router-link></li>
</ul>
</li>
<li class="toctree-l1"><router-link class="reference internal" href="/index/demo/api" to="/index/demo/api">API documentation and generated content</router-link><ul>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/api" to="/index/demo/api#module-test_py_module-test" v-scroll-to="'/index/demo/api#module-test_py_module-test'"><code class="xref py py-mod docutils literal notranslate"><span class="pre">test_py_module</span></code></router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/api" to="/index/demo/api#c-api" v-scroll-to="'/index/demo/api#c-api'">C++ API</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/api" to="/index/demo/api#javascript-api" v-scroll-to="'/index/demo/api#javascript-api'">JavaScript API</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/api" to="/index/demo/api#generated-index" v-scroll-to="'/index/demo/api#generated-index'">Generated Index</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/api" to="/index/demo/api#optional-parameter-args" v-scroll-to="'/index/demo/api#optional-parameter-args'">Optional parameter args</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/api" to="/index/demo/api#data" v-scroll-to="'/index/demo/api#data'">Data</router-link></li>
</ul>
</li>
</ul>
</div>
<div class="toctree-wrapper compound">
<p class="caption"><span class="caption-text">This is an incredibly long caption for a long menu</span></p>
<ul>
<li class="toctree-l1"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long">Long Sticky Nav</router-link><ul>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-1" v-scroll-to="'/index/demo/long#example-menu-1'">Example Menu 1</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-2" v-scroll-to="'/index/demo/long#example-menu-2'">Example Menu 2</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-3" v-scroll-to="'/index/demo/long#example-menu-3'">Example Menu 3</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-4" v-scroll-to="'/index/demo/long#example-menu-4'">Example Menu 4</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-5" v-scroll-to="'/index/demo/long#example-menu-5'">Example Menu 5</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-6" v-scroll-to="'/index/demo/long#example-menu-6'">Example Menu 6</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-7" v-scroll-to="'/index/demo/long#example-menu-7'">Example Menu 7</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-8" v-scroll-to="'/index/demo/long#example-menu-8'">Example Menu 8</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-9" v-scroll-to="'/index/demo/long#example-menu-9'">Example Menu 9</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-10" v-scroll-to="'/index/demo/long#example-menu-10'">Example Menu 10</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-11" v-scroll-to="'/index/demo/long#example-menu-11'">Example Menu 11</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-12" v-scroll-to="'/index/demo/long#example-menu-12'">Example Menu 12</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-13" v-scroll-to="'/index/demo/long#example-menu-13'">Example Menu 13</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-14" v-scroll-to="'/index/demo/long#example-menu-14'">Example Menu 14</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-15" v-scroll-to="'/index/demo/long#example-menu-15'">Example Menu 15</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-16" v-scroll-to="'/index/demo/long#example-menu-16'">Example Menu 16</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-17" v-scroll-to="'/index/demo/long#example-menu-17'">Example Menu 17</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-18" v-scroll-to="'/index/demo/long#example-menu-18'">Example Menu 18</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-19" v-scroll-to="'/index/demo/long#example-menu-19'">Example Menu 19</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-menu-20" v-scroll-to="'/index/demo/long#example-menu-20'">Example Menu 20</router-link></li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-submenu-1" v-scroll-to="'/index/demo/long#example-submenu-1'">Example Submenu 1</router-link><ul>
<li class="toctree-l3"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#submenu-1" v-scroll-to="'/index/demo/long#submenu-1'">Submenu 1</router-link></li>
<li class="toctree-l3"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#submenu-2" v-scroll-to="'/index/demo/long#submenu-2'">Submenu 2</router-link></li>
<li class="toctree-l3"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#submenu-3" v-scroll-to="'/index/demo/long#submenu-3'">Submenu 3</router-link></li>
<li class="toctree-l3"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#submenu-4" v-scroll-to="'/index/demo/long#submenu-4'">Submenu 4</router-link></li>
<li class="toctree-l3"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#submenu-5" v-scroll-to="'/index/demo/long#submenu-5'">Submenu 5</router-link></li>
</ul>
</li>
<li class="toctree-l2"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#example-submenu-2" v-scroll-to="'/index/demo/long#example-submenu-2'">Example Submenu 2</router-link><ul>
<li class="toctree-l3"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#id2" v-scroll-to="'/index/demo/long#id2'">Submenu 1</router-link></li>
<li class="toctree-l3"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#id4" v-scroll-to="'/index/demo/long#id4'">Submenu 2</router-link></li>
<li class="toctree-l3"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#id6" v-scroll-to="'/index/demo/long#id6'">Submenu 3</router-link></li>
<li class="toctree-l3"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#id7" v-scroll-to="'/index/demo/long#id7'">Submenu 4</router-link></li>
<li class="toctree-l3"><router-link class="reference internal" href="/index/demo/long" to="/index/demo/long#id8" v-scroll-to="'/index/demo/long#id8'">Submenu 5</router-link></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</section>
</section>
    <div></div>
    <div id='vueBottomPage'></div>
    </div>
  </div>
</template>