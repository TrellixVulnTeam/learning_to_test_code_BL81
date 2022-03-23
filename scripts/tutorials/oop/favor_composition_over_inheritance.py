# https://python-patterns.guide/gang-of-four/composition-over-inheritance/#problem-the-subclass-explosion
# KZ 3-20-22

import sys
import syslog

# the initial class
class Logger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message)


#  "Imagine a base logging class (above) that has gradually gained subclasses as developers needed to send log messages to new destinations (below)"


if __name__ == '__main__':
    log = Logger(sys.stdout)
    log.log("hello_logging_world")
