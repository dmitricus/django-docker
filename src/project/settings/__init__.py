import os
from .common import *
from .db import *

# Тут подключать настройки которых может не быть
try:
    if os.environ.get('PYTEST_RUN', False):
        from .apps.local import *
    else:
        from .apps.local import *
except ImportError:
    pass
