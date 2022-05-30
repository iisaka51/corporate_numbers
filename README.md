Scraping Corporate Numbers.

First of all, this project is just for my self study for scraping.

The Corporate Number of each organization that has such number designated, and the name and the address of the head office or principal place of business of each organization that has registered.


## How to use

```python
from corporate_number import corporate_number as cn

filename = cn.download('kyoto')
df = cn.load_data(filename)
```

