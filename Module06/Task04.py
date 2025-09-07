def list_of_integer (numbers):
    return sum(numbers)

def main():
    list = [2,4,5,6,7,8,9]

    sum = list_of_integer(list)
    print(f"The sum of the numbers in the {list} is {sum}.")

main()