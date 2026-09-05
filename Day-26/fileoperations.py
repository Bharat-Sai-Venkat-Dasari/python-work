# with open('pfs-63.txt', 'r') as file:
#     print(file.read())
#     file.seek(0)
#     print(file.readline())
#     file.seek(0)
#     print(file.readlines())

# with open('mysql.txt', 'w') as file:
#     file.write('DDL, DML, DQL')

with open('pfs-63.txt', 'a+') as file:
    file.write('Tmrw same branch-5')
    file.seek(0)
    print(file.read())