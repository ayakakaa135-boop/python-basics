import os


"""os.makedirs('file1/file2')"""
os.rename('ee','file')


try:
 os.mkdir('myfile')
except FileExistsError as error:
    print(error)




content = os .scandir()
for item in content:
    if item.is_file():

     print(item.name)
print(os.getcwd())
"""os.chdir('a')
print(os.getcwd())

os.chdir('.. /c')


print(os.getcwd())"""