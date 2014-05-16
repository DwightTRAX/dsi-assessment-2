import nose.tools as n
import numpy as np
import pandas as pd
import sqlite3 as sql
from code import assessment as a

def run_sql_query(command, db='data/housing.sql'):
    if not command:
        return []
    con = sql.connect(db)
    c = con.cursor()
    data = c.execute(command)
    return [d for d in data]
    con.close()

def test_max_lists():
    result = a.max_lists([5, 7, 2, 3, 6], [3, 9, 1, 2, 8])
    n.assert_equal(result, [5, 9, 2, 3, 8])

def test_get_diagonal():
    result = a.get_diagonal([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    n.assert_equal(result, [1, 6, 11])

def test_merge_dictionaries():
    result = a.merge_dictionaries({"a": 1, "b": 5, "c": 1, "e": 8}, {"b": 2, "c": 5, "d": 10, "f": 6})
    n.assert_equal(result, {"a": 1, "b": 7, "c": 6, "d": 10, "e": 8, "f": 6})

def test_make_char_dict():
    result = a.make_char_dict('data/people.txt')
    n.assert_equal(result['j'], [2, 19, 20])
    n.assert_equal(result['g'], [3])

def test_pandas_add_increase_column():
    return
    df = pd.read_csv('data/rent.csv')
    a.pandas_add_increase_column(df)
    cols = ['Neighborhood', 'City', 'State', '2011-01', '2014-01', 'Increase']
    n.assert_equal(df.columns.tolist(), cols)
    answer = ['Green Run', 'Virginia Beach', 'VA', 1150.0, 1150.0, 0.0]
    n.assert_equal(df.loc[123].tolist(), answer)

def test_pandas_only_given_state():
    return
    df = a.pandas_only_given_state(pd.read_csv('data/rent.csv'), 'CA')
    cols = ['Neighborhood', 'City', '2011-01', '2014-01']
    n.assert_equal(df.columns.tolist(), cols)
    n.assert_equal(len(df), 762)
    n.assert_equal(len(df[df['City'] == 'San Francisco']), 62)
    paloalto = df[df['City'] == 'Palo Alto']['Neighborhood'].tolist()
    answer = ['Midtown', 'University South', 'Downtown North', 'Ventura',
              'Evergreen Park', 'Green Acres']

def test_pandas_max_rent():
    df = a.pandas_max_rent(pd.read_csv('data/rent.csv')).reset_index()
    n.assert_equal(len(df), 177)
    cols = ['City', 'State', '2011-01', '2014-01']
    n.assert_equal(df.columns.tolist(), cols)
    sf_row = df[df['City'] == 'San Francisco']
    sf = (sf_row['2011-01'].tolist()[0], sf_row['2014-01'].tolist()[0])
    maine = df[df['State'] == 'ME']
    portland_row = maine[maine['City'] == 'Portland']
    portland = (portland_row['2011-01'].tolist()[0], portland_row['2014-01'].tolist()[0])
    n.assert_equal(sf, (3575., 4900.))
    n.assert_equal(portland, (1600., 1650.))

def test_sql_count_neighborhoods():
    result = run_sql_query(a.sql_count_neighborhoods())
    n.assert_equal(len(result), 177)
    sf, portland = None, None
    for line in result:
        if line[0] == 'San Francisco':
            sf = int(line[2])
        elif line[0] == 'Portland' and line[1] == 'ME':
            portland = int(line[2])
    n.assert_equal(sf, 62)
    n.assert_equal(portland, 13)

def test_sql_highest_rent_increase():
    result = run_sql_query(a.sql_highest_rent_increase())
    n.assert_equal(len(result), 5)
    answer = {'Duboce Triangle', 'North Beach', 'Lake', 'Alamo Square', 'Glen Park'}
    n.assert_equal(set(x[0] for x in result), answer)

def test_sql_rent_and_buy():
    result = run_sql_query(a.sql_rent_and_buy())
    n.assert_equal(len(result), 25)
    mission = None
    marina = None
    for line in result:
        if line[0] == "Mission":
            mission = line[1:]
        elif line[0] == "Marina":
            marina = line[1:]
    n.assert_equal(mission, (3500, 654300))
    n.assert_equal(marina, (3950, 747300))
