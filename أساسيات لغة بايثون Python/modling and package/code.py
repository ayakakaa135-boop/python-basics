from random import choice


# قائمة التعليقات
comments = [
    "Great job!",
    "Needs improvement.",
    "Well explained.",
    "Too short, add more details."
]

# تابع يعيد قائمة التعليقات
def get_comments():
    return '\n'.join(comments)

def add_comment(new_comment):
    if isinstance(new_comment, str):  # يتحقق إن الإدخال سلسلة نصية
        comments.append(new_comment)
        return f'Comment added: "{new_comment}"'
    else:
        return "Error: Comment must be a string!"

def get_random_code():
    return choice(comments)
# اختبار التابع
if __name__=='__main__':
 print(get_random_code())

 add_comment('You only live once')
 print(get_comments())
