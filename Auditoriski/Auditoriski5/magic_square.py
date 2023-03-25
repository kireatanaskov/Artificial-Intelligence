from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # oti kvadratot e 4x4 ni trebaat 16 promenlivi
    # oznaceni so broevi od 1 do 16
    variables = range(1, 17)

    # domen na vrednosti koj moze da go imaat promenlivite
    domain = range(1, 17)

    problem.addVariables(variables, domain)

    problem.addConstraint(AllDifferentConstraint(), variables)

    # sumata vo sekoja redica da bide 34
    for row in range(4): # 0, 1, 2, 3
        """
        problem.addConstraint(ExactSumConstraint(34), [0, 1, 2, 3])
        problem.addConstraint(ExactSumConstraint(34), [4, 5, 6, 7])
        problem.addConstraint(ExactSumConstraint(34), [8, 9, 10, 11]
        problem.addConstraint(ExactSumConstraint(34), [12, 13, 14, 15]   
        """
        problem.addConstraint(ExactSumConstraint(34), [row * 4 + i for i in range(1, 5)])
                                                        # 1, 2, 3, 4
                                                        # 5, 6, 7, 8
                                                        # 9, 10, 11, 12
                                                        # 13, 14, 15, 16
    for col in range(4): # 0, 1, 2, 3
        problem.addConstraint(ExactSumConstraint(34), [col * 4 + i for i in range(1, 5)])

    problem.addConstraint(ExactSumConstraint(34), [1, 6, 11, 16])

    problem.addConstraint(ExactSumConstraint(34), [4, 7, 10, 13])

    solution = problem.getSolution()

    print(solution)
