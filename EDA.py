# from datetime import datetime
import matplotlib.pyplot as plt
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
    return str(hours) + ":" + str(int(mins)) + ":" + str(int(secs))


def convert_secs(mean):
    hours = int(mean)
    # print(hours)
    mins = (mean * 60) % 60
    # print(mins)
    secs = (mean * 3600) % 60
    # print(secs)
    sec= int(secs) + (int(mins) * 60) + (hours * 3600)
    return sec


mean_ride_length = convert(mean_ride_length)

# calculating mode of day_of_week column to estimate which day of the week is the busiest
mode_day = df['day_of_week'].mode()
print(mode_day)  # 7 saturday is the busiest

# partitioning data on the basis of member_casual column
df_member = df[df.member_casual == 'member']
print(df_member)

df_casual = df[df.member_casual == 'casual']
print(df_casual)

# mean ride length of member bikers
mean_member_ride_length = df_member['ride_length'].mean()
print(mean_member_ride_length)
mean_member_ride_length = convert_secs(mean_member_ride_length)

# mean ride length of casual bikers
mean_casual_ride_length = df_casual['ride_length'].mean()
mean_casual_ride_length = convert_secs(mean_casual_ride_length)

# date_time_obj = datetime.strptime(mean_member_ride_length, '%H:%M:%S')


# plotting a comparison bar graph to visualize the difference between the two mean ride lengths calculated abpve
x = ['members', 'casuals']
y = [mean_member_ride_length, mean_casual_ride_length]

print(y)
fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.bar(x,y)
plt.bar(x, y, color='orange')
plt.ylim(ymin=0)
plt.ylabel("mean ride length in seconds")
plt.title("mean ride length members vs casual riders")
plt.show()

def convert_hours(mean):
    return int(mean)
# max ride length of member bikers
max_member_ride_length = df_member['ride_length'].max()
print(max_member_ride_length)
max_member_ride_length = convert_hours(max_member_ride_length)

# max ride length of casual bikers
max_casual_ride_length = df_casual['ride_length'].max()
max_casual_ride_length = convert_hours(max_casual_ride_length)

y_max = [max_member_ride_length, max_casual_ride_length]

print(y_max)
fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.bar(x,y)
plt.bar(x, y_max, color='green')
plt.ylim(ymin=0)
plt.ylabel("mean ride length in seconds")
plt.title("mean ride length members vs casual riders")
plt.show()


#number of member riders by day of week

num_meb_rides_by_day = df_member.groupby('day_of_week').agg({'ride_id': ['count']})

print(num_meb_rides_by_day)

num_meb_rides_by_day.info()

for col in num_meb_rides_by_day.columns:
    print (col)

num_meb_rides_by_day.columns = ['count']

#plotting line
num_meb_rides_by_day.plot.line(title="Number of member rides by days")
plt.show(block="TRUE")



#number of casual riders by day of week

num_cal_rides_by_day = df_casual.groupby('day_of_week').agg({'ride_id': ['count']})

print(num_cal_rides_by_day)

num_cal_rides_by_day.info()

num_cal_rides_by_day.columns = ['count']

#plotting line
num_cal_rides_by_day.plot.line(title="Number of casual rides by days")
plt.show(block="TRUE")


# average ride len of members by day_of_week

avg_meb_ride_len_by_day = df_member.groupby('day_of_week').agg({'ride_length': ['mean']})

print(avg_meb_ride_len_by_day)

avg_meb_ride_len_by_day.info()

avg_meb_ride_len_by_day.columns = ['mean']

#plotting line
avg_meb_ride_len_by_day.plot.line(title="Average of ride length by member bikers by days")
plt.show(block="TRUE")


# average ride len of casuals by day_of_week

avg_cal_ride_len_by_day = df_casual.groupby('day_of_week').agg({'ride_length': ['mean']})

print(avg_cal_ride_len_by_day)

avg_cal_ride_len_by_day.info()

avg_cal_ride_len_by_day.columns = ['mean']

#plotting line
avg_cal_ride_len_by_day.plot.line(title="Average of ride length by casual bikers by days")
plt.show(block="TRUE")
