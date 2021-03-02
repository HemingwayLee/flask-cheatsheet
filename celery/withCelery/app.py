import time
from hello import add

result = add.delay(4, 4)
while True:
    if not result.ready():
        print("not ready!!!")
    else:
        print(f"the result is {result.get(timeout=3)}")
        break

    time.sleep(1)


print("bye...")
