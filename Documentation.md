# PyHance Documentation

## Welcome to PyHance
Welcome to PyHance and thank you for looking at this project!
Now, you may be wondering, what does PyHance do?
PyHance:
* Adds functionality to builtin data types (such as adding a `remove()` method to a custom `string` class)
* Adds new functions (such as a new `range` function that adds an option to be inclusive)


## dictionary
The `dictionary` class is an extension of the builtin `dict` class.
### `key_at` method
The `key_at` method returns the key at a specified index.
Example:
```python
    from pyhance.data_types.dict import dictionary # imports the custom 'dictionary' class
    
    di = dictionary({"a": 1, "b": 2}) # declares a variable of my custom type, "dictionary"
    # The declaration must contain a dictionary as the one and only parameter.
    print(di.key_at(0)) # prints the key at index 0, which in this case, is "a".
```
