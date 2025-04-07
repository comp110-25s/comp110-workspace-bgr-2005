"""tests ex 3"""

__author__ = "730769478"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len

testDict1 = {"a": "b", "c": "d"}
testDict2 = {"apple": "bannana", "citrus": "duerme"}
testDict3 = {}


def test_invert1():
    assert invert(testDict1) == {"b": "a", "d": "c"}, "Test 1 failed"


def test_invert2():
    assert invert(testDict2) == {
        "bannana": "apple",
        "duerme": "citrus",
    }, "Test 2 failed"


def test_invert3():
    assert invert(testDict3) == {}, "Test 3 failed"


testList1 = list(["a", "b", "c"])
testList2 = list(["a", "a", "a"])
testList3 = list("")


def test_coun1():
    assert count(testList1) == {"a": 1, "b": 1, "c": 1}, "test 1 failed"


def test_count2():
    assert count(testList2) == {"a": 3}, "test 2 failed"


def test_count3():
    assert count(testList3) == {}, "test 3 failed"


testDict11 = {"ella": "red", "john": "blue"}
testDict22 = {"ella": "red", "john": "blue", "emma": "blue"}
testDict33 = {"elle": "orange", "ben": "orange", "ron": "red"}


def test_favorite_color1():
    assert favorite_color(testDict11) == "red", "Test 1 Failed"


def test_favorite_color2():
    assert favorite_color(testDict22) == "blue", "Test 2 Failed"


def test_favorite_color3():
    assert favorite_color(testDict33) == "orange", "Test 3 Failed"


testList11 = ["1", "22", "333"]
testList22 = ["1", "22", "23", "4444"]
testList33 = []


def test_bin_len1():
    assert bin_len(testList11) == {1: {"1"}, 2: {"22"}, 3: {"333"}}, "Test 1 Failed"


def test_bin_len2():
    assert bin_len(testList22) == {
        1: {"1"},
        2: {"22", "23"},
        4: {"4444"},
    }, "Test 2 Failed "


def test_bin_len3():
    assert bin_len(testList33) == {}, "Test 3 Failed"
