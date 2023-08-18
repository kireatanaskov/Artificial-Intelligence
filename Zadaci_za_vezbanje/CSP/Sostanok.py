from constraint import *


def check_times(simona, marija, petar, time):
    if simona == 1 and time not in [13, 14, 16, 19]: return False
    if marija == 1 and time not in [14, 15, 18]: return False
    if petar == 1 and time not in [12, 13, 16, 17, 18, 19]: return False

    return True


def two_people(simona, marija, petar):
    return simona == 1 and (marija == 1 or petar == 1)


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", range(12, 21))
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(lambda s: s in [13, 14, 16, 19], ["vreme_sostanok"])

    problem.addConstraint(lambda s: s == 1, ["Simona_prisustvo"])

    problem.addConstraint(check_times, ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"])

    problem.addConstraint(two_people, ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo"])
    # ----------------------------------------------------

    [print(solution) for solution in problem.getSolutions()]