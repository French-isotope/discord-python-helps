import time
from tqdm import *

pbar1 = tqdm(total=100)
pbar2 = tqdm(total=200)

for i in range(10):
    pbar1.update(10)
    pbar2.update(20)
    time.sleep(1)
