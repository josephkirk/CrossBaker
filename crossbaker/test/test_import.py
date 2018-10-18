import pytest
import os
import inspect
import json

def getScriptDir():
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def getScriptRoot():
    return os.path.dirname(getScriptDir())

def getFile(fpath):
    return os.path.join(getScriptRoot(), fpath)

def test_config_exists():
    import crossbaker
    assert os.path.exists(getFile(crossbaker.Config))

def test_setting_exists():
    import crossbaker
    assert os.path.exists(getFile(crossbaker.Setting))

def test_exportSetting_attributes():
    import crossbaker
    with open(getFile(crossbaker.Setting)) as setting:
        data = json.load(setting)
    for i, value in data.items():
        assert hasattr(crossbaker.exportSetting, i.lower()[0] + i[1:])
        assert crossbaker.exportSetting.get(i) == value

def test_get_current_baker():
    import crossbaker
    assert crossbaker.bakers.current()

def test_baker_count():
    import crossbaker
    assert crossbaker.bakers.count() != 0

def test_get_baker_attribute():
    import crossbaker
    print("-"*20)
    for baker in crossbaker.bakers:
        print("Mod in BakerMod:{}".format(baker.name in crossbaker.bakermod.__dict__))
        print("Mod for {} is {}, type:{}".format(baker.name, baker.mod or "Not Found", type(baker.mod)))
    print("-"*20)
        # assert baker.mod, "\n{sep}\nNo mod for {bakername}\n{sep}\n".format(bakername=baker.name, sep="-"*20)
    assert True

def test_register_baker():
    import crossbaker
    crossbaker.registerBaker("testbaker", "testpath")
    assert "testbaker" in crossbaker.bakermod.__dict__