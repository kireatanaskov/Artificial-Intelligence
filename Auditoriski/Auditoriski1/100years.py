# Напишете програма која бара од корисникот да внесе име и години и потоа пресметува во која година тој ќе има 100 години.
# Испечатете го неговото име и годината добиена.

if __name__=="__main__":
    name = input()
    years = int(input())
    currentYear = 2023
    diff = 100 - years
    year100 = currentYear + diff
    print(f"{name} ke ima 100 godini vo {year100}")