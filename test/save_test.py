import os

import pandas as pd

df = pd.DataFrame()

col_num = 1
row_num = 0

while True:
    try:
        value = int(input("Veuillez entrer un nombre entier : "))
        if value == 0:
            break
        if value < 5:
            df.loc[row_num, col_num] = value
            row_num += 1
        else:
            col_num += 1
            row_num = 0
            df.loc[row_num, col_num] = value
            row_num += 1
    except ValueError:
        print("Ce n'est pas un nombre entier. Veuillez réessayer.")
    except KeyboardInterrupt:
        break
    print(df)


if 'chess.csv' in os.listdir():
    df_existing = pd.read_csv('chess.csv', sep=';', index_col=0)
    last_column_name = df_existing.columns[-1]
    print('found' + last_column_name + '!')
else:
    df_existing = pd.DataFrame()
    last_column_name = 'game 0'

last_game_number = int(last_column_name.split(' ')[-1])
df.columns = ['game ' + str(i) for i in range(last_game_number + 1, last_game_number + 1 + len(df.columns))]
df_combined = pd.concat([df_existing, df], axis=1)
df_combined.to_csv('chess.csv', sep=';')
