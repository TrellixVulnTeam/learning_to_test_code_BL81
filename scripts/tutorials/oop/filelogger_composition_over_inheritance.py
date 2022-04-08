# This file demonstrates why you should favor composition over inheritance. The Gang of Four point out very explicitly that you should favor composition over inheritance, mainly because you get the "subclass" explosion problem when you try to modify a class along multiple axes.

# The total number of classes will increase geometrically if m and n both continue to grow. This is the “proliferation of classes” and “explosion of subclasses” that the Gang of Four want to avoid.

# The total number of classes will increase geometrically if m and n both continue to grow. This is the "proliferation of classes" and "explosion of subclasses" that the Gang of Four want to avoid.

# The solution is to recognize that a class responsible for both filtering messages and logging message is too complicated. In modern Object Oriented practice, it would be accused of violating the "Single Responsibility Principle."

"""Initial Class"""
import sys
import syslog

# The initial class

class Logger:
    pass

class SocketLogger(Logger):
    pass

class SyslogLogger(Logger):
    pass




"""Solution 2: The Bridge Pattern"""