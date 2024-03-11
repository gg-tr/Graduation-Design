import pandas as pd
from sqlalchemy import create_engine
con =create_engine('mysql+pymysql://root:chen@localhost:3306/dbm')
df =pd.read_sql('select * from movie',con=con)

def typeList(type):
    type = df[type].values
    typeList = []
    if type is not  None:
        # type = list(map(lambda x:x.split(','),type))
        for i in range(len(type)):
            if type[i] is not None:
                typeList.append(type[i])
    return typeList
