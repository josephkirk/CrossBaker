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

def test_import():
    import crossbaker
    assert crossbaker

def test_config_exists():
    assert os.path.exists(getFile("config.json"))

def test_setting_exists():
    assert os.path.exists(getFile("export_settings.json"))

def test_exportSetting_attributes():
    import crossbaker
    with open(getFile("export_settings.json")) as setting:
        data = json.load(setting)
    for i, value in data.items():
        assert hasattr(crossbaker.exportSetting(), i.lower()[0] + i[1:])
        assert crossbaker.exportSetting.getSetting(i) == value

def test_get_current_baker():
    import crossbaker
    assert crossbaker.bakers.current()

def test_baker_attributes():
    import crossbaker
    with open(getFile("config.json")) as config:
        bakerData = json.load(config)
    assert crossbaker.bakers.countAll() == len(bakerData)

# def test_get_baker_attribute():
#     import crossbaker
#     assert hasattr(crossbaker, "marmoset"), "Marmoset is not found."