import pandas as pd

# Exemple de DataFrame existant
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Nouvelle colonne à ajouter sous forme de DataFrame
new_column = pd.DataFrame({'C': [7, 8, 9, 10]})

# Concaténation de la nouvelle colonne
df = pd.concat([df, new_column], axis=1)

print(df)
