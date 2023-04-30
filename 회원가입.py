import re
import datetime

def create_membership():
    now = datetime.datetime.now()
    stnr_date = now.strftime('%Y%m%d')
    
    users = []
    
    while True:
        user = {}    
        breaker=False
        while True:
            if breaker == True:
                break
            username = input('이름: ')
            if len(username) >=2 and len(username)<=4:
                sum=0
                for i in range(len(username)):                
                    if ord(username[i]) >= 44032 and ord(username[i]) <= 55203:
                        sum+=1 
                    else:
                        print('이름은 한글로 입력해주세요.')
                        break
                if sum == len(username):
                    breaker = True   
                else:
                    pass          
            else:
                print('이름의 길이가 잘못되었습니다.')

        while True:
            password = input('비밀번호: ')
            if password[0].isupper():
                if len(password) >= 8:
                    if '!' in password or '@' in password or '#' in password or '$' in password:
                        break
                    else:
                        print('특수문자 (!, @, #, $) 중 1가지를 포함시켜 주세요.')
                else:
                    print('총 글자 수는 8글자 이상이어야 합니다.')
            else:
                print('첫 문자는 영문 대문자이어야 합니다.')  

        while True:              
            password_confirm = input('비밀번호 확인: ')
            if password == password_confirm:
                break
            else:
                print('비밀번호가 일치하지 않습니다.')
        
        while True:
            email = input("이메일: ")
            regex_email = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[.]?\w{2,3}$"
            valid = re.search(regex_email, email)
            # pattern = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
            # match = re.match(pattern, email)
        
            if email.endswith(".com") == True and '@' in email:
                if valid:
                    break
                else:
                    print('@를 제외한 특수문자는 입력할 수 없습니다.')       
            else:
                print("이메일의 형식이 올바르지 않습니다.")
                    

        user['username'] = username
        user['password'] = password
        user['email'] = email
        user['stnr_date'] = stnr_date
        users.append(user)
        print(users)

        print('회원가입을 추가로 진행하시겠습니까?\n네:아무버튼  아니오:n')
        register_another_input = input('>> ')
        register_another_input = register_another_input.lower()
        if register_another_input == 'n':
            break
        else:
            pass

    return users

def load_to_txt(user_list):
    f = open('memberdb.txt', 'w', encoding='UTF-8')
    for i in range(len(user_list)):
        result=', '.join(s for s in list(user_list[i].values()))
        f.write(f'{result}\n')
    f.close()
    
def run():
    user_list = create_membership()
    load_to_txt(user_list)
    
run()