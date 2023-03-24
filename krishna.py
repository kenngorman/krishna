# krishna

import pandas as pd
import openpyxl
import xlrd

'''
# create dataframe with 3 columns
data = pd.DataFrame({
    "id": [7058, 7059, 7072, 7054],
    "name": ['sravan', 'jyothika', 'harsha', 'ramya'],
    "subjects": ['java', 'python', 'html/php', 'php/js']})
 
# get the cell value using loc() function
# in name column and 1 row
print(data['id'].loc[data.index[0]])
 
# get the cell value using loc() function
# in name column and 2 row
print(data['name'].loc[data.index[1]])
 
# get the cell value using loc() function
# in subjects column and 4 row
print(data['subjects'].loc[data.index[3]])

print(len(data))
print(data.shape)
print(data.count())
print(data)
print()
'''

krishna = pd.read_excel('krishna.xlsx')
print('krishna excel')
print(krishna)
print()
# https://www.geeksforgeeks.org/how-to-search-a-value-within-a-pandas-dataframe-row/
print('month == july:')
food = input("Food:")
print(krishna[krishna['Month'] == 'july'])
print()
print(krishna[krishna['Digit'] == 10])

      