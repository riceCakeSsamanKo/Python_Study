# isinstance(검사할 객체,타입)은 해당 객체가 해당 타입이라면 True, 아니라면 False 반환한다.

def check_instance_type(a):
    if isinstance(a,int):
        print(f"{a} is instance of int")
    elif isinstance(a,float):
        print(f"{a} is instance of float")
    elif isinstance(a,bool):
        print(f"{a} is instance of bool")
    elif isinstance(a,list):
        print(f"{a} is instance of list")
    elif isinstance(a,tuple):
        print(f"{a} is instance of tuple")
    elif isinstance(a,set):
        print(f"{a} is instance of set")
    elif isinstance(a,dict):
        print(f"{a} is instance of dict")
    elif isinstance(a,str):
        print(f"{a} is instance of str")

check_instance_type([1,2,3,4,5])
check_instance_type((1,2,3))
check_instance_type(1.2)
check_instance_type("asdf")