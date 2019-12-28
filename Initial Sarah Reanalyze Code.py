import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

fpath = r"C:\Users\Admin\Documents\Masters Stuff\Meth_Patch_Practice.xlsx"
df = pd.read_excel(fpath, sep='\t')

'''Columns to add: Mouse Strain, Mouse Age, Mouse Number, Injection drug, Addiction Timepoint, Drug applied at the moment, 
Slice Number, Cell Number...  '''

sorted_dfa = df[(df['Injection Condition']=='Sal') & (df['Addiction Timepoint']=='Withdrawal')]
sorted_dfb = df[(df['Injection Condition']=='Meth') & (df['Addiction Timepoint']=='Withdrawal')]

unique_slicesa = set(sorted_dfa['Slice Number'])
unique_slicesb = set(sorted_dfb['Slice Number'])

'''Defines useful functions here'''
def Current_Drug_Assigner(df,sn,drugs,times):
    data = df[df['Slice Number']==sn]
    new_col = []
    for time in data['Time (ms)']:
        if time < times[0]:
            new_col.append(drugs[0])
        elif time < times[1]:
            new_col.append(drugs[1])
        elif time < times[2]:
            new_col.append(drugs[2])
        else :
            new_col.append('Unknown')

    return new_col

flatten = lambda l: [item for sublist in l for item in sublist]

'''Input lists'''
t_list = list(map((lambda x:x*60*1000),[5,15,20]))
d_list = ['Sulpiride','Meth + Sulpiride','Schopolimine + Sulpiride + Meth']

'''Creates drug column'''
new_col_list = []
for slice_number in unique_slicesa:
    new_col_list.append(Current_Drug_Assigner(sorted_dfa,slice_number,d_list,t_list))

sorted_dfa['Applied Drug'] =flatten(new_col_list)

new_col_listb = []
for slice_number in unique_slicesb:
    new_col_listb.append(Current_Drug_Assigner(sorted_dfb,slice_number,d_list,t_list))

sorted_dfb['Applied Drug'] =flatten(new_col_listb)

newdf = pd.concat([sorted_dfa,sorted_dfb])

pd.DataFrame.to_clipboard(newdf)








