import pandas as pd
import os
import re
import glob
import numpy as np

listavuota = []
stock_names = []
path_stock_files = '/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dati ftsemib listino'

for filename in os.listdir(path_stock_files):
    print(filename)
    listavuota.append(filename)

for filecsv in listavuota:
    filecsv = re.sub('\.csv$', '', filecsv)
    stock_names.append(filecsv)

df = pd.concat(map(pd.read_csv, glob.glob(os.path.join(path_stock_files, '*.csv'))), axis=1)
Num_r = [i for i in range(6, df.shape[1], 7)]
df1 = df.iloc[:, Num_r]
df_final = pd.DataFrame(data=df1.values, columns=stock_names).dropna()
dates = pd.to_datetime(df.iloc[:, 0], dayfirst=True)  # format= #'%d/%m/%y')
# Setting dates as index and sorting from first 2019-04-7 to last 2021-02-19
df_final['Data'] = dates
df_final = df_final.set_index(df_final['Data'], drop=True)
df_final = df_final.sort_index()
del df_final['Data']

# df_final_2019 = df_final.loc['2019']
df_final_2020 = df_final.loc['2020']
no_assets = int(df_final_2020.shape[1])


df_final_2020_01 = df_final_2020.loc['2020-01']
df_final_2020_01.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_01_1.txt',header=False,index=False)
r_mean_2020_01 = pd.DataFrame.mean(df_final_2020_01).values.reshape(no_assets, 1)  # mean of returns
np.savetxt('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/r_mean_2020_01_1.txt', r_mean_2020_01)

df_final_2020_02 = df_final_2020.loc['2020-02']
df_final_2020_02.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_02_1.txt',header=False,index=False)
r_mean_2020_02 = pd.DataFrame.mean(df_final_2020_02).values.reshape(no_assets, 1)  # mean of returns
np.savetxt('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/r_mean_2020_02_1.txt', r_mean_2020_02)


df_final_2020_03 = df_final_2020.loc['2020-03']
df_final_2020_03.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_03_1.txt',header=False,index=False)
r_mean_2020_03 = pd.DataFrame.mean(df_final_2020_03).values.reshape(no_assets, 1)  # mean of returns
np.savetxt('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/r_mean_2020_03_1.txt', r_mean_2020_03)


df_final_2020_04 = df_final_2020.loc['2020-04']
df_final_2020_04.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_04_1.txt',header=False,index=False)
r_mean_2020_04 = pd.DataFrame.mean(df_final_2020_04).values.reshape(no_assets, 1)  # mean of returns
np.savetxt('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/r_mean_2020_04_1.txt', r_mean_2020_04)


df_final_2020_05 = df_final_2020.loc['2020-05']
df_final_2020_05.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_05_1.txt',header=False,index=False)
r_mean_2020_05 = pd.DataFrame.mean(df_final_2020_05).values.reshape(no_assets, 1)  # mean of returns
np.savetxt('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/r_mean_2020_05_1.txt', r_mean_2020_05)


df_final_2020_06 = df_final_2020.loc['2020-06']
df_final_2020_06.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_06_1.txt',header=False,index=False)
r_mean_2020_06 = pd.DataFrame.mean(df_final_2020_06).values.reshape(no_assets, 1)  # mean of returns
np.savetxt('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/r_mean_2020_06_1.txt', r_mean_2020_06)


df_final_2020_07 = df_final_2020.loc['2020-07']
df_final_2020_07.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_07_1.txt',header=False,index=False)
r_mean_2020_07 = pd.DataFrame.mean(df_final_2020_07).values.reshape(no_assets, 1)  # mean of returns
np.savetxt('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/r_mean_2020_07_1.txt', r_mean_2020_07)


df_final_2020_08 = df_final_2020.loc['2020-08']
df_final_2020_08.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_08_1.txt',header=False,index=False)
r_mean_2020_08 = pd.DataFrame.mean(df_final_2020_08).values.reshape(no_assets, 1)  # mean of returns
np.savetxt('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/r_mean_2020_08_1.txt', r_mean_2020_08)


df_final_2020_09 = df_final_2020.loc['2020-09']
df_final_2020_09.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_09_1.txt',header=False,index=False)
r_mean_2020_09 = pd.DataFrame.mean(df_final_2020_09).values.reshape(no_assets, 1)  # mean of returns
np.savetxt('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/r_mean_2020_09_1.txt', r_mean_2020_09)


df_final_2020_10 = df_final_2020.loc['2020-10']
df_final_2020_10.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_10_1.txt',header=False,index=False)
r_mean_2020_10 = pd.DataFrame.mean(df_final_2020_10).values.reshape(no_assets, 1)  # mean of returns
np.savetxt('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/r_mean_2020_10_1.txt', r_mean_2020_10)

df_final_2020_11 = df_final_2020.loc['2020-11']
df_final_2020_11.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_11_1.txt',header=False,index=False)
r_mean_2020_11 = pd.DataFrame.mean(df_final_2020_11).values.reshape(no_assets, 1)  # mean of returns
np.savetxt('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/r_mean_2020_11_1.txt', r_mean_2020_11)

df_final_2020_12 = df_final_2020.loc['2020-12']
df_final_2020_12.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_12_1.txt',header=False,index=False)
r_mean_2020_12 = pd.DataFrame.mean(df_final_2020_12).values.reshape(no_assets, 1)  # mean of returns
np.savetxt('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/r_mean_2020_12_1.txt', r_mean_2020_12)



df_ftsemib = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/FTSEMIB_MI.csv',header=0)
df_ftsemib['Date'] = pd.to_datetime(df_ftsemib['Date'])
df_ftsemib.set_index(df_ftsemib['Date'],drop=True,inplace=True)
del df_ftsemib['Date']
df_ftsemib_2020 = df_ftsemib.loc['2020']
a1 = df_ftsemib_2020.loc['2020-02']
a1.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_02.txt')

a2 = df_ftsemib_2020.loc['2020-03']
a2.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_03.txt')

a=df_ftsemib_2020.loc['2020-04']
a.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_04.txt')

b=df_ftsemib_2020.loc['2020-05']
b.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_05.txt')

c=df_ftsemib_2020.loc['2020-06']
c.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_06.txt')
d=df_ftsemib_2020.loc['2020-07']
d.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_07.txt')

e=df_ftsemib_2020.loc['2020-08']
e.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_08.txt')

f=df_ftsemib_2020.loc['2020-09']
f.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_09.txt')

g=df_ftsemib_2020.loc['2020-10']
g.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_10.txt')

h=df_ftsemib_2020.loc['2020-11']
h.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_11.txt')

i=df_ftsemib_2020.loc['2020-12']
i.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_12.txt')





