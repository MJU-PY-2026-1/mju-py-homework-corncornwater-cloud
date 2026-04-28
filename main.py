# 파일이름 :main.py
# 작 성 자 :이재현
stuff_registry = [[3,"iron_ore",60],[1,"oak_plank",30],[2,"air",0]]; #[ 분류코드 ,이름 , 고유가치 ] 
"""
stuff_registry안에 있는 리스트의 첫번째 인덱스는 번호이며 무조건 stuff_registry의 인덱스와 일치야한다.
예를들어. stuff_registry[[0,"철광석",8],....]안 리스트 첫번째 요소 0은 stuff_registry안의 리스트의 인덱스와 일치한다.
"""
selected_code = -1;
name_same = False
# stuff_sum = 0;
# allstuff_sum = 0;
def registry_keycheck(): #아직 손봐야한다....
    for num in range( len(stuff_registry)): 
        if( num != stuff_registry[num][0]):
            print("기존 분류코드 값에 오류가 발생했습니다. 분류코드를 다시 부여합니다") #완성 후 문구 제거
            for num1 in range( len(stuff_registry)):
                stuff_registry[num1][0] = num1;
    return len(stuff_registry)
    
def item_calculate():
    print("a")

def addlist(name, value):
    stuff_registry.append([registry_keycheck(),name,value])
    return 0

def menu(answer):
    if( answer == "BS"):   
        print("원하시는 기능을 선택하려면 []안 글자를 입력하세요")
        print("-> [B] 구매")
        print("-> [S] 판매")
        BS_choice = input("선택한 메뉴 :")
    elif( answer == "L"):
        registry_keycheck()
        print("-"*40)
        print("| 분류코드 | 이름 | 고유 가치(은) |")
        for num3 in range(len(stuff_registry)):
            print(f'|{stuff_registry[num3][0]}번 | {stuff_registry[num3][1]} | *{stuff_registry[num3][2]} 은*')
        print("-"*40)
        print("")
        print("현재 리스트를 추가/삭제 하려면 []안 글자를 입력하세요")
        print("-> [A] 리스트 추가")
        print("-> [D] 리스트 삭제")
        print("-> [0] 메뉴로 돌아가기")
        L_choice = input("선택한 메뉴 :")
        if ( L_choice == "A" ):
            name_same = False
            print("추가할 물건/재료의 이름을 입력해주세요")
            addlist_name = input("이름 : ")
            for num2 in range(len(stuff_registry)):
                if( addlist_name == stuff_registry[num2][1]):
                    print("")
                    print("{이미 같은 이름의 물건/재료가 있습니다! 다시 시도해주세요.}") #같은 물건이 있다면 바로 메뉴로 가야함
                    name_same = True
                    print("")
            if( name_same != True):
                print("재료의 고유 가치를 적어주세요 (만약 물건이라면 X 입력)")
                addlist_value = input("고유 가치 : ")
                if( addlist_value == "X" or addlist_value == "x"): 
                    addlist(addlist_name, "물건" )
                else:
                    addlist(addlist_name, addlist_value)

        elif ( L_choice == "D" ):
            print("삭제할 물건/재료의 분류코드를 입력해주세요")
            stuff_registry.pop(int(input("분류코드 :")))
            registry_keycheck()
        elif ( L_choice == "0" ):
            print("메뉴로 돌아갑니다...")
            return -2

    elif( answer == "END"):
        print("프로그램을 종료합니다")
        return -1
    else:
        print("")
        print("{잘못된 입력입니다!}")
        print("")
        return -2

while(True):
    print("-"*40)
    print("물건가치 은 환전 시스템 2.0")
    print("원하시는 기능을 선택하려면 []안 글자를 입력하세요")
    print("-> [BS] 구매/판매 ")
    print("-> [L] 리스트 살펴보기")
    print("-> [END] 프로그램 종료")
    print("-"*40)
    menu_choice = menu(input("선택한 메뉴 : "))
    if(menu_choice == -1):
        break
    elif(menu_choice == -2):
        continue
