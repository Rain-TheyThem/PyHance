# destination: import village
from pyhance.dict import dictionary as d

# declare dictionary for testing
di = d({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f", 6})

# begin asserting!
# di.key_at() tests
assert di.key_at(0) == "a"
assert di.key_at(1) == "b"
assert di.key_at(2) == "c"
assert di.key_at(3) == "d"
assert di.key_at(4) == "e"
assert di.key_at(5) == "f"

# di.value_at() tests
assert di.value_at(0) == 1
assert di.value_at(1) == 2
assert di.value_at(2) == 3
assert di.value_at(3) == 4
assert di.value_at(4) == 5
assert di.value_at(5) == 6
