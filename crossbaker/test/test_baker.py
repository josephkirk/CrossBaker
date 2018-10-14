import pytest

def test_run_current_baker():
    import crossbaker
    print("exec {} baker using arguments: {}".format(
        crossbaker.bakers.current().path, crossbaker.bakers.current().mod.get()))
    crossbaker.bakers.current().run()
    assert False