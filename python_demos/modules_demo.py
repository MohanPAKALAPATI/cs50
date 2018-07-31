from functions_demo import square
##Above line imports all the lines in the functions_demo file and executes them line by line
##so we get output functions_demo file along with the below line output like below
##0 squared is 0
##1 squared is 1
##2 squared is 4
##3 squared is 9
##4 squared is 16
##5 squared is 25
##6 squared is 36
##7 squared is 49
##8 squared is 64
##9 squared is 81
##10000
## to prevent this we are going to use __name__ == "__main__:
## now we get square of 100 only

print(square(100))
