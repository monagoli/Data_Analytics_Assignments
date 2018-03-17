

```python
##NUPUR'S CODE##

# Dependencies
import requests as req
import numpy as np
import json
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
import seaborn as sns

##### MAP GEOCODES (FIPS) TO STATES/COUNTIES #####
# Create function to make Geocode Data into DataFrame
def makeGeocodeDF(pdExel,sumLevel,fipsCol1,colName,fipsCol2=0):
    # Create DF out of excel
    df = pdExel.loc[pdExel['Summary Level'] == sumLevel]

    # If the summary level is 'county'
    if sumLevel == 50:
        # Add both fips code levels
        df = df[[fipsCol1,fipsCol2,'Area Name (including legal/statistical area description)']]
    else:
        # only add one fips code level
        df = df[[fipsCol1,'Area Name (including legal/statistical area description)']]

    # Rename columns
    df = df.rename(columns={'Area Name (including legal/statistical area description)' : colName})

    # Return DataFrame
    return df

# Read excel file of geo codes
geocodeMap = pd.read_excel('resources/2015-allgeocodes.xlsx', sheetname='Sheet1')

# Create DataFrame of States/State FIPS
geocodeMapState = makeGeocodeDF(geocodeMap,40,'State Code (FIPS)','State')
# Create DataFrame of County Names/County FIPS/State FIPS/
geocodeMapCounty = makeGeocodeDF(geocodeMap,50,'County Code (FIPS)','County','State Code (FIPS)')
# Create DataFrame of States and Abbreviations
abbrMap = pd.read_excel('../Workspace/resources/stateAbbreviation.xlsx')

# Create merged DataFrame with County and State FIPS and Names
geocodeMap = pd.merge(geocodeMapState,geocodeMapCounty, how='outer', on='State Code (FIPS)')

#/ Variables/DFs to use:
    #/ For state/county mapping: geocodeMap
    #/ remember to merge on BOTH State and County (county FIPs repeat)

##### CENSUS DATA #####
#/// SETUP 'GET' Variables \\\#
# Function to dynamically create variable ID lists
def createIdList(r1,r2,s,avoid=[]): #range start, range stop, id string, avoid ids (optional)

    i = [] # List variable

    # For all variables in the range
    for x in range(r1,r2):

        # If there are variables to avoid, pass
        if x in avoid:
            pass

        # If id is greater than 9
        elif x > 9:
            i.append(s+str(x)+'E')

        # Add a leading zero for IDs below 10
        else:
            i.append(s+'0'+str(x)+'E')

    # Return list
    return i

# Function to create a dictionary of IDs and their string
def createIdDict(k,v):

    n = 0 #counter
    d = {} #dictionary

    # For each ID in list
    for x in k:

        # Add it as a key and add appropriate bucket as value
        d[x] = v[n%len(v)] #use remainder to determine bucket (if it loops)
        n += 1 # Increase counter

    # Rename state/county to match geomap
    d['state'] = 'State Code (FIPS)'
    d['county'] = 'County Code (FIPS)'

    # Return Dictionary
    return d

# HOUSEHOLD INCOME: Create List and Dictionary
householdIncomeIdList = createIdList(2,18,'B19001_0')
householdIncomeBuckets = ['< $10k',
                          '$10K - $14,999',
                          '$15K - $19,999',
                          '$20K - $24,999',
                          '$25K - $29,999',
                          '$30K - $34,999',
                          '$35K - $39,999',
                          '$40K - $44,999',
                          '$45K - $49,999',
                          '$50K - $59,999',
                          '$60K - $74,999',
                          '$75K - $99,999',
                          '$100K - $124,999',
                          '$125K - $149,999',
                          '$150K - $199,999',
                          '$200K +']
householdIncomeDict = createIdDict(householdIncomeIdList,householdIncomeBuckets)

# EDUCATIONAL ATTAINMENT: Create List and Dictionary
notInclude = [1,2,3,11,19,27,35,43,44,52,60,68,76] #id's not to include in list
educationIdList = createIdList(1,84,'B15001_0',notInclude)
educationAttainmentBuckets = ['Less than 9th grade',
                              '9th to 12th grade, no diploma',
                              'High school graduate',
                              'Some college, no degree',
                              'Associate\'s degree',
                              'Bachelor\'s degree',
                              'Graduate or professional degree']
educationDict = createIdDict(educationIdList,educationAttainmentBuckets)
# Split education list in 2 because of 50 variable arg max
educationIdList1 = educationIdList[:int(len(educationIdList)/2)]
educationIdList2 = educationIdList[int(len(educationIdList)/2):]

# POPULATION: Create Dictionary
populationDict = createIdDict(['B01001_001E'],['Population'])

# Create string of ID's to query
idLists = [householdIncomeIdList,educationIdList1,educationIdList2] # List of lists
getArgs = []

# Create list of get arguments (all id's)
for l in idLists:

    getIds = '' #string

    # For all IDs in the list
    for i in l:

        getIds = getIds + i + ',' #add ID to final string

    getIds = getIds[:-1] #remove last comma
    getArgs.append(getIds) #add to ID list

# Append population to get args
getArgs.append((list(populationDict.keys()))[0])

#/// Setup Query URL \\\#
# Variables
year = 2016
apiKey = 'a9bba28cbc522f8f9d8ae3b88ef030fba6034516'
baseURL = 'https://api.census.gov/data/{}/acs/acs1/'.format(year)
forArgs = 'county:*'

# Create list of URLs to query
urlList = [] #empty list
for x in getArgs:
    URLArgs = '?get={}&for={}&key={}'.format(x,forArgs,apiKey)
    queryURL = baseURL + URLArgs
    urlList.append(queryURL)


#/// Create Dataframes \\\#
# Create function
def makeDataFrame(url,labelDict):

    #Get response data from API
    response = req.get(url)
    jsonData = response.json() #create json

    # Create data frame from json
    df = pd.DataFrame(jsonData, columns=jsonData[0]) #rename headers with first row values
    df = df.rename(columns=labelDict) #rename columnns using associated dictionary
    df = df.drop(df.index[0]) #remove first row

    # Remove leading zeros from state and county
    df['State Code (FIPS)'] = df['State Code (FIPS)'].str.lstrip('0')
    df['County Code (FIPS)'] = df['County Code (FIPS)'].str.lstrip('0')

    # Make all numbers in DF numeric
    df = df.apply(pd.to_numeric)

    return df

# Make DF using Function
incomeDF = makeDataFrame(urlList[0],householdIncomeDict)
eduDF1 = makeDataFrame(urlList[1],educationDict)
eduDF2 = makeDataFrame(urlList[2],educationDict)
populationDF = makeDataFrame(urlList[3],populationDict)

#/// Merge Education DataFrames \\\#
# Create joint DF
eduDF = pd.merge(eduDF1,eduDF2,how='outer',on=['State Code (FIPS)','County Code (FIPS)'])

# Create dictionary to remove appeneded X's and Y's on column names
removeAppend = {}
for i in educationAttainmentBuckets:
    s1 = i + '_x'
    s2 = i + '_y'
    removeAppend[s1] = i
    removeAppend[s2] = i

# Rename column headers
eduDF = eduDF.rename(columns=removeAppend)

# Sum columns with same names in DF
eduDF = eduDF.groupby(lambda x:x, axis=1).sum()

#/// Map Geocodes and add to DF \\\#
# Create function to automate
def mergeOnGeocode(df1,df2):
    try:
        return pd.merge(df1,df2,how='inner',on=['State Code (FIPS)','County Code (FIPS)'])
    except:
        return pd.merge(df1,df2,how='inner',on=['State Code (FIPS)'])


# Map census DFs to FIPS
incomeDFmapped = mergeOnGeocode(incomeDF,geocodeMap)
eduDFmapped = mergeOnGeocode(eduDF,geocodeMap)

popDFmapped = mergeOnGeocode(populationDF,geocodeMap)
popDFmapped = pd.merge(popDFmapped,abbrMap, how='inner',on=['State'])

#/ Variables/DFs to use:
    #/ To normalize data, use this DF: popDFmapped (FIPS mapped to names)
    #/ Income data DF to use: incomeDFmapped (FIPS mapped to names) or incomeDF (FIPS only)
    #/ Education data DF to use: eduDFmapped (FIPS mapped to names) or eduDF (FIPS only)

#/// Create Normalized DFs \\\*

# Create function to normalize data
def normalizeData(df1,df2,buckets):

    # Merge dicts on geocode
    df = mergeOnGeocode(df1,df2)

    # For each column, divide by the total population column
    for bucket in buckets:
        df[bucket] = df[bucket]/df['Population']

    # Drop population column
    df.drop(['Population'], axis=1, inplace=True)

    # Return df
    return df

# HOUSEHOLDS TOTAL: Create DF
var = 'B19001_001E'
householdDict = createIdDict([var],['Population']) #create dict

URLArgs = '?get={}&for={}&key={}'.format(var,forArgs,apiKey)
queryURL = baseURL + URLArgs #put together query URL

householdDF = makeDataFrame(queryURL,householdDict) #create DF

# +18 POPULATION TOTAL: Create DF
var = 'B15001_001E'
over18Dict = createIdDict([var],['Population']) #create dict

URLArgs = '?get={}&for={}&key={}'.format(var,forArgs,apiKey)
queryURL = baseURL + URLArgs #put together query URL

over18DF = makeDataFrame(queryURL,over18Dict) #create DF

# Normalize Income and Education DFs
normIncome = normalizeData(incomeDF,householdDF,householdIncomeBuckets) #normalizedIncome
normEdu = normalizeData(eduDF,over18DF,educationAttainmentBuckets) #normalizedEdu

#/// Create Normalized DFs for States \\\*

# Function to breakdown DFs by state FIPS
def breakdownByState(dfIn):
    df = dfIn.groupby(['State Code (FIPS)']).sum()
    df.drop(['County Code (FIPS)'], axis=1, inplace=True)
    df = df.reset_index()
    return df

# Function to set state as index
def setStateAsIndex(df):

    # Merge on state only
    df = mergeOnGeocode(df,geocodeMapState)
    df.drop('State Code (FIPS)', axis=1, inplace=True)
    df = df.set_index('State')
    return df

# Function to Normalize state DFs
def createStateNormDF (df1,df2,buckets):

    # Breakdown DFs by STate and Normalize
    df1n = breakdownByState(df1)
    df2n = breakdownByState(df2)
    df = normalizeData(df1n,df2n,buckets)

    # Set state as the index
    df = setStateAsIndex(df)

    return df

# Create State DF's
# Income
incomeByState = setStateAsIndex(breakdownByState(incomeDF))
incomeByState = incomeByState[householdIncomeBuckets] #reorder columns
# Education
eduByState = setStateAsIndex(breakdownByState(eduDF))
eduByState = eduByState[educationAttainmentBuckets] #reorder columns

# Create State Normalized DF's
# Income
incomeByStateNorm = createStateNormDF(incomeDF,householdDF,householdIncomeBuckets)
incomeByStateNorm = incomeByStateNorm[householdIncomeBuckets] #reorder columns
# Education
eduByStateNorm = createStateNormDF(eduDF,over18DF,educationAttainmentBuckets)
eduByStateNorm = eduByStateNorm[educationAttainmentBuckets] #reorder columns

#/// Create Bar Charts \\\*
sns.palplot(sns.hls_palette(16, l=.3, s=.8))

# Function to create bar charts
def createBarChart(df,title,x,y,lt,l,c):

    # Plot DF as bar graph
    df.plot(kind='bar',
            stacked=True,
            title=title,
            figsize=(20,10),
            fontsize=14
           )

    # Add title/labels
    plt.title(title,fontsize=18) #Create graph title
    plt.xlabel(x, fontsize=14) #Create x-axis label
    plt.ylabel(y,fontsize=14) #Create y-axis label
    plt.tick_params(axis='both', labelsize=12) #Format Axis

    # Add legend
    legend = plt.legend(loc='lower center',bbox_to_anchor=(.5, l), ncol=c, borderaxespad=0., title=lt, fontsize=12)
    legend.get_title().set_fontsize('14') #Set legend title font size

    # Show plot
    plt.show()

# Bar Chart: Household Income for All States
createBarChart(incomeByState,'Household Income by Volume for All States','State','Households','Household Income Buckets',-.45,6)

# Normalized Household Income for All States
createBarChart(incomeByStateNorm,'Normalized Household Income for All States','State','Normalized % Population','Household Income Buckets',-.45,6)

# Educational Attainment (18+) for All States
createBarChart(eduByState,'Educational Attainment (18+) by Volume for All States','State','Population','Educational Attainment Buckets',-.4,5)

# Normalized Education (18+) for All States
createBarChart(eduByStateNorm,'Normalized Education (18+) for All States','State','Normalized % Population','Educational Attainment Buckets',-.4,5)
```


![png](output_0_0.png)



![png](output_0_1.png)



![png](output_0_2.png)



![png](output_0_3.png)



![png](output_0_4.png)

<!-- MONA'S CODE -->

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```


```python
res_data = pd.ExcelFile('../Workspace/DataDownload.xls')
restaurant_df = pd.read_excel(res_data, 'RESTAURANTS')

restaurant_df = restaurant_df.rename(columns={'FFR09':'Fast Food Restaurants 2009',
                                              'FFR14':'Fast Food Restaurants 2014',
                                              'PCH_FFR_09_14':'Fast-food restaurants (% change)',
                                              'FFRPTH09':'Fast-food restaurants/1,000 pop 2009',
                                              'FFRPTH14':'Fast-food restaurants/1,000 pop 2014',
                                              'PCH_FFRPTH_09_14':'Fast-food restaurants/1,000 pop (% change)'})
restaurant_df.head()
#This dataframe is just reading in the excel file
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
      <th>FIPS</th>
      <th>State</th>
      <th>County</th>
      <th>Fast Food Restaurants 2009</th>
      <th>Fast Food Restaurants 2014</th>
      <th>Fast-food restaurants (% change)</th>
      <th>Fast-food restaurants/1,000 pop 2009</th>
      <th>Fast-food restaurants/1,000 pop 2014</th>
      <th>Fast-food restaurants/1,000 pop (% change)</th>
      <th>FSR09</th>
      <th>FSR14</th>
      <th>PCH_FSR_09_14</th>
      <th>FSRPTH09</th>
      <th>FSRPTH14</th>
      <th>PCH_FSRPTH_09_14</th>
      <th>PC_FFRSALES07</th>
      <th>PC_FFRSALES12</th>
      <th>PC_FSRSALES07</th>
      <th>PC_FSRSALES12</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>AL</td>
      <td>Autauga</td>
      <td>30</td>
      <td>36</td>
      <td>20.000000</td>
      <td>0.554170</td>
      <td>0.649878</td>
      <td>17.270512</td>
      <td>34</td>
      <td>29</td>
      <td>-14.705882</td>
      <td>0.628059</td>
      <td>0.523513</td>
      <td>-16.645960</td>
      <td>649.511367</td>
      <td>674.80272</td>
      <td>484.381507</td>
      <td>512.280987</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1003</td>
      <td>AL</td>
      <td>Baldwin</td>
      <td>112</td>
      <td>132</td>
      <td>17.857143</td>
      <td>0.624282</td>
      <td>0.659634</td>
      <td>5.662750</td>
      <td>202</td>
      <td>221</td>
      <td>9.405941</td>
      <td>1.125938</td>
      <td>1.104387</td>
      <td>-1.914027</td>
      <td>649.511367</td>
      <td>674.80272</td>
      <td>484.381507</td>
      <td>512.280987</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1005</td>
      <td>AL</td>
      <td>Barbour</td>
      <td>21</td>
      <td>22</td>
      <td>4.761905</td>
      <td>0.759301</td>
      <td>0.818239</td>
      <td>7.762116</td>
      <td>12</td>
      <td>15</td>
      <td>25.000000</td>
      <td>0.433887</td>
      <td>0.557890</td>
      <td>28.579797</td>
      <td>649.511367</td>
      <td>674.80272</td>
      <td>484.381507</td>
      <td>512.280987</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1007</td>
      <td>AL</td>
      <td>Bibb</td>
      <td>7</td>
      <td>5</td>
      <td>-28.571429</td>
      <td>0.305131</td>
      <td>0.222163</td>
      <td>-27.190844</td>
      <td>6</td>
      <td>5</td>
      <td>-16.666667</td>
      <td>0.261540</td>
      <td>0.222163</td>
      <td>-15.055985</td>
      <td>649.511367</td>
      <td>674.80272</td>
      <td>484.381507</td>
      <td>512.280987</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1009</td>
      <td>AL</td>
      <td>Blount</td>
      <td>24</td>
      <td>21</td>
      <td>-12.500000</td>
      <td>0.418549</td>
      <td>0.363832</td>
      <td>-13.073035</td>
      <td>19</td>
      <td>15</td>
      <td>-21.052632</td>
      <td>0.331351</td>
      <td>0.259880</td>
      <td>-21.569656</td>
      <td>649.511367</td>
      <td>674.80272</td>
      <td>484.381507</td>
      <td>512.280987</td>
    </tr>
  </tbody>
</table>
</div>




```python
ff_df=fast_food_df[['FIPS',
                    'State',
                    'County',
                    'Fast Food Restaurants 2009',
                    'Fast Food Restaurants 2014',
                    'Fast-food restaurants (% change)',
                    'Fast-food restaurants/1,000 pop 2009',
                    'Fast-food restaurants/1,000 pop 2014',
                    'Fast-food restaurants/1,000 pop (% change)']].copy()
ff_df.head()
#This is creating a new dataframe with only the data of interest. 
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
      <th>FIPS</th>
      <th>State</th>
      <th>County</th>
      <th>Fast Food Restaurants 2009</th>
      <th>Fast Food Restaurants 2014</th>
      <th>Fast-food restaurants (% change)</th>
      <th>Fast-food restaurants/1,000 pop 2009</th>
      <th>Fast-food restaurants/1,000 pop 2014</th>
      <th>Fast-food restaurants/1,000 pop (% change)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>AL</td>
      <td>Autauga</td>
      <td>30</td>
      <td>36</td>
      <td>20.000000</td>
      <td>0.554170</td>
      <td>0.649878</td>
      <td>17.270512</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1003</td>
      <td>AL</td>
      <td>Baldwin</td>
      <td>112</td>
      <td>132</td>
      <td>17.857143</td>
      <td>0.624282</td>
      <td>0.659634</td>
      <td>5.662750</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1005</td>
      <td>AL</td>
      <td>Barbour</td>
      <td>21</td>
      <td>22</td>
      <td>4.761905</td>
      <td>0.759301</td>
      <td>0.818239</td>
      <td>7.762116</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1007</td>
      <td>AL</td>
      <td>Bibb</td>
      <td>7</td>
      <td>5</td>
      <td>-28.571429</td>
      <td>0.305131</td>
      <td>0.222163</td>
      <td>-27.190844</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1009</td>
      <td>AL</td>
      <td>Blount</td>
      <td>24</td>
      <td>21</td>
      <td>-12.500000</td>
      <td>0.418549</td>
      <td>0.363832</td>
      <td>-13.073035</td>
    </tr>
  </tbody>
</table>
</div>




```python
for index,row in ff_df.iterrows():
    total_gr = row['Fast-food restaurants (% change)']
    yr_gr = total_gr/5
    ff_df.set_value(index,'Yearly Growth Rate %',yr_gr)
    ff09 = row['Fast Food Restaurants 2009']
    ff14 = row['Fast Food Restaurants 2014']
    projection = round((ff14*(yr_gr/100)) + ff14,0)
    ff_df.set_value(index,'Fast Food Restaurants 2015 (PROJECTED)',projection)
ff_df.head()
#This is now the updated dataframe that has the yearly growth rate per county and the PROJECTED fast food restaurant per county 2015
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
      <th>FIPS</th>
      <th>State</th>
      <th>County</th>
      <th>Fast Food Restaurants 2009</th>
      <th>Fast Food Restaurants 2014</th>
      <th>Fast-food restaurants (% change)</th>
      <th>Fast-food restaurants/1,000 pop 2009</th>
      <th>Fast-food restaurants/1,000 pop 2014</th>
      <th>Fast-food restaurants/1,000 pop (% change)</th>
      <th>Yearly Growth Rate %</th>
      <th>Fast Food Restaurants 2015 (PROJECTED)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>AL</td>
      <td>Autauga</td>
      <td>30</td>
      <td>36</td>
      <td>20.000000</td>
      <td>0.554170</td>
      <td>0.649878</td>
      <td>17.270512</td>
      <td>4.000000</td>
      <td>37.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1003</td>
      <td>AL</td>
      <td>Baldwin</td>
      <td>112</td>
      <td>132</td>
      <td>17.857143</td>
      <td>0.624282</td>
      <td>0.659634</td>
      <td>5.662750</td>
      <td>3.571429</td>
      <td>137.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1005</td>
      <td>AL</td>
      <td>Barbour</td>
      <td>21</td>
      <td>22</td>
      <td>4.761905</td>
      <td>0.759301</td>
      <td>0.818239</td>
      <td>7.762116</td>
      <td>0.952381</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1007</td>
      <td>AL</td>
      <td>Bibb</td>
      <td>7</td>
      <td>5</td>
      <td>-28.571429</td>
      <td>0.305131</td>
      <td>0.222163</td>
      <td>-27.190844</td>
      <td>-5.714286</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1009</td>
      <td>AL</td>
      <td>Blount</td>
      <td>24</td>
      <td>21</td>
      <td>-12.500000</td>
      <td>0.418549</td>
      <td>0.363832</td>
      <td>-13.073035</td>
      <td>-2.500000</td>
      <td>20.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ff_df['County'] = ff_df['County'] + ' County'
```


```python
ff_df.head()
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
      <th>FIPS</th>
      <th>Abbreviation</th>
      <th>County</th>
      <th>Fast Food Restaurants 2009</th>
      <th>Fast Food Restaurants 2014</th>
      <th>Fast-food restaurants (% change)</th>
      <th>Yearly Growth Rate %</th>
      <th>Fast Food Restaurants 2015 (PROJECTED)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>AL</td>
      <td>Autauga County</td>
      <td>30</td>
      <td>36</td>
      <td>20.000000</td>
      <td>4.000000</td>
      <td>37.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1003</td>
      <td>AL</td>
      <td>Baldwin County</td>
      <td>112</td>
      <td>132</td>
      <td>17.857143</td>
      <td>3.571429</td>
      <td>137.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1005</td>
      <td>AL</td>
      <td>Barbour County</td>
      <td>21</td>
      <td>22</td>
      <td>4.761905</td>
      <td>0.952381</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1007</td>
      <td>AL</td>
      <td>Bibb County</td>
      <td>7</td>
      <td>5</td>
      <td>-28.571429</td>
      <td>-5.714286</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1009</td>
      <td>AL</td>
      <td>Blount County</td>
      <td>24</td>
      <td>21</td>
      <td>-12.500000</td>
      <td>-2.500000</td>
      <td>20.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# del ff_df['Fast-food restaurants/1,000 pop 2009']
# del ff_df['Fast-food restaurants/1,000 pop 2014']
# del ff_df['Fast-food restaurants/1,000 pop (% change)']
```


```python
resbystate15 = ff_df.groupby(["State"])['Fast Food Restaurants 2015 (PROJECTED)'].sum()
resbystate14 =  ff_df.groupby(["State"])['Fast Food Restaurants 2014'].sum()
resbystate15.head(20)
resbystate=pd.DataFrame({'Abbreviation':resbystate15.index,'Fast Food Restaurant Count 2014':resbystate14.values, 'Fast Food Restaurant Count 2015 (prj)':resbystate15.values}).copy()
resbystate.head()
#this dataframe shows us the totals of restaurants PER state AND the projected volumes
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
      <th>Abbreviation</th>
      <th>Fast Food Restaurant Count 2014</th>
      <th>Fast Food Restaurant Count 2015 (prj)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AK</td>
      <td>429</td>
      <td>425.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AL</td>
      <td>3561</td>
      <td>3626.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AR</td>
      <td>1939</td>
      <td>1963.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AZ</td>
      <td>4211</td>
      <td>4241.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CA</td>
      <td>28292</td>
      <td>28842.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.palplot(sns.hls_palette(16, l=.3, s=.8))
plt.figure(figsize=(20,10))
x_axis = np.arange(len(resbystate))
tick_locations = [value for value in x_axis]
ff1=plt.bar(x_axis, resbystate['Fast Food Restaurant Count 2015 (prj)'], width = 0.2,align='center',label='Projected 2015 Volumes')
ff2=plt.bar(x_axis + 0.25, resbystate['Fast Food Restaurant Count 2014'], width = 0.2,align='center',label='2014 Volumes')

plt.xticks(tick_locations, resbystate['Abbreviation'], rotation="horizontal")
plt.title('Projected Fast Food Restaurant Volume for 2015',size=20)
plt.xlabel('States',size=18)
plt.ylabel('Restaurant Volume',size=18)
plt.legend()
plt.tight_layout()
plt.savefig('Projected Fast Food Restaurant Volumes_2015_.png')
plt.show()
```


![png](output_9_0.png)



![png](output_9_1.png)



```python
# ff_df=ff_df.rename(columns={'State':'Abbreviation'})
# ff_df.head()
countypop = pd.merge(ff_df,popDFmapped,how='inner',on=['Abbreviation','County'])

for index,row in countypop.iterrows():
    pop = row['Population']
    ffres14 = row['Fast Food Restaurants 2014']
    ffres15 = row['Fast Food Restaurants 2015 (PROJECTED)']
    ffpercap14 = ((ffres14/pop)*100)
    ffpercap15 = ((ffres15/pop)*100)
    ff_df.set_value(index,'Fast Food Restaurants Per Capita, 2014',ffpercap14)
    ff_df.set_value(index,'Fast Food Restaurants Per Capita, 2015',ffpercap15)
countypop.head()
#This dataframe merges population and county information with the county and 2015 restaurant volumes (per county)
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
      <th>FIPS</th>
      <th>Abbreviation</th>
      <th>County</th>
      <th>Fast Food Restaurants 2009</th>
      <th>Fast Food Restaurants 2014</th>
      <th>Fast-food restaurants (% change)</th>
      <th>Yearly Growth Rate %</th>
      <th>Fast Food Restaurants 2015 (PROJECTED)</th>
      <th>Fast Food Restaurants Per Capita, 2014</th>
      <th>Fast Food Restaurants Per Capita, 2015</th>
      <th>Population</th>
      <th>State Code (FIPS)</th>
      <th>County Code (FIPS)</th>
      <th>State</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1003</td>
      <td>AL</td>
      <td>Baldwin County</td>
      <td>112</td>
      <td>132</td>
      <td>17.857143</td>
      <td>3.571429</td>
      <td>137.0</td>
      <td>0.089869</td>
      <td>0.091614</td>
      <td>208563</td>
      <td>1</td>
      <td>3</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1015</td>
      <td>AL</td>
      <td>Calhoun County</td>
      <td>95</td>
      <td>103</td>
      <td>8.421053</td>
      <td>1.684211</td>
      <td>105.0</td>
      <td>0.097343</td>
      <td>0.099466</td>
      <td>114611</td>
      <td>1</td>
      <td>15</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1043</td>
      <td>AL</td>
      <td>Cullman County</td>
      <td>50</td>
      <td>53</td>
      <td>6.000000</td>
      <td>1.200000</td>
      <td>54.0</td>
      <td>0.021884</td>
      <td>0.021884</td>
      <td>82471</td>
      <td>1</td>
      <td>43</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1049</td>
      <td>AL</td>
      <td>DeKalb County</td>
      <td>41</td>
      <td>43</td>
      <td>4.878049</td>
      <td>0.975610</td>
      <td>43.0</td>
      <td>0.065543</td>
      <td>0.066062</td>
      <td>70900</td>
      <td>1</td>
      <td>49</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1051</td>
      <td>AL</td>
      <td>Elmore County</td>
      <td>29</td>
      <td>45</td>
      <td>55.172414</td>
      <td>11.034483</td>
      <td>50.0</td>
      <td>0.055542</td>
      <td>0.056030</td>
      <td>81799</td>
      <td>1</td>
      <td>51</td>
      <td>Alabama</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Need to groupby the states in the countypop dataframe so that we can normalize this all 

normalizedres = countypop[['FIPS','Abbreviation','Fast Food Restaurants 2009','Fast Food Restaurants 2014','Fast Food Restaurants 2015 (PROJECTED)', 'Population']].copy()
normalizedres.head()
normalizedres = normalizedres.groupby(['Abbreviation'])['Fast Food Restaurants 2015 (PROJECTED)','Population'].sum()
normalizedres.reset_index(level=['Abbreviation'],inplace=True)

normalizedres.head()
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
      <th>Abbreviation</th>
      <th>Fast Food Restaurants 2015 (PROJECTED)</th>
      <th>Population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AL</td>
      <td>2907.0</td>
      <td>3630681</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AR</td>
      <td>1234.0</td>
      <td>1673132</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AZ</td>
      <td>4148.0</td>
      <td>6764001</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CA</td>
      <td>28573.0</td>
      <td>38745526</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CO</td>
      <td>3418.0</td>
      <td>4755954</td>
    </tr>
  </tbody>
</table>
</div>




```python
for index,row in normalizedres.iterrows():
    popu = row['Population']
    ff2015 = row['Fast Food Restaurants 2015 (PROJECTED)']
    percap = (ff2015/popu)*100
    normalizedres.set_value(index,'Per Capita Fast Food Restaurants',percap)
    
normalizedres.head()
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
      <th>Abbreviation</th>
      <th>Fast Food Restaurants 2015 (PROJECTED)</th>
      <th>Population</th>
      <th>Per Capita Fast Food Restaurants</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AL</td>
      <td>2907.0</td>
      <td>3630681</td>
      <td>0.080068</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AR</td>
      <td>1234.0</td>
      <td>1673132</td>
      <td>0.073754</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AZ</td>
      <td>4148.0</td>
      <td>6764001</td>
      <td>0.061325</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CA</td>
      <td>28573.0</td>
      <td>38745526</td>
      <td>0.073745</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CO</td>
      <td>3418.0</td>
      <td>4755954</td>
      <td>0.071868</td>
    </tr>
  </tbody>
</table>
</div>




```python
top10 = normalizedres.sort_values('Per Capita Fast Food Restaurants',ascending=False).head(10)
bottom10 = normalizedres.sort_values('Per Capita Fast Food Restaurants',ascending=False).tail(10)
top10
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
      <th>Abbreviation</th>
      <th>Fast Food Restaurants 2015 (PROJECTED)</th>
      <th>Population</th>
      <th>Per Capita Fast Food Restaurants</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>46</th>
      <td>WV</td>
      <td>653.0</td>
      <td>731019</td>
      <td>0.089327</td>
    </tr>
    <tr>
      <th>31</th>
      <td>NY</td>
      <td>16669.0</td>
      <td>18741516</td>
      <td>0.088942</td>
    </tr>
    <tr>
      <th>9</th>
      <td>HI</td>
      <td>1244.0</td>
      <td>1428462</td>
      <td>0.087087</td>
    </tr>
    <tr>
      <th>22</th>
      <td>MS</td>
      <td>1130.0</td>
      <td>1323725</td>
      <td>0.085365</td>
    </tr>
    <tr>
      <th>38</th>
      <td>SD</td>
      <td>252.0</td>
      <td>296690</td>
      <td>0.084937</td>
    </tr>
    <tr>
      <th>33</th>
      <td>OK</td>
      <td>2036.0</td>
      <td>2426888</td>
      <td>0.083893</td>
    </tr>
    <tr>
      <th>32</th>
      <td>OH</td>
      <td>8003.0</td>
      <td>9756400</td>
      <td>0.082028</td>
    </tr>
    <tr>
      <th>15</th>
      <td>KY</td>
      <td>1781.0</td>
      <td>2173786</td>
      <td>0.081931</td>
    </tr>
    <tr>
      <th>8</th>
      <td>GA</td>
      <td>6392.0</td>
      <td>7810581</td>
      <td>0.081838</td>
    </tr>
    <tr>
      <th>0</th>
      <td>AL</td>
      <td>2907.0</td>
      <td>3630681</td>
      <td>0.080068</td>
    </tr>
  </tbody>
</table>
</div>




```python
##creating bar chart to show the relation between states with most restaurants per capita
plt.figure(figsize=(20,10))
x_axis=np.arange(len(normalizedres))
tick_locations = [value for value in x_axis]
plt.xticks(tick_locations, normalizedres['Abbreviation'], rotation="horizontal")
plt.bar(x_axis,normalizedres['Per Capita Fast Food Restaurants'],color='m',alpha=0.3,width = 0.4,align='center')
plt.title('Fast Food Restaurants Per Capita',size=18)
plt.xlabel('States',size=14)
plt.ylabel('Restaurants per Capita',size=14)
plt.savefig('Fast_Food_Restaurants_Per_Capita_.png')
plt.tight_layout()
plt.ylim(0.0,0.1)
plt.show()
```


![png](output_14_0.png)



```python
plt.figure(figsize=(20,6))
x_axis=np.arange(len(top10))
tick_locations = [value for value in x_axis]
t1=plt.xticks(tick_locations, top10['State'], rotation="horizontal")
t10=plt.bar(x_axis,top10['Per Capita Fast Food Restaurants'],color='r',alpha=0.4,width = 0.2,align='center',label='Top 10 States')
plt.legend()
plt.ylim(0.0,0.1)
plt.title('Top 10 States with Most Fast Food Restaurants per Capita',size=18)
plt.xlabel('States',size=14)
plt.ylabel('Restaurants per Capita',size=14)
plt.savefig('Top10States.png')
plt.show()
```


![png](output_15_0.png)



```python
plt.figure(figsize=(20,6))
x_axis2 = np.arange(len(bottom10))
tick_locations2 = [value for value in x_axis2]
b1=plt.xticks(tick_locations2,bottom10['State'], rotation="horizontal")
b10=plt.bar(x_axis2,bottom10['Per Capita Fast Food Restaurants'],color='c',alpha=0.4,width = 0.2,align='center',label='Bottom 10 States')
plt.legend()
plt.title('Bottom 10 States with Least Fast Food Restaurants per Capita',size=18)
plt.xlabel("States",size=14)
plt.ylabel('Restaurants per Capita',size=14)
plt.ylim(0.0,0.1)
plt.savefig('Bottom10_States.png')
plt.show()
```


![png](output_16_0.png)

