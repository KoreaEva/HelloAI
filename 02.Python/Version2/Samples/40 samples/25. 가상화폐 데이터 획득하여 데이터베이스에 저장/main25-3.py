import pandas as pd
import sqlite3

db_path = r"25. 가상화폐 데이터 획득하여 데이터베이스에 저장\coin.db"
con = sqlite3.connect(db_path, isolation_level=None)

readed_df = pd.read_sql("SELECT * FROM 'BTC'", con, index_col = 'index')

print(readed_df)