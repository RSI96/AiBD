# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:37:09 2019

@author: student204
"""

import pandas as pd
import numpy as np

df = pd.read_csv('weather.csv', names=['id', 'Year', 'Month', 'element', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                       '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                                       '23', '24', '25', '26', '27', '28', '29', '30', '31'], sep=';', header=None)

df = df.drop(df.index[0])
df = df[df.element != 'PRCP']

df = pd.melt(df, id_vars =['id', 'Year', 'Month', 'element'], value_vars =['1', '2', '3', '4', '5', '6', '7', '8', '9',
'10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
'30', '31'], var_name='Day', value_name='temp')

df['Datetime'] = pd.to_datetime(df[['Year', 'Month', 'Day']], errors='coerce')

df = df.drop(columns=['Year', 'Month', 'Day'])

df = df[df.temp != '-9999']

df = df.pivot_table(index=['id', 'Datetime'], columns='element', values='temp', aggfunc='first').reset_index()

df.to_csv(r'D:\AiBD\Sikora\TIER Protocol Documentation\Analysis Data\Analized Data 2.csv')
#df.to_excel(r'E:\AiBD\Sikora\TIER Protocol Documentation\Analysis Data\Analized Data.xlsx', sheet_name='Analized Data')

print(df)

