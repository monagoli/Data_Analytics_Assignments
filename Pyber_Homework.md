
# Analyses
###### Trend 1: The most rides with the most steady fare rate came from more Urban areas, which could imply that people in this area are less like to own vehicles of their own and need help getting around the busy area. 
##### Trend 2: Rural areas had the most sporadic usage--no trend is readily detectable. Perhaps this could allude to the heavier reliance on public transportation. This can be inferred through the few data points that are very high on average fare, which can imply these riders are traveling longer distances...perhaps to and from work. 
##### Trend 3: In the Rural and Suburban areas, we see that the volume of actual drivers is low. Perhaps these areas with less volume of drivers do in fact have a need for app-based transport services, but they are not readily accessible to them.


```python
import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
```


```python
city_data = 'city_data.csv'
ride_data = 'ride_data.csv'
```


```python
city_df = pd.read_csv(city_data,encoding = "ISO-8859-1")

ride_df = pd.read_csv(ride_data,encoding = "ISO-8859-1")
ride_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>2016-01-16 13:49:27</td>
      <td>$38.35</td>
      <td>5403689035038</td>
    </tr>
    <tr>
      <th>1</th>
      <td>South Roy</td>
      <td>2016-01-02 18:42:34</td>
      <td>$17.49</td>
      <td>4036272335942</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wiseborough</td>
      <td>2016-01-21 17:35:29</td>
      <td>$44.18</td>
      <td>3645042422587</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spencertown</td>
      <td>2016-07-31 14:53:22</td>
      <td>$6.87</td>
      <td>2242596575892</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nguyenbury</td>
      <td>2016-07-09 04:42:44</td>
      <td>$6.28</td>
      <td>1543057793673</td>
    </tr>
  </tbody>
</table>
</div>




```python
city_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nguyenbury</td>
      <td>8</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Douglas</td>
      <td>12</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>West Dawnfurt</td>
      <td>34</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rodriguezburgh</td>
      <td>52</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
travel_data = pd.merge(city_df, ride_df, on="city")
travel_data
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-08-19 04:27:52</td>
      <td>$5.51</td>
      <td>6246006544795</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-04-17 06:59:50</td>
      <td>$5.54</td>
      <td>7466473222333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-05-04 15:06:07</td>
      <td>$30.54</td>
      <td>2140501382736</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-01-25 20:44:56</td>
      <td>$12.08</td>
      <td>1896987891309</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-08-09 18:19:47</td>
      <td>$17.91</td>
      <td>8784212854829</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-10-24 15:15:46</td>
      <td>$33.56</td>
      <td>4797969661996</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-06-06 13:54:23</td>
      <td>$20.81</td>
      <td>9811478565448</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-08-10 07:02:40</td>
      <td>$44.53</td>
      <td>1563171128434</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-07-05 17:37:13</td>
      <td>$29.02</td>
      <td>6897992353955</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-04-25 02:18:31</td>
      <td>$20.05</td>
      <td>1148374505062</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-01-25 08:47:09</td>
      <td>$9.29</td>
      <td>213692794373</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-11-10 01:57:14</td>
      <td>$20.58</td>
      <td>3395682132130</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-08-15 11:55:02</td>
      <td>$27.45</td>
      <td>8456148871668</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-08-01 10:51:49</td>
      <td>$33.51</td>
      <td>6610565660737</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-04-13 12:07:08</td>
      <td>$6.56</td>
      <td>8101498434215</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-01-12 22:51:21</td>
      <td>$20.19</td>
      <td>3054122642867</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-05-31 01:05:31</td>
      <td>$35.22</td>
      <td>5946467060438</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-07-13 16:53:07</td>
      <td>$10.31</td>
      <td>2180910323678</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-01-07 07:15:41</td>
      <td>$11.45</td>
      <td>600800386573</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-04-09 13:17:27</td>
      <td>$27.85</td>
      <td>5748868894243</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-06-30 01:59:04</td>
      <td>$8.27</td>
      <td>4384089549855</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-04-20 05:36:59</td>
      <td>$31.67</td>
      <td>2865704421982</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-05-02 05:55:28</td>
      <td>$40.92</td>
      <td>2769007541388</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-06-22 06:54:57</td>
      <td>$12.58</td>
      <td>6629798205387</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-06-18 06:03:03</td>
      <td>$16.77</td>
      <td>7223504701591</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-01-09 20:28:56</td>
      <td>$27.21</td>
      <td>831362906446</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-07-22 19:28:21</td>
      <td>$35.71</td>
      <td>1234880130185</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-11-26 02:34:57</td>
      <td>$15.49</td>
      <td>5187807155760</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Nguyenbury</td>
      <td>8</td>
      <td>Urban</td>
      <td>2016-07-09 04:42:44</td>
      <td>$6.28</td>
      <td>1543057793673</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Nguyenbury</td>
      <td>8</td>
      <td>Urban</td>
      <td>2016-11-08 19:22:04</td>
      <td>$19.49</td>
      <td>1702803950740</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2377</th>
      <td>East Leslie</td>
      <td>9</td>
      <td>Rural</td>
      <td>2016-04-13 04:30:56</td>
      <td>$40.47</td>
      <td>7075058703398</td>
    </tr>
    <tr>
      <th>2378</th>
      <td>East Leslie</td>
      <td>9</td>
      <td>Rural</td>
      <td>2016-04-26 02:34:30</td>
      <td>$45.80</td>
      <td>9402873395510</td>
    </tr>
    <tr>
      <th>2379</th>
      <td>East Leslie</td>
      <td>9</td>
      <td>Rural</td>
      <td>2016-04-05 18:53:16</td>
      <td>$44.78</td>
      <td>6113138249150</td>
    </tr>
    <tr>
      <th>2380</th>
      <td>East Leslie</td>
      <td>9</td>
      <td>Rural</td>
      <td>2016-11-13 10:21:10</td>
      <td>$15.71</td>
      <td>7275986542384</td>
    </tr>
    <tr>
      <th>2381</th>
      <td>East Leslie</td>
      <td>9</td>
      <td>Rural</td>
      <td>2016-03-06 06:10:40</td>
      <td>$51.32</td>
      <td>6841691147797</td>
    </tr>
    <tr>
      <th>2382</th>
      <td>East Leslie</td>
      <td>9</td>
      <td>Rural</td>
      <td>2016-03-04 10:18:03</td>
      <td>$13.43</td>
      <td>8814831098684</td>
    </tr>
    <tr>
      <th>2383</th>
      <td>East Leslie</td>
      <td>9</td>
      <td>Rural</td>
      <td>2016-11-28 09:09:15</td>
      <td>$37.76</td>
      <td>804829686137</td>
    </tr>
    <tr>
      <th>2384</th>
      <td>East Leslie</td>
      <td>9</td>
      <td>Rural</td>
      <td>2016-09-08 19:19:38</td>
      <td>$30.59</td>
      <td>8211833105097</td>
    </tr>
    <tr>
      <th>2385</th>
      <td>East Leslie</td>
      <td>9</td>
      <td>Rural</td>
      <td>2016-03-02 22:09:34</td>
      <td>$36.61</td>
      <td>5500269118478</td>
    </tr>
    <tr>
      <th>2386</th>
      <td>East Leslie</td>
      <td>9</td>
      <td>Rural</td>
      <td>2016-06-22 07:45:30</td>
      <td>$34.54</td>
      <td>684950063164</td>
    </tr>
    <tr>
      <th>2387</th>
      <td>Hernandezshire</td>
      <td>10</td>
      <td>Rural</td>
      <td>2016-02-20 08:17:32</td>
      <td>$58.95</td>
      <td>3176534714830</td>
    </tr>
    <tr>
      <th>2388</th>
      <td>Hernandezshire</td>
      <td>10</td>
      <td>Rural</td>
      <td>2016-06-26 20:11:50</td>
      <td>$28.78</td>
      <td>6382848462030</td>
    </tr>
    <tr>
      <th>2389</th>
      <td>Hernandezshire</td>
      <td>10</td>
      <td>Rural</td>
      <td>2016-01-24 00:21:35</td>
      <td>$30.32</td>
      <td>7342649945759</td>
    </tr>
    <tr>
      <th>2390</th>
      <td>Hernandezshire</td>
      <td>10</td>
      <td>Rural</td>
      <td>2016-03-05 10:40:16</td>
      <td>$23.35</td>
      <td>7443355895137</td>
    </tr>
    <tr>
      <th>2391</th>
      <td>Hernandezshire</td>
      <td>10</td>
      <td>Rural</td>
      <td>2016-04-11 04:44:50</td>
      <td>$10.41</td>
      <td>9823290002445</td>
    </tr>
    <tr>
      <th>2392</th>
      <td>Hernandezshire</td>
      <td>10</td>
      <td>Rural</td>
      <td>2016-06-26 11:16:28</td>
      <td>$26.29</td>
      <td>304182959218</td>
    </tr>
    <tr>
      <th>2393</th>
      <td>Hernandezshire</td>
      <td>10</td>
      <td>Rural</td>
      <td>2016-11-25 20:34:14</td>
      <td>$38.45</td>
      <td>2898512024847</td>
    </tr>
    <tr>
      <th>2394</th>
      <td>Hernandezshire</td>
      <td>10</td>
      <td>Rural</td>
      <td>2016-11-20 17:32:37</td>
      <td>$26.79</td>
      <td>3095402154397</td>
    </tr>
    <tr>
      <th>2395</th>
      <td>Hernandezshire</td>
      <td>10</td>
      <td>Rural</td>
      <td>2016-02-24 17:30:44</td>
      <td>$44.68</td>
      <td>6389115653382</td>
    </tr>
    <tr>
      <th>2396</th>
      <td>Horneland</td>
      <td>8</td>
      <td>Rural</td>
      <td>2016-07-19 10:07:33</td>
      <td>$12.63</td>
      <td>8214498891817</td>
    </tr>
    <tr>
      <th>2397</th>
      <td>Horneland</td>
      <td>8</td>
      <td>Rural</td>
      <td>2016-03-22 21:22:20</td>
      <td>$31.53</td>
      <td>1797785685674</td>
    </tr>
    <tr>
      <th>2398</th>
      <td>Horneland</td>
      <td>8</td>
      <td>Rural</td>
      <td>2016-01-26 09:38:17</td>
      <td>$21.73</td>
      <td>5665544449606</td>
    </tr>
    <tr>
      <th>2399</th>
      <td>Horneland</td>
      <td>8</td>
      <td>Rural</td>
      <td>2016-03-25 02:05:42</td>
      <td>$20.04</td>
      <td>5729327140644</td>
    </tr>
    <tr>
      <th>2400</th>
      <td>West Kevintown</td>
      <td>5</td>
      <td>Rural</td>
      <td>2016-11-27 20:12:58</td>
      <td>$12.92</td>
      <td>6460741616450</td>
    </tr>
    <tr>
      <th>2401</th>
      <td>West Kevintown</td>
      <td>5</td>
      <td>Rural</td>
      <td>2016-02-19 01:42:58</td>
      <td>$11.15</td>
      <td>8622534016726</td>
    </tr>
    <tr>
      <th>2402</th>
      <td>West Kevintown</td>
      <td>5</td>
      <td>Rural</td>
      <td>2016-03-11 09:03:43</td>
      <td>$42.13</td>
      <td>4568909568268</td>
    </tr>
    <tr>
      <th>2403</th>
      <td>West Kevintown</td>
      <td>5</td>
      <td>Rural</td>
      <td>2016-06-25 08:04:12</td>
      <td>$24.53</td>
      <td>8188407925972</td>
    </tr>
    <tr>
      <th>2404</th>
      <td>West Kevintown</td>
      <td>5</td>
      <td>Rural</td>
      <td>2016-07-24 13:41:23</td>
      <td>$11.78</td>
      <td>2001192693573</td>
    </tr>
    <tr>
      <th>2405</th>
      <td>West Kevintown</td>
      <td>5</td>
      <td>Rural</td>
      <td>2016-06-15 19:53:16</td>
      <td>$13.50</td>
      <td>9577921579881</td>
    </tr>
    <tr>
      <th>2406</th>
      <td>West Kevintown</td>
      <td>5</td>
      <td>Rural</td>
      <td>2016-02-10 00:50:04</td>
      <td>$34.69</td>
      <td>9595491362610</td>
    </tr>
  </tbody>
</table>
<p>2407 rows × 6 columns</p>
</div>




```python
#Finding 4 key variables

#Average Fare per City (in dollars)

city_type = travel_data.groupby(["city","type"]).mean()
del city_type["ride_id"]
city_type.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>driver_count</th>
      <th>fare</th>
    </tr>
    <tr>
      <th>city</th>
      <th>type</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alvarezhaven</th>
      <th>Urban</th>
      <td>$21.00</td>
      <td>$23.93</td>
    </tr>
    <tr>
      <th>Alyssaberg</th>
      <th>Urban</th>
      <td>$67.00</td>
      <td>$20.61</td>
    </tr>
    <tr>
      <th>Anitamouth</th>
      <th>Suburban</th>
      <td>$16.00</td>
      <td>$37.32</td>
    </tr>
    <tr>
      <th>Antoniomouth</th>
      <th>Urban</th>
      <td>$21.00</td>
      <td>$23.62</td>
    </tr>
    <tr>
      <th>Aprilchester</th>
      <th>Urban</th>
      <td>$49.00</td>
      <td>$21.98</td>
    </tr>
  </tbody>
</table>
</div>




```python
driver_count=travel_data.groupby(['city']).count()
del driver_count["type"]
del driver_count["date"]
del driver_count["fare"]
del driver_count["ride_id"]
driver_count.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>driver_count</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alvarezhaven</th>
      <td>31</td>
    </tr>
    <tr>
      <th>Alyssaberg</th>
      <td>26</td>
    </tr>
    <tr>
      <th>Anitamouth</th>
      <td>9</td>
    </tr>
    <tr>
      <th>Antoniomouth</th>
      <td>22</td>
    </tr>
    <tr>
      <th>Aprilchester</th>
      <td>19</td>
    </tr>
  </tbody>
</table>
</div>




```python
test = city_type.plot.scatter(x =driver_count["driver_count"], y='not_sure',s=driver_count["driver_count"]);
plt.show()
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    ~/anaconda3/lib/python3.6/site-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
       2441             try:
    -> 2442                 return self._engine.get_loc(key)
       2443             except KeyError:


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()


    KeyError: 'lets_see'

    
    During handling of the above exception, another exception occurred:


    KeyError                                  Traceback (most recent call last)

    <ipython-input-215-37a3d5266e3b> in <module>()
    ----> 1 test = city_type.plot.scatter(x = 'lets_see', y='not_sure',s=city_type['driver_count']);
          2 plt.show()


    ~/anaconda3/lib/python3.6/site-packages/pandas/plotting/_core.py in scatter(self, x, y, s, c, **kwds)
       2803         axes : matplotlib.AxesSubplot or np.array of them
       2804         """
    -> 2805         return self(kind='scatter', x=x, y=y, c=c, s=s, **kwds)
       2806 
       2807     def hexbin(self, x, y, C=None, reduce_C_function=None, gridsize=None,


    ~/anaconda3/lib/python3.6/site-packages/pandas/plotting/_core.py in __call__(self, x, y, kind, ax, subplots, sharex, sharey, layout, figsize, use_index, title, grid, legend, style, logx, logy, loglog, xticks, yticks, xlim, ylim, rot, fontsize, colormap, table, yerr, xerr, secondary_y, sort_columns, **kwds)
       2625                           fontsize=fontsize, colormap=colormap, table=table,
       2626                           yerr=yerr, xerr=xerr, secondary_y=secondary_y,
    -> 2627                           sort_columns=sort_columns, **kwds)
       2628     __call__.__doc__ = plot_frame.__doc__
       2629 


    ~/anaconda3/lib/python3.6/site-packages/pandas/plotting/_core.py in plot_frame(data, x, y, kind, ax, subplots, sharex, sharey, layout, figsize, use_index, title, grid, legend, style, logx, logy, loglog, xticks, yticks, xlim, ylim, rot, fontsize, colormap, table, yerr, xerr, secondary_y, sort_columns, **kwds)
       1867                  yerr=yerr, xerr=xerr,
       1868                  secondary_y=secondary_y, sort_columns=sort_columns,
    -> 1869                  **kwds)
       1870 
       1871 


    ~/anaconda3/lib/python3.6/site-packages/pandas/plotting/_core.py in _plot(data, x, y, subplots, ax, kind, **kwds)
       1650         if isinstance(data, DataFrame):
       1651             plot_obj = klass(data, x=x, y=y, subplots=subplots, ax=ax,
    -> 1652                              kind=kind, **kwds)
       1653         else:
       1654             raise ValueError("plot kind %r can only be used for data frames"


    ~/anaconda3/lib/python3.6/site-packages/pandas/plotting/_core.py in __init__(self, data, x, y, s, c, **kwargs)
        808             # the handling of this argument later
        809             s = 20
    --> 810         super(ScatterPlot, self).__init__(data, x, y, s=s, **kwargs)
        811         if is_integer(c) and not self.data.columns.holds_integer():
        812             c = self.data.columns[c]


    ~/anaconda3/lib/python3.6/site-packages/pandas/plotting/_core.py in __init__(self, data, x, y, **kwargs)
        782         if is_integer(y) and not self.data.columns.holds_integer():
        783             y = self.data.columns[y]
    --> 784         if len(self.data[x]._get_numeric_data()) == 0:
        785             raise ValueError(self._kind + ' requires x column to be numeric')
        786         if len(self.data[y]._get_numeric_data()) == 0:


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/frame.py in __getitem__(self, key)
       1962             return self._getitem_multilevel(key)
       1963         else:
    -> 1964             return self._getitem_column(key)
       1965 
       1966     def _getitem_column(self, key):


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/frame.py in _getitem_column(self, key)
       1969         # get column
       1970         if self.columns.is_unique:
    -> 1971             return self._get_item_cache(key)
       1972 
       1973         # duplicate columns & possible reduce dimensionality


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/generic.py in _get_item_cache(self, item)
       1643         res = cache.get(item)
       1644         if res is None:
    -> 1645             values = self._data.get(item)
       1646             res = self._box_item_values(item, values)
       1647             cache[item] = res


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/internals.py in get(self, item, fastpath)
       3588 
       3589             if not isnull(item):
    -> 3590                 loc = self.items.get_loc(item)
       3591             else:
       3592                 indexer = np.arange(len(self.items))[isnull(self.items)]


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
       2442                 return self._engine.get_loc(key)
       2443             except KeyError:
    -> 2444                 return self._engine.get_loc(self._maybe_cast_indexer(key))
       2445 
       2446         indexer = self.get_indexer([key], method=method, tolerance=tolerance)


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()


    KeyError: 'lets_see'



```python
#FINDING NUMBER OF RIDES Per City 

# num_rides = travel_data.groupby("city").count()
# num_rides.head()
num_rides = travel_data.groupby(['city',"fare"]).sum()
num_rides = pd.DataFrame(num_rides)

num_rides #this is showing us each ride, their fair, and TOTAL driver(?) count PER city....


# WAIT TO FIND TOTAL NUMBER OF RIDES PER CITY GROUP THE RIDE IDs BY CITY!?

ridesPerCity = travel_data.groupby(['city','ride_id']).sum()
ridesPerCity

hm = travel_data.groupby(['city','ride_id'], as_index=False)['type'].sum()
hm

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>ride_id</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alvarezhaven</td>
      <td>306054352684</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alvarezhaven</td>
      <td>357421158941</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Alvarezhaven</td>
      <td>858631473935</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alvarezhaven</td>
      <td>1108172306544</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alvarezhaven</td>
      <td>1197329964911</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Alvarezhaven</td>
      <td>1806812593131</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Alvarezhaven</td>
      <td>2233026076010</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Alvarezhaven</td>
      <td>2747592323442</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Alvarezhaven</td>
      <td>3565582370530</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Alvarezhaven</td>
      <td>3829336915201</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Alvarezhaven</td>
      <td>3938173695105</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Alvarezhaven</td>
      <td>4267015736324</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Alvarezhaven</td>
      <td>4348900295000</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Alvarezhaven</td>
      <td>5405756761666</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Alvarezhaven</td>
      <td>5487020911007</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Alvarezhaven</td>
      <td>6100187302721</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Alvarezhaven</td>
      <td>6152998520191</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Alvarezhaven</td>
      <td>6282665852239</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Alvarezhaven</td>
      <td>6431434271355</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Alvarezhaven</td>
      <td>6435260355302</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Alvarezhaven</td>
      <td>7413831046469</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Alvarezhaven</td>
      <td>7825539032352</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Alvarezhaven</td>
      <td>7852567608457</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Alvarezhaven</td>
      <td>7948246793429</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Alvarezhaven</td>
      <td>8307812366044</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Alvarezhaven</td>
      <td>8394540350728</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Alvarezhaven</td>
      <td>8878745717970</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Alvarezhaven</td>
      <td>8939751998750</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Alvarezhaven</td>
      <td>8974645194719</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Alvarezhaven</td>
      <td>9047320468692</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2345</th>
      <td>Yolandafurt</td>
      <td>7824370473607</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2346</th>
      <td>Yolandafurt</td>
      <td>7996695327849</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2347</th>
      <td>Yolandafurt</td>
      <td>9030131895269</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2348</th>
      <td>Yolandafurt</td>
      <td>9104387314550</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2349</th>
      <td>Yolandafurt</td>
      <td>9314685389826</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2350</th>
      <td>Yolandafurt</td>
      <td>9895622307900</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2351</th>
      <td>Zimmermanmouth</td>
      <td>388096159087</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2352</th>
      <td>Zimmermanmouth</td>
      <td>589257725947</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2353</th>
      <td>Zimmermanmouth</td>
      <td>885932877834</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2354</th>
      <td>Zimmermanmouth</td>
      <td>1214603530980</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2355</th>
      <td>Zimmermanmouth</td>
      <td>1529363655249</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2356</th>
      <td>Zimmermanmouth</td>
      <td>1942308210837</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2357</th>
      <td>Zimmermanmouth</td>
      <td>2258161061820</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2358</th>
      <td>Zimmermanmouth</td>
      <td>2326214075695</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2359</th>
      <td>Zimmermanmouth</td>
      <td>2489772698062</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2360</th>
      <td>Zimmermanmouth</td>
      <td>3364398658418</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2361</th>
      <td>Zimmermanmouth</td>
      <td>3806179410575</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2362</th>
      <td>Zimmermanmouth</td>
      <td>4966546004949</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2363</th>
      <td>Zimmermanmouth</td>
      <td>5202604424953</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2364</th>
      <td>Zimmermanmouth</td>
      <td>5672693632216</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2365</th>
      <td>Zimmermanmouth</td>
      <td>5690108755824</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2366</th>
      <td>Zimmermanmouth</td>
      <td>6060050374869</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2367</th>
      <td>Zimmermanmouth</td>
      <td>6490497681785</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2368</th>
      <td>Zimmermanmouth</td>
      <td>7176327056501</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2369</th>
      <td>Zimmermanmouth</td>
      <td>7276044030126</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2370</th>
      <td>Zimmermanmouth</td>
      <td>7488861145000</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2371</th>
      <td>Zimmermanmouth</td>
      <td>7547394650211</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2372</th>
      <td>Zimmermanmouth</td>
      <td>7886293230125</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2373</th>
      <td>Zimmermanmouth</td>
      <td>9089069809060</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2374</th>
      <td>Zimmermanmouth</td>
      <td>9508846094814</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
<p>2375 rows × 3 columns</p>
</div>




```python
#total number of drivers per city 
# num_drivers=city_df[["type","driver_count"]]
# num_drivers.head()
num_drivers = city_df.groupby(["type"]).count()
num_drivers

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>driver_count</th>
    </tr>
    <tr>
      <th>type</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rural</th>
      <td>18</td>
      <td>18</td>
    </tr>
    <tr>
      <th>Suburban</th>
      <td>42</td>
      <td>42</td>
    </tr>
    <tr>
      <th>Urban</th>
      <td>66</td>
      <td>66</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-210-c81df567897a> in <module>()
    ----> 1 djskfjksdf
    

    NameError: name 'djskfjksdf' is not defined



```python
#Creating variable that captures city and city type so that we can graph by each "type" of city
city_type=city_df.groupby(["city","type"]).count()
city_type.head()


city_type_count = city_df.groupby(["type"]).count()
city_type_count.head()
del city_type_count["driver_count"]
city_type_count.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
    </tr>
    <tr>
      <th>type</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rural</th>
      <td>18</td>
    </tr>
    <tr>
      <th>Suburban</th>
      <td>42</td>
    </tr>
    <tr>
      <th>Urban</th>
      <td>66</td>
    </tr>
  </tbody>
</table>
</div>


