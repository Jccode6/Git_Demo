import csv,os,sys,pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#0 Genes
#1 IDs
#2 Values
#Open pickle file
file = open('./excercise.pickle', 'rb')

#Load data from file
data = pickle.load(file)

new_array_index = data[0]
new_array_columns = data[1]
new_array_rows = data[2]

#create dataframe in order to find mean
df = pd.DataFrame(data=new_array_rows, columns=new_array_columns)
df2 = df.set_index(new_array_index)

#print mean of genes
print(df2.mean(axis=0))

#Function that plots histogram by gene
def gene_histogram(x):
    fig, ax = plt.subplots(figsize=(10,7))
    plt.hist(x)
    #plt.hist(new_array_rows)
    return plt.show()

gene_histogram('alpha')

#close the file
file.close()
