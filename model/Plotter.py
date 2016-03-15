import matplotlib.pyplot as plt

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

    def pie_sales(self, low_dist, med_dist, high_dist):
        total = low_dist + med_dist + high_dist
        labels = "< $333", "Female"
        size = [m_dist, f_dist]
        colors = ['yellowgreen', 'gold']
        plt.pie(size, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.title("Distribution of Gender (" + str(total) + " people):")
        plt.show()
