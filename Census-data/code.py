# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census=np.concatenate((data,new_record))
#print(census.shape())
age=np.array([i[0] for i in census])
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=age.std()
print(max_age)
print(min_age)
print(round(age_mean,2))
print(round(age_std,2))
race_0=np.array([i[2] for i in census if i[2]==0])
race_1=np.array([i[2] for i in census if i[2]==1])
race_2=np.array([i[2] for i in census if i[2]==2])
race_3=np.array([i[2] for i in census if i[2]==3])
race_4=np.array([i[2] for i in census if i[2]==4])

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

x=np.array([len_0,len_1,len_2,len_3,len_4])

minority_race=x.min()
print(list(x).index(minority_race))

senior_citizens=np.array([i[0] for i in census if i[0]>60])

working_hours_sum=sum(np.array([i[6] for i in census if i[0]>60]))

senior_citizens_len=len(senior_citizens)

avg_working_hours=working_hours_sum/senior_citizens_len
avg_working_hours=round(avg_working_hours,2)
print(avg_working_hours)

high=census[census[:,1]>10]

low=census[census[:,1]<=10]

avg_pay_high=high[:,7].mean()

avg_pay_low=low[:,7].mean()

print(avg_pay_high)
print(avg_pay_low)




#Code starts here




