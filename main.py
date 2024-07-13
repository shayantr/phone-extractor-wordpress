# This is a sample Python script.
import csv
import re
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    y=[]
    z=[]
    with open('wp_users.csv', newline="", encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for file in reader:
            x =file[3]
            x = re.findall(r'\d{10,14}', x)
            y.append(x)
        for i in y:
            for j in i:
                if re.search(r'^98\d+', j):
                    if re.search(r'^9898\d+', j):
                        z.append(re.sub(r'^9898', '0', j))
                    else:
                        z.append(re.sub(r'^98', '0', j))
                elif re.search(r'^9\d+', j):
                    z.append(re.sub(r"^(\d+)", r'0\1', j))
                elif re.search(r'^098\d+', j):
                    z.append(re.sub(r'^098', '0', j))
                    print(1)
                else:
                    z.append(j)

        for i, j in enumerate(z):
            print(i, j)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
