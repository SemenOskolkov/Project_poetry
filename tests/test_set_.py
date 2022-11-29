from code_file.set_ import set_

def test_set_1():
    true_value = 4
    test_coll = {"a": {"b": {"c": 3}}}
    set_(test_coll, ["a", "b", "c"], 4)
    assert test_coll["a"]["b"]["c"] == true_value


def test_set_2():
    true_value = 5
    test_coll = {"a": {"b": {"c": 3}}}
    set_(test_coll, ['x', 'y', 'z'], 5)
    assert test_coll['x']['y']['z'] == true_value


def test_set_3():
    true_value = ""
    test_coll = {"a": {"b": {"c": 3}}}
    set_(test_coll, ['x', 'y', 'z'], "")
    assert test_coll['x']['y']['z'] == true_value


def test_set_4():
    true_value = 3
    test_coll = {"a": {"b": {"c": 3}}}
    set_(test_coll, ["a", "b", "e"], 4)
    assert test_coll["a"]["b"]["c"] == true_value
