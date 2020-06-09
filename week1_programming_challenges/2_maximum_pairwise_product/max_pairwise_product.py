# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max1 = max(numbers)
    numbers.remove(max1)
    product = max1 * max(numbers)

            
    return product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
