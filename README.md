

```python
#OBSERVED TRENDS
#1.After sorting the data for the gender with most purchases, we see that Males make up ~61% of these sales. 
#2.Filtering by age group to find highest purchases, we can see that those between 20-24 years are the most active in buying games. It could be safe to assume that the most popular and active gaming group is that of males btween the ages of 20-24. It would have been interesting to see the gender and age group breakdown if we have game genre accessible. Are these male audiences more inclined to purchase action games or role-playing?
#3. Assuming that my code is correct, it is rather interesting to see that the top 5 Most Popular Items were also the top 5 Most Profitable. This can tell us that the most profitable games knew their target audiences really well and were able to deliver in the most effective way possible
```


```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
```


```python
file1= pd.read_json('../Data_Analytics_Assignments/pandas_homework/input_files/purchase_data.json')
file2 = pd.read_json('../Data_Analytics_Assignments/pandas_homework/input_files/purchase_data2.json')
```


```python
file1.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
file2.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>Male</td>
      <td>93</td>
      <td>Apocalyptic Battlescythe</td>
      <td>4.49</td>
      <td>Iloni35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>12</td>
      <td>Dawne</td>
      <td>3.36</td>
      <td>Aidaira26</td>
    </tr>
    <tr>
      <th>2</th>
      <td>17</td>
      <td>Male</td>
      <td>5</td>
      <td>Putrid Fan</td>
      <td>2.63</td>
      <td>Irim47</td>
    </tr>
    <tr>
      <th>3</th>
      <td>17</td>
      <td>Male</td>
      <td>123</td>
      <td>Twilight's Carver</td>
      <td>2.55</td>
      <td>Irith83</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22</td>
      <td>Male</td>
      <td>154</td>
      <td>Feral Katana</td>
      <td>4.11</td>
      <td>Philodil43</td>
    </tr>
  </tbody>
</table>
</div>




```python
#lets merge the data 
purchase_df = pd.merge(file1,file2, how='outer',on=['Age','Gender','Item ID','Item Name','Price','SN'])
purchase_df.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Total Number of players
_total_players = purchase_df['SN'].nunique()
totalPlayers = pd.DataFrame({"Total Players" : [_total_players]})
totalPlayers
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
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>612</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Finding unique number of items


#this creates a variable that shows all the unique Item Names
items = purchase_df.groupby(by='Item Name').describe()
#items
#This variable will give us the count of the total unique items 
uniqueCountofItems=len(items)
#this will create a dataframe of the unique count
uniqueItems = pd.DataFrame({"Unique Count of Items": [uniqueCountofItems]})
uniqueItems

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
      <th>Unique Count of Items</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>180</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Finding Average Purchase Price
#purchase_df.round({"Price":2})

avg_price = purchase_df["Price"].mean()
avg_price = round(avg_price, 2)
avg_price
avgPrice=pd.DataFrame({"Average Price": [avg_price]})
avgPrice


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
      <th>Average Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.93</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Finding unique counts of purchases
tp = purchase_df.groupby(by='SN').describe()
total_purchases = len(tp)
totalPurchases = pd.DataFrame({"Number of Purchases": [total_purchases]})
totalPurchases
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
      <th>Number of Purchases</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>612</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Finding Total Revenue 

total_revenue = purchase_df['Price'].sum()
total_revenue = round(total_revenue, 2)
totalRevenue = pd.DataFrame({"Total Revenue" : [total_revenue]})
totalRevenue
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
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2514.43</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Now combing relevant information into one dataframe!

purchasingStats = pd.DataFrame({
        "Number of Unique Items" : [uniqueCountofItems],
        "Average Price per Item": [avg_price],
        "Number of Purchases": [total_purchases],
        "Total Revenue":[total_revenue]
    
    })
purchasingStats
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
      <th>Average Price per Item</th>
      <th>Number of Purchases</th>
      <th>Number of Unique Items</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.93</td>
      <td>612</td>
      <td>180</td>
      <td>2514.43</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Finding percentage and count of all players


gender_counts= list(purchase_df['Gender'].value_counts())
gender_counts
# #creating a dataframe that will show us the breakdown by gender
gender_df = pd.DataFrame({"Genders" : ['Men','Women','Other'], 
                          "Player Counts": gender_counts, 
                          })

gender_df



#This will provide us a list of counts per captured gender
# gender_counts= list(purchase_df['Gender'].value_counts())
# gender_counts


malecount= gender_df.iloc[0,1]
malecount

femalecount=gender_df.iloc[1,1]
femalecount

othercount=gender_df.iloc[2,1]
othercount

totalgender= malecount + femalecount + othercount
totalgender

malepercent = ((malecount/totalgender)*100)
malepercent = round(malepercent,2)
malepercent

femalepercent = float((femalecount/totalgender)*100)
femalepercent = round(femalepercent,2)
femalepercent

otherpercent = float((othercount/totalgender)*100)
otherpercent = round(otherpercent,2)
otherpercent




#creating a dataframe that will show us the breakdown by gender
gender_df = pd.DataFrame({"Genders" : ['Men','Women','Other'], 
                           "Player Counts": gender_counts, 
                          "Percentage of Players":[malepercent, femalepercent,otherpercent]})

gender_df
# male = gender_df["Genders"].pd.DataFrame
# male


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
      <th>Genders</th>
      <th>Percentage of Players</th>
      <th>Player Counts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Men</td>
      <td>81.24</td>
      <td>697</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Women</td>
      <td>17.37</td>
      <td>149</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Other</td>
      <td>1.40</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
#The below each broken by gender
# Purchase Count
# Average Purchase Price
# Total Purchase Value
# Normalized Totals


purchasecount_female= len(purchase_df[purchase_df['Gender'] == "Female"].groupby(by='SN'))
purchasecount_male= len(purchase_df[purchase_df['Gender'] == "Male"].groupby(by='SN'))
purchasecount_other = len(purchase_df[purchase_df['Gender'].str.contains("^other",case=False)].groupby(by='SN'))


femgroupby = purchase_df.groupby(purchase_df['Gender']=="Female")['Price']

femprice=purchase_df[purchase_df['Gender']=="Female"].groupby(['Gender']).mean()
femprice =femprice["Price"].unique()
femprice = round(float(femprice[0]),2)
femprice=round(femprice,2)
femprice  

malegroupby = purchase_df.groupby(purchase_df['Gender']=="Male")['Price']

maleprice=purchase_df[purchase_df['Gender']=="Male"].groupby(['Gender']).mean()
maleprice=maleprice["Price"].unique()
maleprice=round(float(maleprice[0]),2)
maleprice=round(maleprice,2)
maleprice


othergroupby = purchase_df.groupby(purchase_df['Gender'].str.contains("^other",case=False))['Price']
otherprice = purchase_df[purchase_df['Gender'].str.contains("^other",case=False)].groupby(['Gender']).mean()
otherprice = otherprice["Price"].unique()
otherprice = round(float(otherprice[0]),2)
otherprice

maletotalprice=purchase_df[purchase_df['Gender']=="Male"].groupby(['Gender']).sum()
maletotalprice = maletotalprice['Price'].unique()
maletotalprice = round(float(maletotalprice[0]),2)
maletotalprice

femaletotalprice=purchase_df[purchase_df['Gender']=="Female"].groupby(['Gender']).sum()
femaletotalprice = femaletotalprice['Price'].unique()
femaletotalprice = round(float(femaletotalprice[0]),2)
femaletotalprice

othertotalprice=purchase_df[purchase_df['Gender'].str.contains("^other",case=False)].groupby(['Gender']).sum()
othertotalprice = othertotalprice['Price'].unique()
othertotalprice = round(float(othertotalprice[0]),2)
othertotalprice

malenormtotal=purchase_df[purchase_df['Gender']=="Male"].groupby(['Gender']).count()
malenormtotal=malenormtotal["Price"].unique()
malenormtotal = maletotalprice/malenormtotal
malenormtotal = round(float(malenormtotal[0]),2)
malenormtotal

femalenormtotal=purchase_df[purchase_df['Gender']=="Female"].groupby(['Gender']).count()
femalenormtotal
femalenormtotal=femalenormtotal["Price"].unique()
femalenormtotal = femaletotalprice/femalenormtotal
femalenormtotal = round(float(femalenormtotal[0]),2)
femalenormtotal

othernormtotal=purchase_df[purchase_df['Gender'].str.contains("^other",case=False)].groupby(['Gender']).count()
othernormtotal=othernormtotal["Price"].unique()
othernormtotal = othertotalprice/othernormtotal
othernormtotal = round(float(othernormtotal[0]),2)
othernormtotal
            
            

purchasecount_df = pd.DataFrame({"Gender":['Female',"Male","Other"],
                                 "Unique Purchases Made": [purchasecount_female, purchasecount_male, purchasecount_other],
                                "Average Purchase Cost": [femprice, maleprice, otherprice],
                                 "Total Purchase Value":[femaletotalprice,maletotalprice,othertotalprice],
                               "Normalized Totals":[femalenormtotal,malenormtotal,othernormtotal]}                              
                             )

purchasecount_df.set_index("Gender", inplace=True)
purchasecount_df

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
      <th>Average Purchase Cost</th>
      <th>Normalized Totals</th>
      <th>Total Purchase Value</th>
      <th>Unique Purchases Made</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>2.85</td>
      <td>2.85</td>
      <td>424.29</td>
      <td>112</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>2.94</td>
      <td>2.94</td>
      <td>2052.28</td>
      <td>498</td>
    </tr>
    <tr>
      <th>Other</th>
      <td>3.15</td>
      <td>3.15</td>
      <td>37.86</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Age Demographics
purchase_df.head()

age_df = pd.DataFrame(purchase_df[['Age','Item ID','Price','SN']])
age_df

age_below10 = age_df['Age'][age_df['Age'] <10 ].count()
age10_14 = age_df["Age"][(age_df['Age'] >= 10) & (age_df['Age'] <= 14)].count()
age15_19= age_df["Age"][(age_df['Age'] >= 15) & (age_df['Age'] <= 19)].count()
age20_24=age_df["Age"][(age_df['Age'] >= 20) & (age_df['Age'] <= 24)].count()
age25_29=age_df["Age"][(age_df['Age'] >= 25) & (age_df['Age'] <= 29)].count()
age30_34=age_df["Age"][(age_df['Age'] >= 30) & (age_df['Age'] <= 34)].count()
age35_39=age_df["Age"][(age_df['Age'] >= 35) & (age_df['Age'] <= 39)].count()
age_40up=age_df["Age"][(age_df['Age'] >=40)].count()


perage_below10= round(((age_below10/_total_players)*100),2)
perage10_14= round(((age10_14/_total_players)*100),2)
perage15_19= round(((age15_19/_total_players)*100),2)
perage20_24=round(((age20_24/_total_players)*100),2)
perage25_29=round(((age25_29/_total_players)*100),2)
perage30_34=round(((age30_34/_total_players)*100),2)
perage35_39=round(((age35_39/_total_players)*100),2)
perage_40up=(round(((age_40up/_total_players)*100),2))

age_demographics=pd.DataFrame({"Percentage of Players":[perage_below10,perage10_14,perage15_19,perage20_24,perage25_29,perage30_34,perage35_39,perage_40up],
                               "Total Count":[age_below10,age10_14,age15_19,age20_24,age25_29,age30_34,age35_39,age_40up],
                              "Age Buckets":['<10','10-14','15-19','20-24','25-29','30-34','35-39','40+']})




age_demographics.set_index("Age Buckets", inplace=True)
age_demographics

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
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Age Buckets</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>5.39</td>
      <td>33</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>6.21</td>
      <td>38</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>23.53</td>
      <td>144</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>60.78</td>
      <td>372</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>21.90</td>
      <td>134</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>11.60</td>
      <td>71</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>7.84</td>
      <td>48</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>2.94</td>
      <td>18</td>
    </tr>
  </tbody>
</table>
</div>




```python
#purchasing analysis

# avgbelow10=age_df[age_demographics['Gender']=="Female"].groupby(['Gender']).mean()
# # femprice =femprice["Price"].unique()
# # femprice = round(float(femprice[0]),2)
# # femprice=round(femprice,2)
# # femprice 

#purch_analysis=pd.DataFrame({"Purchase Count":[age_below10,age10_14,age15_19,age20_24,age25_29,age30_34,age35_39,age_40up],
#                             "Average Purchase Price": })


   
#purchase_df[purchase_df['Gender']=="Male"].groupby(['Gender']).mean()
```


```python
#Top Spenders

ts_df = pd.DataFrame(purchase_df[['SN','Gender','Price']])
ts_df['Purchase Count'] = ts_df.groupby('SN')['SN'].transform('count')
ts_df['Total Purchase Value'] = ts_df['Price'] * ts_df['Purchase Count']
ts_df['Average Purchase Value'] = ts_df['Total Purchase Value'] / ts_df['Purchase Count']
ts_df.set_index(["SN"], inplace=True)
ts_df= ts_df.reset_index().groupby("SN").sum()
ts_df = ts_df.sort_values('Purchase Count',ascending = False)
ts_df.head()
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
      <th>Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
      <th>Average Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>17.06</td>
      <td>25</td>
      <td>85.30</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>12.74</td>
      <td>16</td>
      <td>50.96</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>Aerithllora36</th>
      <td>15.10</td>
      <td>16</td>
      <td>60.40</td>
      <td>15.10</td>
    </tr>
    <tr>
      <th>Qarwen67</th>
      <td>9.97</td>
      <td>16</td>
      <td>39.88</td>
      <td>9.97</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>13.56</td>
      <td>16</td>
      <td>54.24</td>
      <td>13.56</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most Popular Items

popItems = pd.DataFrame(purchase_df[['Item ID','Item Name','Price']])
popItems['Purchase Count'] = popItems.groupby('Item Name')['Item Name'].transform('count')
popItems['Total Purchase Value']= popItems["Price"] * popItems["Purchase Count"]
popItems = popItems.sort_values('Purchase Count',ascending = False)
popItems.set_index(["Item ID","Item Name"], inplace=True)
pop = popItems.reset_index().groupby("Item Name").sum()
pop = pop.sort_values('Purchase Count',ascending = False)
pop.head()

##This piece of code summed up the *actual* Item IDs!! I couldn't figure out how to undo this without undoing all the other sums!! :( 











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
      <th>Item ID</th>
      <th>Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Final Critic</th>
      <td>1342</td>
      <td>38.60</td>
      <td>196</td>
      <td>540.40</td>
    </tr>
    <tr>
      <th>Arcane Gem</th>
      <td>1008</td>
      <td>29.34</td>
      <td>144</td>
      <td>352.08</td>
    </tr>
    <tr>
      <th>Stormcaller</th>
      <td>1410</td>
      <td>40.19</td>
      <td>144</td>
      <td>482.28</td>
    </tr>
    <tr>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>429</td>
      <td>25.85</td>
      <td>121</td>
      <td>284.35</td>
    </tr>
    <tr>
      <th>Trickster</th>
      <td>310</td>
      <td>23.22</td>
      <td>100</td>
      <td>232.20</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most Profitable
profItems = pd.DataFrame(purchase_df[['Item ID','Item Name','Price']])
profItems['Purchase Count'] = profItems.groupby('Item Name')['Item Name'].transform('count')
profItems['Total Purchase Value']= profItems["Price"] * profItems["Purchase Count"]

profItems.set_index(["Item ID","Item Name"], inplace=True)
prof = profItems.reset_index().groupby("Item Name").sum()
prof = prof.sort_values('Total Purchase Value',ascending = False)
prof.head()

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
      <th>Item ID</th>
      <th>Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Final Critic</th>
      <td>1342</td>
      <td>38.60</td>
      <td>196</td>
      <td>540.40</td>
    </tr>
    <tr>
      <th>Stormcaller</th>
      <td>1410</td>
      <td>40.19</td>
      <td>144</td>
      <td>482.28</td>
    </tr>
    <tr>
      <th>Arcane Gem</th>
      <td>1008</td>
      <td>29.34</td>
      <td>144</td>
      <td>352.08</td>
    </tr>
    <tr>
      <th>Retribution Axe</th>
      <td>306</td>
      <td>37.26</td>
      <td>81</td>
      <td>335.34</td>
    </tr>
    <tr>
      <th>Splitter, Foe Of Subtlety</th>
      <td>963</td>
      <td>33.03</td>
      <td>81</td>
      <td>297.27</td>
    </tr>
  </tbody>
</table>
</div>




```python


```
