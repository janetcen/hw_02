import csv
exampleFile = open('jobs_by_industry.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

import matplotlib.pyplot as plt
import csv

Industry = []
Jobs = []

Industry.append(exampleData[3][3])
Jobs.append(exampleData[3][4])
Industry.append(exampleData[5][3])
Jobs.append(exampleData[5][4])
Industry.append(exampleData[7][3])
Jobs.append(exampleData[7][4])
Industry.append(exampleData[17][3])
Jobs.append(exampleData[17][4])
Industry.append(exampleData[10][3])
Jobs.append(exampleData[10][4])
  
plt.pie(Jobs,labels = Industry,autopct = '%.2f%%')
plt.title('Jobs in Each Industry', fontsize = 20)
plt.show()

