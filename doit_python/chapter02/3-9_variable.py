# 변수
a = 1
b = 'python'
c = [1, 2, 3]

print(id(a))
"""
    a = [1, 2, 3] 값을 가지는 리스트 자료형(객체)은 자동으로 메모리에 생성되고
    변수 a 는 [1, 2, 3] 리스트가 저장된
    '메모리의 주소' 를 가리키게 된다. 
"""

# 리스트를 복사할 때
a = [1, 2, 3]
b = a
print(id(b)) # [1, 2, 3] 리스트를 참조하는 변수가 2개가 되었다. a가 가리키는 대상 = b가 가리키는 대상이 동일하다

# is -> 동일한 객체를 가리키고 있는지에 대해서 판단하는 명령어
print(a is b)

# 따라서 a 요소의 값을 바꾸면 b 요소의 값도 변경된다
a[1] = 4
print(a)
print(b)
