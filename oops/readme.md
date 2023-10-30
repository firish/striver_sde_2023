# Things to revise ..

Basics of OOP:

Object: A collection of data (attributes) and methods (functions) that act on the data.
Class: A blueprint for creating objects.
Attributes and Methods:

Attributes: Variables that belong to a class/object.
Methods: Functions that belong to a class/object.
Constructor:

__init__ method: Used for initializing attributes when an object is created.
Inheritance:

Allows a class (child class) to inherit attributes and methods from another class (parent class).
Base/Parent class: The class being inherited from.
Derived/Child class: The class that inherits from the base class.
Polymorphism:

Allows objects of different classes to be treated as objects of a common superclass.
Overloading: Using the same method or operator name but with different signatures.
Overriding: Redefining methods in derived classes.
Encapsulation:

Bundling data (attributes) and methods that operate on that data within a single unit (class).
Private attributes/methods: Denoted by a leading underscore (e.g., _private_var). It's a convention in Python, not strictly private.
Protected attributes/methods: Denoted by two leading underscores (e.g., __private_var). Name mangling is used to make it harder to access from outside the class.
Public attributes/methods: Accessible from anywhere.
Abstraction:

Hiding the complex implementation details and showing only the essential features of an object.
Composition:

Building complex objects by combining simpler objects.
Aggregation:

A form of object composition where one class contains another class but does not necessarily manage its lifecycle.
Association:

A relationship between two or more objects where all objects have their own lifecycle.
Class and Static Methods:

@classmethod: A method that's bound to the class and not the instance. It takes cls as its first parameter.
@staticmethod: A method that belongs to a class but doesn't access or modify class-specific or instance-specific data.
Class Variables vs Instance Variables:

Class Variables: Shared among all instances of a class.
Instance Variables: Unique to each instance.
Magic/Dunder Methods:

Special methods with double underscores at the beginning and end (e.g., __str__, __eq__).
Allow customization of default Python behaviors.
Property Decorators:

@property: Used to define getter methods.
@<attribute>.setter: Used to define setter methods.
@<attribute>.deleter: Used to define deleter methods.
Multiple Inheritance:

A derived class inheriting from more than one base class.
Mixins:

A design pattern where a class provides certain functionality to be "mixed in" to other classes.
Method Resolution Order (MRO):

The order in which base classes are searched when looking for a method.
Duck Typing:

"If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck." In Python, it's more about what the object can do (methods/behavior) rather than what it is.
Composition vs Inheritance:

Two major ways to build relationships between classes. Composition is about using other objects, while inheritance is about extending them.
Dependency Injection:

A technique where an object receives its dependencies from outside rather than creating them internally.
Interfaces and Abstract Classes:

Using the abc module to create abstract base classes and enforce the child classes to implement certain methods.
Namespaces and Scoping:

Understanding how variables are accessed and where they live in relation to classes and objects.
Modules and Packages:

Organizing classes and OOP structures into reusable modules and packages


Magic/Dunder Methods:

These are special methods with double underscores at the beginning and end. They allow customization of default Python behaviors.
__str__: Returns a string representation of the object.
__repr__: Returns an unambiguous representation of the object, ideally one that could recreate the object if passed to eval().
__eq__, __ne__, __lt__, __le__, __gt__, __ge__: Comparison operators.
__add__, __sub__, __mul__, etc.: Arithmetic operators.
__getitem__, __setitem__, __delitem__: Indexing and slicing.
__call__: Makes an object callable.
__len__: Returns the length of an object.
__contains__: Implements membership test operations.
__iter__: Returns an iterator for the object.
And many more...
Decorators:

Functions or classes that can be used to modify or extend the behavior of other functions or classes without changing their source code.
@staticmethod: Indicates a static method.
@classmethod: Indicates a class method.
@property: Used for getters in property-based attribute access.
Custom decorators can also be created to extend functionalities.
Wrappers:

A design pattern used to add new responsibilities to an object dynamically. In Python, this is often achieved using decorators.
Destructor:

__del__ method: Called when an object is about to be destroyed. However, it's not guaranteed when it will be called due to the nature of the garbage collector in Python.
Garbage Collection:

Python has a built-in garbage collector that reclaims memory from objects that are no longer in use.
Reference counting: Every object has a count of the number of references to it.
Cyclic Garbage Collector: Detects and cleans up reference cycles (e.g., two objects referencing each other).
Interfaces and Abstract Classes:

Python doesn't have native support for interfaces like some other languages. However, abstract classes in the abc module can be used to achieve similar functionality.
@abstractmethod: A decorator indicating abstract methods that must be implemented by any child class.
Abstract classes can't be instantiated directly.
Composition Over Inheritance:

A principle suggesting it's better to compose objects (have them reference other objects) than to inherit from classes, leading to more modular and flexible code.
Singleton Pattern:

Ensures a class has only one instance and provides a global point of access to that instance.
Can be implemented using __new__ method, modules, or decorators.
Factory Pattern:

A method for creating objects in superclasses but allowing subclasses to alter the types of objects that will be created.
Dependency Injection:

A technique where an object receives its dependencies from outside rather than creating them internally, promoting decoupling and easier testing.
Namespaces:

A way to encapsulate variables. In Python, every module, class, function, and method defines its own namespace.
Scoping:

Rules that determine the visibility and lifetime of a variable. In Python, the LEGB rule applies: Local, Enclosing, Global, Built-in.
Metaclasses:

A deep OOP concept. They are classes of classes that allow one to customize class creation.
Slots:

__slots__: An attribute in a Python class that can be used to limit the attributes that can be added to an object. It can optimize memory usage for objects.
Descriptors:

An object attribute with "binding behavior", one whose attribute access has been overridden by methods in the descriptor protocol: __get__, __set__, and __delete__.
Proxy and Virtual Proxy:

Design patterns where a placeholder object represents another object. Virtual proxies can delay the creation and initialization of expensive objects until they are actually needed.
Observer Pattern:

A design pattern where an object (known as the subject) maintains a list of its dependents (observers) and notifies them of any state changes.
Decorator Pattern:

A design pattern that allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class.
Chain of Responsibility:

A design pattern consisting of a source of command objects and a series of processing objects. Each processing object contains logic that defines the types of command objects that it can handle.



Args and kwargs in python ,....


Dynamic Attributes and Methods:

Python allows you to add attributes and methods to objects dynamically, even after they've been instantiated.
__getattr__ and __setattr__:

__getattr__: Called when an attribute lookup has not found the attribute in the usual places.
__setattr__: Called when an attribute assignment is attempted.
Reflection:

The ability for a program to inspect and modify its structure and behavior at runtime. In Python, functions like getattr(), setattr(), and hasattr() support reflection.
__dict__:

A dictionary or other mapping object used to store an object’s writable attributes.
Method Types:

Bound methods: Methods derived from associating an instance with a function.
Unbound methods: Methods that are not associated with an instance.
super() Function:

Used to call a method from a parent class, especially useful in the context of multiple inheritance.
__new__ Method:

Responsible for creating a new instance. It's a static method that takes the class as its first argument.
isinstance() and issubclass():

isinstance(): Checks if an object is an instance of a particular class or a tuple of classes.
issubclass(): Checks if a class is a subclass of a second class.
Delegation:

An OOP design pattern where an object passes off some of its responsibilities to a second object.
Adapter Pattern:

A design pattern that allows objects with incompatible interfaces to work together.
State Pattern:

A design pattern that allows an object to change its behavior when its internal state changes.
Strategy Pattern:

A design pattern that defines a family of algorithms, encapsulates each one, and makes them interchangeable.
Command Pattern:

A design pattern that encapsulates a request as an object, thereby allowing users to parameterize clients with different requests.
Memento Pattern:

A design pattern that provides the ability to restore an object to its previous state.
weakref Module:

Allows the Python programmer to create weak references to objects. Useful in managing memory and avoiding circular references.
property() Function:

Besides the @property decorator, there's also a built-in function property() that can be used to define properties.
Immutable Objects:

Objects whose state cannot be modified after they are created, like strings and tuples.
__slots__ Caveats:

While __slots__ can optimize memory, it has caveats like preventing the creation of new attributes outside of those defined in __slots__.
types Module:

Provides names for some object types that are used to check if an object is of a certain type, like FunctionType, MethodType, etc.
functools.wraps:

A decorator used to preserve the metadata of the original function when it's being wrapped by another function (commonly used in custom decorator definitions).
__all__ Attribute:

A list that defines the public interface of a module. It restricts the attributes and methods that are imported when a client imports a module using the wildcard (*) import.