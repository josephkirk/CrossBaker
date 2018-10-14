#/usr/bin/env python3
# -*- coding: utf-8 -*-
import crossbaker
import os
from string import Template
setting = crossbaker.exportSetting()
def parseModule():
    src = os.path.normpath(os.path.join(__path__[0],"marmoset_src.py"))
    gen = os.path.normpath(os.path.join(__path__[0],"marmoset.py"))
    settings = dict(
        import_type=crossbaker.Import.UseFileName,
        mesh_path=setting.meshPath,
        save_path=setting.meshPath,
        export_path=setting.outputPath,
        bakemaps=setting.outputMaps,
        outputs_width=setting.outputSize.w,
        outputs_height=setting.outputSize.h,
        outputs_samples=setting.outputSamples,
        outputs_bits=setting.outputBits
    )
    fsrc = Template(open(src).read())
    with open(gen,"w") as write_file:
        write_file.write(fsrc.substitute(settings))
    return gen

def get():
    return [parseModule()]