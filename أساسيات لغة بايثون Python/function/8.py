"""def fact(n):
    if n<=1:
        return 1
    else:
        return n *fact(n-1)
print(fact(6))

# قائمة فيها كتب
books = ["Python Basics", "Clean Code", "The Pragmatic Programmer", "Think Python"]

# دالة لعرض الكتب
def show_books(book_list):
    if len(books)== 0:
        return
    else:
        print(list[0])
        return show_books(book_list[1
                          : ])

# استدعاء الدالة
show_books(books)"""


data =[['python','byte','reference'],44,12,'cookbox',('books','websites')]
def print_data(data):
    if not data:return
    if(type(data[0])== list or type(data[0])== tuple):
        print_data(data[0])
    else:
        print(data[0])
    print_data(data[1:])

print_data(data)
