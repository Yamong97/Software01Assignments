def list_of_integer (numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def main():
    original_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    cut_down_list = list_of_integer(original_list)

    print(f"The original list is {original_list}.")
    print(f"The cut down list is {cut_down_list}.")

main()
