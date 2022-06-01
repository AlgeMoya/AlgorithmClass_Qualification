'''
print("-------직업조회-------")
print("0. 정보보안전문가")
print("1. 디지털포렌식수사관")
print("2. 자산운용가")
print("3. 약사")
print("4. 건축석공")
print("5. 제과제빵원")
'''

def print_menu():
    print("---------------------")
    print("1. 직업 번호 검색")
    print("2. 직업 정보 조회")
    print("3. 직업/자격증 추천")
    print("4. 나가기")

    inputed_number = int(input("번호를 입력하세요: "))

    if inputed_number == 1:
        jobs = ["정보보안전문가", "디지털포렌식수사관", "자산운용가", "약사", "건축석공", "제과제빵원"]

         # 데이터 검색 및 검색위치 반환
        def is_on_list_jobs(a, b):
             return b in a
        def index_of_list(a, b):
             return a.index(b)

        x = input("검색할 직업명을 입력하시오 : ")

        if is_on_list_jobs(jobs, x) == True:
             print(f"{x}의 직업 번호: ", index_of_list(jobs, x),)
        else:
             print(f"{x}의 직업 정보가 없습니다.")

    elif inputed_number == 2:
        def print_jobs():
            print("---------------------")
            print("0. 정보보안전문가")
            print("1. 디지털포렌식수사관")
            print("2. 자산운용가")
            print("3. 약사")
            print("4. 건축석공")
            print("5. 제과제빵원")
            print("6. 나가기")
            print("---------------------")

            inputed_number = int(input("번호를 입력하세요: "))

            if inputed_number == 0:
                def print_job():
                    print("---------------------")
                    print("1. 직업정보")
                    print("2. 준비방법")
                    print("3. 합격 후기")
                    print("4. 나가기")

                    inputed_number = int(input("번호를 입력하세요: "))

                    if inputed_number == 1:
                        print("정보보안전문가는 정보 보안 정책을 수립하고, 시스템에 대한 접근 및 운영을 통제하며, 침입자가 발생했을 때에는 신속히 탐지대응해 정보자신을 보호한다.")
                        print("연봉수준 > 3803만원")
                    if inputed_number == 2:
                        print("정규 교육과정 - 정보보호전문가가 되기 위해서는 전문 대학 및 대학교에서 컴퓨터공학과, 정보통신공학과, 전자공학과, 전산학과, 정보처리학과, 경영정보학과, 회계학과, 법학과 등을 졸업하면 유리하다.")
                        print("직업 훈련 - 한국정보보호센터와 정보통신교육원등에서 정보보호전문가가 되기 위한 직업훈련교육을 받을 수 있다.")
                    if inputed_number == 3:
                        print("정지영 2020년7월23일 CISSP 어려웠다")
                        print("강석규 2020년8월6일 정보보안산업기사 대체적 쉬움")
                        print("---------------------")
                        inputed_number = int(input("새로운 합격후기를 입력하시려면 1을, 아니라면 아무 숫자나 입력하세요: "))

                        if inputed_number == 1:
                            class Contact:
                                def __init__(self, name, date, Certificate, reviews):
                                    self.name = name
                                    self.date = date
                                    self.Certificate = Certificate
                                    self.reviews = reviews

                                def print_info(self):
                                    print("Name: ", self.name)
                                    print("date: ", self.date)
                                    print("Certificate: ", self.Certificate)
                                    print("reviews: ", self.reviews)

                            def set_contact():
                                print("---------------------")
                                name = input("이름: ")
                                date = input("취득날짜: ")
                                Certificate = input("취득자격증: ")
                                reviews = input("간단한 시험 후기를 남겨주세요.: ")
                                print("---------------------")
                                print(name, date, Certificate, reviews)

                            def run():
                                set_contact()

                            if __name__ == "__main__":
                                run()

                    if inputed_number == 4:
                        exit()
                    else:
                        print("---------------------")

                while True:
                    print_job()

            elif inputed_number == 6:
                exit()
            else:
                print("다시 입력하세요.")

        while True:
            print_jobs()

    elif inputed_number == 3:
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

        certificates = [cert_SIS, cert_CEH, cert_CISA, cert_CISSP, cert_assetmanager, cert_pharmacist, cert_mason, cert_baker1, cert_baker2]
        certificate_list = []
        for i in jobs:
            certificate_list.append(set(i.certificate))

        candidate_job = []

        candidate_job_salary = []

        candidate_cert = set()
        cert_candidate = []
        cert_candidate_separated = []
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

        userinput = input('(1)직업으로 자격증 추천받기, (2)자격증으로 직업 추천받기 \n번호를 선택해주세요: ')
        userinput = int(userinput)

        if userinput == 1:
            userjob = input('원하시는 직업을 입력하세요: ').split()

            if len(userjob) == 1:
                for job in jobs:
                    if (userjob[0] == job.name):

                        for i in job.certificate:
                            candidate_cert = job.certificate
                        print(candidate_cert)
                        if candidate_cert:
                            print('입력하신 직업에 대한 추천 자격증 목록입니다.')
                            for i in candidate_cert:
                                print(i)
            else:
                for joblist in userjob:
                    for job in jobs:
                        if (joblist == job.name):
                            for j in job.certificate:      

                                for x in job.certificate:
                                    candidate_cert.add(x)
                '''
                print(type(candidate_cert))
                print(candidate_cert) # U
                print(type(certificate_list))
                print(certificate_list) # S
                '''

                while len(candidate_cert) > 0: 

                    max_cover_set = certificate_list.index(max(certificate_list, key=lambda x: len(candidate_cert & x)))

                    print(certificate_list[max_cover_set]) # n번 요소의 원소들을 출력
                    candidate_cert -= certificate_list[max_cover_set] # 찾은 집합 원소 제거
                    set_cover.append(max_cover_set)
                    cert_candidate_separated.append(certificate_list[max_cover_set])
                    cert_candidate += certificate_list[max_cover_set]
                    certificate_list[max_cover_set] = {-1}         # dummy 집합으로 교체

                print('입력하신 직업들에 대한 추천 자격증 목록입니다.')
                for i in cert_candidate:
                    print(i)

        elif userinput == 2:

            usercert = input('원하시는 자격증을 입력하세요: ').split()
    
            joblist_temp = []
            for cert in certificates:
                for i in usercert:

                    if (i == cert.name):

                        for j in cert.job:
                            for job in jobs:
                                if (j == job.name):                          
                                    candidate_job += job.name
                                    candidate_job_salary.append(job.salary)

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

    elif inputed_number == 4:
         exit()
    else:
        print("다시 입력하세요.")
                                                             

while True:
    print_menu()
