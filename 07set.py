#set 자료형은 중복이 제거됨
set_01 = 1,1,3,3,4,4,5,5,6,6
set_02 = 1,1,4,4,5,2,10,40,2,5,6
a_set = set(set_01)
b_set = set(set_02)
ab_set1 = a_set & b_set #& 조건문을 사용하여 교집합을 구할 수 있음
ab_set2 = a_set | b_set #& 조건문을 사용하여 합집합을 구할 수 있음

print(ab_set1 , ab_set2)