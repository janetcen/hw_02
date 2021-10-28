
import matplotlib.pyplot as plt
from matplotlib import style
import csv

#year = []
#score = []
#year1 = []
#score1 = []

x_coordinates = [2006, 2007, 2008, 2009, 2010]

asian = [700, 706, 707, 709, 711]
black = [664, 675, 676, 680, 682]


plt.plot(x_coordinates, asian,label = "Asian Students")
plt.plot(x_coordinates, black, label = 'Black Students')


plt.xlabel('Year')
plt.ylabel('Mean Scale Score')
plt.title('NYC Math Test Results by Grade in 2006', fontsize = 20)
plt.grid()
plt.legend()
plt.show()
