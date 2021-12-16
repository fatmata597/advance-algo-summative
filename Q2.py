def grade(n):
    if n <38:
        return n
    else:
        modular = n%5
        if modular < 3:
            return n
        else:
            return n+(5-modular)
print(grade(33), "is your final grade")
print(grade(67), "is your final grade")
print(grade(38), "is your final grade")
print(grade(73), "is your final grade")
