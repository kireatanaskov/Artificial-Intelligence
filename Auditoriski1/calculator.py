# Напишете функција која ќе ги содржи функционалностите на едноставен аритметички калкулатор.
# Интеракција со калкулаторот треба да се врши преку читање на параметри од стандардниот влез со наредбата input(),
# т.е. се внесуваат двата операнди и операторот во командна линија.
# По процесирање на барањето од страна на функцијата се обработува и се печати резултатот на екран.
# Командите кои ги испраќаме на калкулаторот се читаат од стандарден влез и треба да го имаат следниот формат:
#
#     операнд1
#     оператор
#     операнд2
#
# Доколку настанала грешка при внес да се извести корисникот со соодветна порака. Калкулаторот треба да ги подржува следните операции:
#
#     Собирање (+)
#     Одземање (-)
#     Множење (*)
#     Целобројно делење (//)
#     Делење (/)
#     Модуло (остаток) (%)
#     Степенување (**)

operators = ['+', '-', '/', '//', '*', '**', '%']

def calculator(x, y, operator):
    # ako operatorot so go vnesuvame go nema vo operators nizata da se pecati greska
    if operator not in operators:
        return "Greshen operator!"

    if operator == "+":
        return x+y
    elif operator == "-":
        return x-y
    elif operator == "/":
        return x/y
    elif operator == "//":
        return x//y
    elif operator == "*":
        return x*y
    elif operator == "**":
        return x**y
    elif operator == "%":
        return x%y

if __name__=="__main__":
    x = float(input())
    operator = input()
    y = float(input())
    rez = calculator(x, y, operator)
    print("Rezultat: ", rez)