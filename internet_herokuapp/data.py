import os
from dsl import *

resurs = SCOPE("resurs")
resurs["kote.jpg"] = os.path.join(CONFIG.TEST_CONFIG_PATH, "resurs", "kote.jpg")
