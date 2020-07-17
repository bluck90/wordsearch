# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:30:32 2020

@author: btgl1e14
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_excel('Chakras\Adhyaya_One_Chakras.xls', header = 1)
df2 = pd.read_excel('Chakras\Adhyaya_Two_Chakras.xls', header = 1)
df3 = pd.read_excel('Chakras\Adhyaya_Three_Chakras.xls', header = 1)
df4 = pd.read_excel('Chakras\Adhyaya_Four_Chakras.xls', header = 1)
df5 = pd.read_excel('Chakras\Adhyaya_Five_Chakras.xls', header = 1)
df6 = pd.read_excel('Chakras\Adhyaya_Six_Chakras.xls', header = 1)
df7 = pd.read_excel('Chakras\Adhyaya_Seven_Chakras.xls', header = 1)
df8 = pd.read_excel('Chakras\Adhyaya_Eight_Chakras.xls', header = 1)



def write_chakras(df, error_value):
    df = df.fillna(error_value)
    chakras = {}
    for k in range(2, len(df.columns)):
        if str(df.columns[k]).find('Unnamed') > -1:
            continue
        chakra = np.empty((27,27))
        for j in range(0,27):
            error_count = 0
            for i in range(0,27):
                if not str(df.values[i + 27 * j][k]).isdigit():
                    #print('Non-numeric value found in row: ' + str(i + 27*j) + ', col: ' + str(k))
                    if not any(char.isdigit() for char in str(df.values[i + 27 * j][k])):
                        error_count += 1
                        chakra[j][i] = error_value 
                    else:
                        if df.values[i + 27 * j][k] == 'I':
                            chakra[j][i] = error_value    
                            error_count += 1
                        else:
                            if str(df.values[i + 27 * j][k]).find('-') > -1:
                                if len(str(df.values[i + 27 * j][k])) > 1:
                                    chakra[j][i] = int(str(df.values[i + 27 * j][k])[str(df.values[i + 27 * j][k]).find('-') + 1:])
                                else:
                                    chakra[j][i] = error_value 
                                    error_count += 1
                            else:
                                integer = ''.join([c for c in str(df.values[i + 27 * j][k]) if c in '1234567890-.'])
                                chakra[j][i] = integer
                else:
                    chakra[j][i] = int(df.values[i + 27 * j][k])
            if error_count > 0:
                print(str(df.columns[k]) + ' error count: ' + str(error_count))
        chakras[df.columns[k]] = chakra
    return chakras

chakras_1 = write_chakras(df1, 77)
chakras_2 = write_chakras(df2, 77)
chakras_3 = write_chakras(df3, 77)
chakras_4 = write_chakras(df4, 77)
chakras_5 = write_chakras(df5, 77)
chakras_6 = write_chakras(df6, 77)
chakras_7 = write_chakras(df7, 77)
chakras_8 = write_chakras(df8, 77)


######################


