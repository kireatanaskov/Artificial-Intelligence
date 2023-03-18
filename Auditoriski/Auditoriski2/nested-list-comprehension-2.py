def multiply_element(element, i, n):
    if i < n / 2:
        return element * 2
    else:
        return element * 3


if __name__ == "__main__":
    n = int(input())
    m = int(input())

    matrix_elements = []

    # citanje na elementi
    for i in range(0, n):
        elements_row = [int(element) for element in input().split(" ")]
        matrix_elements.append(elements_row)

    # mnozenje na elementite
    result_matrix = [[multiply_element(matrix_elements[i][j], i, n) for j in range(0, m)] for i in range(0, n)]

    print(result_matrix)

