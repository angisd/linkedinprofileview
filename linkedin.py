# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = ['5/28', '6/4', '6/11', '6/18', '6/25', '7/2', '7/9', '7/16', '7/23', '7/30', '8/6', '8/13', '8/20']
# corresponding y axis values
y = [12, 10, 12, 32, 59, 17, 10, 13, 6, 11, 3, 11, 4]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('Week')
# naming the y axis
plt.ylabel('Views')

# giving a title to my graph
plt.title('Trend of Linkedin Profile Views')

# function to show the plot
plt.show()