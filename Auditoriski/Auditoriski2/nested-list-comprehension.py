if __name__ == "__main__":
    n = int(input())
    m = int(input())

    elements_matrix = []

    # citanje na elementi
    for i in range(0, n):
        # se citaat elementi kako string, se deli stringot i sekoj element se pretvara vo int
        elements_row = [int(element) for element in input().split(" ")]
        elements_matrix.append(elements_row)

    result_matrix = [elem * 2 for row in elements_matrix for elem in row]  # so ova se dobiva lista

    print(result_matrix)

    result_matrix_1 = [[elements_matrix[i][j] * 2 for j in range(0, m)] for i in range(0, n)]

    print(result_matrix_1)
