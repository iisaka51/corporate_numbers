The scrapper for the Corporate Numbers.

First of all, this project is just for my self study for scraping.

The Corporate Number of each organization that has such number designated, and the name and the address of the head office or principal place of business of each organization that has registered.


## How to use

```python
In [1]: from corporate_numbers import corporate_numbers as cn

In [2]: print(cn.get_fileids())
['All', 'Hokkaido', 'Aomori', 'Iwate', 'Miyagi', 'Akita', 'Yamagata', 'Fukushima', 'Ibaraki', 'Tochigi', 'Gunma', 'Saitama', 'Chiba', 'Tokyo', 'Kanagawa', 'Niigata', 'Toyama', 'Ishikawa', 'Fukui', 'Yamanashi', 'Nagano', 'Gifu', 'Shizuoka', 'Aichi', 'Mie', 'Shiga', 'Kyoto', 'Osaka', 'Hyogo', 'Nara', 'Wakayama', 'Tottori', 'Shimane', 'Okayama', 'Hiroshima', 'Yamaguchi', 'Tokushima', 'Kagawa', 'Ehime', 'Kochi', 'Fukuoka', 'Saga', 'Nagasaki', 'Kumamoto', 'Oita', 'Miyazaki', 'Kagoshima', 'Okinawa', 'OutSide']

In [3]: filename = cn.download('Kyoto')

In [4]: df = cn.load_data(filename)

In [5]: df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 101871 entries, 0 to 101870
Data columns (total 30 columns):
 #   Column                                                   Non-Null Count   Dtype
---  ------                                                   --------------   -----
 0   1                                                        101871 non-null  int64
 1   1000012160054                                            101871 non-null  int64
 2   01                                                       101871 non-null  int64
 3   1.1                                                      101871 non-null  int64
 4   2018-04-02                                               101871 non-null  object
 5   2015-10-05                                               101871 non-null  object
 6   舞鶴検察審査会                                                  101871 non-null  object
 7   Unnamed: 7                                               1649 non-null    float64
 8   101                                                      101871 non-null  int64
 9   京都府                                                      101871 non-null  object
 10  舞鶴市                                                      101871 non-null  object
 11  字南田辺小字南裏町１４９                                             101871 non-null  object
 12  Unnamed: 12                                              3763 non-null    float64
 13  26                                                       101871 non-null  int64
 14  202                                                      101871 non-null  int64
 15  6240853                                                  101858 non-null  float64
 16  Unnamed: 16                                              0 non-null       float64
 17  Unnamed: 17                                              0 non-null       float64
 18  Unnamed: 18                                              7391 non-null    object
 19  Unnamed: 19                                              7391 non-null    float64
 20  Unnamed: 20                                              653 non-null     float64
 21  Unnamed: 21                                              1118 non-null    object
 22  2015-10-05.1                                             101871 non-null  object
 23  1.2                                                      101871 non-null  int64
 24  Maizuru Committee for the Inquest of Prosecution         248 non-null     object
 25  Kyoto                                                    245 non-null     object
 26  149, Aza Minamitanabe Koaza Minamiuramachi, Maizuru shi  245 non-null     object
 27  Unnamed: 27                                              0 non-null       float64
 28  マイヅルケンサツシンサカイ                                            49015 non-null   object
 29  0                                                        101871 non-null  int64
dtypes: float64(8), int64(9), object(13)
memory usage: 23.3+ MB

In [6]:
```
