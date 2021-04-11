import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
#-------------------------------------------------------------------------------------¯¯#
# PLOT differenza di ritorni close-to-close tra il portafoglio ottimizzato e ftsemib 2020
# #dati con tutti i ritorni dei 40 stock
df_allstocks_02 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_final_2020_02_1.txt' ,header=None)
#Cumulative returns ftse
ftsemib2020_02 = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/df_ftsemib2020_02.txt',header=0)
ftsemib_cumulativeret_02 = ftsemib2020_02['return'].cumsum(axis=0)

#Dates
# date_ftse = pd.read_csv('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/dat/FTSEMIB_MI.csv',header=0)
date_ftse_02 = pd.to_datetime(ftsemib2020_02['Date'])


#-------------------------------------------------------------------------------------------------------------------------------------#
# #Cumulative returns portfolio DEM n.10
lista_dem_10 = [2,9,26]
port_dem_10_02 = df_allstocks_02.iloc[:,lista_dem_10]
port_dem_10_02[2] = port_dem_10_02[2] *3.08913456e-01 # banca mediolanum
port_dem_10_02[9] = port_dem_10_02[9] * 5.81471688e-01  # diasorin
port_dem_10_02[26] = port_dem_10_02[26] * 1.09356739e-01
port_dem_10_02['return'] = port_dem_10_02.sum(axis=1)
#port_dem_10_02['return'] = port_dem_10_02['return'].cumsum()
#
#Cumulative ret GA n.10
lista_ga_10 = [2,9,12,15,26,34]
port_ga_10_02 = df_allstocks_02.iloc[:,lista_ga_10]
port_ga_10_02[2] =port_ga_10_02[2] * 4.07908044e-01    # Amplifon
port_ga_10_02[9] =port_ga_10_02[9] * 3.16987213e-01 # banca mediolanum
port_ga_10_02[12] =port_ga_10_02[12] * 3.73977278e-03   # diasorin
port_ga_10_02[15] =port_ga_10_02[15] * 1.37544284e-01  # generali assicurazioni
port_ga_10_02[26] =port_ga_10_02[26] * 1.01343684e-01  # generali assicurazioni
port_ga_10_02[34] =port_ga_10_02[34] * 3.16670939e-02  # generali assicurazioni

port_ga_10_02['return'] = port_ga_10_02.sum(axis=1)
#port_ga_10_02['return'] = port_ga_10_02['return'].cumsum()
#
#cumulative ret LEVY n.10
lista_levy_10 = [2,9,20,26,32]
port_levy_10_02 = df_allstocks_02.iloc[:,lista_levy_10]
port_levy_10_02[2] = port_levy_10_02[2] * 2.87777768e-01
port_levy_10_02[9] = port_levy_10_02[9] * 5.59519031e-01# enel
port_levy_10_02[20] = port_levy_10_02[20] * 6.98568125e-03 # enel
port_levy_10_02[26] = port_levy_10_02[26] * 1.43236947e-01 # enel
port_levy_10_02[32] = port_levy_10_02[32] * 1.54049325e-03 # enel
#port_levy_10_02[15] = port_levy_10_02[15] * 7.08601010e-01 # enel
#port_levy_10_02[27] = port_levy_10_02[27] * 2.91398975e-01   # Amplifon
port_levy_10_02['return'] = port_levy_10_02.sum(axis=1)
#port_levy_10_02['return'] = port_levy_10_02['return'].cumsum()
#
#cumulative ret NSGA2 n.10
lista_nsga2_10 = [2,9,11,15,26,30,32,34]
port_nsga2_10_02 = df_allstocks_02.iloc[:,lista_nsga2_10]
port_nsga2_10_02[2] = port_nsga2_10_02[2] * 3.22378770e-01    # inwit
port_nsga2_10_02[9] = port_nsga2_10_02[9] * 1.04252958e-03    # inwit
port_nsga2_10_02[11] = port_nsga2_10_02[11] * 7.34975349e-03    # inwit
port_nsga2_10_02[15] = port_nsga2_10_02[15] * 2.68780969e-01    # inwit
port_nsga2_10_02[26] = port_nsga2_10_02[26] * 9.61168656e-02    # inwit
port_nsga2_10_02[30] = port_nsga2_10_02[30] * 1.26189936e-01    # inwit
port_nsga2_10_02[32] = port_nsga2_10_02[32] * 1.44065314e-01    #banca mediolanum
port_nsga2_10_02[34] = port_nsga2_10_02[34] * 3.37788529e-02
port_nsga2_10_02['return'] = port_nsga2_10_02.sum(axis=1)
#port_nsga2_10_02['return'] = port_nsga2_10_02['return'].cumsum()
#
# cumulative ret DE n.10
lista_de_10 = [12,18,26]
port_de_10_02 = df_allstocks_02.iloc[:,lista_de_10]
# ritorni * pesi selezionati
port_de_10_02[12] = port_de_10_02[12] * 0.44477781
port_de_10_02[18] = port_de_10_02[18] *0.12167264
port_de_10_02[26] = port_de_10_02[26] * 0.43354955
port_de_10_02['return'] = port_de_10_02.sum(axis=1)
#port_de_10_02['return'] = port_de_10_02['return'].cumsum()





#--------------------------------------------------------------------------------------------------------------------------#
#cumulative ret DEM n.20
lista_dem_20 = [2,6,8,9,12,15,18,26,29,32,34]
port_dem_20_02 = df_allstocks_02.iloc[:,lista_dem_20]
port_dem_20_02[2] = port_dem_20_02[2] * 0.46672515  # diasorin
port_dem_20_02[6] = port_dem_20_02[6] * 0.00054483  # diasorin
port_dem_20_02[8] = port_dem_20_02[8] * 0.00492482 # diasorin
port_dem_20_02[9] = port_dem_20_02[9] * 0.00651699  # diasorin
port_dem_20_02[12] = port_dem_20_02[12] *0.00608233 # banca mediolanum
port_dem_20_02[15] = port_dem_20_02[15] *0.23898243 # banca mediolanum
port_dem_20_02[18] = port_dem_20_02[18] *0.02485391 # banca mediolanum
port_dem_20_02[26] = port_dem_20_02[26] *0.10915457 # banca mediolanum
port_dem_20_02[29] = port_dem_20_02[29] *0.0164697  # banca mediolanum
port_dem_20_02[32] = port_dem_20_02[32] *0.0993847  # banca mediolanum
port_dem_20_02[34] = port_dem_20_02[34] *0.02536056  # banca mediolanum
port_dem_20_02['return'] = port_dem_20_02.sum(axis=1)
#port_dem_20_02['return'] = port_dem_20_02['return'].cumsum()
#
#Cumulative ret GA n.20
lista_ga_20 = [2,4,9,15,18,26,30,32,34,36]
port_ga_20_02 = df_allstocks_02.iloc[:,lista_ga_20]
port_ga_20_02[2] =port_ga_20_02[2] * 3.33778403e-01   # Amplifon
port_ga_20_02[4] =port_ga_20_02[4] * 2.16532212e-02    # Amplifon
port_ga_20_02[9] =port_ga_20_02[9] * 5.24741831e-02 # banca mediolanum
port_ga_20_02[15] =port_ga_20_02[15] * 2.73135541e-01   # diasorin
port_ga_20_02[18] =port_ga_20_02[18] * 2.09106317e-02  # generali assicurazioni
port_ga_20_02[26] =port_ga_20_02[26] * 6.92884378e-02  # generali assicurazioni
port_ga_20_02[30] =port_ga_20_02[30] * 3.64146728e-02  # generali assicurazioni
port_ga_20_02[32] =port_ga_20_02[32] * 1.28858992e-01  # generali assicurazioni
port_ga_20_02[34] =port_ga_20_02[34] * 5.22964542e-02  # generali assicurazioni
port_ga_20_02[36] =port_ga_20_02[36] * 1.30235744e-03  # generali assicurazioni

port_ga_20_02['return'] = port_ga_20_02.sum(axis=1)
#port_ga_20_02['return'] = port_ga_20_02['return'].cumsum()
#
#cumulative ret LEVY n.20
lista_levy_20 = [2,6,9,15,18,20,26,32,34]
port_levy_20_02 = df_allstocks_02.iloc[:,lista_levy_20]
port_levy_20_02[2] = port_levy_20_02[2] * 3.69065857e-01
port_levy_20_02[6] = port_levy_20_02[6] * 5.93731418e-03 # enel
port_levy_20_02[9] = port_levy_20_02[9] * 9.87218371e-02 # enel
port_levy_20_02[15] = port_levy_20_02[15] * 2.34925726e-01
port_levy_20_02[18] = port_levy_20_02[18] * 4.11104563e-02
port_levy_20_02[20] = port_levy_20_02[20] * 1.76133674e-03    # enel
port_levy_20_02[26] = port_levy_20_02[26] * 6.54449432e-02    # enel
port_levy_20_02[32] = port_levy_20_02[32] * 1.02624660e-01    # enel
port_levy_20_02[34] = port_levy_20_02[34] * 7.97943912e-02   # Amplifon
port_levy_20_02['return'] = port_levy_20_02.sum(axis=1)
#port_levy_20_02['return'] = port_levy_20_02['return'].cumsum()

#cumulative ret NSGA2 n.20
lista_nsga2_20 = [2,9,26,30,34]
port_nsga2_20_02 = df_allstocks_02.iloc[:,lista_nsga2_20]
port_nsga2_20_02[2] = port_nsga2_20_02[2] * 4.23059800e-01    # inwit
port_nsga2_20_02[9] = port_nsga2_20_02[9] * 4.23481504e-01    # inwit
port_nsga2_20_02[26] = port_nsga2_20_02[26] * 1.48300495e-01    # inwit
port_nsga2_20_02[30] = port_nsga2_20_02[30] * 1.56775524e-03
port_nsga2_20_02[34] = port_nsga2_20_02[34] * 3.28702684e-03
#port_nsga2_20_02[27] = port_nsga2_20_02[27] * 4.44424131e-01
port_nsga2_20_02['return'] = port_nsga2_20_02.sum(axis=1)
#port_nsga2_20_02['return'] = port_nsga2_20_02['return'].cumsum()
#
# cumulative ret DE n.20
lista_de_20 = [15,18,26,32]
port_de_20_02 = df_allstocks_02.iloc[:,lista_de_20]
# ritorni * pesi selezionati
port_de_20_02[15] = port_de_20_02[15] * 0.3638808
port_de_20_02[18] = port_de_20_02[18] * 0.39373107
port_de_20_02[26] = port_de_20_02[26] * 0.06934438
port_de_20_02[32] = port_de_20_02[32] * 0.17304376
#port_de_20_02[27] = port_de_20_02[27] * 0.78052662
#port_de[21] = port_de[21] * 0.03335649
port_de_20_02['return'] = port_de_20_02.sum(axis=1)
#port_de_20_02['return'] = port_de_20_02['return'].cumsum()
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


# #Cumulative returns portfolio DEM n.10
lista_dem_10 = [3,21,25,28,39]
port_dem_10_03 = df_allstocks_03.iloc[:,lista_dem_10]
port_dem_10_03[3] = port_dem_10_03[3] *0.40059402 # banca mediolanum
port_dem_10_03[21] = port_dem_10_03[21] *0.24674473 # banca mediolanum
port_dem_10_03[25] = port_dem_10_03[25] *0.03082343 # banca mediolanum
port_dem_10_03[28] = port_dem_10_03[28] *0.40059402 # banca mediolanum
port_dem_10_03[39] = port_dem_10_03[39] * 0.14347057  # diasorin
#port_dem_10_03[26] = port_dem_10_03[26] * 1.09356739e-01
port_dem_10_03['return'] = port_dem_10_03.sum(axis=1)
#port_dem_10_03['return'] = port_dem_10_03['return'].cumsum()
#
#Cumulative ret GA n.10
lista_ga_10 = [3,13,21,27,28,39]
port_ga_10_03 = df_allstocks_03.iloc[:,lista_ga_10]
port_ga_10_03[3] =port_ga_10_03[3] * 3.55085851e-01    # Amplifon
port_ga_10_03[13] =port_ga_10_03[13] * 7.97012895e-02 # banca mediolanum
port_ga_10_03[21] =port_ga_10_03[21] * 2.92257315e-01   # diasorin
port_ga_10_03[27] =port_ga_10_03[27] * 4.86773012e-03  # generali assicurazioni
port_ga_10_03[28] =port_ga_10_03[28] * 1.76962993e-01  # generali assicurazioni
port_ga_10_03[39] =port_ga_10_03[39] * 8.95705270e-02  # generali assicurazioni
port_ga_10_03['return'] = port_ga_10_03.sum(axis=1)
#p#ort_ga_10_03['return'] = port_ga_10_03['return'].cumsum()
#
#cumulative ret LEVY n.10
lista_levy_10 = [3,21,28,39]
port_levy_10_03 = df_allstocks_03.iloc[:,lista_levy_10]
port_levy_10_03[3] = port_levy_10_03[3] * 3.71125402e-01
port_levy_10_03[21] = port_levy_10_03[21] * 3.64655881e-01# enel
port_levy_10_03[28] = port_levy_10_03[28] * 1.48365430e-01 # enel
port_levy_10_03[39] = port_levy_10_03[39] * 1.15835343e-01 # enel
#port_levy_10_03[32] = port_levy_10_03[32] * 1.54049325e-03 # enel
#port_levy_10_03[15] = port_levy_10_03[15] * 7.08601010e-01 # enel
#port_levy_10_03[27] = port_levy_10_03[27] * 2.91398975e-01   # Amplifon
port_levy_10_03['return'] = port_levy_10_03.sum(axis=1)
#port_levy_10_03['return'] = port_levy_10_03['return'].cumsum()
#
#cumulative ret NSGA2 n.10
lista_nsga2_10 = [13,21,24,25,27,28,32,38,39]
port_nsga2_10_03 = df_allstocks_03.iloc[:,lista_nsga2_10]
port_nsga2_10_03[13] = port_nsga2_10_03[13] * 1.08923133e-01    # inwit
port_nsga2_10_03[21] = port_nsga2_10_03[21] * 1.41159939e-01    # inwit
port_nsga2_10_03[24] = port_nsga2_10_03[24] * 8.23832828e-02    # inwit
port_nsga2_10_03[25] = port_nsga2_10_03[25] * 1.03799723e-01    # inwit
port_nsga2_10_03[27] = port_nsga2_10_03[27] * 9.87076304e-02    # inwit
port_nsga2_10_03[28] = port_nsga2_10_03[28] * 8.59051730e-02    # inwit
port_nsga2_10_03[32] = port_nsga2_10_03[32] * 3.03334864e-02    #banca mediolanum
port_nsga2_10_03[38] = port_nsga2_10_03[38] * 1.62484750e-01
port_nsga2_10_03[39] = port_nsga2_10_03[39] * 1.86870609e-01
port_nsga2_10_03['return'] = port_nsga2_10_03.sum(axis=1)
#port_nsga2_10_03['return'] = port_nsga2_10_03['return'].cumsum()
#
# cumulative ret DE n.10
lista_de_10 = [13,21]
port_de_10_03 = df_allstocks_03.iloc[:,lista_de_10]
# ritorni * pesi selezionati
port_de_10_03[13] = port_de_10_03[13] * 0.27457061
port_de_10_03[21] = port_de_10_03[21] *0.72542939
#port_de_10_03[26] = port_de_10_03[26] * 0.43354955
port_de_10_03['return'] = port_de_10_03.sum(axis=1)
#port_de_10_03['return'] = port_de_10_03['return'].cumsum()


#
# cum ret DEM n.20
lista_dem_20 = [7,8,13,16,21,25,28,32,35,39]
port_dem_20_03 = df_allstocks_03.iloc[:,lista_dem_20]
port_dem_20_03[7] = port_dem_20_03[7] * 4.99469542e-03  # diasorin
#port_dem_20_03[6] = port_dem_20_03[6] * 0.00054483  # diasorin
port_dem_20_03[8] = port_dem_20_03[8] * 5.12553816e-02 # diasorin
port_dem_20_03[13] = port_dem_20_03[13] * 1.72674551e-01  # diasorin
port_dem_20_03[16] = port_dem_20_03[16] *3.09202637e-02 # banca mediolanum
port_dem_20_03[21] = port_dem_20_03[21] *2.24282448e-01 # banca mediolanum
port_dem_20_03[25] = port_dem_20_03[25] *1.42639754e-01 # banca mediolanum
port_dem_20_03[28] = port_dem_20_03[28] *1.01662872e-01 # banca mediolanum
#port_dem_20_03[29] = port_dem_20_03[29] *0.0164697  # banca mediolanum
port_dem_20_03[32] = port_dem_20_03[32] *1.54936330e-02  # banca mediolanum
port_dem_20_03[35] = port_dem_20_03[35] *5.85805052e-03  # banca mediolanum
port_dem_20_03[39] = port_dem_20_03[39] *2.49230293e-01  # banca mediolanum
port_dem_20_03['return'] = port_dem_20_03.sum(axis=1)
#port_dem_20_03['return'] = port_dem_20_03['return'].cumsum()
#
#Cumulative ret GA n.20
lista_ga_20 = [13,21,24,25,28,38,39]
port_ga_20_03 = df_allstocks_03.iloc[:,lista_ga_20]
port_ga_20_03[13] =port_ga_20_03[13] * 1.71739859e-01   # Amplifon
port_ga_20_03[21] =port_ga_20_03[21] * 2.02025600e-01    # Amplifon
port_ga_20_03[24] =port_ga_20_03[24] * 4.93813125e-02 # banca mediolanum
port_ga_20_03[25] =port_ga_20_03[25] * 1.39418011e-01   # diasorin
port_ga_20_03[28] =port_ga_20_03[28] * 1.61533302e-01  # generali assicurazioni
port_ga_20_03[38] =port_ga_20_03[38] * 3.17080448e-03  # generali assicurazioni
port_ga_20_03[39] =port_ga_20_03[39] * 2.72605675e-01  # generali assicurazioni
#port_ga_20_03[32] =port_ga_20_03[32] * 1.28858992e-01  # generali assicurazioni
#port_ga_20_03[34] =port_ga_20_03[34] * 5.22964542e-02  # generali assicurazioni
#port_ga_20_03[36] =port_ga_20_03[36] * 1.30235744e-03  # generali assicurazioni
port_ga_20_03['return'] = port_ga_20_03.sum(axis=1)
#port_ga_20_03['return'] = port_ga_20_03['return'].cumsum()
#
#cumulative ret LEVY n.20
lista_levy_20 = [8,13,21,23,24,25,27,28,38,39]
port_levy_20_03 = df_allstocks_03.iloc[:,lista_levy_20]
port_levy_20_03[8] = port_levy_20_03[8] * 3.02493747e-03
port_levy_20_03[13] = port_levy_20_03[13] * 1.61024674e-01 # enel
port_levy_20_03[21] = port_levy_20_03[21] * 2.55403033e-01 # enel
port_levy_20_03[23] = port_levy_20_03[23] * 1.30292912e-03
port_levy_20_03[24] = port_levy_20_03[24] * 5.62872494e-02
port_levy_20_03[25] = port_levy_20_03[25] * 1.01196434e-01    # enel
port_levy_20_03[27] = port_levy_20_03[27] * 1.19156585e-02    # enel
port_levy_20_03[28] = port_levy_20_03[28] * 1.60865333e-01    # enel
port_levy_20_03[38] = port_levy_20_03[38] * 2.62502498e-03    # enel
port_levy_20_03[39] = port_levy_20_03[39] * 2.45420415e-01   # Amplifon
port_levy_20_03['return'] = port_levy_20_03.sum(axis=1)
#port_levy_20_03['return'] = port_levy_20_03['return'].cumsum()

#cumulative ret NSGA2 n.20
lista_nsga2_20 = [3,13,15,21,24,25,28,37,39]
port_nsga2_20_03 = df_allstocks_03.iloc[:,lista_nsga2_20]
port_nsga2_20_03[3] = port_nsga2_20_03[3] * 9.08406690e-02    # inwit
port_nsga2_20_03[13] = port_nsga2_20_03[13] * 6.41475070e-02    # inwit
port_nsga2_20_03[15] = port_nsga2_20_03[15] * 1.16237836e-03    # inwit
port_nsga2_20_03[21] = port_nsga2_20_03[21] * 3.44514658e-01
port_nsga2_20_03[24] = port_nsga2_20_03[24] * 3.44750917e-03
port_nsga2_20_03[25] = port_nsga2_20_03[25] * 1.82217024e-03
port_nsga2_20_03[28] = port_nsga2_20_03[28] * 2.58731008e-01
port_nsga2_20_03[37] = port_nsga2_20_03[37] * 1.36469993e-03
port_nsga2_20_03[39] = port_nsga2_20_03[39] * 2.31272697e-01
#port_nsga2_20_03[27] = port_nsga2_20_03[27] * 4.44424131e-01
port_nsga2_20_03['return'] = port_nsga2_20_03.sum(axis=1)
#port_nsga2_20_03['return'] = port_nsga2_20_03['return'].cumsum()
#
# cumulative ret DE n.20
lista_de_20 = [1,13,19,21,26]
port_de_20_03 = df_allstocks_03.iloc[:,lista_de_20]
# ritorni * pesi selezionati
port_de_20_03[1] = port_de_20_03[1] * 0.10897238
port_de_20_03[13] = port_de_20_03[13] * 0.26308419
port_de_20_03[19] = port_de_20_03[19] * 0.21691407
port_de_20_03[21] = port_de_20_03[21] * 0.37760952
port_de_20_03[26] = port_de_20_03[26] * 0.03341985
#port_de_20_03[27] = port_de_20_03[27] * 0.78052662
#port_de[21] = port_de[21] * 0.03335649
port_de_20_03['return'] = port_de_20_03.sum(axis=1)
#port_de_20_03['return'] = port_de_20_03['return'].cumsum()
#



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

# #Cumulative returns portfolio DEM n.10
lista_dem_10 = [15,27,36]
port_dem_10_04 = df_allstocks_04.iloc[:,lista_dem_10]
port_dem_10_04[15] = port_dem_10_04[15] *0.25098795 # banca mediolanum
port_dem_10_04[27] = port_dem_10_04[27] *0.69640273 # banca mediolanum
port_dem_10_04[36] = port_dem_10_04[36] *0.05260932 # banca mediolanum
#port_dem_10_04[28] = port_dem_10_04[28] *0.40059402 # banca mediolanum
#port_dem_10_04[39] = port_dem_10_04[39] * 0.14347057  # diasorin
#port_dem_10_04[26] = port_dem_10_04[26] * 1.09356739e-01
port_dem_10_04['return'] = port_dem_10_04.sum(axis=1)
#port_dem_10_04['return'] = port_dem_10_04['return'].cumsum()
#
#Cumulative ret GA n.10
lista_ga_10 = [13,15,27,36]
port_ga_10_04 = df_allstocks_04.iloc[:,lista_ga_10]
#port_ga_10_04[3] =port_ga_10_04[3] * 3.55085851e-01    # Amplifon
port_ga_10_04[13] =port_ga_10_04[13] * 2.41597283e-03 # banca mediolanum
port_ga_10_04[15] =port_ga_10_04[15] * 2.52713509e-01   # diasorin
port_ga_10_04[27] =port_ga_10_04[27] * 6.95366723e-01  # generali assicurazioni
port_ga_10_04[36] =port_ga_10_04[36] * 4.92376820e-02  # generali assicurazioni
#port_ga_10_04[39] =port_ga_10_04[39] * 8.95705270e-02  # generali assicurazioni
port_ga_10_04['return'] = port_ga_10_04.sum(axis=1)
#port_ga_10_04['return'] = port_ga_10_04['return'].cumsum()
#
#cumulative ret LEVY n.10
lista_levy_10 = [15,27,36]
port_levy_10_04 = df_allstocks_04.iloc[:,lista_levy_10]
port_levy_10_04[15] = port_levy_10_04[15] * 2.38375483e-01
port_levy_10_04[27] = port_levy_10_04[27] * 7.02011813e-01# enel
port_levy_10_04[36] = port_levy_10_04[36] * 5.88303140e-02 # enel
#port_levy_10_04[39] = port_levy_10_04[39] * 1.15835343e-01 # enel
#port_levy_10_04[32] = port_levy_10_04[32] * 1.54049325e-03 # enel
#port_levy_10_04[15] = port_levy_10_04[15] * 7.08601010e-01 # enel
#port_levy_10_04[27] = port_levy_10_04[27] * 2.91398975e-01   # Amplifon
port_levy_10_04['return'] = port_levy_10_04.sum(axis=1)
#port_levy_10_04['return'] = port_levy_10_04['return'].cumsum()
#
#cumulative ret NSGA2 n.10
lista_nsga2_10 = [13,17,19,24,27,28,36]
port_nsga2_10_04 = df_allstocks_04.iloc[:,lista_nsga2_10]
port_nsga2_10_04[13] = port_nsga2_10_04[13] * 1.44054752e-01    # inwit
port_nsga2_10_04[17] = port_nsga2_10_04[17] * 1.21830353e-01    # inwit
port_nsga2_10_04[19] = port_nsga2_10_04[19] * 9.51616730e-02    # inwit
port_nsga2_10_04[24] = port_nsga2_10_04[24] * 7.34648944e-02    # inwit
port_nsga2_10_04[27] = port_nsga2_10_04[27] * 3.00294853e-01    # inwit
port_nsga2_10_04[28] = port_nsga2_10_04[28] * 1.34669027e-02   # inwit
port_nsga2_10_04[36] = port_nsga2_10_04[36] * 2.51718500e-01    #banca mediolanum
#port_nsga2_10_04[38] = port_nsga2_10_04[38] * 1.62484750e-01
#port_nsga2_10_04[39] = port_nsga2_10_04[39] * 1.86870609e-01
port_nsga2_10_04['return'] = port_nsga2_10_04.sum(axis=1)
#port_nsga2_10_04['return'] = port_nsga2_10_04['return'].cumsum()
#
# cumulative ret DE n.10
lista_de_10 = [15,19]
port_de_10_04 = df_allstocks_04.iloc[:,lista_de_10]
# ritorni * pesi selezionati
port_de_10_04[15] = port_de_10_04[15] * 0.75620496
port_de_10_04[19] = port_de_10_04[19] *0.24379504
#port_de_10_04[26] = port_de_10_04[26] * 0.43354955
port_de_10_04['return'] = port_de_10_04.sum(axis=1)
#port_de_10_04['return'] = port_de_10_04['return'].cumsum()
#

#
#
# cum ret DEM n.20
lista_dem_20 = [13,15,19,27,36]
port_dem_20_04 = df_allstocks_04.iloc[:,lista_dem_20]
port_dem_20_04[13] = port_dem_20_04[13] *0.07700925  # diasorin
#port_dem_20_04[6] = port_dem_20_04[6] * 0.00054483  # diasorin
port_dem_20_04[15] = port_dem_20_04[15] * 0.07367698 # diasorin
#port_dem_20_04[13] = port_dem_20_04[13] * 1.72674551e-01  # diasorin
port_dem_20_04[19] = port_dem_20_04[19] *0.02984323 # banca mediolanum
port_dem_20_04[27] = port_dem_20_04[27] *0.56607451 # banca mediolanum
port_dem_20_04[36] = port_dem_20_04[36] *0.25339602 # banca mediolanum
#port_dem_20_04[28] = port_dem_20_04[28] *1.01662872e-01 # banca mediolanum
#port_dem_20_04[29] = port_dem_20_04[29] *0.0164697  # banca mediolanum
#port_dem_20_04[32] = port_dem_20_04[32] *1.54936330e-02  # banca mediolanum
#port_dem_20_04[35] = port_dem_20_04[35] *5.85805052e-03  # banca mediolanum
#port_dem_20_04[39] = port_dem_20_04[39] *2.49230293e-01  # banca mediolanum
port_dem_20_04['return'] = port_dem_20_04.sum(axis=1)
#port_dem_20_04['return'] = port_dem_20_04['return'].cumsum()
#
#Cumulative ret GA n.20
lista_ga_20 = [13,15,19,24,27,36]
port_ga_20_04 = df_allstocks_04.iloc[:,lista_ga_20]
port_ga_20_04[13] =port_ga_20_04[13] * 9.25963732e-02   # Amplifon
port_ga_20_04[15] =port_ga_20_04[15] * 1.07779280e-01    # Amplifon
port_ga_20_04[19] =port_ga_20_04[19] * 4.74407843e-02 # banca mediolanum
port_ga_20_04[24] =port_ga_20_04[24] * 5.95570961e-03   # diasorin
port_ga_20_04[27] =port_ga_20_04[27] * 5.43662888e-01  # generali assicurazioni
port_ga_20_04[36] =port_ga_20_04[36] * 2.02557217e-01  # generali assicurazioni
port_ga_20_04['return'] = port_ga_20_04.sum(axis=1)
#port_ga_20_04['return'] = port_ga_20_04['return'].cumsum()
#
#cumulative ret LEVY n.20
lista_levy_20 = [13,15,19,24,27,36]
port_levy_20_04 = df_allstocks_04.iloc[:,lista_levy_20]
#port_levy_20_04[8] = port_levy_20_04[8] * 3.02493747e-03
port_levy_20_04[13] = port_levy_20_04[13] * 9.36071346e-02 # enel
port_levy_20_04[15] = port_levy_20_04[15] * 8.44816402e-02 # enel
port_levy_20_04[19] = port_levy_20_04[19] * 5.09263695e-02
port_levy_20_04[24] = port_levy_20_04[24] * 1.24031792e-02
#port_levy_20_04[25] = port_levy_20_04[25] * 1.01196434e-01    # enel
port_levy_20_04[27] = port_levy_20_04[27] * 5.26404506e-01    # enel
port_levy_20_04[36] = port_levy_20_04[36] * 2.32170409e-01    # enel
#port_levy_20_04[38] = port_levy_20_04[38] * 2.62502498e-03    # enel
#port_levy_20_04[39] = port_levy_20_04[39] * 2.45420415e-01   # Amplifon
port_levy_20_04['return'] = port_levy_20_04.sum(axis=1)
#port_levy_20_04['return'] = port_levy_20_04['return'].cumsum()

#cumulative ret NSGA2 n.20
lista_nsga2_20 = [15,24,27,36]
port_nsga2_20_04 = df_allstocks_04.iloc[:,lista_nsga2_20]
#port_nsga2_20_04[3] = port_nsga2_20_04[3] * 9.08406690e-02    # inwit
#port_nsga2_20_04[13] = port_nsga2_20_04[13] * 6.41475070e-02    # inwit
port_nsga2_20_04[15] = port_nsga2_20_04[15] * 1.88989304e-01    # inwit
#port_nsga2_20_04[21] = port_nsga2_20_04[21] * 3.44514658e-01
port_nsga2_20_04[24] = port_nsga2_20_04[24] * 1.48866996e-03
port_nsga2_20_04[27] = port_nsga2_20_04[27] * 7.18475117e-01
port_nsga2_20_04[36] = port_nsga2_20_04[36] *8.95400697e-02
port_nsga2_20_04['return'] = port_nsga2_20_04.sum(axis=1)
#port_nsga2_20_04['return'] = port_nsga2_20_04['return'].cumsum()
#
# cumulative ret DE n.20
lista_de_20 = [13,15,19]
port_de_20_04 = df_allstocks_04.iloc[:,lista_de_20]
# ritorni * pesi selezionati
#port_de_20_04[1] = port_de_20_04[1] * 0.10897238
port_de_20_04[13] = port_de_20_04[13] * 0.08687892
port_de_20_04[15] = port_de_20_04[15] * 0.48851825
port_de_20_04[19] = port_de_20_04[19] * 0.42460283
#port_de_20_04[26] = port_de_20_04[26] * 0.03341985
#port_de_20_04[27] = port_de_20_04[27] * 0.78052662
#port_de[21] = port_de[21] * 0.03335649
port_de_20_04['return'] = port_de_20_04.sum(axis=1)
#port_de_20_04['return'] = port_de_20_04['return'].cumsum()
#












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

# #Cumulative returns portfolio DEM n.10
lista_dem_10 = [13,15,36,37]
port_dem_10_05 = df_allstocks_05.iloc[:,lista_dem_10]
port_dem_10_05[13] = port_dem_10_05[13] *8.96528326e-02 # banca mediolanum
port_dem_10_05[15] = port_dem_10_05[15] *8.40073950e-02 # banca mediolanum
port_dem_10_05[36] = port_dem_10_05[36] *1.75683652e-01 # banca mediolanum
port_dem_10_05[37] = port_dem_10_05[37] *6.50334668e-01 # banca mediolanum
#port_dem_10_05[39] = port_dem_10_05[39] * 0.14347057  # diasorin
#port_dem_10_05[26] = port_dem_10_05[26] * 1.09356739e-01
port_dem_10_05['return'] = port_dem_10_05.sum(axis=1)
#port_dem_10_05['return'] = port_dem_10_05['return'].cumsum()
#
#Cumulative ret GA n.10
lista_ga_10 = [13,15,36,37]
port_ga_10_05 = df_allstocks_05.iloc[:,lista_ga_10]
#port_ga_10_05[3] =port_ga_10_05[3] * 3.55085851e-01    # Amplifon
port_ga_10_05[13] =port_ga_10_05[13] * 1.29044515e-01 # banca mediolanum
port_ga_10_05[15] =port_ga_10_05[15] * 1.67317541e-01   # diasorin
#port_ga_10_05[27] =port_ga_10_05[27] * 6.95366723e-01  # generali assicurazioni
port_ga_10_05[36] =port_ga_10_05[36] * 2.58664901e-01  # generali assicurazioni
port_ga_10_05[37] =port_ga_10_05[37] * 4.44493924e-01  # generali assicurazioni
port_ga_10_05['return'] = port_ga_10_05.sum(axis=1)
#port_ga_10_05['return'] = port_ga_10_05['return'].cumsum()
#
#cumulative ret LEVY n.10
lista_levy_10 = [13,15,30,36,37]
port_levy_10_05 = df_allstocks_05.iloc[:,lista_levy_10]
port_levy_10_05[13] = port_levy_10_05[13] * 6.54612407e-02
port_levy_10_05[15] = port_levy_10_05[15] * 1.41842182e-01# enel
port_levy_10_05[30] = port_levy_10_05[30] * 8.25125680e-03 # enel
port_levy_10_05[36] = port_levy_10_05[36] * 1.31707301e-01 # enel
port_levy_10_05[37] = port_levy_10_05[37] * 6.52124687e-01 # enel
#port_levy_10_05[15] = port_levy_10_05[15] * 7.08601010e-01 # enel
#port_levy_10_05[27] = port_levy_10_05[27] * 2.91398975e-01   # Amplifon
port_levy_10_05['return'] = port_levy_10_05.sum(axis=1)
#port_levy_10_05['return'] = port_levy_10_05['return'].cumsum()
#
#cumulative ret NSGA2 n.10
lista_nsga2_10 = [36,37]
port_nsga2_10_05 = df_allstocks_05.iloc[:,lista_nsga2_10]
port_nsga2_10_05[36] = port_nsga2_10_05[36] * 3.22373995e-01    #banca mediolanum
port_nsga2_10_05[37] = port_nsga2_10_05[37] * 6.76608262e-01
#port_nsga2_10_05[39] = port_nsga2_10_05[39] * 1.86870609e-01
port_nsga2_10_05['return'] = port_nsga2_10_05.sum(axis=1)
#port_nsga2_10_05['return'] = port_nsga2_10_05['return'].cumsum()
#
# cumulative ret DE n.10
lista_de_10 = [36,37]
port_de_10_05 = df_allstocks_05.iloc[:,lista_de_10]
# ritorni * pesi selezionati
port_de_10_05[36] = port_de_10_05[36] * 0.30662125
port_de_10_05[37] = port_de_10_05[37] *0.69337875
#port_de_10_05[26] = port_de_10_05[26] * 0.43354955
port_de_10_05['return'] = port_de_10_05.sum(axis=1)
#port_de_10_05['return'] = port_de_10_05['return'].cumsum()
#


#
# cum ret DEM n.20
lista_dem_20 = [3,6,13,15,30,36,37]
port_dem_20_05 = df_allstocks_05.iloc[:,lista_dem_20]
port_dem_20_05[3] = port_dem_20_05[3] *5.77320531e-02  # diasorin
port_dem_20_05[6] = port_dem_20_05[6] * 1.35686299e-03 # diasorin
port_dem_20_05[15] = port_dem_20_05[15] * 2.38082822e-01 # diasorin
port_dem_20_05[13] = port_dem_20_05[13] * 2.31696501e-01  # diasorin
port_dem_20_05[30] = port_dem_20_05[30] *5.31004045e-02 # banca mediolanum
port_dem_20_05[37] = port_dem_20_05[37] *1.01461490e-01 # banca mediolanum
port_dem_20_05[36] = port_dem_20_05[36] *3.16515818e-01# banca mediolanum
#port_dem_20_05[28] = port_dem_20_05[28] *1.01662872e-01 # banca mediolanum
#port_dem_20_05[29] = port_dem_20_05[29] *0.0164697  # banca mediolanum
#port_dem_20_05[32] = port_dem_20_05[32] *1.54936330e-02  # banca mediolanum
#port_dem_20_05[35] = port_dem_20_05[35] *5.85805052e-03  # banca mediolanum
#port_dem_20_05[39] = port_dem_20_05[39] *2.49230293e-01  # banca mediolanum
port_dem_20_05['return'] = port_dem_20_05.sum(axis=1)
#port_dem_20_05['return'] = port_dem_20_05['return'].cumsum()
#
#Cumulative ret GA n.20
lista_ga_20 = [2,8,13,15,24,30,36,37]
port_ga_20_05 = df_allstocks_05.iloc[:,lista_ga_20]
port_ga_20_05[2] =port_ga_20_05[2] * 7.84410376e-02   # Amplifon
port_ga_20_05[8] =port_ga_20_05[8] * 6.57137964e-03    # Amplifon
port_ga_20_05[13] =port_ga_20_05[13] * 1.90921118e-01 # banca mediolanum
port_ga_20_05[15] =port_ga_20_05[15] * 2.70809543e-01   # diasorin
port_ga_20_05[24] =port_ga_20_05[24] * 4.24158531e-02  # generali assicurazioni
port_ga_20_05[30] =port_ga_20_05[30] * 3.88099190e-02  # generali assicurazioni
port_ga_20_05[37] =port_ga_20_05[37] * 6.55089241e-02  # generali assicurazioni
port_ga_20_05[36] =port_ga_20_05[36] * 3.06496177e-01  # generali assicurazioni
port_ga_20_05['return'] = port_ga_20_05.sum(axis=1)
#port_ga_20_05['return'] = port_ga_20_05['return'].cumsum()
#
#cumulative ret LEVY n.20
lista_levy_20 = [2,3,13,15,30,36,37]
port_levy_20_05 = df_allstocks_05.iloc[:,lista_levy_20]
port_levy_20_05[2] = port_levy_20_05[2] * 6.97339198e-02
port_levy_20_05[3] = port_levy_20_05[3] * 1.97317943e-02 # enel
port_levy_20_05[15] = port_levy_20_05[15] * 2.60725499e-01 # enel
port_levy_20_05[13] = port_levy_20_05[13] * 2.07173869e-01
port_levy_20_05[30] = port_levy_20_05[30] * 2.82061500e-03
#port_levy_20_05[25] = port_levy_20_05[25] * 1.01196434e-01    # enel
port_levy_20_05[37] = port_levy_20_05[37] * 1.45729992e-01    # enel
port_levy_20_05[36] = port_levy_20_05[36] *2.93806570e-01    # enel
#port_levy_20_05[38] = port_levy_20_05[38] * 2.62502498e-03    # enel
#port_levy_20_05[39] = port_levy_20_05[39] * 2.45420415e-01   # Amplifon
port_levy_20_05['return'] = port_levy_20_05.sum(axis=1)
#port_levy_20_05['return'] = port_levy_20_05['return'].cumsum()

#cumulative ret NSGA2 n.20
lista_nsga2_20 = [13,15,36,37]
port_nsga2_20_05 = df_allstocks_05.iloc[:,lista_nsga2_20]
#port_nsga2_20_05[3] = port_nsga2_20_05[3] * 9.08406690e-02    # inwit
port_nsga2_20_05[13] = port_nsga2_20_05[13] * 1.81142078e-01   # inwit
port_nsga2_20_05[15] = port_nsga2_20_05[15] * 2.18279266e-01    # inwit
port_nsga2_20_05[36] = port_nsga2_20_05[36] *2.46348992e-01
port_nsga2_20_05[37] = port_nsga2_20_05[37] * 3.53270949e-01
port_nsga2_20_05['return'] = port_nsga2_20_05.sum(axis=1)
#port_nsga2_20_05['return'] = port_nsga2_20_05['return'].cumsum()
#
# cumulative ret DE n.20
lista_de_20 = [2,5,18,23,26,32,36,37]
port_de_20_05 = df_allstocks_05.iloc[:,lista_de_20]
# ritorni * pesi selezionati
port_de_20_05[2] = port_de_20_05[2] * 2.18358171e-03
port_de_20_05[18] = port_de_20_05[18] * 2.46770743e-01
port_de_20_05[23] = port_de_20_05[23] * 1.93497703e-03
port_de_20_05[5] = port_de_20_05[5] * 1.17556165e-03
port_de_20_05[26] = port_de_20_05[26] * 2.69300657e-03
port_de_20_05[32] = port_de_20_05[32] * 1.38075502e-01
port_de_20_05[36] = port_de_20_05[36] * 2.49713691e-01
port_de_20_05[37] = port_de_20_05[37] * 3.56565226e-01
port_de_20_05['return'] = port_de_20_05.sum(axis=1)
#port_de_20_05['return'] = port_de_20_05['return'].cumsum()
#




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


# #Cumulative returns portfolio DEM n.10
lista_dem_10 = [16,22,25,36,38]
port_dem_10_06 = df_allstocks_06.iloc[:,lista_dem_10]
port_dem_10_06[16] = port_dem_10_06[16] *0.13663755 # banca mediolanum
port_dem_10_06[22] = port_dem_10_06[22] *0.07052724 # banca mediolanum
port_dem_10_06[25] = port_dem_10_06[25] *0.1257773  # banca mediolanum
port_dem_10_06[36] = port_dem_10_06[36] *0.66147807 # banca mediolanum
port_dem_10_06[38] = port_dem_10_06[38] * 0.00557983  # diasorin
#port_dem_10_06[26] = port_dem_10_06[26] * 1.09356739e-01
port_dem_10_06['return'] = port_dem_10_06.sum(axis=1)
#port_dem_10_06['return'] = port_dem_10_06['return'].cumsum()
#
#Cumulative ret GA n.10
lista_ga_10 = [16,25,36]
port_ga_10_06 = df_allstocks_06.iloc[:,lista_ga_10]
#port_ga_10_06[3] =port_ga_10_06[3] * 3.55085851e-01    # Amplifon
port_ga_10_06[16] =port_ga_10_06[16] * 2.34346137e-01 # banca mediolanum
port_ga_10_06[25] =port_ga_10_06[25] * 1.24729243e-01   # diasorin
#port_ga_10_06[27] =port_ga_10_06[27] * 6.95366723e-01  # generali assicurazioni
port_ga_10_06[36] =port_ga_10_06[36] * 6.40501638e-01  # generali assicurazioni
#port_ga_10_06[37] =port_ga_10_06[37] * 4.44493924e-01  # generali assicurazioni
port_ga_10_06['return'] = port_ga_10_06.sum(axis=1)
#port_ga_10_06['return'] = port_ga_10_06['return'].cumsum()
#
#cumulative ret LEVY n.10
lista_levy_10 = [16,25,36]
port_levy_10_06 = df_allstocks_06.iloc[:,lista_levy_10]
port_levy_10_06[16] = port_levy_10_06[16] * 2.53616401e-01
port_levy_10_06[25] = port_levy_10_06[25] * 9.92712234e-02# enel
#port_levy_10_06[30] = port_levy_10_06[30] * 8.25125680e-03 # enel
port_levy_10_06[36] = port_levy_10_06[36] * 6.46585715e-01 # enel
#port_levy_10_06[37] = port_levy_10_06[37] * 6.52124687e-01 # enel
#port_levy_10_06[15] = port_levy_10_06[15] * 7.08601010e-01 # enel
#port_levy_10_06[27] = port_levy_10_06[27] * 2.91398975e-01   # Amplifon
port_levy_10_06['return'] = port_levy_10_06.sum(axis=1)
#port_levy_10_06['return'] = port_levy_10_06['return'].cumsum()
#
#cumulative ret NSGA2 n.10
lista_nsga2_10 = [8,15,16,22,25,36]
port_nsga2_10_06 = df_allstocks_06.iloc[:,lista_nsga2_10]
port_nsga2_10_06[8] = port_nsga2_10_06[8] *9.63335584e-03    # inwit
port_nsga2_10_06[15] = port_nsga2_10_06[15] * 6.78412885e-03    # inwit
port_nsga2_10_06[16] = port_nsga2_10_06[16] * 2.18881771e-01    # inwit
port_nsga2_10_06[22] = port_nsga2_10_06[22] * 1.71906711e-01    # inwit
port_nsga2_10_06[25] = port_nsga2_10_06[25] * 5.22530185e-02    # inwit
# port_nsga2_10_06[28] = port_nsga2_10_06[28] * 1.34669027e-02   # inwit
port_nsga2_10_06[36] = port_nsga2_10_06[36] * 5.34914054e-01   #banca mediolanum
#port_nsga2_10_06[37] = port_nsga2_10_06[37] * 6.76608262e-01
#port_nsga2_10_06[39] = port_nsga2_10_06[39] * 1.86870609e-01
port_nsga2_10_06['return'] = port_nsga2_10_06.sum(axis=1)
#port_nsga2_10_06['return'] = port_nsga2_10_06['return'].cumsum()
#
# cumulative ret DE n.10
lista_de_10 = [16,25,36]
port_de_10_06 = df_allstocks_06.iloc[:,lista_de_10]
# ritorni * pesi selezionati
port_de_10_06[36] = port_de_10_06[36] * 6.49442183e-01
port_de_10_06[16] = port_de_10_06[16] *2.29778560e-01
port_de_10_06[25] = port_de_10_06[25] * 1.20643917e-01
port_de_10_06['return'] = port_de_10_06.sum(axis=1)
#port_de_10_06['return'] = port_de_10_06['return'].cumsum()


# cum ret DEM n.20
lista_dem_20 = [14,16,17,22,25,26,27,36]
port_dem_20_06 = df_allstocks_06.iloc[:,lista_dem_20]
port_dem_20_06[14] = port_dem_20_06[14] *0.04855044  # diasorin
port_dem_20_06[16] = port_dem_20_06[16] * 0.15837056 # diasorin
port_dem_20_06[17] = port_dem_20_06[17] * 0.06489943 # diasorin
port_dem_20_06[22] = port_dem_20_06[22] * 0.19763802  # diasorin
port_dem_20_06[25] = port_dem_20_06[25] *0.09937795 # banca mediolanum
port_dem_20_06[26] = port_dem_20_06[26] *0.01479711 # banca mediolanum
port_dem_20_06[27] = port_dem_20_06[27] *0.13174261# banca mediolanum
port_dem_20_06[36] = port_dem_20_06[36] *0.28409181 # banca mediolanum
#port_dem_20_06[29] = port_dem_20_06[29] *0.0164697  # banca mediolanum
#port_dem_20_06[32] = port_dem_20_06[32] *1.54936330e-02  # banca mediolanum
#port_dem_20_06[35] = port_dem_20_06[35] *5.85805052e-03  # banca mediolanum
#port_dem_20_06[39] = port_dem_20_06[39] *2.49230293e-01  # banca mediolanum
port_dem_20_06['return'] = port_dem_20_06.sum(axis=1)
#port_dem_20_06['return'] = port_dem_20_06['return'].cumsum()
#
#Cumulative ret GA n.20
lista_ga_20 = [5,9,14,15,16,17,18,21,22,25,26,27,36]
port_ga_20_06 = df_allstocks_06.iloc[:,lista_ga_20]
port_ga_20_06[5] =port_ga_20_06[5] *2.71208325e-03   # Amplifon
port_ga_20_06[9] =port_ga_20_06[9] * 2.60470364e-02    # Amplifon
port_ga_20_06[14] =port_ga_20_06[14] * 1.90871874e-03 # banca mediolanum
port_ga_20_06[15] =port_ga_20_06[15] * 2.07413676e-02  # diasorin
port_ga_20_06[16] =port_ga_20_06[16] * 1.96887490e-01  # generali assicurazioni
port_ga_20_06[17] =port_ga_20_06[17] * 6.46334876e-02  # generali assicurazioni
port_ga_20_06[18] =port_ga_20_06[18] * 1.15880059e-03  # generali assicurazioni
port_ga_20_06[21] =port_ga_20_06[21] * 1.18424048e-02  # generali assicurazioni
port_ga_20_06[22] =port_ga_20_06[22] * 1.32697306e-01  # generali assicurazioni
port_ga_20_06[25] =port_ga_20_06[25] * 6.09812787e-02  # generali assicurazioni
port_ga_20_06[26] =port_ga_20_06[26] * 1.19084719e-02  # generali assicurazioni
port_ga_20_06[27] =port_ga_20_06[27] * 1.91761982e-01  # generali assicurazioni
port_ga_20_06[36] =port_ga_20_06[36] * 2.75800217e-01
port_ga_20_06['return'] = port_ga_20_06.sum(axis=1)
#port_ga_20_06['return'] = port_ga_20_06['return'].cumsum()
#
#cumulative ret LEVY n.20
lista_levy_20 = [9,16,19,22,25,26,27,30,31,36]
port_levy_20_06 = df_allstocks_06.iloc[:,lista_levy_20]
port_levy_20_06[9] = port_levy_20_06[9] * 9.95696682e-02
port_levy_20_06[16] = port_levy_20_06[16] * 1.73866869e-01 # enel
port_levy_20_06[19] = port_levy_20_06[19] * 3.34099096e-03 # enel
port_levy_20_06[22] = port_levy_20_06[22] * 1.25751077e-01
port_levy_20_06[25] = port_levy_20_06[25] * 8.50083268e-02
port_levy_20_06[26] = port_levy_20_06[26] * 9.51489648e-02    # enel
port_levy_20_06[27] = port_levy_20_06[27] * 1.40575122e-01    # enel
port_levy_20_06[30] = port_levy_20_06[30] *7.87224941e-03    # enel
port_levy_20_06[31] = port_levy_20_06[31] * 1.41975545e-03    # enel
port_levy_20_06[36] = port_levy_20_06[36] * 2.66844572e-01   # Amplifon
port_levy_20_06['return'] = port_levy_20_06.sum(axis=1)
#port_levy_20_06['return'] = port_levy_20_06['return'].cumsum()

#cumulative ret NSGA2 n.20
lista_nsga2_20 = [5,15,16,17,22,25,31,32,34,36]
port_nsga2_20_06 = df_allstocks_06.iloc[:,lista_nsga2_20]
port_nsga2_20_06[5] = port_nsga2_20_06[5] * 1.80323660e-03    # inwit
port_nsga2_20_06[15] = port_nsga2_20_06[15] * 9.84684267e-03   # inwit
port_nsga2_20_06[16] = port_nsga2_20_06[16] * 2.32090080e-01    # inwit
port_nsga2_20_06[17] = port_nsga2_20_06[17] * 6.63213765e-02
port_nsga2_20_06[22] = port_nsga2_20_06[22] * 2.08643702e-01
port_nsga2_20_06[25] = port_nsga2_20_06[25] * 1.04199693e-01
port_nsga2_20_06[31] = port_nsga2_20_06[31] *1.06723270e-03
port_nsga2_20_06[32] = port_nsga2_20_06[32] * 1.65017471e-03
port_nsga2_20_06[34] = port_nsga2_20_06[34] * 1.11681195e-03
port_nsga2_20_06[36] = port_nsga2_20_06[36] * 3.69119239e-01
port_nsga2_20_06['return'] = port_nsga2_20_06.sum(axis=1)
#port_nsga2_20_06['return'] = port_nsga2_20_06['return'].cumsum()
#
# cumulative ret DE n.20
lista_de_20 = [14,16,19,21,25,36]
port_de_20_06 = df_allstocks_06.iloc[:,lista_de_20]
# ritorni * pesi selezionati
port_de_20_06[14] = port_de_20_06[14] * 3.44557333e-01
port_de_20_06[16] = port_de_20_06[16] * 1.98565617e-01
port_de_20_06[19] = port_de_20_06[19] *2.80216696e-02
port_de_20_06[21] = port_de_20_06[21] * 5.78100772e-02
port_de_20_06[25] = port_de_20_06[25] * 7.34055698e-02
#port_de_20_06[32] = port_de_20_06[32] * 1.38075502e-01
port_de_20_06[36] = port_de_20_06[36] * 2.96296870e-01
#port_de_20_06[37] = port_de_20_06[37] * 3.56565226e-01
port_de_20_06['return'] = port_de_20_06.sum(axis=1)
#port_de_20_06['return'] = port_de_20_06['return'].cumsum()
#



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


# #Cumulative returns portfolio DEM n.10
lista_dem_10 = [0,9,29,37,39]
port_dem_10_07 = df_allstocks_07.iloc[:,lista_dem_10]
port_dem_10_07[0] = port_dem_10_07[0] *0.01998495 # banca mediolanum
port_dem_10_07[9] = port_dem_10_07[9] *0.24118636 # banca mediolanum
port_dem_10_07[29] = port_dem_10_07[29] *0.02939622  # banca mediolanum
port_dem_10_07[37] = port_dem_10_07[37] *0.706822   # banca mediolanum
port_dem_10_07[39] = port_dem_10_07[39] *0.00261047  # diasorin
#port_dem_10_07[26] = port_dem_10_07[26] * 1.09356739e-01
port_dem_10_07['return'] = port_dem_10_07.sum(axis=1)
#port_dem_10_07['return'] = port_dem_10_07['return'].cumsum()
#
#Cumulative ret GA n.10
lista_ga_10 = [0,3,12,37]
port_ga_10_07 = df_allstocks_07.iloc[:,lista_ga_10]
#port_ga_10_07[3] =port_ga_10_07[3] * 3.55085851e-01    # Amplifon
port_ga_10_07[0] =port_ga_10_07[0] * 5.47866933e-02 # banca mediolanum
port_ga_10_07[3] =port_ga_10_07[3] * 9.13422623e-02   # diasorin
#port_ga_10_07[27] =port_ga_10_07[27] * 6.95366723e-01  # generali assicurazioni
port_ga_10_07[12] =port_ga_10_07[12] * 1.15941174e-01  # generali assicurazioni
port_ga_10_07[37] =port_ga_10_07[37] * 7.37795872e-01  # generali assicurazioni
port_ga_10_07['return'] = port_ga_10_07.sum(axis=1)
#port_ga_10_07['return'] = port_ga_10_07['return'].cumsum()
#
#cumulative ret LEVY n.10
lista_levy_10 = [0,7,9,29,37]
port_levy_10_07 = df_allstocks_07.iloc[:,lista_levy_10]
port_levy_10_07[0] = port_levy_10_07[0] * 8.83607202e-02
port_levy_10_07[7] = port_levy_10_07[7] * 1.08242866e-02# enel
port_levy_10_07[9] = port_levy_10_07[9] * 1.62198787e-01 # enel
port_levy_10_07[29] = port_levy_10_07[29] * 3.39344549e-02 # enel
port_levy_10_07[37] = port_levy_10_07[37] * 7.04276329e-01 # enel
#port_levy_10_07[15] = port_levy_10_07[15] * 7.08601010e-01 # enel
#port_levy_10_07[27] = port_levy_10_07[27] * 2.91398975e-01   # Amplifon
port_levy_10_07['return'] = port_levy_10_07.sum(axis=1)
#port_levy_10_07['return'] = port_levy_10_07['return'].cumsum()
#
#cumulative ret NSGA2 n.10
lista_nsga2_10 = [3,9,12,29,30,37]
port_nsga2_10_07 = df_allstocks_07.iloc[:,lista_nsga2_10]
port_nsga2_10_07[3] = port_nsga2_10_07[3] *6.40082991e-02    # inwit
port_nsga2_10_07[9] = port_nsga2_10_07[9] * 1.59471926e-01    # inwit
port_nsga2_10_07[12] = port_nsga2_10_07[12] * 7.29356275e-02    # inwit
port_nsga2_10_07[29] = port_nsga2_10_07[29] * 6.85653782e-02    # inwit
port_nsga2_10_07[30] = port_nsga2_10_07[30] * 4.32408743e-02    # inwit
# port_nsga2_10_07[28] = port_nsga2_10_07[28] * 1.34669027e-02   # inwit
port_nsga2_10_07[37] = port_nsga2_10_07[37] * 5.89451380e-01   #banca mediolanum
#port_nsga2_10_07[37] = port_nsga2_10_07[37] * 6.76608262e-01
#port_nsga2_10_07[39] = port_nsga2_10_07[39] * 1.86870609e-01
port_nsga2_10_07['return'] = port_nsga2_10_07.sum(axis=1)
#port_nsga2_10_07['return'] = port_nsga2_10_07['return'].cumsum()
#
# cumulative ret DE n.10
lista_de_10 = [29,37]
port_de_10_07 = df_allstocks_07.iloc[:,lista_de_10]
# ritorni * pesi selezionati
port_de_10_07[37] = port_de_10_07[37] *0.76484375
port_de_10_07[29] = port_de_10_07[29] *0.23515625
#port_de_10_07[25] = port_de_10_07[25] * 1.20643917e-01
port_de_10_07['return'] = port_de_10_07.sum(axis=1)
#port_de_10_07['return'] = port_de_10_07['return'].cumsum()
#



# cum ret DEM n.20
lista_dem_20 = [3,7,9,12,32,37]
port_dem_20_07 = df_allstocks_07.iloc[:,lista_dem_20]
port_dem_20_07[3] = port_dem_20_07[3] *2.28262022e-01  # diasorin
port_dem_20_07[7] = port_dem_20_07[7] * 2.94866700e-02 # diasorin
port_dem_20_07[9] = port_dem_20_07[9] * 2.56305715e-01 # diasorin
port_dem_20_07[12] = port_dem_20_07[12] * 1.71705086e-01  # diasorin
port_dem_20_07[32] = port_dem_20_07[32] *5.58116811e-02 # banca mediolanum
port_dem_20_07[37] = port_dem_20_07[37] *2.58417117e-01 # banca mediolanum
#port_dem_20_07[27] = port_dem_20_07[27] *0.13174261# banca mediolanum
#port_dem_20_07[36] = port_dem_20_07[36] *0.28409181 # banca mediolanum
#port_dem_20_07[29] = port_dem_20_07[29] *0.0164697  # banca mediolanum
#port_dem_20_07[32] = port_dem_20_07[32] *1.54936330e-02  # banca mediolanum
#port_dem_20_07[35] = port_dem_20_07[35] *5.85805052e-03  # banca mediolanum
#port_dem_20_07[39] = port_dem_20_07[39] *2.49230293e-01  # banca mediolanum
port_dem_20_07['return'] = port_dem_20_07.sum(axis=1)
#port_dem_20_07['return'] = port_dem_20_07['return'].cumsum()
#
#Cumulative ret GA n.20
lista_ga_20 = [2,3,9,12,29,37]
port_ga_20_07 = df_allstocks_07.iloc[:,lista_ga_20]
port_ga_20_07[2] =port_ga_20_07[2] *7.39578746e-03   # Amplifon
port_ga_20_07[3] =port_ga_20_07[3] * 1.59405619e-01    # Amplifon
port_ga_20_07[9] =port_ga_20_07[9] * 2.01361426e-01 # banca mediolanum
port_ga_20_07[12] =port_ga_20_07[12] * 2.18857427e-01  # diasorin
port_ga_20_07[29] =port_ga_20_07[29] * 6.06044500e-02  # generali assicurazioni
port_ga_20_07[37] =port_ga_20_07[37] * 3.51990305e-01  # generali assicurazioni
#port_ga_20_07[18] =port_ga_20_07[18] * 1.15880059e-03  # generali assicurazioni
#port_ga_20_07[21] =port_ga_20_07[21] * 1.18424048e-02  # generali assicurazioni
#port_ga_20_07[22] =port_ga_20_07[22] * 1.32697306e-01  # generali assicurazioni
#port_ga_20_07[25] =port_ga_20_07[25] * 6.09812787e-02  # generali assicurazioni
#port_ga_20_07[26] =port_ga_20_07[26] * 1.19084719e-02  # generali assicurazioni
#port_ga_20_07[27] =port_ga_20_07[27] * 1.91761982e-01  # generali assicurazioni
#port_ga_20_07[36] =port_ga_20_07[36] * 2.75800217e-01
port_ga_20_07['return'] = port_ga_20_07.sum(axis=1)
#port_ga_20_07['return'] = port_ga_20_07['return'].cumsum()
#
#cumulative ret LEVY n.20
lista_levy_20 = [0,3,7,9,12,27,32,37]
port_levy_20_07 = df_allstocks_07.iloc[:,lista_levy_20]
port_levy_20_07[0] = port_levy_20_07[0] * 1.57168275e-02
port_levy_20_07[3] = port_levy_20_07[3] * 1.56481321e-01 # enel
port_levy_20_07[7] = port_levy_20_07[7] * 1.37383213e-02 # enel
port_levy_20_07[9] = port_levy_20_07[9] * 1.46111879e-01
port_levy_20_07[12] = port_levy_20_07[12] * 2.64090358e-01
#port_levy_20_07[26] = port_levy_20_07[26] * 9.51489648e-02    # enel
port_levy_20_07[27] = port_levy_20_07[27] * 5.46051782e-03   # enel
port_levy_20_07[32] = port_levy_20_07[32] *3.71081905e-03    # enel
port_levy_20_07[37] = port_levy_20_07[37] * 3.31750427e-01    # enel
#port_levy_20_07[36] = port_levy_20_07[36] * 2.66844572e-01   # Amplifon
port_levy_20_07['return'] = port_levy_20_07.sum(axis=1)
#port_levy_20_07['return'] = port_levy_20_07['return'].cumsum()

#cumulative ret NSGA2 n.20
lista_nsga2_20 = [2,3,5,6,9,12,27,29,30,36,37]
port_nsga2_20_07 = df_allstocks_07.iloc[:,lista_nsga2_20]
port_nsga2_20_07[2] = port_nsga2_20_07[2] * 2.18782562e-01    # inwit
port_nsga2_20_07[3] = port_nsga2_20_07[3] * 1.18113057e-01   # inwit
port_nsga2_20_07[5] = port_nsga2_20_07[5] * 2.82925822e-03    # inwit
port_nsga2_20_07[6] = port_nsga2_20_07[6] * 3.56216423e-02
port_nsga2_20_07[9] = port_nsga2_20_07[9] * 1.65542679e-01
port_nsga2_20_07[12] = port_nsga2_20_07[12] * 1.38957681e-01
port_nsga2_20_07[27] = port_nsga2_20_07[27] *8.89075425e-02
port_nsga2_20_07[29] = port_nsga2_20_07[29] * 1.29222043e-01
port_nsga2_20_07[30] = port_nsga2_20_07[30] * 1.94325902e-03
port_nsga2_20_07[36] = port_nsga2_20_07[36] * 8.98727566e-02
port_nsga2_20_07[37] = port_nsga2_20_07[37] * 9.63649141e-03
port_nsga2_20_07['return'] = port_nsga2_20_07.sum(axis=1)
#port_nsga2_20_07['return'] = port_nsga2_20_07['return'].cumsum()
#
# cumulative ret DE n.20
lista_de_20 = [6,29,37]
port_de_20_07 = df_allstocks_07.iloc[:,lista_de_20]
# ritorni * pesi selezionati
port_de_20_07[6] = port_de_20_07[6] * 0.23012399
port_de_20_07[29] = port_de_20_07[29] * 0.42827457
port_de_20_07[37] = port_de_20_07[37] *0.34160144
#port_de_20_07[21] = port_de_20_07[21] * 5.78100772e-02
#port_de_20_07[25] = port_de_20_07[25] * 7.34055698e-02
#port_de_20_07[32] = port_de_20_07[32] * 1.38075502e-01
#port_de_20_07[36] = port_de_20_07[36] * 2.96296870e-01
#port_de_20_07[37] = port_de_20_07[37] * 3.56565226e-01
port_de_20_07['return'] = port_de_20_07.sum(axis=1)
#port_de_20_07['return'] = port_de_20_07['return'].cumsum()
#


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


# #Cumulative returns portfolio DEM n.10
lista_dem_10 = [2,25,34]
port_dem_10_08 = df_allstocks_08.iloc[:,lista_dem_10]
port_dem_10_08[2] = port_dem_10_08[2] *3.57044204e-01 # banca mediolanum
port_dem_10_08[25] = port_dem_10_08[25] *6.40875182e-01 # banca mediolanum
port_dem_10_08[34] = port_dem_10_08[34] *1.92306441e-03  # banca mediolanum
#port_dem_10_08[37] = port_dem_10_08[37] *0.706822   # banca mediolanum
#port_dem_10_08[39] = port_dem_10_08[39] *0.00261047  # diasorin
#port_dem_10_08[26] = port_dem_10_08[26] * 1.09356739e-01
port_dem_10_08['return'] = port_dem_10_08.sum(axis=1)
#port_dem_10_08['return'] = port_dem_10_08['return'].cumsum()
#
#Cumulative ret GA n.10
lista_ga_10 = [2,25,32]
port_ga_10_08 = df_allstocks_08.iloc[:,lista_ga_10]
#port_ga_10_08[3] =port_ga_10_08[3] * 3.55085851e-01    # Amplifon
port_ga_10_08[2] =port_ga_10_08[2] * 3.25506063e-01 # banca mediolanum
port_ga_10_08[25] =port_ga_10_08[25] * 6.60921861e-01   # diasorin
#port_ga_10_08[27] =port_ga_10_08[27] * 6.95366723e-01  # generali assicurazioni
port_ga_10_08[32] =port_ga_10_08[32] * 1.35701139e-02  # generali assicurazioni
#port_ga_10_08[37] =port_ga_10_08[37] * 7.37795872e-01  # generali assicurazioni
port_ga_10_08['return'] = port_ga_10_08.sum(axis=1)
#port_ga_10_08['return'] = port_ga_10_08['return'].cumsum()
#
#cumulative ret LEVY n.10
lista_levy_10 = [2,13,22,25,31,32,36]
port_levy_10_08 = df_allstocks_08.iloc[:,lista_levy_10]
port_levy_10_08[2] = port_levy_10_08[2] * 2.35437580e-01
port_levy_10_08[13] = port_levy_10_08[13] * 7.93455303e-03# enel
port_levy_10_08[22] = port_levy_10_08[22] * 1.19259766e-03 # enel
port_levy_10_08[25] = port_levy_10_08[25] * 7.03749721e-01 # enel
port_levy_10_08[31] = port_levy_10_08[31] * 1.15859488e-03 # enel
port_levy_10_08[32] = port_levy_10_08[32] * 4.82535635e-02 # enel
port_levy_10_08[36] = port_levy_10_08[36] * 1.84686086e-03   # Amplifon
port_levy_10_08['return'] = port_levy_10_08.sum(axis=1)
#p#ort_levy_10_08['return'] = port_levy_10_08['return'].cumsum()
#
#cumulative ret NSGA2 n.10
lista_nsga2_10 = [2,25,31,32]
port_nsga2_10_08 = df_allstocks_08.iloc[:,lista_nsga2_10]
port_nsga2_10_08[2] = port_nsga2_10_08[2] *1.11348188e-01    # inwit
port_nsga2_10_08[25] = port_nsga2_10_08[25] * 8.84101449e-01    # inwit
port_nsga2_10_08[31] = port_nsga2_10_08[31] * 1.03155228e-03    # inwit
port_nsga2_10_08[32] = port_nsga2_10_08[32] * 2.75644800e-03    # inwit
#port_nsga2_10_08[30] = port_nsga2_10_08[30] * 4.32408743e-02    # inwit
# port_nsga2_10_08[28] = port_nsga2_10_08[28] * 1.34669027e-02   # inwit
#port_nsga2_10_08[37] = port_nsga2_10_08[37] * 5.89451380e-01   #banca mediolanum
#port_nsga2_10_08[37] = port_nsga2_10_08[37] * 6.76608262e-01
#port_nsga2_10_08[39] = port_nsga2_10_08[39] * 1.86870609e-01
port_nsga2_10_08['return'] = port_nsga2_10_08.sum(axis=1)
#port_nsga2_10_08['return'] = port_nsga2_10_08['return'].cumsum()
#
# cumulative ret DE n.10
lista_de_10 = [2,27]
port_de_10_08 = df_allstocks_08.iloc[:,lista_de_10]
# ritorni * pesi selezionati
port_de_10_08[2] = port_de_10_08[2] *0.77143716
port_de_10_08[27] = port_de_10_08[27] *0.22856284
#port_de_10_08[25] = port_de_10_08[25] * 1.20643917e-01
port_de_10_08['return'] = port_de_10_08.sum(axis=1)
#port_de_10_08['return'] = port_de_10_08['return'].cumsum()
#


# cum ret DEM n.20
lista_dem_20 = [2,12,25,27,29,32]
port_dem_20_08 = df_allstocks_08.iloc[:,lista_dem_20]
port_dem_20_08[2] = port_dem_20_08[2] *1.99752171e-01  # diasorin
port_dem_20_08[12] = port_dem_20_08[12] * 3.04991606e-02 # diasorin
port_dem_20_08[25] = port_dem_20_08[25] * 4.11501377e-01 # diasorin
port_dem_20_08[27] = port_dem_20_08[27] * 1.14459679e-01  # diasorin
port_dem_20_08[29] = port_dem_20_08[29] *1.31137829e-02 # banca mediolanum
port_dem_20_08[32] = port_dem_20_08[32] *2.30588975e-01 # banca mediolanum
#port_dem_20_08[27] = port_dem_20_08[27] *0.13174261# banca mediolanum
#port_dem_20_08[36] = port_dem_20_08[36] *0.28409181 # banca mediolanum
#port_dem_20_08[29] = port_dem_20_08[29] *0.0164697  # banca mediolanum
#port_dem_20_08[32] = port_dem_20_08[32] *1.54936330e-02  # banca mediolanum
#port_dem_20_08[35] = port_dem_20_08[35] *5.85805052e-03  # banca mediolanum
#port_dem_20_08[39] = port_dem_20_08[39] *2.49230293e-01  # banca mediolanum
port_dem_20_08['return'] = port_dem_20_08.sum(axis=1)
#port_dem_20_08['return'] = port_dem_20_08['return'].cumsum()
#
#Cumulative ret GA n.20
lista_ga_20 = [2,12,25,27,32]
port_ga_20_08 = df_allstocks_08.iloc[:,lista_ga_20]
port_ga_20_08[2] =port_ga_20_08[2] *2.26202998e-01   # Amplifon
port_ga_20_08[12] =port_ga_20_08[12] * 4.48842457e-02    # Amplifon
port_ga_20_08[25] =port_ga_20_08[25] * 4.08059452e-01 # banca mediolanum
port_ga_20_08[27] =port_ga_20_08[27] * 9.30103093e-02  # diasorin
port_ga_20_08[32] =port_ga_20_08[32] * 2.25902209e-01  # generali assicurazioni
#port_ga_20_08[37] =port_ga_20_08[37] * 3.51990305e-01  # generali assicurazioni
#port_ga_20_08[18] =port_ga_20_08[18] * 1.15880059e-03  # generali assicurazioni
#port_ga_20_08[21] =port_ga_20_08[21] * 1.18424048e-02  # generali assicurazioni
#port_ga_20_08[22] =port_ga_20_08[22] * 1.32697306e-01  # generali assicurazioni
#port_ga_20_08[25] =port_ga_20_08[25] * 6.09812787e-02  # generali assicurazioni
#port_ga_20_08[26] =port_ga_20_08[26] * 1.19084719e-02  # generali assicurazioni
#port_ga_20_08[27] =port_ga_20_08[27] * 1.91761982e-01  # generali assicurazioni
#port_ga_20_08[36] =port_ga_20_08[36] * 2.75800217e-01
port_ga_20_08['return'] = port_ga_20_08.sum(axis=1)
#port_ga_20_08['return'] = port_ga_20_08['return'].cumsum()
#
#cumulative ret LEVY n.20
lista_levy_20 = [2,6,12,13,25,27,32]
port_levy_20_08 = df_allstocks_08.iloc[:,lista_levy_20]
port_levy_20_08[2] = port_levy_20_08[2] * 2.10810518e-01
port_levy_20_08[6] = port_levy_20_08[6] * 1.07501334e-03 # enel
port_levy_20_08[12] = port_levy_20_08[12] * 7.70812401e-02 # enel
port_levy_20_08[13] = port_levy_20_08[13] * 3.52108289e-02
port_levy_20_08[25] = port_levy_20_08[25] * 4.11038454e-01
#port_levy_20_08[26] = port_levy_20_08[26] * 9.51489648e-02    # enel
port_levy_20_08[27] = port_levy_20_08[27] * 9.73064678e-03  # enel
port_levy_20_08[32] = port_levy_20_08[32] *2.54644892e-01   # enel
#port_levy_20_08[37] = port_levy_20_08[37] * 3.31750427e-01    # enel
#port_levy_20_08[36] = port_levy_20_08[36] * 2.66844572e-01   # Amplifon
port_levy_20_08['return'] = port_levy_20_08.sum(axis=1)
#port_levy_20_08['return'] = port_levy_20_08['return'].cumsum()

#cumulative ret NSGA2 n.20
lista_nsga2_20 = [2,6,12,15,25,27,31,32]
port_nsga2_20_08 = df_allstocks_08.iloc[:,lista_nsga2_20]
port_nsga2_20_08[2] = port_nsga2_20_08[2] * 2.31168975e-01    # inwit
port_nsga2_20_08[6] = port_nsga2_20_08[6] * 5.08332910e-03   # inwit
port_nsga2_20_08[12] = port_nsga2_20_08[12] * 3.70048943e-02    # inwit
port_nsga2_20_08[15] = port_nsga2_20_08[15] * 2.60065966e-02
port_nsga2_20_08[25] = port_nsga2_20_08[25] * 3.27408993e-01
#port_nsga2_20_08[12] = port_nsga2_20_08[12] * 1.38957681e-01
port_nsga2_20_08[27] = port_nsga2_20_08[27] *2.14949388e-01
port_nsga2_20_08[31] = port_nsga2_20_08[31] * 2.64936537e-02
port_nsga2_20_08[32] = port_nsga2_20_08[32] * 1.31558361e-01
port_nsga2_20_08['return'] = port_nsga2_20_08.sum(axis=1)
#port_nsga2_20_08['return'] = port_nsga2_20_08['return'].cumsum()
#
# cumulative ret DE n.20
lista_de_20 = [2,15,27]
port_de_20_08 = df_allstocks_08.iloc[:,lista_de_20]
# ritorni * pesi selezionati
port_de_20_08[2] = port_de_20_08[2] * 0.4718565
port_de_20_08[15] = port_de_20_08[15] * 0.03958886
port_de_20_08[27] = port_de_20_08[27] *0.48855464
#port_de_20_08[21] = port_de_20_08[21] * 5.78100772e-02
#port_de_20_08[25] = port_de_20_08[25] * 7.34055698e-02
#port_de_20_08[32] = port_de_20_08[32] * 1.38075502e-01
#port_de_20_08[36] = port_de_20_08[36] * 2.96296870e-01
#port_de_20_08[37] = port_de_20_08[37] * 3.56565226e-01
port_de_20_08['return'] = port_de_20_08.sum(axis=1)
#port_de_20_08['return'] = port_de_20_08['return'].cumsum()



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


# #Cumulative returns portfolio DEM n.10
lista_dem_10 = [0,1,11,13,27,32]
port_dem_10_09 = df_allstocks_09.iloc[:,lista_dem_10]
port_dem_10_09[0] = port_dem_10_09[0] * 2.90480478e-01 # banca mediolanum
port_dem_10_09[1] = port_dem_10_09[1] * 3.74083447e-02 # banca mediolanum
port_dem_10_09[11] = port_dem_10_09[11] *1.63326821e-03  # banca mediolanum
port_dem_10_09[13] = port_dem_10_09[13] *5.16485520e-01   # banca mediolanum
port_dem_10_09[27] = port_dem_10_09[27] *1.51362072e-01  # diasorin
port_dem_10_09[32] = port_dem_10_09[32] * 2.47763460e-03
port_dem_10_09['return'] = port_dem_10_09.sum(axis=1)
#port_dem_10_09['return'] = port_dem_10_09['return'].cumsum()
#
#Cumulative ret GA n.10
lista_ga_10 = [0,13,27]
port_ga_10_09 = df_allstocks_09.iloc[:,lista_ga_10]
#port_ga_10_09[3] =port_ga_10_09[3] * 3.55085851e-01    # Amplifon
port_ga_10_09[0] =port_ga_10_09[0] * 3.76721464e-01 # banca mediolanum
port_ga_10_09[13] =port_ga_10_09[13] * 4.68584871e-01   # diasorin
port_ga_10_09[27] =port_ga_10_09[27] * 1.54195529e-01 # generali assicurazioni
#port_ga_10_09[32] =port_ga_10_09[32] * 1.35701139e-02  # generali assicurazioni
#port_ga_10_09[37] =port_ga_10_09[37] * 7.37795872e-01  # generali assicurazioni
port_ga_10_09['return'] = port_ga_10_09.sum(axis=1)
#port_ga_10_09['return'] = port_ga_10_09['return'].cumsum()
#
#cumulative ret LEVY n.10
lista_levy_10 = [0,13,27,28]
port_levy_10_09 = df_allstocks_09.iloc[:,lista_levy_10]
port_levy_10_09[0] = port_levy_10_09[0] * 3.07982564e-01
port_levy_10_09[13] = port_levy_10_09[13] * 4.84829617e-01# enel
port_levy_10_09[27] = port_levy_10_09[27] * 1.39453816e-01 # enel
port_levy_10_09[28] = port_levy_10_09[28] * 6.47010995e-02 # enel
#port_levy_10_09[31] = port_levy_10_09[31] * 1.15859488e-03 # enel
#port_levy_10_09[32] = port_levy_10_09[32] * 4.82535635e-02 # enel
#port_levy_10_09[36] = port_levy_10_09[36] * 1.84686086e-03   # Amplifon
port_levy_10_09['return'] = port_levy_10_09.sum(axis=1)
#port_levy_10_09['return'] = port_levy_10_09['return'].cumsum()
#
#cumulative ret NSGA2 n.10
lista_nsga2_10 = [0,13,21,27,28,32]
port_nsga2_10_09 = df_allstocks_09.iloc[:,lista_nsga2_10]
port_nsga2_10_09[0] = port_nsga2_10_09[0] *2.75453108e-01    # inwit
port_nsga2_10_09[13] = port_nsga2_10_09[13] * 4.38776787e-01    # inwit
port_nsga2_10_09[21] = port_nsga2_10_09[21] * 5.20979911e-03    # inwit
port_nsga2_10_09[27] = port_nsga2_10_09[27] * 2.27453731e-01    # inwit
#port_nsga2_10_09[30] = port_nsga2_10_09[30] * 4.32408743e-02    # inwit
port_nsga2_10_09[28] = port_nsga2_10_09[28] * 5.13089234e-02   # inwit
port_nsga2_10_09[32] = port_nsga2_10_09[32] * 1.24336406e-03   #banca mediolanum
#port_nsga2_10_09[37] = port_nsga2_10_09[37] * 6.76608262e-01
#port_nsga2_10_09[39] = port_nsga2_10_09[39] * 1.86870609e-01
port_nsga2_10_09['return'] = port_nsga2_10_09.sum(axis=1)
#port_nsga2_10_09['return'] = port_nsga2_10_09['return'].cumsum()
#
# cumulative ret DE n.10
lista_de_10 = [1,13,27]
port_de_10_09 = df_allstocks_09.iloc[:,lista_de_10]
# ritorni * pesi selezionati
port_de_10_09[1] = port_de_10_09[1] *0.14589101
port_de_10_09[13] = port_de_10_09[13] *0.6130276
port_de_10_09[27] = port_de_10_09[27] * 0.24108139
port_de_10_09['return'] = port_de_10_09.sum(axis=1)
#port_de_10_09['return'] = port_de_10_09['return'].cumsum()
#

#
# cum ret DEM n.20
lista_dem_20 = [0,13,14,16,18,25,27,28,32]
port_dem_20_09 = df_allstocks_09.iloc[:,lista_dem_20]
port_dem_20_09[0] = port_dem_20_09[0] *3.81731996e-01  # diasorin
port_dem_20_09[13] = port_dem_20_09[13] * 1.71164320e-01 # diasorin
port_dem_20_09[14] = port_dem_20_09[14] * 1.57031770e-03 # diasorin
port_dem_20_09[16] = port_dem_20_09[16] * 6.72844556e-03  # diasorin
port_dem_20_09[18] = port_dem_20_09[18] *1.05692042e-03 # banca mediolanum
port_dem_20_09[25] = port_dem_20_09[25] *9.48145932e-02 # banca mediolanum
port_dem_20_09[27] = port_dem_20_09[27] *7.53641351e-02# banca mediolanum
port_dem_20_09[28] = port_dem_20_09[28] *1.77705595e-01 # banca mediolanum
#port_dem_20_09[29] = port_dem_20_09[29] *0.0164697  # banca mediolanum
port_dem_20_09[32] = port_dem_20_09[32] *8.84554915e-02  # banca mediolanum
#port_dem_20_09[35] = port_dem_20_09[35] *5.85805052e-03  # banca mediolanum
#port_dem_20_09[39] = port_dem_20_09[39] *2.49230293e-01  # banca mediolanum
port_dem_20_09['return'] = port_dem_20_09.sum(axis=1)
#port_dem_20_09['return'] = port_dem_20_09['return'].cumsum()
#
#Cumulative ret GA n.20
lista_ga_20 = [0,1,2,3,4,6,13,14,25,27,28,32]
port_ga_20_09 = df_allstocks_09.iloc[:,lista_ga_20]
port_ga_20_09[0] =port_ga_20_09[0] *3.42216499e-01   # Amplifon
port_ga_20_09[1] =port_ga_20_09[1] * 3.71792403e-02    # Amplifon
port_ga_20_09[2] =port_ga_20_09[2] * 4.33847650e-02 # banca mediolanum
port_ga_20_09[3] =port_ga_20_09[3] * 2.29255395e-02  # diasorin
port_ga_20_09[4] =port_ga_20_09[4] * 8.16210539e-03  # generali assicurazioni
port_ga_20_09[6] =port_ga_20_09[6] * 2.09842331e-03  # generali assicurazioni
port_ga_20_09[13] =port_ga_20_09[13] * 7.67420851e-02  # generali assicurazioni
port_ga_20_09[14] =port_ga_20_09[14] * 1.18598718e-03  # generali assicurazioni
port_ga_20_09[28] =port_ga_20_09[28] * 1.64697878e-01  # generali assicurazioni
port_ga_20_09[25] =port_ga_20_09[25] * 3.25409724e-02  # generali assicurazioni
port_ga_20_09[32] =port_ga_20_09[32] * 4.07240371e-03  # generali assicurazioni
port_ga_20_09[27] =port_ga_20_09[27] * 2.64580453e-01  # generali assicurazioni
#port_ga_20_09[36] =port_ga_20_09[36] * 2.75800217e-01
port_ga_20_09['return'] = port_ga_20_09.sum(axis=1)
#port_ga_20_09['return'] = port_ga_20_09['return'].cumsum()
#
#cumulative ret LEVY n.20
lista_levy_20 = [0,1,2,3,4,6,12,13,22,25,27,28,37]
port_levy_20_09 = df_allstocks_09.iloc[:,lista_levy_20]
port_levy_20_09[0] = port_levy_20_09[0] * 2.80402296e-01
port_levy_20_09[1] = port_levy_20_09[1] * 6.98765019e-02 # enel
port_levy_20_09[2] = port_levy_20_09[2] * 1.13737686e-01 # enel
port_levy_20_09[3] = port_levy_20_09[3] * 9.10755688e-03
port_levy_20_09[4] = port_levy_20_09[4] * 4.28163055e-02
port_levy_20_09[6] = port_levy_20_09[6] * 2.00559783e-03    # enel
port_levy_20_09[12] = port_levy_20_09[12] * 1.28502709e-02  # enel
port_levy_20_09[13] = port_levy_20_09[13] *1.60891644e-01  # enel
port_levy_20_09[22] = port_levy_20_09[22] * 1.34163202e-03    # enel
port_levy_20_09[25] = port_levy_20_09[25] * 7.47307435e-02   # Amplifon
port_levy_20_09[27] = port_levy_20_09[27] * 2.14716688e-01
port_levy_20_09[28] = port_levy_20_09[28] * 7.51150226e-03   # Amplifon
port_levy_20_09[37] = port_levy_20_09[37] * 7.67664295e-03   # Amplifon
#port_levy_20_09[25] = port_levy_20_09[25] * 7.47307435e-02   # Amplifon
port_levy_20_09['return'] = port_levy_20_09.sum(axis=1)
#port_levy_20_09['return'] = port_levy_20_09['return'].cumsum()

#cumulative ret NSGA2 n.20
lista_nsga2_20 = [0,4,12,13,21,25,27,28,36,39]
port_nsga2_20_09 = df_allstocks_09.iloc[:,lista_nsga2_20]
port_nsga2_20_09[0] = port_nsga2_20_09[0] * 2.72002082e-01    # inwit
port_nsga2_20_09[4] = port_nsga2_20_09[4] * 2.42761514e-02   # inwit
port_nsga2_20_09[12] = port_nsga2_20_09[12] * 1.48633038e-03   # inwit
port_nsga2_20_09[13] = port_nsga2_20_09[13] * 3.05444229e-01
port_nsga2_20_09[21] = port_nsga2_20_09[21] * 4.72063228e-03
port_nsga2_20_09[25] = port_nsga2_20_09[25] * 1.08035786e-01
port_nsga2_20_09[27] = port_nsga2_20_09[27] *2.13759467e-01
port_nsga2_20_09[28] = port_nsga2_20_09[28] * 4.68894089e-02
port_nsga2_20_09[36] = port_nsga2_20_09[36] * 2.06698503e-02
port_nsga2_20_09[39] = port_nsga2_20_09[39] * 1.10509953e-03
#port_nsga2_20_09[37] = port_nsga2_20_09[37] * 9.63649141e-03
port_nsga2_20_09['return'] = port_nsga2_20_09.sum(axis=1)
#port_nsga2_20_09['return'] = port_nsga2_20_09['return'].cumsum()
#
# cumulative ret DE n.20
lista_de_20 = [1,2,13,27]
port_de_20_09 = df_allstocks_09.iloc[:,lista_de_20]
# ritorni * pesi selezionati
port_de_20_09[1] = port_de_20_09[1] * 0.21193472
port_de_20_09[2] = port_de_20_09[2] * 0.25596096
port_de_20_09[13] = port_de_20_09[13] *0.22800028
port_de_20_09[27] = port_de_20_09[27] * 0.29701253
#port_de_20_09[25] = port_de_20_09[25] * 7.34055698e-02
#port_de_20_09[32] = port_de_20_09[32] * 1.38075502e-01
#port_de_20_09[36] = port_de_20_09[36] * 2.96296870e-01
#port_de_20_09[37] = port_de_20_09[37] * 3.56565226e-01
port_de_20_09['return'] = port_de_20_09.sum(axis=1)
#port_de_20_09['return'] = port_de_20_09['return'].cumsum()
#













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


# #Cumulative returns portfolio DEM n.10
lista_dem_10 = [2,15,36]
port_dem_10_10 = df_allstocks_10.iloc[:,lista_dem_10]
port_dem_10_10[2] = port_dem_10_10[2] * 1.91199757e-01 # banca mediolanum
port_dem_10_10[15] = port_dem_10_10[15] * 7.97203390e-01 # banca mediolanum
port_dem_10_10[36] = port_dem_10_10[36] *9.99668521e-03  # banca mediolanum
#port_dem_10_10[13] = port_dem_10_10[13] *5.16485520e-01   # banca mediolanum
#port_dem_10_10[27] = port_dem_10_10[27] *1.51362072e-01  # diasorin
#port_dem_10_10[32] = port_dem_10_10[32] * 2.47763460e-03
port_dem_10_10['return'] = port_dem_10_10.sum(axis=1)
#port_dem_10_10['return'] = port_dem_10_10['return'].cumsum()
#
#Cumulative ret GA n.10
lista_ga_10 = [2,3,15]
port_ga_10_10 = df_allstocks_10.iloc[:,lista_ga_10]
#port_ga_10_10[3] =port_ga_10_10[3] * 3.55085851e-01    # Amplifon
port_ga_10_10[2] =port_ga_10_10[2] * 2.38326176e-01 # banca mediolanum
port_ga_10_10[3] =port_ga_10_10[3] * 1.82240883e-01   # diasorin
port_ga_10_10[15] =port_ga_10_10[15] * 5.78535021e-01 # generali assicurazioni
#port_ga_10_10[32] =port_ga_10_10[32] * 1.35701139e-02  # generali assicurazioni
#port_ga_10_10[37] =port_ga_10_10[37] * 7.37795872e-01  # generali assicurazioni
port_ga_10_10['return'] = port_ga_10_10.sum(axis=1)
#port_ga_10_10['return'] = port_ga_10_10['return'].cumsum()
#
#cumulative ret LEVY n.10
lista_levy_10 = [2,3,15,20,27]
port_levy_10_10 = df_allstocks_10.iloc[:,lista_levy_10]
port_levy_10_10[2] = port_levy_10_10[2] * 3.28030652e-01
port_levy_10_10[3] = port_levy_10_10[3] * 1.48713368e-01
port_levy_10_10[15] = port_levy_10_10[15] * 5.16840946e-01 # enel
port_levy_10_10[20] = port_levy_10_10[20] * 3.31262847e-03 # enel
port_levy_10_10[27] = port_levy_10_10[27] * 3.06269674e-03 # enel
#port_levy_10_10[32] = port_levy_10_10[32] * 4.82535635e-02 # enel
#port_levy_10_10[36] = port_levy_10_10[36] * 1.84686086e-03   # Amplifon
port_levy_10_10['return'] = port_levy_10_10.sum(axis=1)
#port_levy_10_10['return'] = port_levy_10_10['return'].cumsum()
#
#cumulative ret NSGA2 n.10
lista_nsga2_10 = [2,15,36]
port_nsga2_10_10 = df_allstocks_10.iloc[:,lista_nsga2_10]
port_nsga2_10_10[2] = port_nsga2_10_10[2] *1.91199757e-01    # inwit
port_nsga2_10_10[15] = port_nsga2_10_10[15] * 7.97203390e-01    # inwit
port_nsga2_10_10[36] = port_nsga2_10_10[36] * 9.99668521e-03    # inwit
port_nsga2_10_10['return'] = port_nsga2_10_10.sum(axis=1)
#p#ort_nsga2_10_10['return'] = port_nsga2_10_10['return'].cumsum()
#
# cumulative ret DE n.10
lista_de_10 = [28,30,36]
port_de_10_10 = df_allstocks_10.iloc[:,lista_de_10]
# ritorni * pesi selezionati
port_de_10_10[28] = port_de_10_10[28] *6.08781796e-01
port_de_10_10[30] = port_de_10_10[30] *1.55958499e-02
port_de_10_10[36] = port_de_10_10[36] * 3.75438328e-01
port_de_10_10['return'] = port_de_10_10.sum(axis=1)
#port_de_10_10['return'] = port_de_10_10['return'].cumsum()

#
# cum ret DEM n.20
lista_dem_20 = [2,3,8,15,18,20,30,36]
port_dem_20_10 = df_allstocks_10.iloc[:,lista_dem_20]
port_dem_20_10[2] = port_dem_20_10[2] *0.10794322  # diasorin
port_dem_20_10[3] = port_dem_20_10[3] * 0.3192328  # diasorin
port_dem_20_10[8] = port_dem_20_10[8] * 0.11310896 # diasorin
port_dem_20_10[15] = port_dem_20_10[15] * 0.25992455  # diasorin
port_dem_20_10[18] = port_dem_20_10[18] *0.10566379 # banca mediolanum
port_dem_20_10[20] = port_dem_20_10[20] *0.00178197 # banca mediolanum
port_dem_20_10[30] = port_dem_20_10[30] *0.05929651# banca mediolanum
port_dem_20_10[36] = port_dem_20_10[36] *0.0330482  # banca mediolanum
#port_dem_20_10[29] = port_dem_20_10[29] *0.0164697  # banca mediolanum
#port_dem_20_10[32] = port_dem_20_10[32] *8.84554915e-02  # banca mediolanum
#port_dem_20_10[35] = port_dem_20_10[35] *5.85805052e-03  # banca mediolanum
#port_dem_20_10[39] = port_dem_20_10[39] *2.49230293e-01  # banca mediolanum
port_dem_20_10['return'] = port_dem_20_10.sum(axis=1)
#port_dem_20_10['return'] = port_dem_20_10['return'].cumsum()
#
#Cumulative ret GA n.20
lista_ga_20 = [2,3,8,15,18,20,28,30,36]
port_ga_20_10 = df_allstocks_10.iloc[:,lista_ga_20]
port_ga_20_10[2] =port_ga_20_10[2] *9.05699758e-02   # Amplifon
#port_ga_20_10[1] =port_ga_20_10[1] * 3.71792403e-02    # Amplifon
#port_ga_20_10[2] =port_ga_20_10[2] * 4.33847650e-02 # banca mediolanum
port_ga_20_10[3] =port_ga_20_10[3] * 3.01601352e-01  # diasorin
port_ga_20_10[8] =port_ga_20_10[8] * 1.48772813e-01  # generali assicurazioni
port_ga_20_10[15] =port_ga_20_10[15] * 2.63809050e-01  # generali assicurazioni
port_ga_20_10[18] =port_ga_20_10[18] * 1.00404555e-02  # generali assicurazioni
port_ga_20_10[20] =port_ga_20_10[20] * 1.54642888e-03  # generali assicurazioni
port_ga_20_10[28] =port_ga_20_10[28] * 2.85895158e-03  # generali assicurazioni
port_ga_20_10[30] =port_ga_20_10[30] * 1.25950067e-01  # generali assicurazioni
port_ga_20_10[36] =port_ga_20_10[36] * 5.47314682e-02  # generali assicurazioni
#port_ga_20_10[27] =port_ga_20_10[27] * 2.64580453e-01  # generali assicurazioni
#port_ga_20_10[36] =port_ga_20_10[36] * 2.75800217e-01
port_ga_20_10['return'] = port_ga_20_10.sum(axis=1)
#port_ga_20_10['return'] = port_ga_20_10['return'].cumsum()
#
#cumulative ret LEVY n.20
lista_levy_20 = [2,3,8,15,18,28,30,36]
port_levy_20_10 = df_allstocks_10.iloc[:,lista_levy_20]
#port_levy_20_10[0] = port_levy_20_10[0] * 2.80402296e-01
#port_levy_20_10[1] = port_levy_20_10[1] * 6.98765019e-02 # enel
port_levy_20_10[2] = port_levy_20_10[2] * 2.98833258e-02 # enel
port_levy_20_10[3] = port_levy_20_10[3] * 3.31542951e-01
port_levy_20_10[8] = port_levy_20_10[8] * 1.87825322e-01
port_levy_20_10[15] = port_levy_20_10[15] * 2.53843436e-01    # enel
port_levy_20_10[18] = port_levy_20_10[18] * 8.03183467e-03  # enel
port_levy_20_10[28] = port_levy_20_10[28] *5.17326080e-03  # enel
port_levy_20_10[30] = port_levy_20_10[30] * 1.11636514e-01    # enel
port_levy_20_10[36] = port_levy_20_10[36] * 7.11426389e-02   # Amplifon
#port_levy_20_10[27] = port_levy_20_10[27] * 2.14716688e-01
#port_levy_20_10[28] = port_levy_20_10[28] * 7.51150226e-03   # Amplifon
#port_levy_20_10[37] = port_levy_20_10[37] * 7.67664295e-03   # Amplifon
#port_levy_20_10[25] = port_levy_20_10[25] * 7.47307435e-02   # Amplifon
port_levy_20_10['return'] = port_levy_20_10.sum(axis=1)
#port_levy_20_10['return'] = port_levy_20_10['return'].cumsum()

#cumulative ret NSGA2 n.20
lista_nsga2_20 = [2,3,4,15,30,36]
port_nsga2_20_10 = df_allstocks_10.iloc[:,lista_nsga2_20]
port_nsga2_20_10[2] = port_nsga2_20_10[2] * 1.00735167e-01    # inwit
port_nsga2_20_10[3] = port_nsga2_20_10[3] * 4.33444465e-02   # inwit
port_nsga2_20_10[4] = port_nsga2_20_10[4] * 1.61596165e-03   # inwit
port_nsga2_20_10[15] = port_nsga2_20_10[15] * 7.76171523e-01
port_nsga2_20_10[30] = port_nsga2_20_10[30] * 1.31265436e-03
port_nsga2_20_10[36] = port_nsga2_20_10[36] * 7.47144219e-02
port_nsga2_20_10['return'] = port_nsga2_20_10.sum(axis=1)
#port_nsga2_20_10['return'] = port_nsga2_20_10['return'].cumsum()
#
# cumulative ret DE n.20
lista_de_20 = [28,30,36]
port_de_20_10 = df_allstocks_10.iloc[:,lista_de_20]
# ritorni * pesi selezionati
port_de_20_10[28] = port_de_20_10[28] * 0.29754107
port_de_20_10[30] = port_de_20_10[30] * 0.33206667
port_de_20_10[36] = port_de_20_10[36] *0.37039226
port_de_20_10['return'] = port_de_20_10.sum(axis=1)
#port_de_20_10['return'] = port_de_20_10['return'].cumsum()
#


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


# #Cumulative returns portfolio DEM n.10
lista_dem_10 = [1,35,36]
port_dem_10_11 = df_allstocks_11.iloc[:,lista_dem_10]
port_dem_10_11[1] = port_dem_10_11[1] * 0.11801771 # banca mediolanum
port_dem_10_11[35] = port_dem_10_11[35] * 0.49489872 # banca mediolanum
port_dem_10_11[36] = port_dem_10_11[36] *0.38708357  # banca mediolanum
#port_dem_10_11[13] = port_dem_10_11[13] *5.16485520e-01   # banca mediolanum
#port_dem_10_11[27] = port_dem_10_11[27] *1.51362072e-01  # diasorin
#port_dem_10_11[32] = port_dem_10_11[32] * 2.47763460e-03
port_dem_10_11['return'] = port_dem_10_11.sum(axis=1)
#port_dem_10_11['return'] = port_dem_10_11['return'].cumsum()
#
#Cumulative ret GA n.10
lista_ga_10 = [1,28,35,36]
port_ga_10_11 = df_allstocks_11.iloc[:,lista_ga_10]
#port_ga_10_11[3] =port_ga_10_11[3] * 3.55085851e-01    # Amplifon
port_ga_10_11[1] =port_ga_10_11[1] * 1.07678995e-01 # banca mediolanum
port_ga_10_11[28] =port_ga_10_11[28] * 2.41452599e-03   # diasorin
port_ga_10_11[35] =port_ga_10_11[35] * 2.03527079e-01 # generali assicurazioni
port_ga_10_11[36] =port_ga_10_11[36] * 6.85550994e-01  # generali assicurazioni
#port_ga_10_11[37] =port_ga_10_11[37] * 7.37795872e-01  # generali assicurazioni
port_ga_10_11['return'] = port_ga_10_11.sum(axis=1)
#port_ga_10_11['return'] = port_ga_10_11['return'].cumsum()
#
#cumulative ret LEVY n.10
lista_levy_10 = [1,35,36]
port_levy_10_11 = df_allstocks_11.iloc[:,lista_levy_10]
port_levy_10_11[1] = port_levy_10_11[1] * 1.14037084e-01
port_levy_10_11[35] = port_levy_10_11[35] * 4.87149400e-01
port_levy_10_11[36] = port_levy_10_11[36] * 3.98030696e-01 # enel
#port_levy_10_11[20] = port_levy_10_11[20] * 3.31262847e-03 # enel
#port_levy_10_11[27] = port_levy_10_11[27] * 3.06269674e-03 # enel
#port_levy_10_11[32] = port_levy_10_11[32] * 4.82535635e-02 # enel
#port_levy_10_11[36] = port_levy_10_11[36] * 1.84686086e-03   # Amplifon
port_levy_10_11['return'] = port_levy_10_11.sum(axis=1)
#port_levy_10_11['return'] = port_levy_10_11['return'].cumsum()
#
#cumulative ret NSGA2 n.10
lista_nsga2_10 = [0,3,7,10,15,21,27,32,36,37]
port_nsga2_10_11 = df_allstocks_11.iloc[:,lista_nsga2_10]
port_nsga2_10_11[0] = port_nsga2_10_11[0] *9.92908393e-03    # inwit
port_nsga2_10_11[3] = port_nsga2_10_11[3] * 3.78354545e-02    # inwit
port_nsga2_10_11[7] = port_nsga2_10_11[7] * 1.15368624e-01    # inwit
port_nsga2_10_11[10] = port_nsga2_10_11[10] * 3.81374343e-03    # inwit
port_nsga2_10_11[15] = port_nsga2_10_11[15] * 1.12426268e-01    # inwit
port_nsga2_10_11[21] = port_nsga2_10_11[21] * 1.63370183e-02   # inwit
port_nsga2_10_11[27] = port_nsga2_10_11[27] * 1.49103567e-01   #banca mediolanum
port_nsga2_10_11[32] = port_nsga2_10_11[32] * 1.81504458e-01
port_nsga2_10_11[36] = port_nsga2_10_11[36] * 1.84719892e-01
port_nsga2_10_11[37] = port_nsga2_10_11[37] *1.88305954e-01
port_nsga2_10_11['return'] = port_nsga2_10_11.sum(axis=1)
#port_nsga2_10_11['return'] = port_nsga2_10_11['return'].cumsum()
#
# cumulative ret DE n.10
lista_de_10 = [25,32,35]
port_de_10_11 = df_allstocks_11.iloc[:,lista_de_10]
# ritorni * pesi selezionati
port_de_10_11[25] = port_de_10_11[25] *0.28381474
port_de_10_11[32] = port_de_10_11[32] *0.01488203
port_de_10_11[35] = port_de_10_11[35] * 0.70130322
port_de_10_11['return'] = port_de_10_11.sum(axis=1)
#port_de_10_11['return'] = port_de_10_11['return'].cumsum()

#
# cum ret DEM n.20
lista_dem_20 = [1,2,3,7,15,24,25,28,30,32,33,35,36,37]
port_dem_20_11 = df_allstocks_11.iloc[:,lista_dem_20]
port_dem_20_11[1] = port_dem_20_11[1] *5.74299170e-02  # diasorin
port_dem_20_11[2] = port_dem_20_11[2] *4.08110346e-03 # diasorin
port_dem_20_11[3] = port_dem_20_11[3] * 1.91985073e-01  # diasorin
port_dem_20_11[7] = port_dem_20_11[7] * 9.66261981e-03 # diasorin
port_dem_20_11[15] = port_dem_20_11[15] * 3.16858931e-02  # diasorin
port_dem_20_11[24] = port_dem_20_11[24] *8.37079373e-03 # banca mediolanum
port_dem_20_11[25] = port_dem_20_11[25] *2.10631385e-02 # banca mediolanum
port_dem_20_11[28] = port_dem_20_11[28] *3.03514109e-02
port_dem_20_11[30] = port_dem_20_11[30] *1.70665854e-02# banca mediolanum
port_dem_20_11[32] = port_dem_20_11[32] *8.27398319e-02  # banca mediolanum
port_dem_20_11[33] = port_dem_20_11[33] *3.33187989e-03  # banca mediolanum
port_dem_20_11[37] = port_dem_20_11[37] *1.61605216e-02  # banca mediolanum
port_dem_20_11[35] = port_dem_20_11[35] *6.40110903e-02 # banca mediolanum
port_dem_20_11[36] = port_dem_20_11[36] *4.59321651e-01  # banca mediolanum
port_dem_20_11['return'] = port_dem_20_11.sum(axis=1)
#port_dem_20_11['return'] = port_dem_20_11['return'].cumsum()
#
#Cumulative ret GA n.20
lista_ga_20 = [1,3,15,27,28,30,32,35,36,37]
port_ga_20_11 = df_allstocks_11.iloc[:,lista_ga_20]
port_ga_20_11[1] =port_ga_20_11[1] *2.75613406e-02   # Amplifon
port_ga_20_11[3] =port_ga_20_11[3] * 6.78033060e-02  # diasorin
port_ga_20_11[15] =port_ga_20_11[15] * 1.10991241e-01  # generali assicurazioni
port_ga_20_11[27] =port_ga_20_11[27] * 1.37088105e-01  # generali assicurazioni
port_ga_20_11[28] =port_ga_20_11[28] * 4.35484882e-02  # generali assicurazioni
port_ga_20_11[30] =port_ga_20_11[30] * 4.21035467e-02  # generali assicurazioni
port_ga_20_11[32] =port_ga_20_11[32] * 1.20441446e-01  # generali assicurazioni
port_ga_20_11[35] =port_ga_20_11[35] * 3.19014118e-02  # generali assicurazioni
port_ga_20_11[36] =port_ga_20_11[36] * 3.14161937e-01  # generali assicurazioni
port_ga_20_11[37] =port_ga_20_11[37] * 1.04378942e-01  # generali assicurazioni
#port_ga_20_11[36] =port_ga_20_11[36] * 2.75800217e-01
port_ga_20_11['return'] = port_ga_20_11.sum(axis=1)
#port_ga_20_11['return'] = port_ga_20_11['return'].cumsum()
#
#cumulative ret LEVY n.20
lista_levy_20 = [1,3,5,15,25,27,32,35,36,37]
port_levy_20_11 = df_allstocks_11.iloc[:,lista_levy_20]
#port_levy_20_11[0] = port_levy_20_11[0] * 2.80402296e-01
port_levy_20_11[1] = port_levy_20_11[1] * 4.94294045e-02 # enel
#port_levy_20_11[2] = port_levy_20_11[2] * 2.98833258e-02 # enel
port_levy_20_11[3] = port_levy_20_11[3] * 1.58812166e-01
port_levy_20_11[5] = port_levy_20_11[5] * 3.68778529e-03
port_levy_20_11[15] = port_levy_20_11[15] * 1.74208932e-03   # enel
port_levy_20_11[25] = port_levy_20_11[25] * 1.34761696e-01  # enel
port_levy_20_11[27] = port_levy_20_11[27] *7.84418608e-02  # enel
port_levy_20_11[32] = port_levy_20_11[32] * 1.24484153e-01    # enel
port_levy_20_11[35] = port_levy_20_11[35] * 7.67574616e-02   # Amplifon
port_levy_20_11[36] = port_levy_20_11[36] * 3.31686867e-01
port_levy_20_11[37] = port_levy_20_11[37] * 3.94482716e-02   # Amplifon
#port_levy_20_11[37] = port_levy_20_11[37] * 7.67664295e-03   # Amplifon
#port_levy_20_11[25] = port_levy_20_11[25] * 7.47307435e-02   # Amplifon
port_levy_20_11['return'] = port_levy_20_11.sum(axis=1)
#port_levy_20_11['return'] = port_levy_20_11['return'].cumsum()

#cumulative ret NSGA2 n.20
lista_nsga2_20 = [0,3,7,19,21,25,27,32,36,37]
port_nsga2_20_11 = df_allstocks_11.iloc[:,lista_nsga2_20]
port_nsga2_20_11[0] = port_nsga2_20_11[0] * 1.18320980e-01    # inwit
port_nsga2_20_11[3] = port_nsga2_20_11[3] * 5.04822417e-02   # inwit
port_nsga2_20_11[7] = port_nsga2_20_11[7] * 3.74573980e-02   # inwit
port_nsga2_20_11[19] = port_nsga2_20_11[19] * 2.70714359e-02
port_nsga2_20_11[21] = port_nsga2_20_11[21] * 3.53791053e-03
port_nsga2_20_11[25] = port_nsga2_20_11[25] * 3.21031131e-02
port_nsga2_20_11[27] = port_nsga2_20_11[27] *1.92466694e-01
port_nsga2_20_11[32] = port_nsga2_20_11[32] * 1.40341417e-01
port_nsga2_20_11[36] = port_nsga2_20_11[36] * 1.83564663e-01
#port_nsga2_20_11[39] = port_nsga2_20_11[39] * 1.10509953e-03
port_nsga2_20_11[37] = port_nsga2_20_11[37] * 2.13626742e-01
port_nsga2_20_11['return'] = port_nsga2_20_11.sum(axis=1)
#port_nsga2_20_11['return'] = port_nsga2_20_11['return'].cumsum()
#
# cumulative ret DE n.20
lista_de_20 = [25,32,35]
port_de_20_11 = df_allstocks_11.iloc[:,lista_de_20]
# ritorni * pesi selezionati
port_de_20_11[25] = port_de_20_11[25] * 0.43445131
port_de_20_11[32] = port_de_20_11[32] * 0.2150719
port_de_20_11[35] = port_de_20_11[35] *0.3504768
#port_de_20_11[27] = port_de_20_11[27] * 0.29701253
#port_de_20_11[25] = port_de_20_11[25] * 7.34055698e-02
#port_de_20_11[32] = port_de_20_11[32] * 1.38075502e-01
#port_de_20_11[36] = port_de_20_11[36] * 2.96296870e-01
#port_de_20_11[37] = port_de_20_11[37] * 3.56565226e-01
port_de_20_11['return'] = port_de_20_11.sum(axis=1)
#port_de_20_11['return'] = port_de_20_11['return'].cumsum()
#











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


# #Cumulative returns portfolio DEM n.10
lista_dem_10 = [13,23]
port_dem_10_12 = df_allstocks_12.iloc[:,lista_dem_10]
port_dem_10_12[13] = port_dem_10_12[13] * 0.44981983 # banca mediolanum
port_dem_10_12[23] = port_dem_10_12[23] * 0.55018017 # banca mediolanum
#port_dem_10_12[36] = port_dem_10_12[36] *0.38708357  # banca mediolanum
#port_dem_10_12[13] = port_dem_10_12[13] *5.16485520e-01   # banca mediolanum
#port_dem_10_12[27] = port_dem_10_12[27] *1.51362072e-01  # diasorin
#port_dem_10_12[32] = port_dem_10_12[32] * 2.47763460e-03
port_dem_10_12['return'] = port_dem_10_12.sum(axis=1)
#port_dem_10_12['return'] = port_dem_10_12['return'].cumsum()
#
#Cumulative ret GA n.10
lista_ga_10 = [13,15,23,24,38]
port_ga_10_12 = df_allstocks_12.iloc[:,lista_ga_10]
#port_ga_10_12[3] =port_ga_10_12[3] * 3.55085851e-01    # Amplifon
port_ga_10_12[13] =port_ga_10_12[13] * 6.52915389e-01 # banca mediolanum
port_ga_10_12[15] =port_ga_10_12[15] * 7.86746857e-02   # diasorin
port_ga_10_12[23] =port_ga_10_12[23] * 2.63282298e-01 # generali assicurazioni
port_ga_10_12[24] =port_ga_10_12[24] * 1.16587975e-03  # generali assicurazioni
port_ga_10_12[38] =port_ga_10_12[38] * 3.22299360e-03  # generali assicurazioni
port_ga_10_12['return'] = port_ga_10_12.sum(axis=1)
#port_ga_10_12['return'] = port_ga_10_12['return'].cumsum()
#
#cumulative ret LEVY n.10
lista_levy_10 = [11,13,23,24]
port_levy_10_12 = df_allstocks_12.iloc[:,lista_levy_10]
port_levy_10_12[11] = port_levy_10_12[11] * 1.76899646e-03
port_levy_10_12[13] = port_levy_10_12[13] * 4.59501874e-01
port_levy_10_12[23] = port_levy_10_12[23] * 5.36657588e-01 # enel
port_levy_10_12[24] = port_levy_10_12[24] * 1.12465851e-03 # enel
#port_levy_10_12[27] = port_levy_10_12[27] * 3.06269674e-03 # enel
#port_levy_10_12[32] = port_levy_10_12[32] * 4.82535635e-02 # enel
#port_levy_10_12[36] = port_levy_10_12[36] * 1.84686086e-03   # Amplifon
port_levy_10_12['return'] = port_levy_10_12.sum(axis=1)
#port_levy_10_12['return'] = port_levy_10_12['return'].cumsum()
#
#cumulative ret NSGA2 n.10
lista_nsga2_10 = [13,23,29,39]
port_nsga2_10_12 = df_allstocks_12.iloc[:,lista_nsga2_10]
port_nsga2_10_12[13] = port_nsga2_10_12[13] *7.64482529e-01    # inwit
port_nsga2_10_12[23] = port_nsga2_10_12[23] * 2.21137662e-01    # inwit
port_nsga2_10_12[29] = port_nsga2_10_12[29] * 2.67572939e-03    # inwit
port_nsga2_10_12[39] = port_nsga2_10_12[39] * 1.15278905e-02    # inwit
port_nsga2_10_12['return'] = port_nsga2_10_12.sum(axis=1)
#port_nsga2_10_12['return'] = port_nsga2_10_12['return'].cumsum()
#
# cumulative ret DE n.10
lista_de_10 = [7,9,11,23,24,30]
port_de_10_12 = df_allstocks_12.iloc[:,lista_de_10]
# ritorni * pesi selezionati
port_de_10_12[7] = port_de_10_12[7] *0.05205553
port_de_10_12[9] = port_de_10_12[9] *0.00181225
port_de_10_12[11] = port_de_10_12[11] * 0.00221963
port_de_10_12[23] = port_de_10_12[23] * 0.43343181
port_de_10_12[24] = port_de_10_12[24] * 0.50489749
port_de_10_12[30] = port_de_10_12[30] * 0.00558329
port_de_10_12['return'] = port_de_10_12.sum(axis=1)
#port_de_10_12['return'] = port_de_10_12['return'].cumsum()
#

#
# cum ret DEM n.20
lista_dem_20 = [11,13,15,19,21,23,38,39]
port_dem_20_12 = df_allstocks_12.iloc[:,lista_dem_20]
port_dem_20_12[11] = port_dem_20_12[11] *9.21009224e-02  # diasorin
port_dem_20_12[13] = port_dem_20_12[13] *4.66176348e-01 # diasorin
port_dem_20_12[15] = port_dem_20_12[15] * 1.15380633e-01  # diasorin
port_dem_20_12[19] = port_dem_20_12[19] *2.11416620e-02 # diasorin
port_dem_20_12[21] = port_dem_20_12[21] * 7.57709014e-03  # diasorin
port_dem_20_12[23] = port_dem_20_12[23] *1.11330498e-01 # banca mediolanum
port_dem_20_12[38] = port_dem_20_12[38] *8.88416124e-02 # banca mediolanum
port_dem_20_12[39] = port_dem_20_12[39] *9.64421768e-02
port_dem_20_12['return'] = port_dem_20_12.sum(axis=1)
#port_dem_20_12['return'] = port_dem_20_12['return'].cumsum()
#
#Cumulative ret GA n.20
lista_ga_20 = [6,7,13,15,23,36,38,39]
port_ga_20_12 = df_allstocks_12.iloc[:,lista_ga_20]
port_ga_20_12[6] =port_ga_20_12[6] *9.69674138e-02   # Amplifon
port_ga_20_12[7] =port_ga_20_12[7] * 1.56173968e-02  # diasorin
port_ga_20_12[13] =port_ga_20_12[13] * 4.25928360e-01  # generali assicurazioni
port_ga_20_12[15] =port_ga_20_12[15] * 1.49157107e-01  # generali assicurazioni
port_ga_20_12[23] =port_ga_20_12[23] * 8.77374874e-02  # generali assicurazioni
port_ga_20_12[36] =port_ga_20_12[36] * 3.29674977e-03  # generali assicurazioni
port_ga_20_12[38] =port_ga_20_12[38] * 7.83879908e-02  # generali assicurazioni
port_ga_20_12[39] =port_ga_20_12[39] * 1.41385749e-01
port_ga_20_12['return'] = port_ga_20_12.sum(axis=1)
#port_ga_20_12['return'] = port_ga_20_12['return'].cumsum()
#
#cumulative ret LEVY n.20
lista_levy_20 = [12,13,15,23,38,39]
port_levy_20_12 = df_allstocks_12.iloc[:,lista_levy_20]
port_levy_20_12[12] = port_levy_20_12[12] * 7.70151736e-03 # enel
port_levy_20_12[13] = port_levy_20_12[13] * 4.81287007e-01
port_levy_20_12[15] = port_levy_20_12[15] * 1.89722758e-01
port_levy_20_12[23] = port_levy_20_12[23] * 1.70636528e-01   # enel
port_levy_20_12[38] = port_levy_20_12[38] * 1.90088144e-02  # enel
port_levy_20_12[39] = port_levy_20_12[39] * 1.29037276e-01  # enel
port_levy_20_12['return'] = port_levy_20_12.sum(axis=1)
#port_levy_20_12['return'] = port_levy_20_12['return'].cumsum()

#cumulative ret NSGA2 n.20
lista_nsga2_20 = [2,12,13,16,26,39]
port_nsga2_20_12 = df_allstocks_12.iloc[:,lista_nsga2_20]
port_nsga2_20_12[2] = port_nsga2_20_12[2] * 1.18056763e-03    # inwit
port_nsga2_20_12[12] = port_nsga2_20_12[12] * 3.24869039e-02   # inwit
port_nsga2_20_12[13] = port_nsga2_20_12[13] * 6.74573771e-01   # inwit
port_nsga2_20_12[16] = port_nsga2_20_12[16] * 4.79985546e-02
port_nsga2_20_12[26] = port_nsga2_20_12[26] * 5.09511994e-03
port_nsga2_20_12[39] = port_nsga2_20_12[39] * 2.37400589e-01
port_nsga2_20_12['return'] = port_nsga2_20_12.sum(axis=1)
#port_nsga2_20_12['return'] = port_nsga2_20_12['return'].cumsum()
#
# cumulative ret DE n.20
lista_de_20 = [6,23,24,36,39]
port_de_20_12 = df_allstocks_12.iloc[:,lista_de_20]
# ritorni * pesi selezionati
port_de_20_12[6] = port_de_20_12[6] * 0.29367199
port_de_20_12[23] = port_de_20_12[23] * 0.18797093
port_de_20_12[24] = port_de_20_12[24] *0.26465413
port_de_20_12[36] = port_de_20_12[36] * 0.06300167
port_de_20_12[39] = port_de_20_12[39] * 0.19070128
#port_de_20_12[32] = port_de_20_12[32] * 1.38075502e-01
#port_de_20_12[36] = port_de_20_12[36] * 2.96296870e-01
#port_de_20_12[37] = port_de_20_12[37] * 3.56565226e-01
port_de_20_12['return'] = port_de_20_12.sum(axis=1)
#port_de_20_12['return'] = port_de_20_12['return'].cumsum()
#









#cumulative ret LEVY n.20
lista_levy_20 = [8,13,21,23,24,25,27,28,38,39]
port_levy_20_03 = df_allstocks_03.iloc[:,lista_levy_20]
port_levy_20_03[8] = port_levy_20_03[8] * 3.02493747e-03
port_levy_20_03[13] = port_levy_20_03[13] * 1.61024674e-01 # enel
port_levy_20_03[21] = port_levy_20_03[21] * 2.55403033e-01 # enel
port_levy_20_03[23] = port_levy_20_03[23] * 1.30292912e-03
port_levy_20_03[24] = port_levy_20_03[24] * 5.62872494e-02
port_levy_20_03[25] = port_levy_20_03[25] * 1.01196434e-01    # enel
port_levy_20_03[27] = port_levy_20_03[27] * 1.19156585e-02    # enel
port_levy_20_03[28] = port_levy_20_03[28] * 1.60865333e-01    # enel
port_levy_20_03[38] = port_levy_20_03[38] * 2.62502498e-03    # enel
port_levy_20_03[39] = port_levy_20_03[39] * 2.45420415e-01   # Amplifon
port_levy_20_03['return'] = port_levy_20_03.sum(axis=1)
#port_levy_20_03['return'] = port_levy_20_03['return'].cumsum()

#cumulative ret NSGA2 n.20
lista_nsga2_20 = [3,13,15,21,24,25,28,37,39]
port_nsga2_20_03 = df_allstocks_03.iloc[:,lista_nsga2_20]
port_nsga2_20_03[3] = port_nsga2_20_03[3] * 9.08406690e-02    # inwit
port_nsga2_20_03[13] = port_nsga2_20_03[13] * 6.41475070e-02    # inwit
port_nsga2_20_03[15] = port_nsga2_20_03[15] * 1.16237836e-03    # inwit
port_nsga2_20_03[21] = port_nsga2_20_03[21] * 3.44514658e-01
port_nsga2_20_03[24] = port_nsga2_20_03[24] * 3.44750917e-03
port_nsga2_20_03[25] = port_nsga2_20_03[25] * 1.82217024e-03
port_nsga2_20_03[28] = port_nsga2_20_03[28] * 2.58731008e-01
port_nsga2_20_03[37] = port_nsga2_20_03[37] * 1.36469993e-03
port_nsga2_20_03[39] = port_nsga2_20_03[39] * 2.31272697e-01
#port_nsga2_20_03[27] = port_nsga2_20_03[27] * 4.44424131e-01
port_nsga2_20_03['return'] = port_nsga2_20_03.sum(axis=1)
#port_nsga2_20_03['return'] = port_nsga2_20_03['return'].cumsum()
#
# cumulative ret DE n.20
lista_de_20 = [1,13,19,21,26]
port_de_20_03 = df_allstocks_03.iloc[:,lista_de_20]
# ritorni * pesi selezionati
port_de_20_03[1] = port_de_20_03[1] * 0.10897238
port_de_20_03[13] = port_de_20_03[13] * 0.26308419
port_de_20_03[19] = port_de_20_03[19] * 0.21691407
port_de_20_03[21] = port_de_20_03[21] * 0.37760952
port_de_20_03[26] = port_de_20_03[26] * 0.03341985
#port_de_20_03[27] = port_de_20_03[27] * 0.78052662
#port_de[21] = port_de[21] * 0.03335649
port_de_20_03['return'] = port_de_20_03.sum(axis=1)














































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

de_cumret_10 = pd.concat([port_de_10_02['return'],port_de_10_03['return'],
                          port_de_10_04['return'],port_de_10_05['return'],
                          port_de_10_06['return'],port_de_10_07['return'],
                          port_de_10_08['return'],port_de_10_09['return'],
                          port_de_10_10['return'],port_de_10_11['return'],port_de_10_12['return']],axis=0).cumsum(axis=0)

dem_cumret_10 = pd.concat([port_dem_10_02['return'],port_dem_10_03['return'],
                           port_dem_10_04['return'],port_dem_10_05['return'],port_dem_10_06['return'],
                           port_dem_10_07['return'],port_dem_10_08['return'],port_dem_10_09['return'],
                           port_dem_10_10['return'],port_dem_10_11['return'],port_dem_10_12['return']],axis=0).cumsum(axis=0)

ga_cumret_10 = pd.concat([port_ga_10_02['return'],port_ga_10_03['return'],port_ga_10_04['return'],
port_ga_10_05['return'],port_ga_10_06['return'],port_ga_10_07['return'],port_ga_10_08['return'],port_ga_10_09['return'],
port_ga_10_10['return'],port_ga_10_11['return'],port_ga_10_12['return']],axis=0).cumsum(axis=0)

levy_cumret_10 = pd.concat([port_levy_10_02['return'],
                            port_levy_10_03['return'],port_levy_10_04['return'],port_levy_10_05['return'],port_levy_10_06['return'],
port_levy_10_07['return'],port_levy_10_08['return'],port_levy_10_09['return'],port_levy_10_10['return'],port_levy_10_11['return'],
port_levy_10_12['return']],axis=0).cumsum(axis=0)

nsga2_cumret_10 = pd.concat([port_nsga2_10_02['return'], port_nsga2_10_03['return'],port_nsga2_10_04['return'],port_nsga2_10_05['return'],port_nsga2_10_06['return'],
port_nsga2_10_07['return'],port_nsga2_10_08['return'],port_nsga2_10_09['return'],port_nsga2_10_10['return'],
port_nsga2_10_11['return'],port_nsga2_10_12['return']],axis=0).cumsum(axis=0)
#
#
fig5, ax5 = plt.subplots(figsize=(10,6))
formatter = mdates.DateFormatter('%Y-%m')
ax5.xaxis.set_minor_formatter(formatter)
ax5.xaxis.set_major_formatter(formatter)
ax5.tick_params(axis='x', rotation=45)
sns.lineplot(x=dates.values,y=ftsemib_ret_all, label = 'FTSE-MIB', markevery=21,marker='o', markersize=12, linestyle='dashdot',linewidth=2)
sns.lineplot(x=dates.values,y=de_cumret_10, label = 'MOEA/D-DE')#, markevery=25, markers=maks1[1])
sns.lineplot(x=dates.values,y=dem_cumret_10, label= "MOEA/D-DEM")#, markevery=25, markers=maks1[2])
sns.lineplot(x=dates.values,y=ga_cumret_10, label = "MOEA/D-GA")#,markevery=25, markers=maks1[3])
sns.lineplot(x=dates.values,y=levy_cumret_10, label="MOEA/D-LEVY")#,markevery=25, markers=maks1[4])
sns.lineplot(x=dates.values,y=nsga2_cumret_10, label = "NSGAII")# ,markevery=25, markers=maks1[0])
plt.ylabel('Cumulative return')
plt.title('FTSE MIB vs high risk portfolios')
plt.savefig('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/images/highrisk.png')



de_cumret_20 = pd.concat([port_de_20_02['return'],port_de_20_03['return'],port_de_20_04['return'],port_de_20_05['return'],port_de_20_06['return'],
port_de_20_07['return'],port_de_20_08['return'],port_de_20_09['return'],port_de_20_10['return'],
port_de_20_11['return'],port_de_20_12['return']],axis=0).cumsum(axis=0)

dem_cumret_20 = pd.concat([port_dem_20_02['return'],port_dem_20_03['return'],port_dem_20_04['return'],
                           port_dem_20_05['return'],port_dem_20_06['return'],port_dem_20_07['return'],
                           port_dem_20_08['return'],port_dem_20_09['return'],port_dem_20_10['return'],
                           port_dem_20_11['return'],port_dem_20_12['return']],axis=0).cumsum(axis=0)

ga_cumret_20 = pd.concat([port_ga_20_02['return'],port_ga_20_03['return'],port_ga_20_04['return'],port_ga_20_05['return'],
                          port_ga_20_06['return'],port_ga_20_07['return'],port_ga_20_08['return'],
                          port_ga_20_09['return'],port_ga_20_10['return'],port_ga_20_11['return'],port_ga_20_12['return']],axis=0).cumsum(axis=0)

levy_cumret_20 = pd.concat([port_levy_20_02['return'],port_levy_20_03['return'],
                            port_levy_20_04['return'],port_levy_20_05['return'],port_levy_20_06['return'],
                            port_levy_20_07['return'],port_levy_20_08['return'],port_levy_20_09['return'],
                            port_levy_20_10['return'],port_levy_20_11['return'],port_levy_20_12['return']],axis=0).cumsum(axis=0)

nsga2_cumret_20 = pd.concat([port_nsga2_20_02['return'],port_nsga2_20_03['return'],port_nsga2_20_04['return'],port_nsga2_20_05['return'],
                             port_nsga2_20_06['return'],port_nsga2_20_07['return'],port_nsga2_20_08['return'],port_nsga2_20_09['return'],
                             port_nsga2_20_10['return'],port_nsga2_20_11['return'],port_nsga2_20_12['return']],axis=0).cumsum(axis=0)


fig6, ax6 = plt.subplots(figsize=(10,6))
formatter = mdates.DateFormatter('%Y-%m')
ax6.xaxis.set_minor_formatter(formatter)
ax6.xaxis.set_major_formatter(formatter)
ax6.tick_params(axis='x', rotation=45)
sns.lineplot(x=dates.values,y=ftsemib_ret_all, label = 'FTSE-MIB', markevery=21,marker='o', markersize=12, linestyle='dashdot',linewidth=2)
sns.lineplot(x=dates.values,y=de_cumret_20, label = 'MOEA/D-DE')#, markevery=25, markers=maks1[1])
sns.lineplot(x=dates.values,y=dem_cumret_20, label= "MOEA/D-DEM")#, markevery=25, markers=maks1[2])
sns.lineplot(x=dates.values,y=ga_cumret_20, label = "MOEA/D-GA")#,markevery=25, markers=maks1[3])
sns.lineplot(x=dates.values,y=levy_cumret_20, label="MOEA/D-LEVY")#,markevery=25, markers=maks1[4])
sns.lineplot(x=dates.values,y=nsga2_cumret_20, label = "NSGAII")# ,markevery=25, markers=maks1[0])
plt.ylabel('Cumulative return')
plt.title('FTSE MIB vs mid risk portfolios')
plt.savefig('/home/davide/PycharmProjects/pythonProject2/genetic_algo_progetto/po_with_moead-levy_/images/midrisk.png')









