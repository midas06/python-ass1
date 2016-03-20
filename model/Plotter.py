import matplotlib.pyplot as plt
import numpy as np


class Plotter(object):

    def pie_bmi(self, normal_dist, ov_dist, obese_dist, uw_dist):
        total = normal_dist + ov_dist + obese_dist + uw_dist
        labels = "Normal", "Overweight", "Obesity", "Underweight"
        size = [normal_dist, ov_dist, obese_dist, uw_dist]
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        plt.pie(size, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.title("Distribution of BMI indexes (" + str(total) + " people):")
        plt.show()

    def pie_gender(self, m_dist, f_dist):
        total = m_dist + f_dist
        labels = "Male", "Female"
        size = [m_dist, f_dist]
        colors = ['yellowgreen', 'gold']
        plt.pie(size, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.title("Distribution of Gender (" + str(total) + " people):")
        plt.show()

    def scatter_sales(self, sales_list):
        plt.scatter(range(len(sales_list)), sales_list)
        plt.title("Range of Sales Numbers")
        plt.ylabel("Sales ($)")
        plt.show()

    def bar_bmi_vs_gender(self, male_bmi, female_bmi):
        n_groups = 4

        x = male_bmi
        y = female_bmi

        fig, ax = plt.subplots()

        index = np.arange(n_groups)
        bar_width = 0.25
        plt.bar(index, x, bar_width, color='b', label='Male')
        plt.bar(index + bar_width, y, bar_width,color='r', label='Female')
        plt.xlabel('bmi')
        plt.ylabel('no. of people')
        plt.title('bmi by gender')
        plt.xticks(index + bar_width, ('Normal', 'Overweight', 'Obesity', 'Underweight'))
        plt.legend()

        plt.show()

