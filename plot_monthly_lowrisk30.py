import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
#-------------------------------------------------------------------------------------¯¯#
# PLOT differenza di ritorni close-to-close tra il portafoglio ottimizzato e ftsemib 2020
# #dati con tutti i ritorni dei 40 stock
df_allstocks_02 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_02_1.txt',header=None)
#Cumulative returns ftse
ftsemib2020_02 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_02.txt',header=0)
ftsemib_cumulativeret_02 = ftsemib2020_02['return'].cumsum(axis=0)

#Dates
# date_ftse = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/FTSEMIB_MI.csv',header=0)
date_ftse_02 = pd.to_datetime(ftsemib2020_02['Date'])




#
#
#
#--------------------------------------------------------------------------------------------------------------------------#
#cumulative ret DEM n.30
lista_dem_30 = [2,4,5,11,15,20,25,30,32,34]
port_dem_30_02 = df_allstocks_02.iloc[:,lista_dem_30]
port_dem_30_02[2] = port_dem_30_02[2] * 2.52322840e-01  # diasorin
port_dem_30_02[4] = port_dem_30_02[4] *3.23125167e-02  # diasorin
port_dem_30_02[5] = port_dem_30_02[5] * 3.22876328e-03 # diasorin
port_dem_30_02[11] = port_dem_30_02[11] * 2.89231323e-02  # diasorin
port_dem_30_02[15] = port_dem_30_02[15] *2.23107075e-01 # banca mediolanum
port_dem_30_02[20] = port_dem_30_02[20] *1.36195781e-03 # banca mediolanum
port_dem_30_02[25] = port_dem_30_02[25] *1.11339449e-02 # banca mediolanum
port_dem_30_02[30] = port_dem_30_02[30] *2.70736585e-01  # banca mediolanum
port_dem_30_02[32] = port_dem_30_02[32] *1.71400273e-01  # banca mediolanum
port_dem_30_02[34] = port_dem_30_02[34] *4.65140550e-03  # banca mediolanum
port_dem_30_02['return'] = port_dem_30_02.sum(axis=1)
#port_dem_30_02['return'] = port_dem_30_02['return'].cumsum()
#
#Cumulative ret GA n.30
lista_ga_30 = [2,11,15,30,32,34]
port_ga_30_02 = df_allstocks_02.iloc[:,lista_ga_30]
port_ga_30_02[2] =port_ga_30_02[2] * 2.86854743e-01   # Amplifon
port_ga_30_02[11] =port_ga_30_02[11] * 6.75642855e-02    # Amplifon
#port_ga_30_02[9] =port_ga_30_02[9] * 5.24741831e-02 # banca mediolanum
port_ga_30_02[15] =port_ga_30_02[15] * 2.18055626e-01   # diasorin
port_ga_30_02[30] =port_ga_30_02[30] * 2.43736289e-01  # generali assicurazioni
port_ga_30_02[32] =port_ga_30_02[32] * 1.45139377e-01  # generali assicurazioni
port_ga_30_02[34] =port_ga_30_02[34] * 3.77237569e-02  # generali assicurazioni
port_ga_30_02['return'] = port_ga_30_02.sum(axis=1)
#
#cumulative ret LEVY n.30
lista_levy_30 = [2,4,11,15,30,32,34,36]
port_levy_30_02 = df_allstocks_02.iloc[:,lista_levy_30]
port_levy_30_02[2] = port_levy_30_02[2] * 2.57721785e-01
port_levy_30_02[4] = port_levy_30_02[4] * 3.61904307e-02 # enel
port_levy_30_02[11] = port_levy_30_02[11] * 9.63764305e-03 # enel
port_levy_30_02[15] = port_levy_30_02[15] * 2.29568426e-01
port_levy_30_02[30] = port_levy_30_02[30] * 2.50208832e-01
port_levy_30_02[32] = port_levy_30_02[32] * 1.60148201e-01    # enel
port_levy_30_02[34] = port_levy_30_02[34] * 1.11823139e-02   # Amplifon
port_levy_30_02[36] = port_levy_30_02[36] * 4.41922056e-02  # Amplifon
port_levy_30_02['return'] = port_levy_30_02.sum(axis=1)


#cumulative ret NSGA2 n.30
lista_nsga2_30 = [2,9,11,15,26,30,32,34]
port_nsga2_30_02 = df_allstocks_02.iloc[:,lista_nsga2_30]
port_nsga2_30_02[2] = port_nsga2_30_02[2] * 3.68539771e-01    # inwit
port_nsga2_30_02[9] = port_nsga2_30_02[9] * 1.77315648e-02   # inwit
port_nsga2_30_02[11] = port_nsga2_30_02[11] * 9.35427735e-02    # inwit
port_nsga2_30_02[15] = port_nsga2_30_02[15] * 2.48362253e-01
port_nsga2_30_02[26] = port_nsga2_30_02[26] * 1.15555381e-01
port_nsga2_30_02[30] = port_nsga2_30_02[30] * 3.16041995e-03
port_nsga2_30_02[32] = port_nsga2_30_02[32] * 1.32744109e-01
port_nsga2_30_02[34] = port_nsga2_30_02[34] * 1.97417677e-02
port_nsga2_30_02['return'] = port_nsga2_30_02.sum(axis=1)
#port_nsga2_30_02['return'] = port_nsga2_30_02['return'].cumsum()
#
# cumulative ret DE n.30
lista_de_30 = [4,9,15,21,26,30,32]
port_de_30_02 = df_allstocks_02.iloc[:,lista_de_30]
port_de_30_02[4] = port_de_30_02[4] * 5.10635782e-02
port_de_30_02[9] = port_de_30_02[9] * 1.11801073e-02
port_de_30_02[15] = port_de_30_02[15] * 3.35624078e-01
port_de_30_02[21] = port_de_30_02[21] * 1.92752483e-03
port_de_30_02[26] = port_de_30_02[26] * 5.36721310e-02
port_de_30_02[30] = port_de_30_02[30] * 2.24872226e-01
port_de_30_02[32] = port_de_30_02[32] * 3.21641309e-01
port_de_30_02['return'] = port_de_30_02.sum(axis=1)
#port_de_30_02['return'] = port_de_30_02['return'].cumsum()
#




#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
df_allstocks_03 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_03_1.txt',header=None)
#Cumulative returns ftse
ftsemib2020_03 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_03.txt',header=0)
ftsemib_cumulativeret_03 = ftsemib2020_03['return'].cumsum(axis=0)

#Dates
# date_ftse = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/FTSEMIB_MI.csv',header=0)
date_ftse_03 = pd.to_datetime(ftsemib2020_03['Date'])



# cum ret DEM n.30
lista_dem_30 = [8,13,21,22,24,27,33,34,35,37,38,39]
port_dem_30_03 = df_allstocks_03.iloc[:,lista_dem_30]
port_dem_30_03[34] = port_dem_30_03[34] * 7.68685855e-03  # diasorin
port_dem_30_03[8] = port_dem_30_03[8] * 1.66616945e-02 # diasorin
port_dem_30_03[13] = port_dem_30_03[13] * 3.84549074e-02  # diasorin
port_dem_30_03[21] = port_dem_30_03[21] *5.51428017e-02 # banca mediolanum
port_dem_30_03[22] = port_dem_30_03[22] *3.05253228e-02 # banca mediolanum
port_dem_30_03[24] = port_dem_30_03[24] *1.10029901e-01 # banca mediolanum
port_dem_30_03[27] = port_dem_30_03[27] *2.28092662e-01  # banca mediolanum
port_dem_30_03[33] = port_dem_30_03[33] *1.00499218e-01  # banca mediolanum
port_dem_30_03[35] = port_dem_30_03[35] *7.91415386e-03  # banca mediolanum
port_dem_30_03[37] = port_dem_30_03[37] *5.38041709e-02
port_dem_30_03[38] = port_dem_30_03[38] *1.13648499e-01  # banca mediolanum
port_dem_30_03[39] = port_dem_30_03[39] *2.36665425e-01  # banca mediolanum
port_dem_30_03['return'] = port_dem_30_03.sum(axis=1)
#port_dem_30_03['return'] = port_dem_30_03['return'].cumsum()
#
#Cumulative ret GA n.30
lista_ga_30 = [13,21,22,24,25,27,28,29,33,34,37,38,39]
port_ga_30_03 = df_allstocks_03.iloc[:,lista_ga_30]
port_ga_30_03[13] =port_ga_30_03[13] * 6.58690517e-02   # Amplifon
port_ga_30_03[21] =port_ga_30_03[21] * 7.92128532e-02    # Amplifon
port_ga_30_03[22] =port_ga_30_03[22] * 1.03305856e-02 # banca mediolanum
port_ga_30_03[24] =port_ga_30_03[24] * 1.24984530e-01
port_ga_30_03[25] =port_ga_30_03[25] * 7.21512344e-03 # banca mediolanum
port_ga_30_03[27] =port_ga_30_03[27] * 1.43767712e-01 # banca mediolanum
port_ga_30_03[29] =port_ga_30_03[29] * 3.84136621e-02
port_ga_30_03[33] =port_ga_30_03[33] * 6.39971880e-02
port_ga_30_03[34] =port_ga_30_03[34] * 1.57743041e-03
port_ga_30_03[37] =port_ga_30_03[37] * 3.92164026e-02
port_ga_30_03[28] =port_ga_30_03[28] * 1.95855241e-02 # generali assicurazioni
port_ga_30_03[38] =port_ga_30_03[38] * 2.06585537e-01  # generali assicurazioni
port_ga_30_03[39] =port_ga_30_03[39] * 1.98694043e-01 # generali assicurazioni
port_ga_30_03['return'] = port_ga_30_03.sum(axis=1)
#port_ga_30_03['return'] = port_ga_30_03['return'].cumsum()
#
#cumulative ret LEVY n.20
lista_levy_30 = [13,21,23,24,26,27,28,33,37,38,39]
port_levy_30_03 = df_allstocks_03.iloc[:,lista_levy_30]
port_levy_30_03[13] = port_levy_30_03[13] * 3.54589006e-02 # enel
port_levy_30_03[21] = port_levy_30_03[21] * 5.31911370e-02 # enel
port_levy_30_03[23] = port_levy_30_03[23] * 1.35813788e-01
port_levy_30_03[24] = port_levy_30_03[24] * 5.62872494e-02
port_levy_30_03[26] = port_levy_30_03[26] * 7.40285842e-03    # enel
port_levy_30_03[27] = port_levy_30_03[27] * 1.89276029e-01   # enel
port_levy_30_03[28] = port_levy_30_03[28] * 4.01392249e-02    # enel
port_levy_30_03[33] = port_levy_30_03[33] *7.12762900e-02
port_levy_30_03[37] = port_levy_30_03[37] * 4.31513639e-02
port_levy_30_03[38] = port_levy_30_03[38] * 2.37145725e-01   # enel
port_levy_30_03[39] = port_levy_30_03[39] * 1.87134007e-01   # Amplifon
port_levy_30_03['return'] = port_levy_30_03.sum(axis=1)
#port_levy_30_03['return'] = port_levy_30_03['return'].cumsum()

#cumulative ret NSGA2 n.20
lista_nsga2_30 = [3,21]
port_nsga2_30_03 = df_allstocks_03.iloc[:,lista_nsga2_30]
port_nsga2_30_03[3] = port_nsga2_30_03[3] * 8.13489906e-01    # inwit
port_nsga2_30_03[21] = port_nsga2_30_03[21] * 1.86312603e-01
port_nsga2_30_03['return'] = port_nsga2_30_03.sum(axis=1)
#port_nsga2_30_03['return'] = port_nsga2_30_03['return'].cumsum()
#
# cumulative ret DE n.20
lista_de_30 = [2,13,21,27,29,31,34]
port_de_30_03 = df_allstocks_03.iloc[:,lista_de_30]
# ritorni * pesi selezionati
port_de_30_03[2] = port_de_30_03[2] * 0.04147995
port_de_30_03[13] = port_de_30_03[13] * 0.10962705
port_de_30_03[27] = port_de_30_03[27] * 0.31130497
port_de_30_03[21] = port_de_30_03[21] * 0.06398787
port_de_30_03[29] = port_de_30_03[29] * 0.38131373
port_de_30_03[31] = port_de_30_03[31] * 0.03243227
port_de_30_03[34] = port_de_30_03[34] * 0.05985416
port_de_30_03['return'] = port_de_30_03.sum(axis=1)













#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
df_allstocks_04 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_04_1.txt',header=None)
#Cumulative returns ftse
ftsemib2020_04 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_04.txt',header=0)
ftsemib_cumulativeret_04 = ftsemib2020_04['return'].cumsum(axis=0)

#Dates
# date_ftse = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/FTSEMIB_MI.csv',header=0)
date_ftse_04 = pd.to_datetime(ftsemib2020_04['Date'])


# cum ret DEM n.30
lista_dem_30 = [13,17,19,24,27,36,38]
port_dem_30_04 = df_allstocks_04.iloc[:,lista_dem_30]
port_dem_30_04[13] = port_dem_30_04[13] *0.13825717  # diasorin
port_dem_30_04[17] = port_dem_30_04[17] * 0.08913146 # diasorin
port_dem_30_04[38] = port_dem_30_04[38] * 0.00632596  # diasorin
port_dem_30_04[19] = port_dem_30_04[19] *0.10868075 # banca mediolanum
port_dem_30_04[27] = port_dem_30_04[27] *0.3208298 # banca mediolanum
port_dem_30_04[36] = port_dem_30_04[36] *0.29279083 # banca mediolanum
port_dem_30_04[24] = port_dem_30_04[24] *0.04392838 # banca mediolanum
port_dem_30_04['return'] = port_dem_30_04.sum(axis=1)
#port_dem_30_04['return'] = port_dem_30_04['return'].cumsum()
#
#Cumulative ret GA n.30
lista_ga_30 = [13,15,17,19,24,27,36]
port_ga_30_04 = df_allstocks_04.iloc[:,lista_ga_30]
port_ga_30_04[13] =port_ga_30_04[13] * 1.30900489e-01   # Amplifon
port_ga_30_04[15] =port_ga_30_04[15] * 1.15098311e-02    # Amplifon
port_ga_30_04[17] =port_ga_30_04[17] * 9.86901689e-02 # banca mediolanum
port_ga_30_04[24] =port_ga_30_04[24] * 4.45270590e-02   # diasorin
port_ga_30_04[27] =port_ga_30_04[27] * 3.45679671e-01  # generali assicurazioni
port_ga_30_04[36] =port_ga_30_04[36] * 2.84051015e-01  # generali assicurazioni
port_ga_30_04[19] =port_ga_30_04[19] * 8.46307421e-02  # generali assicurazioni
port_ga_30_04['return'] = port_ga_30_04.sum(axis=1)
#port_ga_30_04['return'] = port_ga_30_04['return'].cumsum()
#
#cumulative ret LEVY n.30
lista_levy_30 = [13,17,19,24,27,28,36]
port_levy_30_04 = df_allstocks_04.iloc[:,lista_levy_30]
port_levy_30_04[13] = port_levy_30_04[13] * 1.31265730e-01 # enel
port_levy_30_04[17] = port_levy_30_04[17] * 1.35302544e-01 # enel
port_levy_30_04[19] = port_levy_30_04[19] * 1.16827156e-01
port_levy_30_04[24] = port_levy_30_04[24] * 6.36884332e-02
port_levy_30_04[28] = port_levy_30_04[28] * 1.29052147e-03    # enel
port_levy_30_04[27] = port_levy_30_04[27] * 2.75304365e-01    # enel
port_levy_30_04[36] = port_levy_30_04[36] * 2.75378295e-01    # enel
port_levy_30_04['return'] = port_levy_30_04.sum(axis=1)
#port_levy_30_04['return'] = port_levy_30_04['return'].cumsum()

#cumulative ret NSGA2 n.20
lista_nsga2_30 = [15,27]
port_nsga2_30_04 = df_allstocks_04.iloc[:,lista_nsga2_30]
port_nsga2_30_04[15] = port_nsga2_30_04[15] * 1.68537685e-01    # inwit
port_nsga2_30_04[27] = port_nsga2_30_04[27] * 8.31395661e-01
port_nsga2_30_04['return'] = port_nsga2_30_04.sum(axis=1)

# cumulative ret DE n.20
lista_de_30 = [13,15,19]
port_de_30_04 = df_allstocks_04.iloc[:,lista_de_30]
# ritorni * pesi selezionati
#port_de_30_04[1] = port_de_30_04[1] * 0.10897238
port_de_30_04[13] = port_de_30_04[13] * 0.28614454
port_de_30_04[15] = port_de_30_04[15] * 0.28275946
port_de_30_04[19] = port_de_30_04[19] * 0.431096
port_de_30_04['return'] = port_de_30_04.sum(axis=1)




























#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
df_allstocks_05 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_05_1.txt',header=None)
#Cumulative returns ftse
ftsemib2020_05 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_05.txt',header=0)
ftsemib_cumulativeret_05 = ftsemib2020_05['return'].cumsum(axis=0)

#Dates
# date_ftse = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/FTSEMIB_MI.csv',header=0)
date_ftse_05 = pd.to_datetime(ftsemib2020_05['Date'])



# cum ret DEM n.30
lista_dem_30 = [2,5,7,8,9,12,13,15,16,17,21,25,36]
port_dem_30_05 = df_allstocks_05.iloc[:,lista_dem_30]
port_dem_30_05[2] = port_dem_30_05[2] *3.31383608e-03  # diasorin
port_dem_30_05[5] = port_dem_30_05[5] * 1.46949647e-03 # diasorin
port_dem_30_05[7] = port_dem_30_05[7] * 1.34277646e-03 # diasorin
port_dem_30_05[8] = port_dem_30_05[8] * 1.76387069e-01  # diasorin
port_dem_30_05[9] = port_dem_30_05[9] *4.42997857e-02 # banca mediolanum
port_dem_30_05[12] = port_dem_30_05[12] *1.89100510e-01 # banca mediolanum
port_dem_30_05[13] = port_dem_30_05[13] *2.28203672e-01# banca mediolanum
port_dem_30_05[15] = port_dem_30_05[15] *1.71037251e-01 # banca mediolanum
port_dem_30_05[16] = port_dem_30_05[16] *7.34658053e-03  # banca mediolanum
port_dem_30_05[17] = port_dem_30_05[17] *6.13432725e-03  # banca mediolanum
port_dem_30_05[21] = port_dem_30_05[21] *3.29634343e-03  # banca mediolanum
port_dem_30_05[25] = port_dem_30_05[25] *3.79493845e-02
port_dem_30_05[36] = port_dem_30_05[36] *1.28702125e-01
port_dem_30_05['return'] = port_dem_30_05.sum(axis=1)
#port_dem_30_05['return'] = port_dem_30_05['return'].cumsum()
#
#Cumulative ret GA n.30
lista_ga_30 = [2,8,9,12,13,15,24,25,27,36]
port_ga_30_05 = df_allstocks_05.iloc[:,lista_ga_30]
port_ga_30_05[2] =port_ga_30_05[2] * 5.96388223e-02  # Amplifon
port_ga_30_05[8] =port_ga_30_05[8] * 1.03208259e-01    # Amplifon
port_ga_30_05[9] =port_ga_30_05[9] * 1.38864717e-01 # banca mediolanum
port_ga_30_05[12] =port_ga_30_05[12] * 1.02178861e-01   # diasorin
port_ga_30_05[13] =port_ga_30_05[13] * 1.63590518e-01  # generali assicurazioni
port_ga_30_05[15] =port_ga_30_05[15] *1.76340617e-01  # generali assicurazioni
port_ga_30_05[24] =port_ga_30_05[24] * 4.71769856e-02  # generali assicurazioni
port_ga_30_05[25] =port_ga_30_05[25] * 3.91118620e-02
port_ga_30_05[27] = port_ga_30_05[27] *1.22199473e-02
port_ga_30_05[36] = port_ga_30_05[36] * 1.57554710e-01
port_ga_30_05['return'] = port_ga_30_05.sum(axis=1)
#port_ga_30_05['return'] = port_ga_30_05['return'].cumsum()
#
#cumulative ret LEVY n.30
lista_levy_30 = [2,8,9,12,13,15,24,25,27,36]
port_levy_30_05 = df_allstocks_05.iloc[:,lista_levy_30]
port_levy_30_05[2] = port_levy_30_05[2] * 4.24869339e-02
port_levy_30_05[8] = port_levy_30_05[8] * 1.03519820e-01 # enel
port_levy_30_05[9] = port_levy_30_05[9] * 1.85407447e-01 # enel
port_levy_30_05[12] = port_levy_30_05[12] * 1.05358916e-01
port_levy_30_05[13] = port_levy_30_05[13] * 1.42947356e-01
port_levy_30_05[15] = port_levy_30_05[15] * 1.62064172e-01    # enel
port_levy_30_05[24] = port_levy_30_05[24] * 4.84211765e-02    # enel
port_levy_30_05[25] = port_levy_30_05[25] *3.88968510e-02    # enel
port_levy_30_05[27] = port_levy_30_05[27] * 2.25226099e-02    # enel
port_levy_30_05[36] = port_levy_30_05[36] * 1.48342672e-01   # Amplifon
port_levy_30_05['return'] = port_levy_30_05.sum(axis=1)
#port_levy_30_05['return'] = port_levy_30_05['return'].cumsum()

#cumulative ret NSGA2 n.30
lista_nsga2_30 = [13,15,27,36,37]
port_nsga2_30_05 = df_allstocks_05.iloc[:,lista_nsga2_30]
#port_nsga2_30_05[3] = port_nsga2_30_05[3] * 9.08406690e-02    # inwit
port_nsga2_30_05[13] = port_nsga2_30_05[13] * 2.25431579e-01   # inwit
port_nsga2_30_05[15] = port_nsga2_30_05[15] * 2.95075425e-01    # inwit
port_nsga2_30_05[27] = port_nsga2_30_05[27] *2.01334216e-03
port_nsga2_30_05[36] = port_nsga2_30_05[36] * 3.17485990e-01
port_nsga2_30_05[37] = port_nsga2_30_05[37] * 1.59920715e-01
port_nsga2_30_05['return'] = port_nsga2_30_05.sum(axis=1)

# cumulative ret DE n.20
lista_de_30 = [0,1,3,6,7,8,9,14,15,17,18,22,24,27,29,30,31,34,35,36,37,38,39]
port_de_30_05 = df_allstocks_05.iloc[:,lista_de_30]
# ritorni * pesi selezionati
port_de_30_05[0] = port_de_30_05[0] * 0.01064318
port_de_30_05[1] = port_de_30_05[1] * 0.00349856
port_de_30_05[3] = port_de_30_05[3] *0.01103864
port_de_30_05[6] = port_de_30_05[6] * 0.02837917
port_de_30_05[7] = port_de_30_05[7] * 0.01071539
port_de_30_05[8] = port_de_30_05[8] * 0.16401806
port_de_30_05[9] = port_de_30_05[9] * 0.05913193
port_de_30_05[14] = port_de_30_05[14] * 0.00714803
port_de_30_05[15] = port_de_30_05[15] * 0.02838016
port_de_30_05[17] = port_de_30_05[17] * 0.00798063
port_de_30_05[18] = port_de_30_05[18] *0.28511318
port_de_30_05[22] = port_de_30_05[22] * 0.02617575
port_de_30_05[24] = port_de_30_05[24] * 0.01154618
port_de_30_05[27] = port_de_30_05[27] * 0.02925893
port_de_30_05[29] = port_de_30_05[29] * 0.02318791
port_de_30_05[30] = port_de_30_05[30] * 0.04998185
port_de_30_05[31] = port_de_30_05[31] * 0.00142512
port_de_30_05[34] = port_de_30_05[34] * 0.01445805
port_de_30_05[35] = port_de_30_05[35] * 0.01929816
port_de_30_05[36] = port_de_30_05[36] * 0.11217985
port_de_30_05[37] = port_de_30_05[37] * 0.02528978
port_de_30_05[38] = port_de_30_05[38] * 0.02448652
port_de_30_05[39] = port_de_30_05[39] * 0.04605697
port_de_30_05['return'] = port_de_30_05.sum(axis=1)



















#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
df_allstocks_06 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_06_1.txt',header=None)
#Cumulative returns ftse
ftsemib2020_06 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_06.txt',header=0)
ftsemib_cumulativeret_06 = ftsemib2020_06['return'].cumsum(axis=0)

#Dates
# date_ftse = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/FTSEMIB_MI.csv',header=0)
date_ftse_06 = pd.to_datetime(ftsemib2020_06['Date'])


# cum ret DEM n.30
lista_dem_30 = [5,7,12,14,15,16,17,22,25,27,31]
port_dem_30_06 = df_allstocks_06.iloc[:,lista_dem_30]
port_dem_30_06[5] = port_dem_30_06[5] *5.16932470e-03  # diasorin
port_dem_30_06[7] = port_dem_30_06[7] * 9.22957433e-03 # diasorin
port_dem_30_06[12] = port_dem_30_06[12] *4.12744560e-03 # diasorin
port_dem_30_06[14] = port_dem_30_06[14] * 3.86974777e-02  # diasorin
port_dem_30_06[15] = port_dem_30_06[15] *4.11753746e-01 # banca mediolanum
port_dem_30_06[16] = port_dem_30_06[16] *1.26155423e-01 # banca mediolanum
port_dem_30_06[17] = port_dem_30_06[17] *1.32049947e-01# banca mediolanum
port_dem_30_06[22] = port_dem_30_06[22] *1.25415873e-02 # banca mediolanum
port_dem_30_06[25] = port_dem_30_06[25] *1.09567193e-01  # banca mediolanum
port_dem_30_06[27] = port_dem_30_06[27] *1.46327154e-01  # banca mediolanum
port_dem_30_06[31] = port_dem_30_06[31] *1.57269888e-03  # banca mediolanum
#port_dem_30_06[39] = port_dem_30_06[39] *2.49230293e-01  # banca mediolanum
port_dem_30_06['return'] = port_dem_30_06.sum(axis=1)
#port_dem_30_06['return'] = port_dem_30_06['return'].cumsum()
#
#Cumulative ret GA n.30
lista_ga_30 = [9,11,15,16,17,22,27,32]
port_ga_30_06 = df_allstocks_06.iloc[:,lista_ga_30]
port_ga_30_06[11] =port_ga_30_06[11] *8.26004479e-03   # Amplifon
port_ga_30_06[9] =port_ga_30_06[9] * 2.24112925e-02    # Amplifon
port_ga_30_06[15] =port_ga_30_06[15] * 3.64437628e-01 # diasorin
port_ga_30_06[16] =port_ga_30_06[16] * 1.51153443e-01 # generali assicurazioni
port_ga_30_06[17] =port_ga_30_06[17] * 1.50034584e-01  # generali assicurazioni
port_ga_30_06[22] =port_ga_30_06[22] * 9.40406662e-03  # generali assicurazioni
port_ga_30_06[27] =port_ga_30_06[27] * 2.30812030e-01  # generali assicurazioni
port_ga_30_06[32] =port_ga_30_06[32] * 6.27057011e-02  # generali assicurazioni
port_ga_30_06['return'] = port_ga_30_06.sum(axis=1)
#port_ga_30_06['return'] = port_ga_30_06['return'].cumsum()
#
#cumulative ret LEVY n.30
lista_levy_30 = [15,16,17,22,25,27,38]
port_levy_30_06 = df_allstocks_06.iloc[:,lista_levy_30]
port_levy_30_06[15] = port_levy_30_06[15] * 4.07532607e-01
port_levy_30_06[16] = port_levy_30_06[16] * 9.32390682e-02 # enel
port_levy_30_06[17] = port_levy_30_06[17] * 1.38886182e-01 # enel
port_levy_30_06[22] = port_levy_30_06[22] * 3.96540962e-02
port_levy_30_06[25] = port_levy_30_06[25] * 1.12917394e-01
#port_levy_30_06[26] = port_levy_30_06[26] * 9.51489648e-02    # enel
port_levy_30_06[27] = port_levy_30_06[27] * 1.33537589e-01    # enel
port_levy_30_06[38] = port_levy_30_06[38] *7.28557161e-02    # enel
port_levy_30_06['return'] = port_levy_30_06.sum(axis=1)
#port_levy_30_06['return'] = port_levy_30_06['return'].cumsum()

#cumulative ret NSGA2 n.30
lista_nsga2_30 = [14,15,16,17,22,25,27,31,32,36,38]
port_nsga2_30_06 = df_allstocks_06.iloc[:,lista_nsga2_30]
port_nsga2_30_06[14] = port_nsga2_30_06[14] * 7.88349981e-03    # inwit
port_nsga2_30_06[15] = port_nsga2_30_06[15] * 2.36765211e-01   # inwit
port_nsga2_30_06[16] = port_nsga2_30_06[16] * 7.45943243e-02    # inwit
port_nsga2_30_06[17] = port_nsga2_30_06[17] * 1.37253445e-01
port_nsga2_30_06[22] = port_nsga2_30_06[22] * 1.32875950e-01
port_nsga2_30_06[25] = port_nsga2_30_06[25] * 6.65329595e-02
port_nsga2_30_06[27] = port_nsga2_30_06[27] *5.27684505e-02
port_nsga2_30_06[31] = port_nsga2_30_06[31] * 4.70190778e-03
port_nsga2_30_06[32] = port_nsga2_30_06[32] * 2.15167394e-02
port_nsga2_30_06[36] = port_nsga2_30_06[36] * 2.33494340e-01
port_nsga2_30_06[38] = port_nsga2_30_06[38] * 2.89432685e-02
port_nsga2_30_06['return'] = port_nsga2_30_06.sum(axis=1)
#port_nsga2_30_06['return'] = port_nsga2_30_06['return'].cumsum()
#
# cumulative ret DE n.30
lista_de_30 = [5,9,15,16,25,32]
port_de_30_06 = df_allstocks_06.iloc[:,lista_de_30]
# ritorni * pesi selezionati
port_de_30_06[5] = port_de_30_06[5] * 0.02530905
port_de_30_06[9] = port_de_30_06[9] * 0.10782503
port_de_30_06[15] = port_de_30_06[15] *0.50875003
port_de_30_06[16] = port_de_30_06[16] * 0.15934494
port_de_30_06[25] = port_de_30_06[25] * 0.12538722
port_de_30_06[32] = port_de_30_06[32] * 0.07338373
#port_de_30_06[37] = port_de_30_06[37] * 3.56565226e-01
port_de_30_06['return'] = port_de_30_06.sum(axis=1)


















#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
df_allstocks_07 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_07_1.txt',header=None)
#Cumulative returns ftse
ftsemib2020_07 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_07.txt',header=0)
ftsemib_cumulativeret_07 = ftsemib2020_07['return'].cumsum(axis=0)

#Dates
# date_ftse = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/FTSEMIB_MI.csv',header=0)
date_ftse_07 = pd.to_datetime(ftsemib2020_07['Date'])


# cum ret DEM n.30
lista_dem_30 = [2,3,6,8,9,12,20,22,27,29,36,38]
port_dem_30_07 = df_allstocks_07.iloc[:,lista_dem_30]
port_dem_30_07[2] = port_dem_30_07[2] *2.57905965e-01  # diasorin
port_dem_30_07[3] = port_dem_30_07[3] * 1.27380462e-01 # diasorin
port_dem_30_07[6] = port_dem_30_07[6] * 4.48582889e-02 # diasorin
port_dem_30_07[8] = port_dem_30_07[8] * 7.24423665e-03  # diasorin
port_dem_30_07[9] = port_dem_30_07[9] *9.50184166e-02 # banca mediolanum
port_dem_30_07[12] = port_dem_30_07[12] *1.05804229e-01 # banca mediolanum
port_dem_30_07[20] = port_dem_30_07[20] *4.12983390e-03 # banca mediolanum
port_dem_30_07[22] = port_dem_30_07[22] *1.89725781e-03 # banca mediolanum
port_dem_30_07[27] = port_dem_30_07[27] *1.35456832e-02  # banca mediolanum
port_dem_30_07[29] = port_dem_30_07[29] *7.76800954e-02  # banca mediolanum
port_dem_30_07[36] = port_dem_30_07[36] *1.38499147e-01  # banca mediolanum
port_dem_30_07[38] = port_dem_30_07[38] *1.25277091e-01  # banca mediolanum
port_dem_30_07['return'] = port_dem_30_07.sum(axis=1)
#port_dem_30_07['return'] = port_dem_30_07['return'].cumsum()
#
#Cumulative ret GA n.30
lista_ga_30 = [2,3,6,9,12,27,29,36,37]
port_ga_30_07 = df_allstocks_07.iloc[:,lista_ga_30]
port_ga_30_07[2] =port_ga_30_07[2] *2.18545082e-01   # Amplifon
port_ga_30_07[3] =port_ga_30_07[3] * 1.19575012e-01    # Amplifon
port_ga_30_07[6] =port_ga_30_07[6] * 4.03306521e-02 # banca mediolanum
port_ga_30_07[9] =port_ga_30_07[9] * 1.60169783e-01  # diasorin
port_ga_30_07[12] =port_ga_30_07[12] * 1.26895925e-01  # generali assicurazioni
port_ga_30_07[27] =port_ga_30_07[27] * 6.85844228e-02  # generali assicurazioni
port_ga_30_07[29] =port_ga_30_07[29] * 9.34488403e-02  # generali assicurazioni
port_ga_30_07[36] =port_ga_30_07[36] * 1.11986275e-01  # generali assicurazioni
port_ga_30_07[37] =port_ga_30_07[37] * 6.03382536e-02  # generali assicurazioni
port_ga_30_07['return'] = port_ga_30_07.sum(axis=1)
#port_ga_30_07['return'] = port_ga_30_07['return'].cumsum()
#
#cumulative ret LEVY n.30
lista_levy_30 = [2,3,6,9,12,27,29,36,37,38,39]
port_levy_30_07 = df_allstocks_07.iloc[:,lista_levy_30]
port_levy_30_07[2] = port_levy_30_07[2] * 2.00719586e-01
port_levy_30_07[3] = port_levy_30_07[3] * 9.19583202e-02 # enel
port_levy_30_07[6] = port_levy_30_07[6] * 6.35219746e-02 # enel
port_levy_30_07[9] = port_levy_30_07[9] * 1.18596745e-01
port_levy_30_07[12] = port_levy_30_07[12] * 6.16222135e-02
port_levy_30_07[27] = port_levy_30_07[27] * 1.22329701e-01   # enel
port_levy_30_07[29] = port_levy_30_07[29] *1.57408336e-01    # enel
port_levy_30_07[36] = port_levy_30_07[36] * 9.04582723e-02    # enel
port_levy_30_07[37] = port_levy_30_07[37] * 3.38579950e-02
port_levy_30_07[38] = port_levy_30_07[38] *5.81784499e-02
port_levy_30_07[39] = port_levy_30_07[39] * 1.02371969e-03
port_levy_30_07['return'] = port_levy_30_07.sum(axis=1)
#port_levy_30_07['return'] = port_levy_30_07['return'].cumsum()

#cumulative ret NSGA2 n.30
lista_nsga2_30 = [3,9,12,37]
port_nsga2_30_07 = df_allstocks_07.iloc[:,lista_nsga2_30]
# inwit
port_nsga2_30_07[3] = port_nsga2_30_07[3] * 1.99308864e-03  # inwit
port_nsga2_30_07[9] = port_nsga2_30_07[9] * 1.91208109e-02    # inwit
port_nsga2_30_07[12] = port_nsga2_30_07[12] * 4.13490797e-02
port_nsga2_30_07[37] = port_nsga2_30_07[37] * 9.36203792e-01
port_nsga2_30_07['return'] = port_nsga2_30_07.sum(axis=1)
#port_nsga2_30_07['return'] = port_nsga2_30_07['return'].cumsum()
#
# cumulative ret DE n.30
lista_de_30 = [6,23,28,29,36]
port_de_30_07 = df_allstocks_07.iloc[:,lista_de_30]
# ritorni * pesi selezionati
port_de_30_07[6] = port_de_30_07[6] * 0.28628972
port_de_30_07[23] = port_de_30_07[23] * 0.01373511
port_de_30_07[28] = port_de_30_07[28] *0.07649779
port_de_30_07[29] = port_de_30_07[29] * 0.39007146
port_de_30_07[36] = port_de_30_07[36] * 0.23340592
port_de_30_07['return'] = port_de_30_07.sum(axis=1)





















#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
df_allstocks_08 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_08_1.txt',header=None)
#Cumulative returns ftse
ftsemib2020_08 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_08.txt',header=0)
ftsemib_cumulativeret_08 = ftsemib2020_08['return'].cumsum(axis=0)

#Dates
# date_ftse = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/FTSEMIB_MI.csv',header=0)
date_ftse_08 = pd.to_datetime(ftsemib2020_08['Date'])


# cum ret DEM n.30
lista_dem_30 = [2,6,12,15,25,27,28,31,32,34,37]
port_dem_30_08 = df_allstocks_08.iloc[:,lista_dem_30]
port_dem_30_08[2] = port_dem_30_08[2] *0.02403096  # diasorin
port_dem_30_08[6] = port_dem_30_08[6] * 0.01102389 # diasorin
port_dem_30_08[12] = port_dem_30_08[12] * 0.06220418 # diasorin
port_dem_30_08[15] = port_dem_30_08[15] * 0.14519476  # diasorin
port_dem_30_08[25] = port_dem_30_08[25] *0.17606105 # banca mediolanum
port_dem_30_08[27] = port_dem_30_08[27] *0.38773921 # banca mediolanum
port_dem_30_08[28] = port_dem_30_08[28] *0.01313635# banca mediolanum
port_dem_30_08[31] = port_dem_30_08[31] *0.02933299 # banca mediolanum
port_dem_30_08[32] = port_dem_30_08[32] *0.14671379  # banca mediolanum
port_dem_30_08[34] = port_dem_30_08[34] *0.00102014  # banca mediolanum
port_dem_30_08[37] = port_dem_30_08[37] *0.0019909   # banca mediolanum
port_dem_30_08['return'] = port_dem_30_08.sum(axis=1)


#Cumulative ret GA n.30
lista_ga_30 = [2,6,12,15,25,27,31,32]
port_ga_30_08 = df_allstocks_08.iloc[:,lista_ga_30]
port_ga_30_08[2] =port_ga_30_08[2] *9.10134440e-02   # Amplifon
port_ga_30_08[6] =port_ga_30_08[6] * 1.08881043e-02    # Amplifon
port_ga_30_08[12] =port_ga_30_08[12] * 6.33582024e-02 # banca mediolanum
port_ga_30_08[15] =port_ga_30_08[15] * 4.45806617e-02  # diasorin
port_ga_30_08[25] =port_ga_30_08[25] * 1.75061803e-01  # generali assicurazioni
port_ga_30_08[27] =port_ga_30_08[27] * 3.40937264e-01  # generali assicurazioni
port_ga_30_08[31] =port_ga_30_08[31] * 4.01114670e-02  # generali assicurazioni
port_ga_30_08[32] =port_ga_30_08[32] * 2.33242726e-01  # generali assicurazioni
port_ga_30_08['return'] = port_ga_30_08.sum(axis=1)


#cumulative ret LEVY n.30
lista_levy_30 = [2,6,7,12,15,25,27,31,32]
port_levy_30_08 = df_allstocks_08.iloc[:,lista_levy_30]
port_levy_30_08[2] = port_levy_30_08[2] * 2.85969978e-02
port_levy_30_08[6] = port_levy_30_08[6] * 2.68837267e-02 # enel
port_levy_30_08[7] = port_levy_30_08[7] * 5.87285431e-03 # enel
port_levy_30_08[12] = port_levy_30_08[12] *7.43727323e-02
port_levy_30_08[15] = port_levy_30_08[15] * 1.43593128e-03
port_levy_30_08[25] = port_levy_30_08[25] * 1.72025702e-01    # enel
port_levy_30_08[27] = port_levy_30_08[27] * 4.04449512e-01  # enel
port_levy_30_08[31] = port_levy_30_08[31] *6.02305743e-02   # enel
port_levy_30_08[32] = port_levy_30_08[32] * 2.26081652e-01    # enel
port_levy_30_08['return'] = port_levy_30_08.sum(axis=1)


#cumulative ret NSGA2 n.30
lista_nsga2_30 = [2,6,12,15,25,27,31,32]
port_nsga2_30_08 = df_allstocks_08.iloc[:,lista_nsga2_30]
port_nsga2_30_08[2] = port_nsga2_30_08[2] * 9.44596432e-02    # inwit
port_nsga2_30_08[6] = port_nsga2_30_08[6] * 8.42806872e-03   # inwit
port_nsga2_30_08[12] = port_nsga2_30_08[12] * 6.03072968e-02    # inwit
port_nsga2_30_08[15] = port_nsga2_30_08[15] * 5.23580472e-02
port_nsga2_30_08[25] = port_nsga2_30_08[25] * 2.18878931e-01
port_nsga2_30_08[27] = port_nsga2_30_08[27] *3.27662652e-01
port_nsga2_30_08[31] = port_nsga2_30_08[31] * 4.30322434e-02
port_nsga2_30_08[32] = port_nsga2_30_08[32] * 1.94782663e-01
port_nsga2_30_08['return'] = port_nsga2_30_08.sum(axis=1)
#port_nsga2_30_08['return'] = port_nsga2_30_08['return'].cumsum()
#
# cumulative ret DE n.30
lista_de_30 = [2,15,27]
port_de_30_08 = df_allstocks_08.iloc[:,lista_de_30]
# ritorni * pesi selezionati
port_de_30_08[2] = port_de_30_08[2] * 0.15311417
port_de_30_08[15] = port_de_30_08[15] * 0.27712293
port_de_30_08[27] = port_de_30_08[27] *0.56976289
port_de_30_08['return'] = port_de_30_08.sum(axis=1)

























#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
df_allstocks_09 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_09_1.txt',header=None)
#Cumulative returns ftse
ftsemib2020_09 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_09.txt',header=0)
ftsemib_cumulativeret_09 = ftsemib2020_09['return'].cumsum(axis=0)

#Dates
# date_ftse = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/FTSEMIB_MI.csv',header=0)
date_ftse_09 = pd.to_datetime(ftsemib2020_09['Date'])


# cum ret DEM n.30
lista_dem_30 = [0,1,4,14,25,28,31,32]
port_dem_30_09 = df_allstocks_09.iloc[:,lista_dem_30]
port_dem_30_09[0] = port_dem_30_09[0] *0.24947416  # diasorin
port_dem_30_09[1] = port_dem_30_09[1] * 0.00192391 # diasorin
port_dem_30_09[4] = port_dem_30_09[4] * 0.12336422 # diasorin
port_dem_30_09[14] = port_dem_30_09[14] * 0.06392887  # diasorin
port_dem_30_09[28] = port_dem_30_09[28] *0.01724333 # banca mediolanum
port_dem_30_09[25] = port_dem_30_09[25] *0.35627475# banca mediolanum
port_dem_30_09[31] = port_dem_30_09[31] *0.0526378# banca mediolanum
port_dem_30_09[32] = port_dem_30_09[32] *0.13515295 # banca mediolanum
port_dem_30_09['return'] = port_dem_30_09.sum(axis=1)

#
#Cumulative ret GA n.30
lista_ga_30 = [0,1,3,4,6,8,21,25,27,31,32,39]
port_ga_30_09 = df_allstocks_09.iloc[:,lista_ga_30]
port_ga_30_09[0] =port_ga_30_09[0] *2.07043801e-01   # Amplifon
port_ga_30_09[1] =port_ga_30_09[1] * 1.40054140e-01    # Amplifon
#port_ga_30_09[2] =port_ga_30_09[2] * 4.33847650e-02 # banca mediolanum
port_ga_30_09[3] =port_ga_30_09[3] * 2.73619506e-03  # diasorin
port_ga_30_09[4] =port_ga_30_09[4] * 4.00384816e-02  # generali assicurazioni
port_ga_30_09[6] =port_ga_30_09[6] * 1.14151061e-01  # generali assicurazioni
port_ga_30_09[8] =port_ga_30_09[8] * 5.19594202e-03  # generali assicurazioni
port_ga_30_09[21] =port_ga_30_09[21] * 2.03136685e-01  # generali assicurazioni
port_ga_30_09[25] =port_ga_30_09[25] * 1.66105044e-01  # generali assicurazioni
port_ga_30_09[27] =port_ga_30_09[27] * 1.16150158e-03  # generali assicurazioni
port_ga_30_09[31] =port_ga_30_09[31] * 2.52377739e-02  # generali assicurazioni
port_ga_30_09[32] =port_ga_30_09[32] * 8.75587774e-02  # generali assicurazioni
port_ga_30_09[39] =port_ga_30_09[39] * 7.48224132e-03
port_ga_30_09['return'] = port_ga_30_09.sum(axis=1)
#port_ga_30_09['return'] = port_ga_30_09['return'].cumsum()
#
#cumulative ret LEVY n.30
lista_levy_30 = [0,1,4,6,8,14,21,25,31,32]
port_levy_30_09 = df_allstocks_09.iloc[:,lista_levy_30]
port_levy_30_09[0] = port_levy_30_09[0] * 1.85683310e-01
port_levy_30_09[1] = port_levy_30_09[1] * 8.06251954e-02 # enel
port_levy_30_09[4] = port_levy_30_09[4] * 4.82891881e-02
port_levy_30_09[6] = port_levy_30_09[6] * 5.94900288e-02    # enel
port_levy_30_09[8] = port_levy_30_09[8] * 2.94428223e-02  # enel
port_levy_30_09[14] = port_levy_30_09[14] * 3.78968231e-02  # enel
port_levy_30_09[21] = port_levy_30_09[21] * 1.79628379e-01    # enel
port_levy_30_09[25] = port_levy_30_09[25] * 2.62337172e-01  # Amplifon
port_levy_30_09[31] = port_levy_30_09[31] * 6.17902313e-02
port_levy_30_09[32] = port_levy_30_09[32] * 5.48096093e-02   # Amplifon
port_levy_30_09['return'] = port_levy_30_09.sum(axis=1)



#cumulative ret NSGA2 n.30
lista_nsga2_30 = [0,1,4,6,8,13,21,25,27,28,38,39]
port_nsga2_30_09 = df_allstocks_09.iloc[:,lista_nsga2_30]
port_nsga2_30_09[0] = port_nsga2_30_09[0] * 2.88058668e-01   # inwit
port_nsga2_30_09[1] = port_nsga2_30_09[1] * 7.41152117e-02   # inwit
port_nsga2_30_09[4] = port_nsga2_30_09[4] * 4.78793698e-02   # inwit
port_nsga2_30_09[6] = port_nsga2_30_09[6] * 3.36663280e-02
port_nsga2_30_09[8] = port_nsga2_30_09[8] * 4.55098195e-02
port_nsga2_30_09[13] = port_nsga2_30_09[13] * 1.07537425e-03
port_nsga2_30_09[21] = port_nsga2_30_09[21] * 7.08763132e-02
port_nsga2_30_09[25] = port_nsga2_30_09[25] * 2.09608078e-01
port_nsga2_30_09[27] = port_nsga2_30_09[27] * 2.10919326e-01
port_nsga2_30_09[28] = port_nsga2_30_09[28] * 1.05465427e-02
port_nsga2_30_09[38] = port_nsga2_30_09[38] * 4.80044394e-03
port_nsga2_30_09[39] = port_nsga2_30_09[39] * 2.13798244e-03
port_nsga2_30_09['return'] = port_nsga2_30_09.sum(axis=1)

#
# cumulative ret DE n.30
lista_de_30 = [0,1,2,4,6,9,10,11,18,19,21,35,37,38]
port_de_30_09 = df_allstocks_09.iloc[:,lista_de_30]
# ritorni * pesi selezionati
port_de_30_09[0] = port_de_30_09[0] * 1.16737469e-01
port_de_30_09[1] = port_de_30_09[1] *1.05909163e-01
port_de_30_09[2] = port_de_30_09[2] *1.65074851e-01
port_de_30_09[4] = port_de_30_09[4] * 4.44674876e-02
port_de_30_09[6] = port_de_30_09[6] * 1.95101363e-01
port_de_30_09[9] = port_de_30_09[9] * 8.45369907e-02
port_de_30_09[10] = port_de_30_09[10] * 1.54383046e-02
port_de_30_09[11] = port_de_30_09[11] * 2.13452829e-02
port_de_30_09[18] = port_de_30_09[18] * 1.45603896e-02
port_de_30_09[19] = port_de_30_09[19] * 7.58764218e-03
port_de_30_09[21] = port_de_30_09[21] * 1.44390873e-01
port_de_30_09[35] = port_de_30_09[35] * 2.23710800e-02
port_de_30_09[37] = port_de_30_09[37] * 2.57657682e-02
port_de_30_09[38] = port_de_30_09[38] * 3.66149096e-02
port_de_30_09['return'] = port_de_30_09.sum(axis=1)













































#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
df_allstocks_10 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_10_1.txt',header=None)
#Cumulative returns ftse
ftsemib2020_10 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_10.txt',header=0)
ftsemib_cumulativeret_10 = ftsemib2020_10['return'].cumsum(axis=0)
#Dates
# date_ftse = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/FTSEMIB_MI.csv',header=0)
date_ftse_10 = pd.to_datetime(ftsemib2020_10['Date'])


# cum ret DEM n.30
lista_dem_30 = [2,3,8,16,18,20,24,30,36]
port_dem_30_10 = df_allstocks_10.iloc[:,lista_dem_30]
port_dem_30_10[2] = port_dem_30_10[2] *0.10794322  # diasorin
port_dem_30_10[3] = port_dem_30_10[3] * 0.27249369  # diasorin
port_dem_30_10[8] = port_dem_30_10[8] * 0.42950546 # diasorin
port_dem_30_10[16] = port_dem_30_10[16] * 0.07744371  # diasorin
port_dem_30_10[18] = port_dem_30_10[18] *0.00363841 # banca mediolanum
port_dem_30_10[20] = port_dem_30_10[20] *0.01335939 # banca mediolanum
port_dem_30_10[30] = port_dem_30_10[30] *0.10573876# banca mediolanum
port_dem_30_10[36] = port_dem_30_10[36] *0.09251493 # banca mediolanum
port_dem_30_10[24] = port_dem_30_10[24] *0.00530566  # banca mediolanum
port_dem_30_10['return'] = port_dem_30_10.sum(axis=1)
#port_dem_30_10['return'] = port_dem_30_10['return'].cumsum()
#

#Cumulative ret GA n.30
lista_ga_30 = [3,8,15,16,19,20,30,36,38]
port_ga_30_10 = df_allstocks_10.iloc[:,lista_ga_30]
port_ga_30_10[19] =port_ga_30_10[19] * 1.59729709e-02 # banca mediolanum
port_ga_30_10[3] =port_ga_30_10[3] * 2.96603859e-01  # diasorin
port_ga_30_10[8] =port_ga_30_10[8] * 4.23382554e-01  # generali assicurazioni
port_ga_30_10[15] =port_ga_30_10[15] * 2.63809050e-01  # generali assicurazioni
port_ga_30_10[16] =port_ga_30_10[16] * 1.11577578e-03  # generali assicurazioni
port_ga_30_10[20] =port_ga_30_10[20] * 3.06883771e-02  # generali assicurazioni
port_ga_30_10[30] =port_ga_30_10[30] * 1.28770118e-01  # generali assicurazioni
port_ga_30_10[36] =port_ga_30_10[36] * 7.75750081e-02  # generali assicurazioni
port_ga_30_10[38] =port_ga_30_10[38] * 2.58129819e-02  # generali assicurazioni
port_ga_30_10['return'] = port_ga_30_10.sum(axis=1)
#port_ga_30_10['return'] = port_ga_30_10['return'].cumsum()
#
#cumulative ret LEVY n.30
lista_levy_30 = [2,3,8,14,15,16,19,30,36]
port_levy_30_10 = df_allstocks_10.iloc[:,lista_levy_30]
port_levy_30_10[2] = port_levy_30_10[2] * 2.98833258e-02 # enel
port_levy_30_10[3] = port_levy_30_10[3] * 2.93178597e-01
port_levy_30_10[8] = port_levy_30_10[8] * 4.05482430e-01
port_levy_30_10[14] = port_levy_30_10[14] * 5.60781616e-03    # enel
port_levy_30_10[15] = port_levy_30_10[15] * 1.00612736e-02  # enel
port_levy_30_10[16] = port_levy_30_10[16] *4.40298220e-02  # enel
port_levy_30_10[19] = port_levy_30_10[19] * 2.59262065e-02    # enel
port_levy_30_10[30] = port_levy_30_10[30] * 1.32166614e-01   # Amplifon
port_levy_30_10[36] = port_levy_30_10[36] * 8.17912621e-02
port_levy_30_10['return'] = port_levy_30_10.sum(axis=1)
#port_levy_30_10['return'] = port_levy_30_10['return'].cumsum()

#cumulative ret NSGA2 n.30
lista_nsga2_30 = [2,3,8,15,30,36]
port_nsga2_30_10 = df_allstocks_10.iloc[:,lista_nsga2_30]
port_nsga2_30_10[2] = port_nsga2_30_10[2] * 1.38730895e-01   # inwit
port_nsga2_30_10[3] = port_nsga2_30_10[3] * 2.35602756e-01  # inwit
port_nsga2_30_10[8] = port_nsga2_30_10[8] * 5.11920176e-03   # inwit
port_nsga2_30_10[15] = port_nsga2_30_10[15] * 5.78435568e-01
port_nsga2_30_10[30] = port_nsga2_30_10[30] * 3.32035783e-02
port_nsga2_30_10[36] = port_nsga2_30_10[36] * 7.25340404e-03
port_nsga2_30_10['return'] = port_nsga2_30_10.sum(axis=1)
#port_nsga2_30_10['return'] = port_nsga2_30_10['return'].cumsum()
#

# cumulative ret DE n.30
lista_de_30 = [3,12,16,18,28,30,36]
port_de_30_10 = df_allstocks_10.iloc[:,lista_de_30]
port_de_30_10[3] = port_de_30_10[3] * 2.44726064e-01
port_de_30_10[12] = port_de_30_10[12] * 1.86268619e-01
port_de_30_10[16] = port_de_30_10[16] *8.33198521e-02
port_de_30_10[18] = port_de_30_10[18] *6.79911121e-02
port_de_30_10[28] = port_de_30_10[28] *4.42916737e-02
port_de_30_10[30] = port_de_30_10[30] *2.12973339e-01
port_de_30_10[36] = port_de_30_10[36] *1.60184326e-01
port_de_30_10['return'] = port_de_30_10.sum(axis=1)































#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
df_allstocks_11 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_11_1.txt',header=None)
#Cumulative returns ftse
ftsemib2020_11 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_11.txt',header=0)
ftsemib_cumulativeret_11 = ftsemib2020_11['return'].cumsum(axis=0)
#Dates
# date_ftse = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/FTSEMIB_MI.csv',header=0)
date_ftse_11 = pd.to_datetime(ftsemib2020_11['Date'])


# cum ret DEM n.30
lista_dem_30 = [0,3,15,19,25,27,29,30,32,36,37,39]
port_dem_30_11 = df_allstocks_11.iloc[:,lista_dem_30]
port_dem_30_11[0] = port_dem_30_11[0] *0.17541178  # diasorin
port_dem_30_11[3] = port_dem_30_11[3] * 0.05565699 # diasorin
port_dem_30_11[15] = port_dem_30_11[15] * 0.11330604  # diasorin
port_dem_30_11[19] = port_dem_30_11[19] *0.02847842 # banca mediolanum
port_dem_30_11[25] = port_dem_30_11[25] *2.10631385e-02 # banca mediolanum
port_dem_30_11[27] = port_dem_30_11[27] *0.14615817
port_dem_30_11[29] = port_dem_30_11[29] *0.00206456
port_dem_30_11[30] = port_dem_30_11[30] *0.04104592# banca mediolanum
port_dem_30_11[32] = port_dem_30_11[32] *0.12229675  # banca mediolanum
port_dem_30_11[36] = port_dem_30_11[36] *0.15693871  # banca mediolanum
port_dem_30_11[37] = port_dem_30_11[37] *0.15546047  # banca mediolanum
port_dem_30_11[39] = port_dem_30_11[39] *0.15546047 # banca mediolanum
port_dem_30_11['return'] = port_dem_30_11.sum(axis=1)
#port_dem_30_11['return'] = port_dem_30_11['return'].cumsum()
#
#Cumulative ret GA n.30
lista_ga_30 = [0,3,7,15,19,27,30,32,36,37]
port_ga_30_11 = df_allstocks_11.iloc[:,lista_ga_30]
port_ga_30_11[0] =port_ga_30_11[0] * 1.54396841e-01  # Amplifon
port_ga_30_11[3] =port_ga_30_11[3] * 4.06838838e-02 # diasorin
port_ga_30_11[7] =port_ga_30_11[7] * 6.93994649e-02  # generali assicurazioni
port_ga_30_11[15] =port_ga_30_11[15] * 9.53752955e-02  # generali assicurazioni
port_ga_30_11[19] =port_ga_30_11[19] * 2.15490554e-02  # generali assicurazioni
port_ga_30_11[27] =port_ga_30_11[27] * 1.89828475e-01  # generali assicurazioni
port_ga_30_11[30] =port_ga_30_11[30] * 1.51992083e-02  # generali assicurazioni
port_ga_30_11[32] =port_ga_30_11[32] * 1.40406269e-01  # generali assicurazioni
port_ga_30_11[36] =port_ga_30_11[36] * 1.16584410e-01  # generali assicurazioni
port_ga_30_11[37] =port_ga_30_11[37] * 1.56010394e-01  # generali assicurazioni
port_ga_30_11['return'] = port_ga_30_11.sum(axis=1)
#port_ga_30_11['return'] = port_ga_30_11['return'].cumsum()

#
#cumulative ret LEVY n.30
lista_levy_30 = [0,3,7,15,27,32,36,37]
port_levy_30_11 = df_allstocks_11.iloc[:,lista_levy_30]
port_levy_30_11[0] = port_levy_30_11[0] * 1.56208114e-01 # enel
port_levy_30_11[3] = port_levy_30_11[3] * 9.74448199e-02
port_levy_30_11[7] = port_levy_30_11[7] * 6.71780036e-02
port_levy_30_11[15] = port_levy_30_11[15] * 1.20266985e-01   # enel
port_levy_30_11[27] = port_levy_30_11[27] * 1.76906973e-01  # enel
port_levy_30_11[32] = port_levy_30_11[32] * 1.44339188e-01    # enel
port_levy_30_11[36] = port_levy_30_11[36] * 1.09965487e-01
port_levy_30_11[37] = port_levy_30_11[37] * 1.26722624e-01  # Amplifon
port_levy_30_11['return'] = port_levy_30_11.sum(axis=1)


#cumulative ret NSGA2 n.30
lista_nsga2_30 = [1,28,35,36,37]
port_nsga2_30_11 = df_allstocks_11.iloc[:,lista_nsga2_30]
port_nsga2_30_11[1] = port_nsga2_30_11[1] * 1.06969197e-01    # inwit
port_nsga2_30_11[28] = port_nsga2_30_11[28] * 4.47419769e-02   # inwit
port_nsga2_30_11[35] = port_nsga2_30_11[35] * 7.69156959e-01   # inwit
port_nsga2_30_11[36] = port_nsga2_30_11[36] * 7.90040953e-02
port_nsga2_30_11[37] = port_nsga2_30_11[37] * 2.13626742e-01
port_nsga2_30_11['return'] = port_nsga2_30_11.sum(axis=1)
#port_nsga2_30_11['return'] = port_nsga2_30_11['return'].cumsum()
#

# cumulative ret DE n.30
lista_de_30 = [5,8,9,21,25,27,32,33,34,36]
port_de_30_11 = df_allstocks_11.iloc[:,lista_de_30]
# ritorni * pesi selezionati
port_de_30_11[5] = port_de_30_11[5] * 0.06281626
port_de_30_11[8] = port_de_30_11[8] * 0.00444969
port_de_30_11[9] = port_de_30_11[9] * 0.02387967
port_de_30_11[21] = port_de_30_11[21] * 0.00412318
port_de_30_11[25] = port_de_30_11[25] * 0.18559277
port_de_30_11[27] = port_de_30_11[27] * 0.23688085
port_de_30_11[32] = port_de_30_11[32] * 0.3574814
port_de_30_11[33] = port_de_30_11[33] * 0.01298049
port_de_30_11[34] = port_de_30_11[34] * 0.03863761
port_de_30_11[36] = port_de_30_11[36] *0.07315808
port_de_30_11['return'] = port_de_30_11.sum(axis=1)




#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------#
df_allstocks_12 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_12_1.txt',header=None)
#Cumulative returns ftse
ftsemib2020_12 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_12.txt',header=0)
ftsemib_cumulativeret_12 = ftsemib2020_12['return'].cumsum(axis=0)
#Dates
# date_ftse = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/FTSEMIB_MI.csv',header=0)
date_ftse_12 = pd.to_datetime(ftsemib2020_12['Date'])

# cum ret DEM n.30
lista_dem_30 = [2,6,11,12,15,16,19,20,22,24,26,28,29,32,33,35,36,37,38,39]
port_dem_30_12 = df_allstocks_12.iloc[:,lista_dem_30]
port_dem_30_12[2] = port_dem_30_12[2] * 8.41072985e-02  # diasorin
port_dem_30_12[6] = port_dem_30_12[6] * 8.56351426e-02 # diasorin
port_dem_30_12[11] = port_dem_30_12[11] * 1.41505208e-02  # diasorin
port_dem_30_12[12] = port_dem_30_12[12] * 3.63018157e-02 # diasorin
port_dem_30_12[15] = port_dem_30_12[15] * 6.00690272e-02  # diasorin
port_dem_30_12[16] = port_dem_30_12[16] * 6.90989276e-02 # banca mediolanum
port_dem_30_12[19] = port_dem_30_12[19] * 1.44368465e-02 # banca mediolanum
port_dem_30_12[20] = port_dem_30_12[20] * 1.03802742e-03 # banca mediolanum
port_dem_30_12[22] = port_dem_30_12[22] * 3.54092459e-03 # banca mediolanum
port_dem_30_12[24] = port_dem_30_12[24] * 5.53051259e-02 # banca mediolanum
port_dem_30_12[26] = port_dem_30_12[26] * 2.77868741e-02 # banca mediolanum
port_dem_30_12[28] = port_dem_30_12[28] * 1.27559624e-02 # banca mediolanum
port_dem_30_12[29] = port_dem_30_12[29] * 3.74779206e-02 # banca mediolanum
port_dem_30_12[32] = port_dem_30_12[32] * 2.01045732e-02 # banca mediolanum
port_dem_30_12[33] = port_dem_30_12[33] * 1.05664206e-03 # banca mediolanum
port_dem_30_12[35] = port_dem_30_12[35] * 2.04988271e-02 # banca mediolanum
port_dem_30_12[36] = port_dem_30_12[36] * 1.47798536e-01 # banca mediolanum
port_dem_30_12[37] = port_dem_30_12[37] * 3.59103883e-02 # banca mediolanum
port_dem_30_12[38] = port_dem_30_12[38] * 8.08099133e-02 # banca mediolanum
port_dem_30_12[39] = port_dem_30_12[39] * 1.90167176e-01 # banca mediolanum
port_dem_30_12['return'] = port_dem_30_12.sum(axis=1)


#
#Cumulative ret GA n.30
lista_ga_30 = [2,6,13,15,21,24,26,28,29,30,34,36,37,38,39]
port_ga_30_12 = df_allstocks_12.iloc[:,lista_ga_30]
port_ga_30_12[2] =port_ga_30_12[2] *1.11425249e-01   # Amplifon
port_ga_30_12[6] =port_ga_30_12[6] *1.75016348e-01  # diasorin
port_ga_30_12[13] =port_ga_30_12[13] * 1.34310854e-01 # generali assicurazioni
port_ga_30_12[15] =port_ga_30_12[15] * 1.00448877e-01  # generali assicurazioni
port_ga_30_12[21] =port_ga_30_12[21] * 9.76841876e-03  # generali assicurazioni
port_ga_30_12[24] =port_ga_30_12[24] * 3.05236833e-02  # generali assicurazioni
port_ga_30_12[26] =port_ga_30_12[26] * 1.20750704e-02  # generali assicurazioni
port_ga_30_12[28] =port_ga_30_12[28] * 3.08625092e-03
port_ga_30_12[29] =port_ga_30_12[29] * 5.56272365e-02
port_ga_30_12[30] =port_ga_30_12[30] * 7.36754834e-03
port_ga_30_12[34] =port_ga_30_12[34] * 4.25813868e-03
port_ga_30_12[36] =port_ga_30_12[36] * 5.88595092e-02
port_ga_30_12[37] =port_ga_30_12[37] * 1.91212746e-02
port_ga_30_12[38] =port_ga_30_12[38] * 8.51305877e-02
port_ga_30_12[39] =port_ga_30_12[39] * 1.90798793e-01
port_ga_30_12['return'] = port_ga_30_12.sum(axis=1)


#cumulative ret LEVY n.30
lista_levy_30 = [2,13,15,16,23,29,35,36,38,39]
port_levy_30_12 = df_allstocks_12.iloc[:,lista_levy_30]
port_levy_30_12[2] = port_levy_30_12[2] * 2.01402830e-01 # enel
port_levy_30_12[13] = port_levy_30_12[13] * 7.02192714e-02
port_levy_30_12[15] = port_levy_30_12[15] * 3.78230402e-02
port_levy_30_12[16] = port_levy_30_12[16] * 5.70183781e-03   # enel
port_levy_30_12[23] = port_levy_30_12[23] * 1.13744011e-02  # enel
port_levy_30_12[29] = port_levy_30_12[29] * 2.61993982e-01
port_levy_30_12[35] = port_levy_30_12[35] * 4.38231280e-02
port_levy_30_12[36] = port_levy_30_12[36] * 1.25994188e-01
port_levy_30_12[38] = port_levy_30_12[38] * 3.50245145e-02
port_levy_30_12[39] = port_levy_30_12[39] * 2.06117604e-01
port_levy_30_12['return'] = port_levy_30_12.sum(axis=1)
#port_levy_30_12['return'] = port_levy_30_12['return'].cumsum()


#cumulative ret NSGA2 n.30
lista_nsga2_30 = [13,23]
port_nsga2_30_12 = df_allstocks_12.iloc[:,lista_nsga2_30]
port_nsga2_30_12[13] = port_nsga2_30_12[13] * 1.82301595e-01    # inwit
port_nsga2_30_12[23] = port_nsga2_30_12[23] * 8.17648684e-01   # inwit
port_nsga2_30_12['return'] = port_nsga2_30_12.sum(axis=1)



# cumulative ret DE n.30
lista_de_30 = [3,6,7,13,14,25,26,36,38,39]
port_de_30_12 = df_allstocks_12.iloc[:,lista_de_30]
# ritorni * pesi selezionati
port_de_30_12[3] = port_de_30_12[3] * 2.50566903e-02
port_de_30_12[6] = port_de_30_12[6] * 3.51188767e-01
port_de_30_12[7] = port_de_30_12[7] * 1.22519239e-02
port_de_30_12[13] = port_de_30_12[13] * 2.14804760e-03
port_de_30_12[14] = port_de_30_12[14] * 3.74067453e-03
port_de_30_12[25] = port_de_30_12[25] * 4.20402117e-02
port_de_30_12[26] = port_de_30_12[26] * 1.27110505e-03
port_de_30_12[36] = port_de_30_12[36] * 1.50303518e-01
port_de_30_12[38] = port_de_30_12[38] * 1.98960776e-02
port_de_30_12[39] = port_de_30_12[39] * 3.90649889e-01
port_de_30_12['return'] = port_de_30_12.sum(axis=1)





# #-----------------------------------------------------------------------------------------------------------------------#
dates = pd.concat([date_ftse_02,date_ftse_03,
                   date_ftse_04,date_ftse_05,
                   date_ftse_06,
                   date_ftse_07,date_ftse_08,
                   date_ftse_09,date_ftse_10,
                   date_ftse_11,date_ftse_12],axis=0,ignore_index=True)

ftsemib_ret_all = pd.concat([ftsemib2020_02['return'],ftsemib2020_03['return'],
                             ftsemib2020_04['return'],ftsemib2020_05['return'],ftsemib2020_06['return'],ftsemib2020_07['return'],
                             ftsemib2020_08['return'],ftsemib2020_09['return'],ftsemib2020_10['return'],
                             ftsemib2020_11['return'],ftsemib2020_12['return']],axis=0,ignore_index=True).cumsum()

de_cumret_30 = pd.concat([port_de_30_02['return'],port_de_30_03['return'],
                          port_de_30_04['return'],port_de_30_05['return'],
                          port_de_30_06['return'],port_de_30_07['return'],
                          port_de_30_08['return'],port_de_30_09['return'],
                          port_de_30_10['return'],port_de_30_11['return'],port_de_30_12['return']],axis=0).cumsum(axis=0)

dem_cumret_30 = pd.concat([port_dem_30_02['return'],port_dem_30_03['return'],
                           port_dem_30_04['return'],port_dem_30_05['return'],port_dem_30_06['return'],
                           port_dem_30_07['return'],port_dem_30_08['return'],port_dem_30_09['return'],
                           port_dem_30_10['return'],port_dem_30_11['return'],port_dem_30_12['return']],axis=0).cumsum(axis=0)

ga_cumret_30 = pd.concat([port_ga_30_02['return'],port_ga_30_03['return'],port_ga_30_04['return'],
port_ga_30_05['return'],port_ga_30_06['return'],port_ga_30_07['return'],port_ga_30_08['return'],port_ga_30_09['return'],
port_ga_30_10['return'],port_ga_30_11['return'],port_ga_30_12['return']],axis=0).cumsum(axis=0)

levy_cumret_30 = pd.concat([port_levy_30_02['return'],
                            port_levy_30_03['return'],port_levy_30_04['return'],port_levy_30_05['return'],port_levy_30_06['return'],
port_levy_30_07['return'],port_levy_30_08['return'],port_levy_30_09['return'],port_levy_30_10['return'],port_levy_30_11['return'],
port_levy_30_12['return']],axis=0).cumsum(axis=0)

nsga2_cumret_30 = pd.concat([port_nsga2_30_02['return'], port_nsga2_30_03['return'],port_nsga2_30_04['return'],port_nsga2_30_05['return'],port_nsga2_30_06['return'],
port_nsga2_30_07['return'],port_nsga2_30_08['return'],port_nsga2_30_09['return'],port_nsga2_30_10['return'],
port_nsga2_30_11['return'],port_nsga2_30_12['return']],axis=0).cumsum(axis=0)
#
#
fig5, ax5 = plt.subplots(figsize=(10,6))
formatter = mdates.DateFormatter('%Y-%m')
ax5.xaxis.set_minor_formatter(formatter)
ax5.xaxis.set_major_formatter(formatter)
ax5.tick_params(axis='x', rotation=45)
sns.lineplot(x=dates.values,y=ftsemib_ret_all, label = 'FTSE-MIB', markevery=21,marker='o', markersize=12, linestyle='dashdot',linewidth=2)
sns.lineplot(x=dates.values,y=de_cumret_30, label = 'MOEA/D-DE')#, markevery=25, markers=maks1[1])
sns.lineplot(x=dates.values,y=dem_cumret_30, label= "MOEA/D-DEM")#, markevery=25, markers=maks1[2])
sns.lineplot(x=dates.values,y=ga_cumret_30, label = "MOEA/D-GA")#,markevery=25, markers=maks1[3])
sns.lineplot(x=dates.values,y=levy_cumret_30, label="MOEA/D-LEVY")#,markevery=25, markers=maks1[4])
sns.lineplot(x=dates.values,y=nsga2_cumret_30, label = "NSGAII")# ,markevery=25, markers=maks1[0])
plt.ylabel('Cumulative return')
plt.title('FTSE MIB vs low risk portfolios')
plt.savefig('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/images/lowrisk.png')



























































