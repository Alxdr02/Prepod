grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
a=len(grades[0]),len(grades[1]),len(grades[2]),len(grades[3]),len(grades[4])
print(a)
b=sum(grades[0]),sum(grades[1]),sum(grades[2]),sum(grades[3]),sum(grades[4])
print(b)
c=(b[0]/a[0],b[1]/a[1],b[2]/a[2],b[3]/a[3],b[4]/a[4])
print(c)
print({students[0]:(c[0]),students[1]:(c[1]),students[2]:(c[2]),students[3]:(c[3]),students[4]:(c[4])})



