import pandas as pd
import numpy as np
from openpyxl import workbook
import matplotlib.pyplot as plt


year = [1950, 2000, 2010];
pop = [2.5, 3.5, 4];
# plt.plot(year, pop);
# plt.scatter(year, pop)
# plt.bar(year,pop)
# plt.pie(pop, labels=year, autopct='%1.2f%%')
# plt.xlabel('Year')
# plt.ylabel('Pop')
# # plt.yticks([2.5, 3.5, 4])
# plt.show();


# langs = ['C', 'C++', 'Java', 'Python', 'PHP']
# students = [23, 17, 35, 29, 12]
# plt.bar(langs, students)
# plt.pie(students, labels=langs, autopct='%1.2f%%')
# plt.show()





# df1 = pd.read_excel(r'/Users/farhan/Desktop/Experiment.xlsx');

# # setting first column as index
# df1.set_index('Id', drop = True, inplace = True)





# Co-relation between two columns
# print(df1['Pref'].corr(df1['Buy']));



# use it for missing values
# test = df1['Age'].interpolate(method='linear', limit_direction='forward', inplace=True);
# df1.to_excel('/Users/farhan/Desktop/Experiment.xlsx');
# print(test);



# creating pivot tables
# pivot = df1.pivot_table(index='Name', values = 'Age', aggfunc = np.mean);
# print(pivot);



# drop duplicates and remove them from excel sheet
# df1.drop_duplicates(['Name', 'Age'], keep='first', inplace=True);
# df1.to_excel('/Users/farhan/Desktop/Experiment.xlsx');



# Print rows where gender is null
# counter = 0;
# missing = pd.isnull(df1['Gender']);
# for value in missing:
#     if(value):
#         print(df1.loc[counter,'Id':'Name']);
#     counter = counter +1;



# same as using counter
# test = df1.isnull();
# rows = test.any(axis=1);
# print(df1[rows]['Name']);



# Replace missing values with 'F' and writing it in excel
# df1['Gender'].fillna('F',inplace = True);
# df1.to_excel('/Users/farhan/Desktop/Experiment.xlsx');

