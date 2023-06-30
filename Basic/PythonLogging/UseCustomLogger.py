import logging
#import PythonLogging.CustomLogger as cl
import CustomLogger as cl

class CustomLoggerDemo():
    log = cl.customLogger()

    def methodOne(self):
        self.log.critical("The critical message")
        self.log.error("The is error message")
        self.log.warning("This is Warning Message")
        self.log.info("This is Info Message")
        self.log.debug("This is Debug Message")

    def methodTwo(self):
        m2 = cl.customLogger()
        m2.critical("The critical message")
        m2.error("The is error message")
        m2.warning("This is Warning Message")
        m2.info("This is Info Message")
        m2.debug("This is Debug Message")

cld =CustomLoggerDemo()
cld.methodOne()
cld.methodTwo()



