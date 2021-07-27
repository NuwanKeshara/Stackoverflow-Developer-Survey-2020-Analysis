# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 15:34:33 2021

@author: Nuwan
"""

import pandas as pd

survey_df = pd.read_csv('C:/Users/Nuwan/Desktop/Stackoverflow-Developer-Survey-2020-Analysis/survey_results_public.csv')
print(survey_df)
print(survey_df.columns)

schema_df = pd.read_csv('C:/Users/Nuwan/Desktop/Stackoverflow-Developer-Survey-2020-Analysis/survey_results_schema.csv' ,
                        index_col='Column').QuestionText

print(schema_df)
print(schema_df['Respondent'])


analysis_columns = [
                    'Country',
                    'Age',
                    'Gender',
                    'EdLevel',
                    'UndergradMajor',
                    
                    'Hobbyist',
                    'Age1stCode',
                    'YearsCode',
                    'YearsCodePro',
                    'LanguageWorkedWith',
                    'LanguageDesireNextYear',
                    'NEWLearn',
                    'NEWStuck',
                   
                    'Employment',
                    'DevType',
                    'WorkWeekHrs',
                    'JobSat',
                    'JobFactors',
                    'NEWOvertime',
                    'NEWEdImpt']

questions_df = schema_df[analysis_columns].copy()
print(questions_df)

data_df = survey_df[analysis_columns].copy()
print(data_df)
print(data_df.loc[0])


#data_df details
print(data_df.shape)
print(data_df.info())
print(data_df.columns)
print(data_df.describe())


#questions_df details
print(questions_df.shape)
print(questions_df)

########################################
#Data Cleaning and Preparation 

print(data_df.Age1stCode)
print(questions_df['Age1stCode'])


data_df['Age1stCode'] = pd.to_numeric(data_df.Age1stCode , errors='coerce')
data_df['YearsCode'] = pd.to_numeric(data_df.YearsCode , errors='coerce')
data_df['YearsCodePro'] = pd.to_numeric(data_df.YearsCodePro , errors='coerce')

print(type(data_df.Age1stCode.loc[64457]))

######################################

data_df.drop(data_df[data_df.Age < 1].index , inplace=True)
data_df.drop(data_df[data_df.Age > 100].index , inplace = True)

data_df.drop(data_df[data_df.WorkWeekHrs > 140].index , inplace = True)

######################################

print(data_df['Gender'].value_counts())

import numpy as np

data_df.where(~(data_df.Gender.str.contains(';',na=False)),np.nan, inplace =True)

print(data_df.sample(10))


######################################
#Explortary Analysis and Visualization

import seaborn as sns
import matplotlib 
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
matplotlib.reParams['font.size'] = 14
matplotlib.rcParams['figure.figsize']=(9,5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


questions_df.Country

data_df.Country.nunique()

top_countries = data_df.Country.value_counts().head(10)

plt.figure(figsize=(12,6))
plt.xticks(rotation=75)
plt.title(questions_df.Country)
sns.barplot(x=top_countries.index, y=top_countries);


plt.figure(figsize=(12, 6))
plt.title(questions_df.Age)
plt.xlabel('Age')
plt.ylabel('Number of respondents')

plt.hist(data_df.Age, bins=np.arange(10,80,5), color='purple');


gender_counts = data_df.Gender.value_counts()
plt.figure(figsize=(12,6))
plt.title(questions_df.Gender)
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=180);


sns.countplot(y=data_df.EdLevel)
plt.xticks(rotation=75);
plt.title(questions_df['EdLevel'])
plt.ylabel(None);


undergrad_pct = data_df.UndergradMajor.value_counts() * 100 / data_df.UndergradMajor.count()

sns.barplot(x=undergrad_pct, y=undergrad_pct.index)

plt.title(questions_df.UndergradMajor)
plt.ylabel(None);
plt.xlabel('Percentage');



(data_df.Employment.value_counts(normalize=True, ascending=True)*100).plot(kind='barh', color='g')
plt.title(questions_df.Employment)
plt.xlabel('Percentage');




























