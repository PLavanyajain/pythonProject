import logging

class LogGen:

    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename=".//Logs//lav.log",
                           # format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%y %I%M%S%p')
        #logging.basicConfig(filename="C://Users//Lavanya//PycharmProjects//pythonProject//Logs//Autiomation.log",
                            #format='%(asctime)s : %(levelname)s  %(message)s',  # it will print the time,date,level
                           # datefmt='%d/%m/%Y %I:%M %S %p',
                           # level=logging.DEBUG
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

