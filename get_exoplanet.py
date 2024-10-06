import pandas as pd

def get_exoplanet_data():
    # Zaktualizowany URL do pobierania danych z odpowiedniej tabeli "ps" (planetary system)
    url = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,ra,dec,pl_bmasse+from+ps&format=csv'
    exoplanets = pd.read_csv(url)
    return exoplanets

exoplanet_data = get_exoplanet_data()
print("\nDane o egzoplanetach:")
print(exoplanet_data.head())
