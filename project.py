from distutils.command.config import LANG_EXT
from gettext import lngettext
from queue import PriorityQueue

class certificate:
    name = None # 이름
    department = None # 분류
    agency = None # 기관
    validity = None # 유효기간
    timesperyear = None # 연간 시행 횟수
    job = []

    def __init__(self, name, department, agency, validity, timesperyear, job):
        self.name = name
        self.department = department
        self.agency = agency
        self.validity = validity
        self.timesperyear = timesperyear
        self.job = job

class job:
    name = None # 이름
    department = None # 분류
    description = None # 설명
    major = [] # 관련학과
    certificate = [] # 자격증
    salary = None # 임금
    study = None # 공부방법
    hoogi = None # 합격후기

    def __init__(self, name, department, description, major, certificate, salary, study, hoogi):
        self.name = name
        self.department = department
        self.description = description
        self.major = major
        self.certificate = certificate
        self.salary = salary
        self.study = study
        self.hoogi = hoogi

job_ITsecurity = job("정보보안전문가", "정보기술", "여기에 설명 입력", ["컴퓨터공학과", "정보보안학과", "정보통신공학과"], ["정보보호전문가", "윤리적해커인증", "정보시스템관리사", "정보시스템보안전문가"], 3650, "여기에 공부방법 입력", "여기에 후기 입력")
job_digitalforensic = job("디지털포렌식수사관", "정보기술", "여기에 설명 입력", ["컴퓨터공학과", "정보보안학과", "정보통신공학과"], ["정보보호전문가", "윤리적해커인증", "정보시스템관리사", "정보시스템보안전문가"], 3750, "여기에 공부방법 입력", "여기에 후기 입력")
job_assetmanager = job("자산운용가", "금융", "여기에 설명 입력", ["경영학과", "경제학과", "수학과", "통계학과"], ["투자자산운용사"], 6350, "여기에 공부방법 입력", "여기에 후기 입력") 
job_pharmacist = job("약사", "보건의료", "여기에 설명 입력", ["약학과"], ["약사"], 6406, "여기에 공부방법 입력", "여기에 후기 입력")
job_mason = job("건축석공", "건설", "여기에 설명 입력", ["학과 없음"], ["석공기능사"], 3500, "여기에 공부방법 입력", "여기에 후기 입력")
job_baker = job("제과제빵원", "생산", "여기에 설명 입력", ["식품영양학과", "식품조리학과"], ["제과기능사", "제빵기능사"], 3700, "여기에 공부방법 입력", "여기에 후기 입력")

# 직업 목록
jobs = [job_ITsecurity, job_digitalforensic, job_assetmanager, job_pharmacist, job_mason, job_baker]

cert_SIS = certificate("정보보호전문가", "정보기술", "한국인터넷진흥원", "3년", "2회", ["정보보안전문가", "디지털포렌식수사관"])
cert_CEH = certificate("윤리적해커인증", "정보기술", "ICECC", "3년", "2회", ["정보보안전문가"])
cert_CISA = certificate("정보시스템감리사", "정보기술", "한국지능정보사회진흥원", "3년", "2회", ["정보보안전문가"])
cert_CISSP = certificate("정보시스템보안전문가", "정보기술", "국제정보시스템보호인증협회", "3년", "2회", ["정보보안전문가"])
cert_assetmanager = certificate("투자자산운용사", "금융", "한국금융투자협회", "5년", "3회", ["자산운용가"])
cert_pharmacist = certificate("약사", "보건의료", "한국보건의료인국가시험원", "영구", "1회", ["약사"])
cert_mason = certificate("석공기능사", "건설", "한국산업인력공단", "영구", "3회", ["건축석공"])
cert_baker1 = certificate("제과기능사", "생산", "한국산업인력공단", "영구", "30회", ["제과제빵원"])
cert_baker2 = certificate("제빵기능사", "생산", "한국산업인력공단", "영구", "30회", ["제과제빵원"])

# 자격증 목록
certificates = [cert_SIS, cert_CEH, cert_CISA, cert_CISSP, cert_assetmanager, cert_pharmacist, cert_mason, cert_baker1, cert_baker2]
certificate_list = []
for i in jobs:
    certificate_list.append(set(i.certificate))

# 추천 직업 후보
candidate_job = []
# 추천 직업별 연봉 목록
candidate_job_salary = []
# 추천 자격증 후보
candidate_cert = set()
cert_candidate = []
set_cover = []

def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        qsort(a, low, pivot-1)
        qsort(a, pivot+1, high)

def partition(a, pivot, high):
    i = pivot+1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:
            i += 1
        while j > pivot and a[j] > a[pivot]:
            j -= 1
        if j <= i:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    a[pivot], a[j] = a[j], a[pivot]
    return j

userinput = input('직업으로 자격증 추천받기 - 1, 자격증으로 직업 추천받기 - 2: ')
userinput = int(userinput)

# 직업으로 자격증 추천받기: 집합커버 알고리즘
if userinput == 1:
    userjob = input('원하시는 직업을 입력하세요: ').split()
    # 직업이 1개일 때는 집합커버를 하지 않음
    if len(userjob) == 1:
        for job in jobs:
            if (userjob[0] == job.name): # 입력받은 직업과 저장된 직업명이 일치할 때
                candidate_cert = job.certificate # 해당 직업의 자격증들을 배열에 저장
                if candidate_cert:
                    print('입력하신 직업에 대한 추천 자격증 목록입니다.')
                    for i in candidate_cert:
                        print(i)
    else:
        for joblist in userjob: # 배열을 만들어서 직업별 자격증을 전부 넣은 조합을 만든다.
            for job in jobs:
                if (joblist == job.name):
                    for j in job.certificate:                    
                        for x in job.certificate:
                            candidate_cert.add(x)
        # 자격증 목록에 대해 집합커버할 수 있는 조합을 집합커버 알고리즘으로 자격증 목록에서 가져온다.
        while len(candidate_cert) > 0: # 커버 안 된 원소가 있는 동안
            # 가장 많은 원소를 커버하는 집합 인덱스 찾기
            max_cover_set = certificate_list.index(max(certificate_list, key=lambda x: len(candidate_cert & x)))
            print(certificate_list[max_cover_set]) # n번 요소의 원소들을 출력
            candidate_cert -= certificate_list[max_cover_set] # 찾은 집합 원소 제거
            set_cover.append(max_cover_set)
            cert_candidate += certificate_list[max_cover_set]
            certificate_list[max_cover_set] = {-1}         # dummy 집합으로 교체
        print('입력하신 직업들에 대한 추천 자격증 목록입니다.')
        for i in cert_candidate:
            print(i)
        
# 자격증으로 직업 추천받기: 퀵 정렬 알고리즘
elif userinput == 2:
    usercert = input('원하시는 자격증을 입력하세요: ').split() # 사용자로부터 자격증 입력 받기
    joblist_temp = [] # 자격증별 직업 넣은 배열 만들기
    for cert in certificates:
        for i in usercert:
            if (i == cert.name): # 반복문으로 job의 구성요소에 자격증을 가지는 게 있는지 확인
                for j in cert.job:
                    for job in jobs:
                        if (j == job.name):
                            candidate_job += job.name # 해당 자격증의 직업들과 연봉을 배열로 저장
                            candidate_job_salary.append(job.salary)
    # 퀵 정렬
    a = candidate_job_salary
    qsort(a, 0, len(a)-1)
    candidate_job_salary = a
    candidate_job_salary.reverse()
    candidate_job = []
    for i in candidate_job_salary:
        for j in jobs:
            if (j.salary == i):
                candidate_job.append(j.name)    
    print('입력하신 자격증에 대한 추천 직업과 임금을 임금 순으로 보여드립니다.')
    for i in range(0, len(candidate_job)):
        print('직업: {0}, 임금: {1}'.format(candidate_job[i], candidate_job_salary[i]))
else:
    print('입력이 잘못되었습니다.')