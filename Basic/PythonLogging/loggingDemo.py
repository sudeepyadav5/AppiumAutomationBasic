import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%d/%m/%y %I:%M:%S %p %A', level=logging.DEBUG ,filename="Test.log",filemode='w')
logging.critical("The critical message")
logging.error("The is error message")
logging.warning("This is Warning Message")
logging.info("This is Info Message")
logging.debug("This is Debug Message")

#%(asctime)s: - Date Time
# %(levelname)s: - Logging Message.
# %(message)s' - Logging Message.
# datefmt='%d/%m/%y - Logging %d for Date, %m for Month and %y for Year.
# %I:%M:%S %p %A', - %I for Hours, %M for minutes and %S for Second. / %p for PM and %A for AM
# level=logging.DEBUG ,filename="Test.log",filemode='w') - filename=test.log means new file where these information will show
# filemode='w' means - log infor showing without append infomation
# filemode='a' means - log infor showing with append infomation