import math


#initialize rows and cols variables
rows = 0
cols = 0
a = ''
# get input from user:

a = input('Press 1 for easy mode or 2 for difficult mode.\n') # user chooses if they want to play easy or difficult mode

    #if easy mode:
if a == '1': 
    rows = 5
    cols = 5

# if hard mode:
elif a == '2':
    rows = 10
    cols = 10

else:
    print( "You did not press 1 or 2.")


# initialize minefield (array with rows and column as designated)
def initialize_mine_field(rows, cols):

    arr = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(len(arr)):
        return print(arr[i])

print(initialize_mine_field(rows,cols))