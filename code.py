# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-

'''
직업 정보 조회
'''

#%%
from tkinter import *
from tkinter import messagebox
import tkinter.font as font

# 직업 정보 사전
jobs_info = {'정보보안전문가': {'직업정보': '설명:\n설명\n\n관련학과:\n관련학과\n\n임금:\n임금\n',
                                '자격증': '정보보호전문가\n윤리적해커인증\n정보시스템감리사\n정보시스템보안전문가',
                                '공부방법': '공부방법',
                                '자격증합격후기': '자격증합격후기'},
             '자산운영가': {'직업정보': '설명:\n설명\n\n관련학과:\n관련학과\n\n임금:\n임금\n',
                                '자격증': '투자자산운용사',
                                '공부방법': '공부방법',
                                '자격증합격후기': '자격증합격후기'},
             '약사': {'직업정보': '설명:\n설명\n\n관련학과:\n관련학과\n\n임금:\n임금\n',
                                '자격증': '약사',
                                '공부방법': '공부방법',
                                '자격증합격후기': '자격증합격후기'},
             '건축석공': {'직업정보': '설명:\n설명\n\n관련학과:\n관련학과\n\n임금:\n임금\n',
                                '자격증': '석공기능사',
                                '공부방법': '공부방법',
                                '자격증합격후기': '자격증합격후기'},
             '제과제빵원': {'직업정보': '설명:\n설명\n\n관련학과:\n관련학과\n\n임금:\n임금\n',
                                '자격증': '제과기능사\n제빵기능사',
                                '공부방법': '공부방법',
                                '자격증합격후기': '자격증합격후기'}}

# 자격증 정보 사전
cert_info = {
    '정보보호전문가': {'분류': '정보기술', '세분류': '정보보안', '시행기관': '한국인터넷진흥원', '유효기간': '3년', '연간 시행횟수': '2회', '직업': '컴퓨터보안전문가'}, 
    '윤리적해커인증': {'분류': '정보기술', '세분류': '정보보안', '시행기관': 'ICECC', '유효기간': '3년', '연간 시행횟수': '2회', '직업': '컴퓨터보안전문가'}, 
    '정보시스템감리사': {'분류': '정보기술', '세분류': '정보보안', '시행기관': '한국지능정보사회진흥원', '유효기간': '3년', '연간 시행횟수': '2회', '직업': '컴퓨터보안전문가'}, 
    '정보시스템보안전문가': {'분류': '정보기술', '세분류': '정보보안', '시행기관': '국제정보시스템보호인증협회', '유효기간': '3년', '연간 시행횟수': '2회', '직업': '컴퓨터보안전문가'}, 
    '투자자산운용사': {'분류': '금융', '세분류': '투자', '시행기관': '한국금융투자협회', '유효기간': '5년', '연간 시행횟수': '3회', '직업': '자산운용가'}, 
    '약사': {'분류': '보건의료', '세분류': '보건의료', '시행기관': '한국보건의료인국가시험원', '유효기간': '영구', '연간 시행횟수': '1회', '직업': '약사'}, 
    '석공기능사': {'분류': '건설', '세분류': '건설구조', '시행기관': '한국산업인력공단', '유효기간': '영구', '연간 시행횟수': '3회', '직업': '건축석공'}, 
    '제과기능사': {'분류': '설치정비생산', '세분류': '제과제빵', '시행기관': '한국산업인력공단', '유효기간': '영구', '연간 시행횟수': '30회', '직업': '제과제빵원'}, 
    '제빵기능사': {'분류': '설치정비생산', '세분류': '제과제빵', '시행기관': '한국산업인력공단', '유효기간': '영구', '연간 시행횟수': '30회', '직업': '제과제빵원'},  
}

class JobSearchWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title('직업 조회')
        self.geometry('400x650')
        self.defaultFont = font.nametofont('TkDefaultFont')
        self.defaultFont.configure(size=20, weight=font.BOLD)

        self.jobs = jobs_info.keys()        # 직업 정보 제목(정보보안전문가 등)
        self.certs = cert_info.keys()       # 자격증 정보 제목
        self.search_text = StringVar()      # 검색어
        self.job = ''                       # 선택된 직업 종류(self.jobs 중 하나)
        self.info = ''                      # 선택된 직업 종류 중 세부 정보(직업정보, 자격증 등 그 중 하나)

        self.next_page = None               # 전환된 화면

        # 뒤로/종료 버튼 설정
        self.back_button = Button(self, text = '뒤로')
        self.back_button.place(x=20, y=560)
        Button(self, text = '종료', command = self.destroy).place(x=300, y=560)

        # 주 화면 설정
        self.change_page(page_1)

    # 화면 전환
    def change_page(self, current_page):
        if (self.next_page):                # 이 전 화면이 있으면 먼저 삭제
            self.next_page.destroy()
        self.next_page = current_page(self) # 새로운 화면 생성
        self.next_page.pack()

# 직업 조회
class page_1(Frame):
    def __init__(self, master):
        super(page_1, self).__init__(master)

        # 맨 상단 제목
        frame1 = Frame(self)
        frame1.pack(pady = 10)
        Label(frame1, text = '직업 조회', bg='yellow').pack(fill = 'both')

        # 라디오버튼 추가

        # 검색 버튼과 입력란
        frame2 = Frame(frame1)
        frame2.pack(padx=20, pady=20)

        Button(frame2, text='검색', command = lambda: master.change_page(page_1)).pack(side='left')
        radiobtn_var = IntVar()
        select_findbyjob = Radiobutton(frame2, text="직업으로 자격증 찾기", value = 1, variable = radiobtn_var)
        select_findbycert = Radiobutton(frame2, text="자격증으로 직업 찾기", value = 2, variable = radiobtn_var)
        select_findjobinfo = Radiobutton(frame2, text="직업 정보 보기", value = 3, variable = radiobtn_var)

        select_findbyjob.pack()
        select_findbycert.pack()
        select_findjobinfo.pack()
        entry = Entry(frame2, textvariable=master.search_text, font = ('', 20))
        entry.pack(side='left', fill = 'both')
        entry.bind('<Return>', lambda e: master.change_page(page_1))    # 엔터를 누르면 검색 버튼과 같은 기능을 하도록 설정
        
        # 검색어를 기준으로 직업 정보 제목에서 검색
        search_text = self.master.search_text.get()
        found = self.find_job(search_text)
        print(radiobtn_var.get())
        if (not found):                     # 없는 경우 공백으로 처리
            search_text = ''

        # 검색어에 해당하는 제목만 버튼으로 생성, 공백이면 모두 생성(초기 화면과 동일)
        for job in self.master.jobs:
            if (search_text in job):
                Button(frame1, text=job, command=lambda x=job: self.button_clicked(x)).pack(fill='x', padx=20, pady=5)

        # 검색어 입력란 초기화 및 뒤로 가기 버튼 감추기
        self.master.search_text.set('')
        self.master.back_button.place_forget()

        # 검색 결과가 없는 경우
        if (not found):
            messagebox.showinfo('직업 조회', '검색 결과가 없습니다!', master=self)

    # 직업 정보 검색: 검색어를 기준으로 직업 정보 제목에서 검색
    def find_job(self, search_text): # self, 입력한 문자열
        for job in self.master.jobs:
            if (search_text in job):
                return True
        return False

    # 자격증으로 직업 찾기
    def find_job_bycert(self, search_text):
        for cert in self.master.certs:  # 자격증 정보 Keys
            if (search_text in cert):
                return True
            return False

    # 직업으로 자격증 찾기
    def find_cert_byjob(self, search_text):
        for job in self.master.jobs:  # 직업 정보 Keys
            if (search_text in job):
                return True
            return False
            
    # 버튼 클릭 시 직업별 정보 조회 화면 전환
    def button_clicked(self, job): # 직업을 넘겨줌
        self.master.job = job
        self.master.change_page(page_2)

# 직업별 정보 조회
class page_2(Frame):
    def __init__(self, master):
        super(page_2, self).__init__(master)

        # 맨 상단 제목(직업별)
        frame1 = Frame(self)
        frame1.pack(pady = 10)
        Label(frame1, text = self.master.job, width=400, bg='yellow').pack(fill = 'both')

        # 직업별 세부 정보 버튼 생성
        frame2 = Frame(frame1)
        frame2.pack(pady=20, fill='x')
        for info in jobs_info[self.master.job]:
            Button(frame2, text=info, command=lambda x=info: self.button_clicked(x)).pack(fill='x', padx=20, pady=5)

        # 뒤로 가기 버튼 보이기 및 이 전 화면 등록
        self.master.back_button.place(x=20, y=560)
        self.master.back_button['command'] = lambda: self.master.change_page(page_1)

    # 버튼 클릭 시 상세 정보 조회 화면 전환
    def button_clicked(self, info):
        self.master.info = info
        self.master.change_page(page_3)

# 상세 정보 조회
class page_3(Frame):
    def __init__(self, master):
        super(page_3, self).__init__(master)

        # 맨 상단 제목(상세 정보)
        frame1 = Frame(self)
        frame1.pack(pady = 10)
        Label(frame1, text = self.master.info, width=400, bg='yellow').pack(fill = 'both')

        # 상세 정보 출력
        frame2 = Frame(frame1)
        frame2.pack(pady=20, fill='x')
        text = Text(frame2, height=30)
        text.pack(fill='x', padx=20, pady=5)
        text.insert(1.0, jobs_info[self.master.job][self.master.info])

        # 뒤로 가기 버튼에 해당하는 이 전 화면 등록
        self.master.back_button['command'] = lambda: self.master.change_page(page_2)

if __name__ == '__main__':
    window = JobSearchWindow()
    window.mainloop()

# %%
