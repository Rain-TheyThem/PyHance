# Exceptions

## AssertionError
Raised when the `assert` statement fails
## AttributeError
Raised when an attribute assignment or reference fails
## EOFError
Raised when an `input()` call ends without receiving data
## FloatingPointError
Unused
## GeneratorExit
Raised when a generator or coroutine is closed
## ImportError
Raised when the import statement has troubles trying to load a module or when the “from list” in `from ... import` has a name that cannot be found.
## ModuleNotFoundError
Raised by the `import` statement when a module isn’t found.
## IndexError
Raised when a sequence subscript is out of range
## KeyError
Raised when a key isn’t found in a dictionary
## KeyboardInterrupt
Raised when a user presses the `Ctrl+C` keys
## MemoryError
Raised when an operation runs out of memory, but the situation may still be rescued by deleting a couple of objects.
## NameError
Raised when a variable isn’t found
## NotImplementedError
In user defined base classes, abstract methods should raise this exception when they require derived classes to override the method, or while the class is being developed to indicate that the real implementation still needs to be added.
## OSError
Raised when a system function returns a system-related error
## OverflowError
Raised when the result of an arithmetic operation is too large to be represented. This cannot occur for integers (which would rather raise `MemoryError` than give up). However, for historical reasons, OverflowError is sometimes raised for integers that are outside a required range. Because of the lack of standardization of floating point exception handling in C, most floating point operations are not checked.
## RecursionError
Raised when the maximum recursion depth is exceeded
## ReferenceError
Raised when a weak reference proxy, created by the `weakref.proxy()` function, is used to access an attribute of the referent after it has been garbage collected
## RuntimeError
Raised when an error doesn’t fall into any of the other categories
## StopIteration
Raised to indicate that there are no further items produced by the iterator
## StopAsyncIteration
Must be raised by `__anext__()` method of an asynchronous iterator object to stop the iteration.
## SyntaxError
Raised when the parser detects a syntax error
## IndetationError
Base class for syntax errors related to incorrect indentation.
## TabError
Raised when indentation is a mixture of tabs and spaces
## SystemError
Raised when the interpreter finds an internal error, but the situation does not look so serious to cause it to abandon all hope.
## SystemExit
Raised by the `sys.exit()` function.
## TypeError
Raised when an operation or function is applied to an object of inappropriate type
## UnboubdLocalError
Raised when a reference is made to an empty local variable
## UnicodeError
Raised when a Unicode-related encoding or decoding error occurs
## UnicodeEncodeError
Raised when a Unicode-related encoding error occurs
## UnicodeDecodeError
Raised when a Unicode-related decoding error occurs
## UnicodeTranslateError
Raised when a Unicode-related translating error occurs
## ValueError
Raised when an operation or function gets an argument with an inappropriate value, and is not described by a more specific error, such as IndexError
## ZeroDivisionError
Raised when the second argument of a division or modulo operation is 0