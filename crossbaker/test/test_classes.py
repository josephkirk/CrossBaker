import pytest
from crossbaker import Size, App, BakerApp

def test_size():
    size = Size(1,2)
    assert hasattr(size, "w") and hasattr(size, "h") 
    assert hasattr(size, "width") and hasattr(size, "height") 
    size.w = 2
    size.h = 4
    assert size.width == 2 and size.height == 4