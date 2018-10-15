<<<<<<< HEAD
#  Crossbaker
Interface to communicate across multiple baking packages

> ## *Design*
```mermaid
graph LR
DCC(DCC App) --TCP/IP--- UI[Qt UI]
UI --Subprocess--> BK[Bakers]
subgraph BakerApp
BK --- M((Marmoset))
BK --- S((Substance))
BK --- X((XNormals))
BK --- E((...))
end
UI --Subprocess--> IC[Image Comps]
subgraph ImageApp
IC --- P((Photoshop))
IC --- Pi((Pillow))
end
BK --Result--> IC

```

#  Usage
```python
import crossbaker
crossbaker.initUI()
```
##  config.json
> Path to baking application.

##  export_setting.json
> Setting to feed baking application.

##  crossbaker.exportSettings
> Contain all setting to export with

##  crossbaker.bakers
> Iterable contain all available baker found in system.
>```python
> crossbaker.bakers.count(): #return available bakers count.
> crossbaker.bakers.current(): #return current BakerApp.
> crossbaker.bakers.run() : #run current baker specified in exportSetting.
> crossbaker.bakers.get(bakername): #return BakerApp for baker name.
> # Baker can also be access directly via attribute. Exp:
> crossbaker.bakers.marmoset
> crossbaker.bakers.substance
>```

## crossbaker.exportSettings
>Iterable contain settings to run baker with.
>```python
>crossbaker.exportSettings.get(settingname) #: get setting by name.
>crossbaker.exportSettings.baker #: current baker to use.
>crossbaker.exportSettings.meshpath #: path to exported mesh.
>crossbaker.exportSettings.outputPath #: path to exported bake maps.
>crossbaker.exportSettings.outputSize """ Size: Output images size.
>:: param w : int : # map width
>:: param h : int : # map height
>"""
>crossbaker.exportSettings.outputSamples #: Output images AA samples.
>crossbaker.exportSettings.outputBits #: Output images bits depth.
>crossbaker.exportSettings.outputPSD #: Composite all export images as one psd file.
>crossbaker.exportSettings.useTextureSet #: Use Texture set when baking
>```

## Classes
## crossbaker.BakerApp
>```python
>"""
>::param name : str : baking application name.
>::param path : str : path to baking application executable.
>::method run : run subprocess call baker app with setting from exportSettings.
>"""
>```
## crossbaker.ImageApp
=======
---


---

<blockquote>
<p>Written with <a href="https://stackedit.io/">StackEdit</a>.</p>
</blockquote>
<h1 id="crossbaker">Crossbaker</h1>
<p>Interface to communicate across multiple baking packages</p>
<blockquote>
<h2 id="design"><em>Design</em></h2>
</blockquote>
<div class="mermaid"><svg xmlns="http://www.w3.org/2000/svg" id="mermaid-svg-VxP3XAD2IeqHWfFB" width="100%" style="max-width: 924.1499938964844px;" viewBox="0 0 924.1499938964844 853.9499969482422"><g transform="translate(-12, -12)"><g class="output"><g class="clusters"><g class="cluster" id="subGraph1" style="opacity: 1;" transform="translate(760.1499938964844,159.2916717529297)"><rect width="336" height="278.5833435058594" x="-168" y="-139.2916717529297"></rect><g class="label"><g transform="translate(0,0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"></div></foreignObject></g></g><text x="0" y="-125.29167175292969" fill="black" stroke="none" id="mermaid-svg-VxP3XAD2IeqHWfFBText" style="text-anchor: middle;">ImageApp</text></g><g class="cluster" id="subGraph0" style="opacity: 1;" transform="translate(575.5666580200195,588.2666702270508)"><rect width="362.96665954589844" height="539.3666534423828" x="-181.48332977294922" y="-269.6833267211914"></rect><g class="label"><g transform="translate(0,0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"></div></foreignObject></g></g><text x="0" y="-255.68331909179688" fill="black" stroke="none" id="mermaid-svg-VxP3XAD2IeqHWfFBText" style="text-anchor: middle;">BakerApp</text></g></g><g class="edgePaths"><g class="edgePath" style="opacity: 1;"><path class="path" d="M105.64999389648438,322.13333892822266L155.5583267211914,322.13333892822266L205.46665954589844,322.13333892822266" marker-end="url(#arrowhead11788)" style="fill:none"></path><defs><marker id="arrowhead11788" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 0 0 L 0 0 z" style="fill: #333"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M244.9550040837525,345.4916687011719L329.2083282470703,541.2166748046875L394.0833282470703,541.2166748046875L425.4583282470703,541.2166748046875" marker-end="url(#arrowhead11789)" style="fill:none"></path><defs><marker id="arrowhead11789" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M473.2135676997285,517.8583450317383L545.4916610717773,399.42501068115234L592.1499938964844,399.42501068115234L628.7583236694336,399.42501068115234" marker-end="url(#arrowhead11790)" style="fill:none"></path><defs><marker id="arrowhead11790" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 0 0 L 0 0 z" style="fill: #333"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M492.4583282470703,541.2166748046875L545.4916610717773,541.2166748046875L592.1499938964844,541.2166748046875L628.6499938964844,541.2166748046875" marker-end="url(#arrowhead11791)" style="fill:none"></path><defs><marker id="arrowhead11791" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 0 0 L 0 0 z" style="fill: #333"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M473.34632807408667,564.5750045776367L545.4916610717773,681.7000045776367L592.1499938964844,681.7000045776367L630.0666580200195,681.7000045776367" marker-end="url(#arrowhead11792)" style="fill:none"></path><defs><marker id="arrowhead11792" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 0 0 L 0 0 z" style="fill: #333"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M466.78135363326027,564.5750045776367L545.4916610717773,799.591667175293L592.1499938964844,799.591667175293L651.2416610717773,799.591667175293" marker-end="url(#arrowhead11793)" style="fill:none"></path><defs><marker id="arrowhead11793" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 0 0 L 0 0 z" style="fill: #333"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M249.16392056001195,298.77500915527344L329.2083282470703,167.69583892822266L394.0833282470703,167.69583892822266L458.9583282470703,167.69583892822266L545.4916610717773,167.69583892822266L592.1499938964844,167.69583892822266L617.1499938964844,167.69583892822266" marker-end="url(#arrowhead11794)" style="fill:none"></path><defs><marker id="arrowhead11794" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M704.3914567973982,144.33750915527344L757.0499877929688,103.05000305175781L782.0499877929688,103.05000305175781L807.0499877929688,103.05000305175781" marker-end="url(#arrowhead11795)" style="fill:none"></path><defs><marker id="arrowhead11795" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 0 0 L 0 0 z" style="fill: #333"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M704.3914567973982,191.05416870117188L757.0499877929688,232.3416748046875L782.0499877929688,232.3416748046875L823.8583221435547,232.3416748046875" marker-end="url(#arrowhead11796)" style="fill:none"></path><defs><marker id="arrowhead11796" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 0 0 L 0 0 z" style="fill: #333"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M470.0512782360207,517.8583450317383L545.4916610717773,359.00417709350586L592.1499938964844,359.00417709350586L664.5330265034661,191.05416870117188" marker-end="url(#arrowhead11797)" style="fill:none"></path><defs><marker id="arrowhead11797" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g></g><g class="edgeLabels"><g class="edgeLabel" style="opacity: 1;" transform="translate(155.5583267211914,322.13333892822266)"><g transform="translate(-24.90833282470703,-13.358329772949219)" class="label"><foreignObject width="49.81666564941406" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel">TCP/IP</span></div></foreignObject></g></g><g class="edgeLabel" style="opacity: 1;" transform="translate(329.2083282470703,541.2166748046875)"><g transform="translate(-39.875,-13.358329772949219)" class="label"><foreignObject width="79.75" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel">Subprocess</span></div></foreignObject></g></g><g class="edgeLabel" style="opacity: 1;" transform=""><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" style="opacity: 1;" transform=""><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" style="opacity: 1;" transform=""><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" style="opacity: 1;" transform=""><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" style="opacity: 1;" transform="translate(458.9583282470703,167.69583892822266)"><g transform="translate(-39.875,-13.358329772949219)" class="label"><foreignObject width="79.75" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel">Subprocess</span></div></foreignObject></g></g><g class="edgeLabel" style="opacity: 1;" transform=""><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" style="opacity: 1;" transform=""><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" style="opacity: 1;" transform="translate(545.4916610717773,359.00417709350586)"><g transform="translate(-21.65833282470703,-13.358329772949219)" class="label"><foreignObject width="43.31666564941406" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel">Result</span></div></foreignObject></g></g></g><g class="nodes"><g class="node" style="opacity: 1;" id="IC" transform="translate(674.5999908447266,167.69583892822266)"><rect rx="0" ry="0" x="-57.44999694824219" y="-23.35832977294922" width="114.89999389648438" height="46.71665954589844"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-47.44999694824219,-13.358329772949219)"><foreignObject width="94.89999389648438" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Image Comps</div></foreignObject></g></g></g><g class="node" style="opacity: 1;" id="P" transform="translate(855.0999908447266,103.05000305175781)"><circle x="-48.05000305175781" y="-23.35832977294922" r="48.05000305175781"></circle><g class="label" transform="translate(0,0)"><g transform="translate(-38.05000305175781,-13.358329772949219)"><foreignObject width="76.10000610351562" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Photoshop</div></foreignObject></g></g></g><g class="node" style="opacity: 1;" id="Pi" transform="translate(855.0999908447266,232.3416748046875)"><circle x="-31.241668701171875" y="-23.35832977294922" r="31.241668701171875"></circle><g class="label" transform="translate(0,0)"><g transform="translate(-21.241668701171875,-13.358329772949219)"><foreignObject width="42.48333740234375" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Pillow</div></foreignObject></g></g></g><g class="node" style="opacity: 1;" id="BK" transform="translate(458.9583282470703,541.2166748046875)"><rect rx="0" ry="0" x="-33.5" y="-23.35832977294922" width="67" height="46.71665954589844"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-23.5,-13.358329772949219)"><foreignObject width="47" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Bakers</div></foreignObject></g></g></g><g class="node" style="opacity: 1;" id="M" transform="translate(674.5999908447266,399.42501068115234)"><circle x="-45.84166717529297" y="-23.35832977294922" r="45.84166717529297"></circle><g class="label" transform="translate(0,0)"><g transform="translate(-35.84166717529297,-13.358329772949219)"><foreignObject width="71.68333435058594" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Marmoset</div></foreignObject></g></g></g><g class="node" style="opacity: 1;" id="S" transform="translate(674.5999908447266,541.2166748046875)"><circle x="-45.94999694824219" y="-23.35832977294922" r="45.94999694824219"></circle><g class="label" transform="translate(0,0)"><g transform="translate(-35.94999694824219,-13.358329772949219)"><foreignObject width="71.89999389648438" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Substance</div></foreignObject></g></g></g><g class="node" style="opacity: 1;" id="X" transform="translate(674.5999908447266,681.7000045776367)"><circle x="-44.53333282470703" y="-23.35832977294922" r="44.53333282470703"></circle><g class="label" transform="translate(0,0)"><g transform="translate(-34.53333282470703,-13.358329772949219)"><foreignObject width="69.06666564941406" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">XNormals</div></foreignObject></g></g></g><g class="node" style="opacity: 1;" id="E" transform="translate(674.5999908447266,799.591667175293)"><circle x="-15.675003051757812" y="-23.35832977294922" r="23.35832977294922"></circle><g class="label" transform="translate(0,0)"><g transform="translate(-5.6750030517578125,-13.358329772949219)"><foreignObject width="11.350006103515625" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">...</div></foreignObject></g></g></g><g class="node" style="opacity: 1;" id="DCC" transform="translate(62.82499694824219,322.13333892822266)"><rect rx="5" ry="5" x="-42.82499694824219" y="-23.35832977294922" width="85.64999389648438" height="46.71665954589844"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-32.82499694824219,-13.358329772949219)"><foreignObject width="65.64999389648438" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">DCC App</div></foreignObject></g></g></g><g class="node" style="opacity: 1;" id="UI" transform="translate(234.89999389648438,322.13333892822266)"><rect rx="0" ry="0" x="-29.433334350585938" y="-23.35832977294922" width="58.866668701171875" height="46.71665954589844"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-19.433334350585938,-13.358329772949219)"><foreignObject width="38.866668701171875" height="26.716659545898438"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Qt UI</div></foreignObject></g></g></g></g></g></g></svg></div>
<h1 id="usage">Usage</h1>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">import</span> crossbaker
crossbaker<span class="token punctuation">.</span>initUI<span class="token punctuation">(</span><span class="token punctuation">)</span>
</code></pre>
<h2 id="config.json">config.json</h2>
<blockquote>
<p>Path to baking application.</p>
</blockquote>
<h2 id="export_setting.json">export_setting.json</h2>
<blockquote>
<p>Setting to feed baking application.</p>
</blockquote>
<h2 id="crossbaker.exportsettings">crossbaker.exportSettings</h2>
<blockquote>
<p>Contain all setting to export with</p>
</blockquote>
<h2 id="crossbaker.bakers">crossbaker.bakers</h2>
<blockquote>
<p>Iterable contain all available baker found in system.</p>
<pre class=" language-python"><code class="prism  language-python">crossbaker<span class="token punctuation">.</span>bakers<span class="token punctuation">.</span>count<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span> <span class="token comment">#return available bakers count.</span>
crossbaker<span class="token punctuation">.</span>bakers<span class="token punctuation">.</span>current<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span> <span class="token comment">#return current BakerApp.</span>
crossbaker<span class="token punctuation">.</span>bakers<span class="token punctuation">.</span>run<span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">:</span> <span class="token comment">#run current baker specified in exportSetting.</span>
crossbaker<span class="token punctuation">.</span>bakers<span class="token punctuation">.</span>get<span class="token punctuation">(</span>bakername<span class="token punctuation">)</span><span class="token punctuation">:</span> <span class="token comment">#return BakerApp for baker name.</span>
<span class="token comment"># Baker can also be access directly via attribute. Exp:</span>
crossbaker<span class="token punctuation">.</span>bakers<span class="token punctuation">.</span>marmoset
crossbaker<span class="token punctuation">.</span>bakers<span class="token punctuation">.</span>substance
</code></pre>
</blockquote>
<h2 id="crossbaker.exportsettings-1">crossbaker.exportSettings</h2>
<blockquote>
<p>Iterable contain settings to run baker with.</p>
<pre class=" language-python"><code class="prism  language-python">crossbaker<span class="token punctuation">.</span>exportSettings<span class="token punctuation">.</span>get<span class="token punctuation">(</span>settingname<span class="token punctuation">)</span> <span class="token comment">#: get setting by name.</span>
crossbaker<span class="token punctuation">.</span>exportSettings<span class="token punctuation">.</span>baker <span class="token comment">#: current baker to use.</span>
crossbaker<span class="token punctuation">.</span>exportSettings<span class="token punctuation">.</span>meshpath <span class="token comment">#: path to exported mesh.</span>
crossbaker<span class="token punctuation">.</span>exportSettings<span class="token punctuation">.</span>outputPath <span class="token comment">#: path to exported bake maps.</span>
crossbaker<span class="token punctuation">.</span>exportSettings<span class="token punctuation">.</span>outputSize <span class="token triple-quoted-string string">""" Size: Output images size.
:: param w : int : # map width
:: param h : int : # map height
"""</span>
crossbaker<span class="token punctuation">.</span>exportSettings<span class="token punctuation">.</span>outputSamples <span class="token comment">#: Output images AA samples.</span>
crossbaker<span class="token punctuation">.</span>exportSettings<span class="token punctuation">.</span>outputBits <span class="token comment">#: Output images bits depth.</span>
crossbaker<span class="token punctuation">.</span>exportSettings<span class="token punctuation">.</span>outputPSD <span class="token comment">#: Composite all export images as one psd file.</span>
crossbaker<span class="token punctuation">.</span>exportSettings<span class="token punctuation">.</span>useTextureSet <span class="token comment">#: Use Texture set when baking</span>
</code></pre>
</blockquote>
<h2 id="classes">Classes</h2>
<h2 id="crossbaker.bakerapp">crossbaker.BakerApp</h2>
<blockquote>
<pre class=" language-python"><code class="prism  language-python"><span class="token triple-quoted-string string">"""
::param name : str : baking application name.
::param path : str : path to baking application executable.
::method run : run subprocess call baker app with setting from exportSettings.
"""</span>
</code></pre>
</blockquote>
<h2 id="crossbaker.imageapp">crossbaker.ImageApp</h2>

>>>>>>> 0b1b833eafbdec1c5884d754b3458b8631d94a68
