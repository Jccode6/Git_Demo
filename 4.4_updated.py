import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_columns = ['Month','Radiology Visits', 'Patient Days', 'ER Visits', 'Clinic Visits']
#import data
df = pd.read_fwf('https://home.gwu.edu/~maxal/pubh4201/RADIOLOGY.txt', names= data_columns, set_index='Month')
#Create Radiology scatter

#Find mean
radiology_mean = df['Radiology Visits'].mean()
#Create scatter with x axis as month and y axis as visits
plt.scatter(df['Month'], df['Radiology Visits'])
#Set tick range for x axis
plt.xticks(np.arange(0,31,10))
#Set tick tange for y axis
plt.yticks(np.arange(2500,3501,500))
#Create mean line
plt.axhline(radiology_mean, color='r')
plt.title('visits to radiology')
plt.show()

#Create Patient Day scatter

patient_mean = df['Patient Days'].mean()
plt.scatter(df['Month'], df['Patient Days'])
plt.xticks(np.arange(0,31,10))
plt.yticks(np.arange(5000,7001,1000))
plt.axhline(patient_mean, color='r')
plt.title('patient days')
plt.show()

#Create ER Visit scatter

ER_mean = df['ER Visits'].mean()
plt.scatter(df['Month'], df['ER Visits'])
plt.xticks(np.arange(0,31,10))
plt.yticks(np.arange(1000,1801,200))
plt.axhline(ER_mean, color='r')
plt.title('ER Visits')
plt.show()

#Create Clinic visit scatter
clinic_mean = df['Clinic Visits'].mean()
plt.scatter(df['Month'], df['Clinic Visits'])
plt.xticks(np.arange(0,31,10))
plt.yticks(np.arange(900,1301,1000))
plt.axhline(clinic_mean, color='r')
plt.title('clinic visits')
plt.show()
