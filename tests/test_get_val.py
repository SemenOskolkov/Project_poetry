from code_file.get_val import get_val

def test_get_val_key():
    assert get_val({"hello": "world"}, "hello") == "world"
    assert get_val({"hello": "world"}, "hello", "python") == "world"
    assert get_val({"hello": "world"}, "", "python") == "python"
    assert get_val({"hello": ""}, "hello") == ""

def test_get_val_default():
    assert get_val({}, "hello", "python") == "python"
    assert get_val({}, "hello", "") == ""

def test_get_val_none():
    assert get_val({}, "", "") == ""
