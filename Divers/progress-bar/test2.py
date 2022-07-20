# code from https://stackoverflow.com/questions/45742888/using-multiple-bars

"""
Try using the position parameter when initialising the bars:

pbar1 = tqdm(total=100, position=1)
pbar2 = tqdm(total=200, position=0)
From the tqdm GitHub page:

position : int, optional

Specify the line offset to print this bar (starting from 0) Automatic if unspecified. Useful to manage multiple bars at once (eg, from threads).
"""

import time
from tqdm import *

pbar1 = tqdm(total=100)
pbar2 = tqdm(total=200)

for i in range(10):
    pbar1.update(10)
    pbar2.update(20)
    time.sleep(1)

