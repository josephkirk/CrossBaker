---

## *Design*
-----
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

---

##  *Usage*
-----
```python
import crossbaker
crossbaker.initUI()
```
###  config.json
> Path to baking application.

###  export_setting.json
> Setting to feed baking application.

###  crossbaker.exportSettings
> Contain all setting to export with

###  crossbaker.bakers
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

### crossbaker.exportSettings
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
### crossbaker.BakerApp
>```python
>"""
>::param name : str : baking application name.
>::param path : str : path to baking application executable.
>::method run : run subprocess call baker app with setting from exportSettings.
>"""
>```
### crossbaker.ImageApp