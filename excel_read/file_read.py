import openpyxl
import tkinter.filedialog
import os, json

import selenium.webdriver.common.devtools.v129.dom


# file read
def file_read(a='1'):
    # a = input('1 : 자동 실행, 2 : 직접 선택\n')
    if a == '1':  # 동일 디렉토리에 있는 xlsx 파일 중 첫 번째 파일 선택
        file = os.listdir(os.getcwd())
        return openpyxl.load_workbook([s for s in file if '.xlsx' in s][0])
    elif a == '2':  # 탐색기로 파일 선택
        ################## TBD ##################
        return openpyxl.load_workbook(tkinter.filedialog.askopenfilename(initialdir='', title='한 개의 파일 선택'))
    else:
        return print('잘못된 선택')


def sheet_read(a='1'):
    if a == '1':  # 특정 sheet를 읽을 경우
        return 'TC'
    else:   # 여러 sheet를 읽을 경우
        ################## TBD ##################
        for sheet_nm in file_read().sheetnames:
            sheet = file_read()[sheet_nm]
        return None


class FUNC:
    def __init__(self):
        self.file = file_read()
        self.file_sheet = self.file[sheet_read()]
        self.case_item = {}
        self.case_result = {}
        self.tc_count = FUNC.col_count(self)

    # row : 행, col : 열
    def col_count(self):  # TC 총 개수 (A열 개수)
        for col_data in self.file_sheet.iter_cols(max_col=1, min_row=1):
            return len(col_data)

    def test_item_array(self):
        i = 1
        j = 1
        for col_data in self.file_sheet.iter_rows(min_col=2, min_row=2, max_col=12, max_row=self.tc_count):
            for item_v in col_data:
                if item_v.value is None:
                    globals()[f'em_{i}'] = ''
                elif item_v.value is not None:
                    globals()[f'em_{i}'] = item_v.value
                # print(f'em_{i} : ', globals()[f'em_{i}'])
                # print('end')

                if i % 11 == 0:
                    self.case_item[f"case_{j}"] = {
                        "function_name": globals()[f'em_{i - 10}'],
                        "number": globals()[f'em_{i - 9}'],
                        "idx": globals()[f'em_{i - 6}'],
                        "input_1": globals()[f'em_{i - 5}'],
                        "input_2": globals()[f'em_{i - 4}'],
                        "input_3": globals()[f'em_{i - 3}'],
                        "input_4": globals()[f'em_{i - 2}']
                    }
                    self.case_result[f"case_{j}"] = {
                        "function_name": globals()[f'em_{i - 10}'],
                        "number": globals()[f'em_{i - 9}'],
                        "Expected_result": globals()[f'em_{i - 1}'],
                        "Actual_result": globals()[f'em_{i - 0}']
                    }
                i += 1
            j += 1
        return json.dumps({
            "item": self.case_item,
            "result": self.case_result
        })
    def result_write(self):
        pass

if __name__ == "__main__":
    run = FUNC()
    print(type(run.test_item_array()))