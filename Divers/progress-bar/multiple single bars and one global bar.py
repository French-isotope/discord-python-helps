from tqdm import tqdm
import time

for i in tqdm(range(5), desc="i", colour='green'):
    for j in tqdm(range(10), desc="j", colour='red'):
        time.sleep(0.5)
