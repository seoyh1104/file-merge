""" file_merge.py
Author : Yuhui Seo
Last Modification : 2023.03.13
"""
import os
import chardet  # pip install chardet

class SystemInfo:
    def __init__(self):
        pass

    def set_relative_file_path(self):
        program_directory = os.path.dirname(os.path.abspath(__file__))
        os.chdir(program_directory)

def read_file(path):
    """파일을 열어서 인코딩을 확인하고, 맞게 열어서 반환한다."""
    # 파일 열어서 인코딩 확인
    rawdata = open(path, 'rb').read()
    result = chardet.detect(rawdata)
    enc = result['encoding']

    # 인코딩 맞게 열기
    file = open(path, "r", encoding=enc)
    return file


def main():
    sys_info = SystemInfo()
    SystemInfo.set_relative_file_path(sys_info)

    # 각 년도별 폴더 이름 설정
    folders = ['2020', '2021', '2022', '2023']

    # 년도별로 파일 내용을 읽어와서 이어붙이기
    for folder in folders:
        # 년도별 파일 저장 디렉토리 경로
        dir_path = os.path.join(os.getcwd(), folder)

        # 년도별 파일 리스트
        # file_list = os.listdir(dir_path)

        # 확장자가 .txt인 파일만 file_list에 포함시킴
        file_list = [f for f in os.listdir(dir_path) if f.endswith('.txt')]

        # 파일 리스트를 날짜순으로 정렬
        file_list.sort()

        # 파일 내용 이어붙이기
        file_content = ''
        # for file_name in file_list:
        for i, file_name in enumerate(file_list):
            # 파일 경로
            file_path = os.path.join(dir_path, file_name)

            # 파일명에서 년, 월, 일 정보 가져오기
            year = file_name[:4]
            month = file_name[4:6]
            day = file_name[6:8]

            # 파일 내용 읽어오기
            file = read_file(file_path)
            file_content += f'{year}년 {month}월 {day}일\n{file.read().strip()}'

            # 가독성을 위해 마지막 파일이 아니면 파일 사이에 행 추가
            if i < len(file_list) - 1:
                file_content += '\n\n\n'

        # 파일 쓰기
        md_file_name = folder + '.md'
        with open(md_file_name, 'w', encoding='utf8') as file:
            file.write(file_content)


if __name__ == '__main__':
    main()
