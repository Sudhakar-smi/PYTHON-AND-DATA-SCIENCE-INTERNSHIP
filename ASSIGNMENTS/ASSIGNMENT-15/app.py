import sys
from datetime import datetime

a = datetime.now()

print("Python Version :", sys.version)
print("Current Date :", a.strftime("%d/%m/%Y"))
print("Current Time :", a.strftime("%H:%M:%S"))