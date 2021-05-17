# -*- coding: utf-8 -*-
"""
Created on Sun May  9 13:54:59 2021

@author: Falacio
"""

import subprocess
import time
from getpass import getuser
usuario = getuser()

ruta_full = 'C:/Users/'+ usuario +'/.chia/mainnet/log/debug.log'
ruta_farm = 'C:/Users/'+ usuario +'/.chia/mainnet/log/farm_debug.log'
with open(ruta_full) as full_log, open(ruta_farm, 'w') as farm_log:
    for linea in full_log:
        if 'harvester' in linea or 'farmer' in linea:
            farm_log.write(linea)
time.sleep(5)
subprocess.run(["notepad",ruta_farm])
