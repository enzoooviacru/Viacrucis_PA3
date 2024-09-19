# PA3 - Python Data Analysis (PANDAS)

#### This repository serves as a submission for Programming Assignment#3 involving 2 problems to be solved used PANDAS.

### REMINDER: Please download the "cars.csv" file before running any of the codes.

### Problem 1:
#### For the first problem, we are tasked to load the "cars.csv" file into a data frame named cars using pandas and to display its first and last five rows.

#### What to do:

##### Import pandas library to use its functions.
##### Load the "cars.csv" file by using the function `pd.read_csv()`.
##### Display the first and last 5 rows of the data frame using the `.head()` and `.tail()` function of PANDAS library respectively.

## Code
```python
import pandas as pd

#Read/load the csv file and store it in a variable named "cars" to be able to use its data
cars = pd.read_csv('cars.csv')

#Storing the first and last 5 rows in "head" and "tail" with head() and tail() function respectively
head = cars.head()
tail = cars.tail()

#Concatenating tail to head into variable "headtail" for better readability
headtail = pd.concat([head, tail])

#Displaying the first and last five rows of the dataframe with print() finction
print("The first and last 5 rows of dataframe 'cars':")
headtail
```

## Output
![PA3 PROBLEM1 OUTPUT](https://github.com/user-attachments/assets/53582f4c-0f86-490c-bfb5-7f6699a724b0)


### Problem 2:

#### Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.

#### What to do:

##### a)Display the first five rows with odd-numbered columns of cars.csv file
##### b)Display the row that contains the ‘Model’ of ‘Mazda RX4’
##### c)How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
##### d)Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have

## Code
```python
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
```

## Output
#### For a)
![PA3 PROBLEM2 OUTPUTA](https://github.com/user-attachments/assets/725d940c-cb1a-49f0-96a2-49bce42f6286)

#### For b)
![PA3 PROBLEM2 OUTPUTB](https://github.com/user-attachments/assets/482139eb-a346-4251-b91d-1aabe83f0575)

#### For c)
![PA3 PROBLEM2 OUTPUTC](https://github.com/user-attachments/assets/e949291d-dbca-4ae2-be60-b96b59cb7a7d)

#### For d)
![PA3 PROBLEM2 OUTPUTD](https://github.com/user-attachments/assets/844816c7-3e20-4f8e-9d38-6f0fee2064a0)

## Author
### Lorenzo G. Viacrucis
### 2ECE-D
