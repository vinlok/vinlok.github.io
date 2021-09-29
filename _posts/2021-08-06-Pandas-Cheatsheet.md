---
layout: post
title: "Pandas-cheatsheet"
date: 2017-3-25
categories: ['Data Analytics']
excerpt_separator: <!--more-->
---


Pandas is an external Library imported in Python commonly as Alias as pd. It is commonly used to perform EDA.

## Reading from CSV

```
import pandas as pd

df= pd.read_csv("some.csv)
type(df)
```

# Dataframes
## head()
- df.head(1)
## tail()
- df.tail(1)
## shape()
- To see number of rows and columns
df.shape()
## sample()
- df.sample(3) to retrieve sample rows which are random evertime.
- df.sample(3,random_state=1) to get fixed set of rows. Here the random_state is any integer
## describe()
- df.describe() returns count, meand, std, min, 25_percentile, 50_percentile , 75_percentile and max

## df.info()
- shows number of columns
- comluns names
- number of non-null values

## df.dtypes
- to see the data types for the dataframe.

# Operations on columns
- To see all columns
df.columns

- Individual
df["age"] will return a series with index starting at 0.
- Multiple
df[["age","address"]]
or
df.age 
- Adding column in a dataframe

df["new column"] = df.age*12

## To see the data types of columns auto detected by Panda
df.dttypes
"object" data type is string



# Operation on rows
## Selecting rows

- df.loc(0) : returns the first row of df
- df.loc(0:2) : 0-2 inclusive 
- selecting rows with specific column
df.loc[0,"is_trial"] : return row 0 only for column is_trial
- selecting rows with specific columns
df.loc[0:2,"age":"product"]: This select rows 0 to 2 and columns age to product consecutively
- select all rows for given column:
df.loc[:,"age":"product"]

# Slicing
## selecting/Slicing specific rows and columns
df.loc[[1,3],["is_trial","age"]]

## selecting/Slicing by integer position

df.iloc[0] : returns row at 0 index

df.iloc[0:2]: 0 to 1 like python *not Inclusive*

df.iloc[]


## Functions on columns:
### Calculate statistics on a specific columns
df.age.mean()
df.age.median()
df.age.max()
df.age.min()
### Categorical data
df.age.unique()
df.age.value_counts()
## Calculate statistics on data frame
df.count()
df.mean()

This will only perform the statistics on the numeric columns of a data frame.

# Chaining commands

Commands in pandas can be chained together to perform complex operations. Example:

df.iloc[:4] would return first four rows with columns: col1, col2,col3 and col4

then if we do df.iloc[:4].col1 we can only select the col1

# Arithmetic Operations

- Multiplication:
df.age*12 : Age of all customers is multiplied by 12

- Division: 
df.age_in_months/df.age

- addition

df.age_inmonth/df.age + 1

# Conditional statements

df["product"] == "standard"

checks each element in columns "product" to see if its value is equals to standard or not. It returns corresponding index and Boolean True or False for each index

df.age <= 40 will return indexes with boleans

You can also do this:

df["new_col"] = (
    (df["product] == "Standard") &
    (df["is_trial] == True)
)

df.head(3)

# Sorting

Two ways:

## By value
df.sort_values("column_name", ascending=False)

df.sort_values(["col1","col2"], ascending=[False,True])

- To sort inplace
df.sort_values("column_name", ascending=False, inPlace=True)

## sort_index()

# Filtering Data

- Filtering is done by using data mask. You can create a data mask in panda using the conditionals and then pass it to the dataframe.
First way:


```
age_mask = df.age > 45 # This will return all rows indexes with boolean values set to True or False depending on the condition
df[age_mask] # This is where we apply the data mask and return all the ages > 45

station_mask = (df.station == ["station1","station2","station3])
df[station_mask]
```

second way:
```
df[df["is_trial"]== False]
```

- Multiple conditionals using bitwise operators

& operator
age_trial_mask = (df.age < 45) & (df.is_trial == False

| or operation

df[
    (df["product"] == "plus") |
    (df["product"] == "premium")
]

~ compliment


# Grouping data

g = df.groupby("exercise)

- g will be an object created

g.minutes.mean()

or

df.groupby("exercise").minutes.mean()

- You can also do a count by a given column

df.groupby("exercise")["day"].count()

## Groupby multiple columns
df.groupby(["location","exercise"]).minutes.mean()

- This returns the grouped data by location for each type of exercise example bike and run. It will then perform mean() on it.

- This will yield multi index with location as outer index and exercise as the inner index
 
- Restting index:
df.groupby(["location","exercise"]).minutes.mean().reset_index()

# Aggregating data

## agg function

### On Columns
df.col_name.agg()
or
df.col_name.agg(["mean", "std"])

### On dataframes

df.agg(["count","median"])

### On groups

df.groupby("col_name").agg()

You can rename the columns by using dictionary as below:

df.groupby("exercise").agg(
    {
        "minutes" : "mean",
        "intensity": ["min", "max"]
    }
)


# Using custom functions on Panda

## .apply()

- You can create a custom function and use .apply to process a given column on dataframe.

```
df.col_name.apply(functio_name)
```

This will apply the function on each element on the column and convert the result.

## .map()
- Operated only on panda series (Not on dataframe) elementwise
- Does not perform aggregations
- This can be used to do a find and replace on a given column using dictionary:

location_map={
    "run":"land",
    "swim":"water"
}

df.exercise.map(location_map)

This will take run and swim as keys and map it to land and water creating a new dataframe.

## .applymap()
- Works on dataframe elementwise.
- Example convert case of dataframe to uppercase.


# Merging data

orders = pd.read_csv("orders.csv")

customers = pd.read_csv(|"customers.csv")

pd.merge(orders,customers, on="customer_id)

This is equivalent of join sql statement


# Datetime

- By default pandas read datetime as string.
- You can convert the columns from string to datetime type as below

df["col_name"] = pd.to_datetime(df.col_name)

- df.info will show changed col.

- On datetime col, we can extract month, year, day, hh, mm, ss etc.
```
orders["buy_year"] = orders.buy_date.dt.year
```

- On add or remove using timedelta.


# Data Cleaning 

- Missing value in pada is represent as NaN: Not a Number
- df.info shows null value count
- .isna() method is also used which returns elements which are Null. It essentially returns a data mask with bolean True and False.
- To remove all the null values from the dataframe you can do this:
1. Find the null values: 
 df.col_name.isna(): Here the values with null will be true and not null will be false.

2. The do a ~ on this as we only want to select non null values

~df.col_name.isna()

3. Now apply the data mask on the dataframe:

df[~df.col_name.isna()]

## .dropna

df.dropna(subset=["col_name"])

## .fillna
df.shipping.fillna(0)
- Needs to be done with care
## Impute using mean or median

## Renaming columns
- column names with space are not valid as they cannot be used as variables in python. Hence, they should be renamed or removed.
df.rename(columns={
    'price per pound':'price_lb',
    'Shipping price':'shipping_price'
},inplace=True)

## Remove a char from col name

df.columns = df.columns.str.replace(' ', '')

## .astype() to Convert Column to a given data type

df['col_name'] = df.col_name.astype('float')



## Dropping columns: .drop()

df.drop('col_name', axis=1)

axis=1 for columns
axis=0 for row

## Convert all the values to capital for a given column:

df.col_name = df.col_name.str.upper()

## Replacing char in column values with something

pop = df.population.str.replace(",",".")

pop.astype('int')

## Remove spaces from col values

df.col_name.strip()



