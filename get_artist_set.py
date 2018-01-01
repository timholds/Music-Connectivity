import pandas as pd

def import_data():

    ''' Get the of all song data from the csv into a DataFrame, turn it into data
     just about the set of artists, and then put this into a csv file'''

    data = pd.read_csv('artists-full.csv', encoding = 'latin1')

    columns = ['Artist', 'Feature1', 'Feature2', 'Feature3']
    df = pd.DataFrame(data, columns=columns)

    # From the data, get a list of all artists that show up in any songs
    artists = set(df.loc['Artists'] | df.loc['Features1'] |
                  df.loc['Features2'] | df.loc['Features3'])

    # Make one long column with all of the artists and write it to csv
    pd.Series(artists, columns='Artists').to_csv('Artists-set.csv')

import_data()



