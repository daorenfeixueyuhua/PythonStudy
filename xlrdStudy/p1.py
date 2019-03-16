import xlrd


class Student():
    def __init__(self, teamName, name, job):
        self.teamName = teamName
        self.name = name
        self.job = job

    def __str__(self):
        return str(self.teamName)+" "+self.name+" "+self.job



# 打开excel表
data = xlrd.open_workbook('./test.xlsx')

print(data)

# 打开sheet
table = data.sheet_by_index(0)

nrows = table.nrows

ncols = table.ncols

student = list()


for i in range(1, nrows-1):
    for j in range(1, ncols-1):
        s = Student(table.cell_value(i, 0), table.cell_value(i, j), table.cell_value(0, j))
        student.append(s)

for i in student:
    print(i)



