from model.Processor import *
import  matplotlib.pyplot as plt

p = Processor()
p.add_data("test.csv")
#for i in p.database.get_age_array():
    #print(i)


#p.add_data("test.csv")
age = p.database.get_age_array()
sales = p.database.get_sales_array()
plt.plot(age, sales, 'bo')
plt.show()
