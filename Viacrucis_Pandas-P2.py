#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

#Read/load the csv file and store it in a variable named "cars" to be able to use its data
cars = pd.read_csv('cars.csv')

#a) Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
#Using the `.iloc` function, we can set the range of values for rows of 0 to 5 and columns starting from 1 with an increment of 2 
a = cars.iloc[:5, 1::2]
print("The first five rows with odd-numbered columns is:")
print(a)
print()

#b) Display the row that contains the "Model" of "Mazda RX4". 
#Using the `.loc` function, find the row with "Mazda RX4" under the "Model" category and print all its columns
b = cars.loc[cars['Model']=='Mazda RX4']
print("The row that contains the ‘Model’ of ‘Mazda RX4’ is:")
print(b)
print()

#c) How many cylinders ("cyl’") does the car model "Camaro Z28’" have?
#Using the `.loc` function, find the row with "Camaro Z28" under the "Model" category and print only the column of its cylinders "cyl" and for readability also print "Model"
c = cars.loc[cars['Model']=='Camaro Z28', ['Model', 'cyl']]
print("Cylinders of car model 'Camaro Z28':")
print(c)
print()

#d) Determine how many cylinders ("cyl") and what gear type ("gear") do the car models "Mazda RX4 Wag", "Ford Pantera L" and "Honda Civic" have.
#Using the `.loc` function, find the row with "Mazda RX4 Wag", "Ford Pantera ", and "Honda Civic" under the "Model" category and print only the column of its cylinders "cyl", gear type "gear", and for readability "Model"
x = cars.loc[cars['Model']=='Mazda RX4 Wag', ['Model', 'cyl', 'gear']]
y = cars.loc[cars['Model']=='Ford Pantera L', ['Model', 'cyl', 'gear']]
z = cars.loc[cars['Model']=='Honda Civic', ['Model', 'cyl', 'gear']]

#Concatenating x, y, and z for readability
d = pd.concat([x, y, z])

#Displaying using the print() function
print("Cylinders and gear type of models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic':")
print(d)

