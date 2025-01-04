from dsl import *

CONFIG.THREADS  = 1
CONFIG.RETRIES  = 2
CONFIG.REPORTS  = "console,allure"
CONFIG.BASE_URL = "https://demoqa.com"
CONFIG.TEST_FATALITY = True
CONFIG.PAGE_LOAD_STRATEGY = "EAGER"
CONFIG.VACUUM = True
#CONFIG.REMOTE_EXECUTOR = "127.0.0.1:4444"
#CONFIG.CHROME_VERSION = "125.0"

CONFIG.SELENOID_OPTIONS = {
	"enableVideo": True
	, "enableVNC": True
	, "name": "raname"
}
