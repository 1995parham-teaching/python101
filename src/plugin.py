# In The Name Of God
# ========================================
# [] File Name : plugin.py
#
# [] Creation Date : 22-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'


class PluginMount(type):
    """
    Place this metaclass on any standard Python class to turn it into
    plugin mount point. All subclass will be automatically registered
    as plugins.
    """

    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'plugins'):
            # The class has no plugin list, so it must be a mount point,
            # so we add one for plugins to be registered in later.
            cls.plugins = []
        else:
            # Since the plugins attribute already exists, this is an
            # individual plugin, and it need to be registered
            cls.plugins.append(cls)
        super(PluginMount, cls).__init__(name, bases, attrs)


class InputValidator(metaclass=PluginMount):
    def validate(self, string):
        """
        :param string: input string
        :type string: str
        :return: boolean indicate validation result
        :rtype: bool
        """
        raise NotImplementedError


class AsciiInputValidator(InputValidator):
    def validate(self, string):
        """
        :param string: input string
        :type string: str
        :return: boolean indicate validation result
        :rtype: bool
        """
        try:
            string.encode('ascii')
        except UnicodeError:
            return False
        else:
            return True


class UTF8InputValidator(InputValidator):
    def validate(self, string):
        """
        :param string: input string
        :type string: str
        :return: boolean indicate validation result
        :rtype: bool
        """
        try:
            string.encode('utf-8')
        except UnicodeError:
            return False
        else:
            return True


print(InputValidator.plugins)
print(AsciiInputValidator().validate("Hello"))
print(AsciiInputValidator().validate('سلام'))
print(UTF8InputValidator().validate('سلام'))
