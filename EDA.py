import ImportAndMerge

# print(ImportAndMerge.dataframe)

df = ImportAndMerge.dataframe

for col in df.columns:
    print(col)

# calculating mean ride length
mean_ride_length = df['ride_length'].mean()
print(mean_ride_length)


# 0.015103037745700041

# converting the above result in hours:mins:seconds format
def convert(mean):
    hours = int(mean)
    mins = (mean * 60) % 60
    secs = (mean * 3600) % 60
    print(str(hours) + ":" + str(int(mins)) + ":" + str(int(secs)))


convert(mean_ride_length)

# calculating mode of day_of_week column to estimate which day of the week is the busiest
mode_day = df['day_of_week'].mode()
print(mode_day)  # 7 saturday is the busiest

# partitioning data on the basis of member_casual column
df_member = df[df.member_casual == 'member']
print(df_member)


