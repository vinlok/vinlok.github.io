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

## To see columns
df.columns

## To see specific columns


## To see the data types of columns auto detected by Panda
df.dttypes
object data type is string

# Accessing column
## Individual
df["age"] will return a series with index starting at 0.
## Multiple
df[["age","address"]]
or
df.age 

# Selecting rows

df.loc(0) : returns the first row of df
df.loc(0:2) : 0-2 inclusive bot
## selecting rows with specific column
df.loc[0,"is_trial"] : return row 0 only for column is_trial
## selecting rows with specific columns
df.loc[0:2,"age":"product"]: This select rows 0 to 2 and columns age to product consecutively
## select all rows for given column:
df.loc[:,"age":"product"]

## selecting/Slicing specific rows and columns
df.loc[[1,3],["is_trial","age"]]


## selecting/Slicing by integer position

df.iloc[0] : returns row at 0 index

df.iloc[0:2]: 0 to 1 like python *not Inclusive*

df.iloc[]


## df.info()
- shows number of columns
- comluns names
- number of non-null values

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


# describe()
- df.describe() returns count, meand, std, min, 25_percentile, 50_percentile , 75_percentile and max

