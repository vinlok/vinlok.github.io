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




