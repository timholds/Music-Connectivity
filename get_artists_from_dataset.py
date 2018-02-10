import pandas as pd
import numpy as np

def clean(string):
    clean_string = string.replace(u'\xa0', u' ').encode('utf-8'),
    return clean_string


def import_data():

    ''' Get the of all song data from the csv into a DataFrame, turn it into data
     just about the set of artists, and then put this into a csv file'''
    data = pd.read_csv('data/genius-parsed.csv', encoding = 'utf-8')
    #data = pd.read_csv('/Data/genius-old.csv')#, encoding = 'latin1')
    columns = ['Artist', 'Feature1', 'Feature2', 'Feature3', 'Feature4']
    df = pd.DataFrame(data, columns=columns)

    # Get an array of strings for each column. Clean out repeats
    artists_set1 = df.loc[:, 'Artist'].unique().tolist()
    artists_set2 = df.loc[:, 'Feature1'].unique().tolist()
    artists_set3 = df.loc[:, 'Feature2'].unique().tolist()
    artists_set4 = df.loc[:, 'Feature3'].unique().tolist()
    artists_set5 = df.loc[:, 'Feature4'].unique().tolist()

    # Combine the artists from different columns
    artists_list = [artists_set1, artists_set2, artists_set3, artists_set4, artists_set5]
    flat_artists_list = [item for sublist in artists_list for item in sublist]
    # Get rid of duplicates by creating a set
    artists_set = set(flat_artists_list)
    # Turn the set back into a list
    artists = list(artists_set)
    print(type(artists))
    artists_clean = [str(artist).replace(u'\xa0', u' ').encode('utf-8') for artist in artists]

    #artists_clean = map(clean, str(artists))


    print('length of artists is {}'.format(len(artists)))
    print(list(artists_clean))

    # Write the list to csv
    with open ('data/artists.csv', 'w', encoding='utf-8') as f: #artist_series.to_csv('Artists-set.csv', index=False)
        for artist in artists:
            f.write(str(artist) + '\n')

import_data()



