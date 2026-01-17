"""
Topic: Plugin Architecture with Metaclasses
Concepts: plugin mount point, automatic registration, metaclass for patterns
Learning objectives:
    - Implement a plugin system using metaclasses
    - Understand automatic subclass registration
    - Design extensible architectures

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"


class PluginMount(type):
    """
    Metaclass that turns any class into a plugin mount point.

    When a class uses this metaclass, all its subclasses are automatically
    registered in a 'plugins' list. This enables plugin discovery without
    explicit registration.
    """

    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, "plugins"):
            # This is the mount point class (no plugins attribute yet)
            # Initialize an empty plugin list for subclasses to register in
            cls.plugins = []
        else:
            # This is a plugin (subclass of mount point)
            # Register it automatically
            cls.plugins.append(cls)
        super().__init__(name, bases, attrs)


class InputValidator(metaclass=PluginMount):
    """
    Plugin mount point for input validators.

    To create a new validator, simply subclass this class.
    It will be automatically registered in InputValidator.plugins.
    """

    def validate(self, string):
        """
        Validate the input string.

        Args:
            string: Input string to validate

        Returns:
            bool: True if valid, False otherwise
        """
        raise NotImplementedError


class AsciiInputValidator(InputValidator):
    """Validator that checks if input contains only ASCII characters."""

    def validate(self, string):
        """Check if string can be encoded as ASCII."""
        try:
            string.encode("ascii")
        except UnicodeError:
            return False
        else:
            return True


class UTF8InputValidator(InputValidator):
    """Validator that checks if input is valid UTF-8."""

    def validate(self, string):
        """Check if string can be encoded as UTF-8."""
        try:
            string.encode("utf-8")
        except UnicodeError:
            return False
        else:
            return True


# All validators are automatically registered
print("Registered plugins:", InputValidator.plugins)

# Test the validators
print("\n--- Testing Validators ---")
print("ASCII 'Hello':", AsciiInputValidator().validate("Hello"))
print("ASCII 'سلام':", AsciiInputValidator().validate("سلام"))
print("UTF8 'سلام':", UTF8InputValidator().validate("سلام"))


# Demonstrate plugin discovery pattern
def validate_all(string):
    """Run all registered validators on input."""
    print(f"\nValidating: '{string}'")
    for plugin_cls in InputValidator.plugins:
        validator = plugin_cls()
        result = validator.validate(string)
        print(f"  {plugin_cls.__name__}: {result}")


validate_all("Hello World")
validate_all("سلام دنیا")


# === Expected Output ===
# Registered plugins: [<class '__main__.AsciiInputValidator'>, <class '__main__.UTF8InputValidator'>]
#
# --- Testing Validators ---
# ASCII 'Hello': True
# ASCII 'سلام': False
# UTF8 'سلام': True
#
# Validating: 'Hello World'
#   AsciiInputValidator: True
#   UTF8InputValidator: True
#
# Validating: 'سلام دنیا'
#   AsciiInputValidator: False
#   UTF8InputValidator: True

# === Exercises ===
# 1. Add a LengthValidator that checks if string length is within a range
# 2. Modify the mount point to support enabling/disabling plugins
