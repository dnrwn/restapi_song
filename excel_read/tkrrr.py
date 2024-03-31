from tkinter import filedialog


def aa(a):
    match a:
        case '1':
            filedialog.askopenfilename(initialdir='', title='한 개의 파일 선택')

b = input()
aa(b)