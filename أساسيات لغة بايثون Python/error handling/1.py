"""with open("C:\\Users\\haama\\PycharmProjects\\pythonProject3\\error handling\\file.txt", "a") as f:
    f.write("Hello from Python!\n")"""
with open("C:\\Users\\haama\\PycharmProjects\\pythonProject3\\error handling\\file.txt", "r") as f1, \
     open("C:\\Users\\haama\\PycharmProjects\\pythonProject3\\error handling\\file2.txt", "w") as f2:
    content = f1.read()
    f2.write(content)

with open("C:\\Users\\haama\\PycharmProjects\\pythonProject3\\error handling\\file.txt", "r") as f:
    content = f.read()
    print(content)
with open("C:\\Users\\haama\\PycharmProjects\\pythonProject3\\error handling\\image.png", "rb") as img:
    data = img.read()
    print(type(data))
