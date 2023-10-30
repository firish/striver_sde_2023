import time

# defining a class
class Hero:


    # Constructor - Advantages
    # A constructor is a special method named __init__ that gets called when you create a new instance of a class
    # Code Reusability: Instead of writing separate methods to initialize attributes, you can reuse the constructor to set default or initial values for these attributes.
    # Encapsulation: By using constructors, you can keep the initialization logic encapsulated within the class. This ensures that the internal details of how an object is initialized are hidden from the outside world.
    # Consistency: With constructors, you can ensure that every instance of a class starts its life in a consistent state. 
    # Chaining and Delegation: In cases of inheritance, you can use the super() function in the constructor to call the constructor of a parent class. 
    # Chaining and Delegation: This ensures that the initialization logic in the parent class is also executed, maintaining the integrity and behavior of the inheritance chain.
    # Pattern Implementation: Enforce design patterns like singleton factory, where only one instance of class can be created.
    def __init__(self, name=None, health=100, level=0, power=10, is_alive=True):
        self.name = name
        self.health = health
        self.level = level
        self.power = power
        self.is_alive = is_alive
        
        self._bonus = "no_bonus"
        self._magic = "no_magic"
        self.__weapon = "no_weapon"
    

    # Access Modification
    # Python follows a principle called "we are all consenting adults here," 
    # which means it trusts the developer not to misuse the internal parts of a class.
    

    # GETTER-SETTER in Python
    # You don't need them officially, as direct access is allowed.
    # Still it is goof practice to use them, as they have benefits like
    # Encapsulation: Bundle and return related variables in a list
    # Data Validations: Setters allow you to introduce validation logic. For instance, if you have an attribute that should always be positive, you can check this in the setter and raise an error if someone tries to set a negative value.
    # Lazy Evaluation: If computing a value is expensive, you might not want to do it when the object is created. Instead, you can compute it when it's first accessed using a getter and then cache the result for future accesses.
    # Attribute Aliasing: If you ever need to change the name of an attribute but want to maintain backward compatibility, you can use a getter (and possibly a setter) with the old attribute name.
    # Logging: If you want to log every access or modification of an attribute, you can do this in setter-getts.
    # Consistaincy: If setting a value has some side effect, then that can be done before existing the setter.

    # Setter-Getter pair
    def get_health(self):
        print('Log: Health of hero {} was accessed at {}'.format(self.name, time.time()))
        return self.health
    def set_health(self, damage=0, boost=0, flag=False):
        if damage < 0 or boost < 0 or not isinstance(damage, int) or not isinstance(boost, int):
            raise ValueError("Boost or Damage must be positive integers.")
        if flag:
            if self.health + boost > 100:
                boost = 100 - self.health
            self.health += boost
            if self.health > 0 and not self.is_alive:
                self.is_alive = True
        else:
            if self.health - damage <= 0:
                damage = self.health
                self.is_alive = False
            self.health -= damage
        print('Log: Health of hero, {}: {}, Alive: {}'.format(self.name, self.health, self.is_alive))
    

    # "Conveying" Access Modification in Python to other Developers
    # Public: by default everything is public
    # Protected: Attributes or methods prefixed with a single underscore (_bonus)
    # Private: Attributes or methods with two leading underscores (__weapon)
    # Private: Python will name-mangle these names, which means the interpreter changes the name of the variable to make it harder to access from outside the class.
    # private: For instance, __private_var in a class named MyClass would be mangled to _MyClass__private_var
    # Note: Just like attributes, methods can also be public, protected, or private based on the naming conventions mentioned above.
    def get_bonus(self):
        return self._bonus
    def set_bonus(self, type):
        self._bonus = type
    # should only be called from within the class
    def __sharpen_weapon(self):
        self.__weapon += "_sharpened"
    
    
    # "Forcing" Access Modification in Python
    # This can be done by using the keyword "@property"
    # The @property decorator in Python is a built-in decorator that allows for the creation of "getter" methods for attributes, enabling a form of access control and modification.
    @property
    def magic(self):
        return self._magic
    # adding a setter
    @magic.setter
    def set_magic(self, type):
        self._magic = type
    # adding a deleter
    @magic.deleter
    def set_magic(self):
        self._magic = ""
    # If you define a property using @property but don't provide an associated setter (like for __weapon), 
    # then that property becomes read-only (private):
    @property
    def weapon(self):
        return self.__weapon
    
    
    # Next, static and synamic allocation in the class. 


# driver code

# creating an object
h1 = Hero('John_Snow')
h1.set_health(damage=30)
h1.set_health(damage=150)
h1.set_health(boost=80, flag=1)


# Conventions of access Modification
try:
    print(h1._bonus)
    print(h1.__weapon)
except Exception as err:
    print("Error accessing hero weapon: " + str(err))
print(h1._Hero__weapon)

