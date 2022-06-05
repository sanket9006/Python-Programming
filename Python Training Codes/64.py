import os.path
import time
print("Last modified: %s" % time.ctime(os.path.getmtime("50.py")))
print("Created: %s" % time.ctime(os.path.getctime("50.py")))
