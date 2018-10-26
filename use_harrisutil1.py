#!/usr/bin/env python
import sys
from harris.sis import harrisutil
import harris.cn

harrisutil.launch()
harrisutil.communicate()
harrisutil._track()

for path in sys.path:
    print(path)
