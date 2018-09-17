## Fill each each function stub according to the docstring.
## To run the unit tests: Make sure you are in the root dir:assessment-2
## Then run the tests with this command: "make test"

import numpy as np
import pandas as pd
from collections import Counter


def max_lists(list1, list2):
    '''
    INPUT: list, list
    OUTPUT: list

    list1 and list2 have the same length. Return a list which contains the
    maximum element of each list for every index.
    '''
    result = []
    for i in range(len(list1)):
        result.append(max(list1[i],list2[i]))
    return result



def get_diagonal(mat):
    '''
    INPUT: 2 dimensional list
    OUTPUT: list

    Given a matrix encoded as a 2 dimensional python list, return a list
    containing all the values in the diagonal starting at the index 0, 0.

    E.g.
    mat = [[1, 2], [3, 4], [5, 6]]
    | 1  2 |
    | 3  4 |
    | 5  6 |
    get_diagonal(mat) => [1, 4]

    You may assume that the matrix is nonempty.
    '''
    l = min(len(mat),len(mat[0]))
    result = []
    for i in range(l):
        result.append(mat[i][i])
    return result


def merge_dictionaries(d1, d2):
    '''
    INPUT: dictionary, dictionary
    OUTPUT: dictionary

    Return a new dictionary which contains all the keys from d1 and d2 with
    their associated values. If a key is in both dictionaries, the value should
    be the sum of the two values.
    '''

    return dict(Counter(d1) + Counter(d2))


def make_char_dict(filename):
    '''
    INPUT: string
    OUTPUT: dictionary (string => list)

    Given a file containing rows of text, create a dictionary whose keys
    are single characters. The value associated with each key is a list of all
    the line numbers which start with that letter. The first line should have
    line number 1.  Characters which never are the first letter of a line do
    not need to be included in your dictionary.
    '''
    d = {}
    with open(filename) as f:
        l = 0
        for line in f:
            l += 1
            for char in line:
                if char in d:
                    if d[char][-1] != l:
                        d[char].append(l)
                else:
                    d[char] = []
                    d[char].append(l)
    return d



### Pandas
# For each of these, you will be dealing with a DataFrame which contains median
# rental prices in the US by neighborhood. The DataFrame will have these
# columns:
# Neighborhood, City, State, med_2011, med_2014

def pandas_add_increase_column(df):
    '''
    INPUT: DataFrame
    OUTPUT: None

    Add a column to the DataFrame called 'Increase' which contains the
    amount that the median rent increased by from 2011 to 2014.
    '''
    df['Increase'] = df['med_2014'].fillna(0) - df['med_2011'].fillna(0)
    #return df


def pandas_only_given_state(df, state):
    '''
    INPUT: DataFrame, string
    OUTPUT: DataFrame

    Return a new pandas DataFrame which contains the entries for the given
    state. Only include these columns:
        Neighborhood, City, med_2011, med_2014
    '''
    df = df[df['State'] == state][['Neighborhood', 'City', 'med_2011', 'med_2014']]
    return df


def pandas_max_rent(df):
    '''
    INPUT: DataFrame
    OUTPUT: DataFrame

    Return a new pandas DataFrame which contains every city and the highest
    median rent from that city for 2011 and 2014.

    Note that city names are not unique and you need to use the state as well
    so that Portland, ME and Portland, OR are recognized as different.

    Your DataFrame should contain these columns:
        City, State, med_2011, med_2014
    '''
    df1 = df[['City', 'State', 'med_2011']].fillna(0).groupby(['City','State'], as_index=False)['med_2011'].max()
    df2 = df[['City', 'State', 'med_2014']].fillna(0).groupby(['City','State'], as_index=False)['med_2014'].max()

    #df = df[['City', 'State', 'med_2011', 'med_2014']].groupby('City')['med_2011', 'med_2014'].max()
    df = pd.merge(df1, df2, on =['City', 'State'])
    return df

### SQL
# For each of these, your python function should return a string that is the
# SQL statement which answers the question.
# For example:
#    return '''SELECT * FROM rent;'''
# You may want to run "sqlite3 data/housing.sqlite" in the command line to test
# out your queries if the test is failing.
#
# There are two tables in the database with these columns:
# (this is the same data that you dealt with in the pandas questions)
#     rent: Neighborhood, City, State, med_2011, med_2014
#     buy:  Neighborhood, City, State, med_2011, med_2014
# The values in the date columns are integers corresponding to the price on
# that date.

def sql_count_neighborhoods():
    '''
    INPUT: None
    OUTPUT: string

    Return a SQL query that gives the number of neighborhoods in each city
    according to the rent table. Keep in mind that city names are not always
    unique unless you include the state as well, so your result should have
    these columns (though you do not need to name them): city, state, cnt
    '''
    q = '''
    SELECT City,State,count(Neighborhood) AS cnt
    FROM rent
    GROUP BY City,State
    ;
    '''
    return q


def sql_highest_rent_increase():
    '''
    INPUT: None
    OUTPUT: string

    Return a SQL query that gives the 5 San Francisco neighborhoods with the
    highest rent increase.
    '''

    q = '''
    SELECT Neighborhood, (med_2014-med_2011) AS increase
    FROM rent
    WHERE City = 'San Francisco'
    ORDER BY increase DESC
    LIMIT 5
    ;

    '''
    return q


def sql_rent_and_buy():
    '''
    INPUT: None
    OUTPUT: string

    Return a SQL query that gives the rent price and buying price for 2014 for
    all the neighborhoods in San Francisco.
    Your result should have these columns (though you do not need to name
    them): neighborhood, rent, buy
    '''
    q = '''
    SELECT r.Neighborhood, r.med_2014, b.med_2014
    FROM rent AS r
    INNER JOIN
    buy AS b
    ON (r.Neighborhood = b.Neighborhood AND r.City = b.City AND r.State = b.State)
    WHERE r.city = 'San Francisco'
    ;

    '''
    return q
