import openpyxl
import tkinter.filedialog
import os
import datetime


def time():
    return datetime.datetime.now().strftime('%y%m%d_%H%M%S')


# 동일 디렉토리에 있는 xlsx 파일 중 첫 번째 파일 선택
def ex_search_1():
    file = os.listdir(os.getcwd())
    return [s for s in file if '.xlsx' in s][0]


# 탐색기로 파일 선택
def ex_search_2():
    return tkinter.filedialog.askopenfilename(initialdir='', title='한 개의 파일 선택')


# file read
def file_read():
    # a = input('1 : 자동 실행, 2 : 직접 선택\n')
    a = '1'
    if a == '1':
        return openpyxl.load_workbook(ex_search_1())
    elif a == '2':
        return openpyxl.load_workbook(ex_search_2())
    else:
        return print('잘못된 선택')


# def file_read_2():
#     # 여러 sheet를 읽을 경우
#     for sheet_nm in file_read().sheetnames:
#         sheet = file_read()[sheet_nm]


def func_connect():
    file = file_read()
    file_sheet = file['TC']

    # 첫 열 값 추출
    i = 1  # 행
    for row_data in file_sheet.iter_rows(min_col=2, max_row=1):
        for item in row_data:
            if item.value is not None:
                globals()[f'item_{i}'] = item.value
                # print(globals()[f'item_{i}'])
            i += 1

    # 첫 열 제외 값 추출
    z = 1  # 행
    print('#########################################')
    for row_data in file_sheet.iter_rows(min_row=2, min_col=2):  # row 열, col 행
        print('for 1')
        y = 1  # 열
        x = 1  # 첫 열 값
        for cell in row_data:
            globals()[f'postman_{y}'] = {}
            if cell.value is not None:
                globals()[f'cell_{z}_{y}'] = cell.value  # 동적 변수 생성 및 값 삽입
                globals()[f'postman_{y}'][globals()[f'item_{x}']] = globals()[f'cell_{z}_{y}']
                y += 1
            x += 1
        z += 1

    # file_name = f'TC_result_{time()}.xlsx'
    # file.save(file_name)  # file Save 동작은 for문 밖으로 실행해야 함 (for 문 안에서 할 경우 여러 파일 생성됨)
    file.close()
    # print('작성 완료\nFile Name : ', file_name)


if __name__ == '__main__':
    func_connect()
