# destination: import village
from pyhance.dict import dictionary as d
from pyhance.list import list_ as l
from pyhance.string import string as s
from pyhance.range import range_ as r

# declare dictionary for testing
di = d({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6})

# declare list for testing
li = l(["h", 1, 123, True, False, 3.14159265358, 2.1, [1], (2, 3), 1, 123, True, True])
rtli = l(li.copy()).remove_all(True)

# declare string for testing
st = s("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

# declare ranges for testing
stoponly = r(5)
stopnstep = r(10, step=2)
stopnstart = r(start=5, stop=10)
stopstepnstart = r(start=4, stop=10, step=2)
negstep = r(start=10, stop=0, step=-1)

# begin asserting!


# tests for dict.py
# key_at() tests
assert di.key_at(0) == "a"
assert di.key_at(1) == "b"
assert di.key_at(2) == "c"
assert di.key_at(3) == "d"
assert di.key_at(4) == "e"
assert di.key_at(5) == "f"

# value_at() tests
assert di.value_at(0) == 1
assert di.value_at(1) == 2
assert di.value_at(2) == 3
assert di.value_at(3) == 4
assert di.value_at(4) == 5
assert di.value_at(5) == 6

# item_at() tests
assert di.item_at(0) == {"a": 1}
assert di.item_at(1) == {"b": 2}
assert di.item_at(2) == {"c": 3}
assert di.item_at(3) == {"d": 4}
assert di.item_at(4) == {"e": 5}
assert di.item_at(5) == {"f": 6}

# key_index() tests
assert di.key_index("a") == 0
assert di.key_index("b") == 1
assert di.key_index("c") == 2
assert di.key_index("d") == 3
assert di.key_index("e") == 4
assert di.key_index("f") == 5

# value_index() tests
assert di.value_index(1) == 0
assert di.value_index(2) == 1
assert di.value_index(3) == 2
assert di.value_index(4) == 3
assert di.value_index(5) == 4
assert di.value_index(6) == 5

# item_index() tests
assert di.item_index({"a": 1}) == 0
assert di.item_index({"b": 2}) == 1
assert di.item_index({"c": 3}) == 2
assert di.item_index({"d": 4}) == 3
assert di.item_index({"e": 5}) == 4
assert di.item_index({"f": 6}) == 5


# tests for list.py
# tests for remove_all method
assert rtli == li.remove_all(True)

# tests for string.py
# remove tests
assert st.remove("lorem") == st.replace("lorem", "")
assert st.remove("ispum") == st.replace("ispum", "")
assert st.remove("e") == st.replace("e", "")
assert st.remove("i") == st.replace("i", "")

# copy tests
assert st.copy() == st


# range_ tests
assert stoponly == [0, 1, 2, 3, 4]
