import pandas as pd
import os
import re
import glob

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
df_final.to_csv('genetic_algo_progetto/po_with_moead-levy_/dat/df_final1.txt',header=False,index=False)

no_assets = int(df_final.shape[1])
returns_mean = pd.DataFrame.mean(df_final).values.reshape(no_assets, 1)  # mean of returns
returns_std = pd.DataFrame.std(df_final).values.reshape(no_assets, 1)  # std. of returns
cov_matrix =pd.DataFrame.cov(df_final)
df_ftsemib1 = pd.DataFrame([returns_mean[:,0],returns_std[:,0]]).transpose()
df_ftsemib1.to_csv('/home/davide/PycharmProjects/pythonProject2/genetic algo progetto/po_with_moead-levy_/dat/df_ftsemib1.txt',
                   index=False, header=False)






