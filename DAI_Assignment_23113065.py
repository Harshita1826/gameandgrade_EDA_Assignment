# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GsoyfhpuQaqTae5vL2exYWgFLlzx2AR2
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('gameandgrade.csv')

df.info()

df.describe()

cate= ['Sex', 'School Code']
num= result = [item for item in df.columns if item not in cate]
independent_vars= [item for item in df.columns if item not in ['Grade']]
independent_vars_num= [item for item in independent_vars if item not in cate]

"""UNIVARIATE ANALYSIS"""

for column in num:
        plt.figure(figsize=(4, 2))
        df[column].hist(bins=(column.max()-column-min), color='skyblue', edgecolor='black')
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

for column in cate:
        plt.figure(figsize=(4, 2))
        df[column].value_counts().plot(kind='bar')
        plt.title(f'Bar Plot of {column}')
        plt.xticks(rotation=45)
        plt.show()

"""MULTIVARIATE ANALYSIS"""

correlation_matrix = df.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

for i, var in enumerate(independent_vars, 1):
    plt.subplot(3, 3, i)
    sns.boxplot(x=df[var], y=df["Grade"])
    plt.xlabel(var)
    plt.ylabel("Grade")
    plt.title(f"{var} vs. Grade")

plt.tight_layout()
plt.subplots_adjust(hspace=1, wspace=2)
plt.show()

plt.figure(figsize=(10, 6))

sns.pairplot(df)

plt.suptitle('Pair Plot for DataFrame')
plt.show()

for var in independent_vars:
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=df[var], y=df["Grade"], alpha=0.6)
    plt.title(f"Scatter Plot: {var} vs. Grade")
    plt.xlabel(var)
    plt.ylabel("Grade")
    plt.show()

