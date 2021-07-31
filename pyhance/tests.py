# destination: import village
from pyhance.dict import dictionary as d
from pyhance.list import list_ as l
from pyhance.string import string as s
from pyhance.range import range_ as r

# declare dictionary for testing
di = d({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6})

# declare list for testing
li = l([
    "h", 1, 123, True, False, 3.14159265358, 2.1, [1], (2, 3), 1, 123, True,
    True
])
rtli = l(li.copy()).remove_all(True)

# declare string for testing
st = s("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

# declare ranges for testing
stoponly = r(5)
stopnstep = r(10, step=2)
stopnstart = r(start=5, stop=10)
stopstepnstart = r(start=4, stop=10, step=2)
negstep = r(start=10, stop=0, step=-1)

istoponly = r(5, inclusive=True)
istopnstep = r(10, step=2, inclusive=True)
istopnstart = r(start=5, stop=10, inclusive=True)
istopstepnstart = r(start=4, stop=10, step=2, inclusive=True)
inegstep = r(start=10, stop=0, step=-1, inclusive=True)

# begin asserting!

# tests for dict.py
# key_at() tests
assert di.item_at(0) == "a"
assert di.item_at(1) == "b"
assert di.item_at(2) == "c"
assert di.item_at(3) == "d"
assert di.item_at(4) == "e"
assert di.item_at(5) == "f"

# value_at() tests
assert di.item_at(0, item_type="value") == 1
assert di.item_at(1, item_type="value") == 2
assert di.item_at(2, item_type="value") == 3
assert di.item_at(3, item_type="value") == 4
assert di.item_at(4, item_type="value") == 5
assert di.item_at(5, item_type="value") == 6

# item_at() tests
assert di.item_at(0, item_type="pair") == {"a": 1}
assert di.item_at(1, item_type="pair") == {"b": 2}
assert di.item_at(2, item_type="pair") == {"c": 3}
assert di.item_at(3, item_type="pair") == {"d": 4}
assert di.item_at(4, item_type="pair") == {"e": 5}
assert di.item_at(5, item_type="pair") == {"f": 6}

# key_index() tests
assert di.index_of("a") == 0
assert di.index_of("b") == 1
assert di.index_of("c") == 2
assert di.index_of("d") == 3
assert di.index_of("e") == 4
assert di.index_of("f") == 5

# value_index() tests
assert di.index_of(1, item_type="value") == 0
assert di.index_of(2, item_type="value") == 1
assert di.index_of(3, item_type="value") == 2
assert di.index_of(4, item_type="value") == 3
assert di.index_of(5, item_type="value") == 4
assert di.index_of(6, item_type="value") == 5

# item_index() tests
assert di.index_of({"a": 1}, item_type="pair") == 0
assert di.index_of({"b": 2}, item_type="pair") == 1
assert di.index_of({"c": 3}, item_type="pair") == 2
assert di.index_of({"d": 4}, item_type="pair") == 3
assert di.index_of({"e": 5}, item_type="pair") == 4
assert di.index_of({"f": 6}, item_type="pair") == 5

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
assert stoponly == range(5)
assert stopnstep == range(0, 10, 2)
assert stopnstart == range(5, 10)
assert stopstepnstart == range(4, 10, 2)
assert negstep == range(10, 0, -1)

assert istoponly == range(6)
assert istopnstep == range(0, 11, 2)
assert istopnstart == range(5, 11)
assert istopstepnstart == range(4, 11, 2)
assert inegstep == range(10, -1, -1)
