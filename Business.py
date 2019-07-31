import business_dynamics
# These may be slow!
list_of_record = business_dynamics.get_businesses()

year_list = []
births_list = []

for i in range(len(list_of_record)):
    birth = list_of_record[i]["Data"]["Job Creation"]["Births"]
    year = list_of_record[i]["Year"]
    state = list_of_record[47]["State"]
    print(year, birth, state )
    year_list.append(year)
    births_list.append(birth)
print(year_list)
print(births_list)

# for i in range(len(list_of_record)):
#     deaths = list_of_record[i]["Data"]["Job Destruction"]["Deaths"]
#     year = list_of_record[i]["Year"]
#     state = list_of_record[47]["State"]
#     print(year, deaths, state )

import matplotlib.pyplot as plt
# Plot
N = 500
x = year_list
y = births_list
# colors = (0,0,0)
# area = np.pi*3

plt.scatter(x, y)
plt.title('Scatter plot pythonspot.com')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
