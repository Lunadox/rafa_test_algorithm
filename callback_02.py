# 해보기
# callback_02.py 흐름이해

# 더 해 보기
# 상대 컴퓨터에서 callback_01 완성
# callback_01 1.function 분리
#             2. callback func만들기

def fun_callback(input, extend_input):
    print('fun_callback sum : ',input)
    print('fun_callback extend_input : ',extend_input)
    return


def fun_call(one, two, f_callback, three):
    result = one  + two
    f_callback(result, three) 
    return


first = 10 
second = 20
third = 30
fun_call(first, second, fun_callback,third)
