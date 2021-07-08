import datacompy, pandas as pd
df1 = pd.read_csv('bulk.csv')
df2 = pd.read_csv('existing02.csv')

compare = datacompy.Compare(
    df1,
    df2,

    join_columns='first_name', 'cow',
    abs_tol=0.0001,
    rel_tol=0,
)
print(compare.report())