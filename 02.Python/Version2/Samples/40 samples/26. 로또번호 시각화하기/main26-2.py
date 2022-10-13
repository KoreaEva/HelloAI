import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

file_path = r'26. 로또번호 시각화하기\lotto.xlsx'
df_from_excel = pd.read_excel(file_path,engine='openpyxl')

df_from_excel = df_from_excel.drop(index=[0,1])

df_from_excel.columns = [
                        '년도', '회차','추첨일','1등당첨자수',
                        '1등당첨금액','2등당첨자수','2등당첨금액','3등당첨자수',
                        '3등당첨금액','4등당첨자수','4등당첨금액','5등당첨자수',
                        '5등당첨금액','당첨번호1','당첨번호2','당첨번호3',
                        '당첨번호4','당첨번호5','당첨번호6','보너스번호'
                        ]

df_from_excel['1등당첨금액']=df_from_excel['1등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)
df_from_excel['2등당첨금액']=df_from_excel['2등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)
df_from_excel['3등당첨금액']=df_from_excel['3등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)
df_from_excel['4등당첨금액']=df_from_excel['4등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)
df_from_excel['5등당첨금액']=df_from_excel['5등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)

df_from_excel["1등당첨금액"] = pd.to_numeric(df_from_excel["1등당첨금액"])
df_from_excel["2등당첨금액"] = pd.to_numeric(df_from_excel["2등당첨금액"])
df_from_excel["3등당첨금액"] = pd.to_numeric(df_from_excel["3등당첨금액"])
df_from_excel["4등당첨금액"] = pd.to_numeric(df_from_excel["4등당첨금액"])
df_from_excel["5등당첨금액"] = pd.to_numeric(df_from_excel["5등당첨금액"])

print( df_from_excel[['1등당첨금액','2등당첨금액','3등당첨금액','4등당첨금액','5등당첨금액']] )

font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

x = df_from_excel['회차'].iloc[:100].values
price = df_from_excel['1등당첨금액'].iloc[:100].values / 100000000

plt.figure(figsize=(10, 5))
plt.xlabel('회차') 
plt.ylabel('당첨금액(단위:억원)') 

plt.bar(x, price, width=0.4)

plt.show()