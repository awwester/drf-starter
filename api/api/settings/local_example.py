"""
Copy this file into api/settings/local.py to start running the project. This is
done automatically with `make setup` command. You may override settings locally
if you wish in that file.
"""

from .base import *


MIDDLEWARE += ['core.middleware.TimeDelayMiddleware']
if TEST_MODE:
    REQUEST_TIME_DELAY = 0
else:
    REQUEST_TIME_DELAY = float(os.getenv('REQUEST_TIME_DELAY', 0))
