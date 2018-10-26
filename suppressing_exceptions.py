#!/usr/bin/env python
from contextlib import suppress
import os

folder = 'wombat'

with suppress(FileExistsError):
    os.mkdir(folder)





