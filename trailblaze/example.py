import time
import random

from trailblaze import Trail, blaze


for i in range(20):
    blaze("a")
    time.sleep(random.random() * 0.1)
    blaze("b")
    time.sleep(random.random() * 0.1 + 0.1)
    if random.random() > 0.5:
        blaze("c")

print("-" * 40)

trail = Trail(decimals=3)
for i in range(100):
    trail.blaze("a")
    time.sleep(random.random() * 0.005)
    trail.blaze("b")
    time.sleep(random.random() * 0.005 + 0.1)
