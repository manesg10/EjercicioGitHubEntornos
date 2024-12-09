import time
from datetime import datetime

try:
    while True:

        ahora = datetime.now().strftime("%H:%M:%S")
        print(ahora,  end="\r")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nReloj detenido")