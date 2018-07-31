def square(x_input):
    return(x_input * x_input)


def main():
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))

if __name__ == "__main__":
    main()                #if function calling name is main
                           #then main will starts execution
