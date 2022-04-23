# waffers101/Case-Study-How-Does-a-Bike-Share-Navigate-Speedy-Success
import pandas as pd

df1=pd.read_csv(".XLs files/csvs/202103-divvy-tripdata.csv")
df2=pd.read_csv(".XLs files/csvs/202104-divvy-tripdata.csv")
df3=pd.read_csv(".XLs files/csvs/202105-divvy-tripdata.csv")
df4=pd.read_csv(".XLs files/csvs/202106-divvy-tripdata.csv")
df5=pd.read_csv(".XLs files/csvs/202107-divvy-tripdata.csv")
df6=pd.read_csv(".XLs files/csvs/202108-divvy-tripdata.csv")
df7=pd.read_csv(".XLs files/csvs/202109-divvy-tripdata.csv")
df8=pd.read_csv(".XLs files/csvs/202110-divvy-tripdata.csv")
df9=pd.read_csv(".XLs files/csvs/202111-divvy-tripdata.csv")
df10=pd.read_csv(".XLs files/csvs/202112-divvy-tripdata.csv")
df11=pd.read_csv(".XLs files/csvs/202201-divvy-tripdata.csv")
df12=pd.read_csv(".XLs files/csvs/202202-divvy-tripdata.csv")



frames = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12]

dataframe = pd.concat(frames)
print(dataframe.shape)

print(dataframe.head())