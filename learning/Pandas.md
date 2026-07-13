<div align="center">

# 🐼 Pandas Documentation

### Learning Notes by Rajan Maurya

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="90">

### GitHub
**https://github.com/rajanmaurya12012008**

---

*"Learning Pandas one step at a time."*

</div>

---

# 📖 Table of Contents

- Introduction
- About Pandas
- Why I Started Learning Pandas
- Features
- Installation
- Importing Pandas
- Data Structures
- Creating My First Dataset
- Reading Data
- Writing Data
- Basic Commands
- Data Selection
- Filtering Data
- Sorting Data
- Handling Missing Values
- Basic Statistics
- What I Understood
- Key Points
- Conclusion

---

# 🚀 Introduction

Pandas is one of the most useful Python libraries for working with data.

When I started learning Data Science and Machine Learning, I found that almost every project uses Pandas. It makes working with tables, datasets, and CSV files much easier than using normal Python lists.

Instead of writing many lines of code, Pandas allows us to perform complex operations using simple functions.

---

# 🐼 About Pandas

Pandas is an open-source Python library developed for data manipulation and data analysis.

It helps us organize data into rows and columns, clean missing values, filter records, sort information, calculate statistics, and prepare datasets for Machine Learning.

It is built on top of **NumPy**, which makes it both fast and efficient.

---

# ❓ What is Pandas?

In simple words,

> Pandas is a Python library that helps us read, organize, clean, analyze, and process data.

It works with different file formats like:

- CSV
- Excel
- JSON
- SQL Database
- HTML Tables
- XML

---

# 🎯 Why I Started Learning Pandas

I started learning Pandas because:

- It is one of the most important libraries in Data Science.
- Most Machine Learning datasets are handled using Pandas.
- It makes data cleaning much easier.
- It saves time by providing ready-made functions.
- It is widely used in industries.

---

# ✨ Features of Pandas

✅ Easy to Learn

✅ Fast Data Processing

✅ Supports Multiple File Formats

✅ Powerful Data Filtering

✅ Data Cleaning

✅ Missing Value Handling

✅ Sorting & Searching

✅ Statistical Analysis

✅ Data Transformation

✅ Machine Learning Friendly

---

# 💻 Installation

Install Pandas using pip.

```bash
pip install pandas
```

Check installed version.

```python
import pandas as pd

print(pd.__version__)
```

Example Output

```
2.x.x
```

---

# 📥 Importing Pandas

```python
import pandas as pd
```

Here,

`pd` is just a short name (alias) for Pandas.

---

# 🧱 Data Structures in Pandas

Pandas mainly provides two data structures.

---

## 1️⃣ Series

A Series is a one-dimensional data structure.

Example

```python
import pandas as pd

numbers = pd.Series([10,20,30,40])

print(numbers)
```

Output

```
0    10
1    20
2    30
3    40
dtype: int64
```

---

## 2️⃣ DataFrame

A DataFrame is a two-dimensional table made up of rows and columns.

It is the most commonly used object in Pandas.

---

# 📊 Creating My First DataFrame

```python
import pandas as pd

student = {
    "ID":[101,102,103,104],
    "Name":["Rajan","Rahul","Aman","Priya"],
    "Age":[19,20,18,19],
    "Course":["AI","CSE","IT","ECE"],
    "Marks":[91,85,78,95]
}

df = pd.DataFrame(student)

print(df)
```

Output

```
    ID   Name   Age Course  Marks
0  101  Rajan   19     AI     91
1  102 Rahul   20    CSE     85
2  103 Aman    18     IT     78
3  104 Priya   19    ECE     95
```

---

# 📂 Reading Data

### Read CSV

```python
df = pd.read_csv("students.csv")
```

### Read Excel

```python
df = pd.read_excel("students.xlsx")
```

### Read JSON

```python
df = pd.read_json("students.json")
```

### Read SQL

```python
df = pd.read_sql(query, connection)
```

---

# 💾 Writing Data

```python
df.to_csv("output.csv")
```

```python
df.to_excel("output.xlsx")
```

```python
df.to_json("output.json")
```

---

# 🛠️ Basic Pandas Commands

## Display First Five Rows

```python
df.head()
```

Output

```
First five records
```

---

## Display Last Five Rows

```python
df.tail()
```

---

## Dataset Shape

```python
df.shape
```

Output

```
(4,5)
```

Meaning

4 Rows

5 Columns

---

## Column Names

```python
df.columns
```

Output

```
Index(['ID','Name','Age','Course','Marks'])
```

---

## Data Types

```python
df.dtypes
```

Output

```
ID         int64
Name      object
Age        int64
Course    object
Marks      int64
```

---

## Dataset Information

```python
df.info()
```

This displays:

- Number of rows
- Number of columns
- Data types
- Missing values
- Memory usage

---

## Statistical Summary

```python
df.describe()
```

Output

```
Count
Mean
Std
Min
Max
25%
50%
75%
```

---

# 🔍 Selecting Data

Single Column

```python
df["Name"]
```

Multiple Columns

```python
df[["Name","Marks"]]
```

Using loc

```python
df.loc[0]
```

Using iloc

```python
df.iloc[0]
```

---

# 🎯 Filtering Data

Students scoring above 80.

```python
df[df["Marks"]>80]
```

Students whose age is 19.

```python
df[df["Age"]==19]
```

---

# 📈 Sorting Data

Ascending

```python
df.sort_values("Marks")
```

Descending

```python
df.sort_values("Marks",ascending=False)
```

---

# ❌ Handling Missing Values

Check Missing Values

```python
df.isnull()
```

Count Missing Values

```python
df.isnull().sum()
```

Remove Missing Values

```python
df.dropna()
```

Replace Missing Values

```python
df.fillna(0)
```

---

# 📊 Basic Statistical Operations

Average

```python
df["Marks"].mean()
```

Maximum

```python
df["Marks"].max()
```

Minimum

```python
df["Marks"].min()
```

Total

```python
df["Marks"].sum()
```

Count

```python
df.count()
```

Unique Values

```python
df["Course"].unique()
```

---

# 💡 What I Understood

While learning Pandas, I realized that working with datasets becomes much easier compared to normal Python.

Instead of writing long loops, Pandas provides built-in functions that perform tasks quickly.

I also learned that almost every Data Science and Machine Learning project starts with loading and cleaning data using Pandas.

---

# 🎯 Why I Will Use Pandas

I will use Pandas for:

- Reading datasets
- Cleaning data
- Removing duplicate values
- Handling missing values
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Machine Learning projects

---

# 📝 Key Points

✔ Built on NumPy

✔ Open Source

✔ Fast and Efficient

✔ Supports Multiple File Formats

✔ Easy Data Cleaning

✔ Easy Data Analysis

✔ Widely Used in AI & ML

✔ Beginner Friendly

---

# 📚 Conclusion

After learning the basics of Pandas, I understood why it is considered one of the most important Python libraries for data analysis.

It provides simple and powerful tools for working with structured data. Whether the task is reading a CSV file, cleaning missing values, filtering records, or preparing data for Machine Learning, Pandas makes the process much easier.

This documentation represents my learning journey, and I will continue exploring more advanced Pandas concepts in future notes.

---

<div align="center">

### ⭐ Thank You ⭐

**Made with ❤️ while learning Pandas**

**Author:** Rajan Maurya

**GitHub:** https://github.com/rajanmaurya12012008

</div>