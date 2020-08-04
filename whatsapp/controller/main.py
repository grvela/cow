import logging 
logging.basicConfig(filename='error.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s => %(message)s')


from driver import WhatsappDriver

from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementNotVisibleException

try:
    
    WindowChrome = WhatsappDriver()
    WindowChrome.start()

except(WebDriverException, ConnectionError, ConnectionRefusedError,
       ConnectionResetError, ConnectionAbortedError, TimeoutException) as Error:
    logging.exception(Error)
