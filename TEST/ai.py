# # mysplit() 구현하기
# # 사용자 정의 함수인 def을 활용해서 split()이 작동하는 것과 같은 원리로 작동하는 함수를 구현하라
# # split()은 문자열을 괄호 안에 있는 값을 기준으로 분리해서 리스트에 저장한다.
# # 괄호 안이 비어있을 경우 공백을 기준으로 분리해서 리스트에 저장한다.
# print("ABCDVEFGH".split()) # ['ABCDVEFGH']
# print("ABCDVEFGH".split('V')) # ['ABCD','EFGH']

# 문자열과 기준을 입력받는다.
def mysplit(str,V=' '):
# 문자열 안에 기준이 있다면 기준을 기준으로 좌측 우측을 문자열 타입으로 리스트에 저장한다.
    List = []
    strings = ''
# 기준을 기준으로 좌측 우측을 리스트에 추가한다.
# 문자열을 하나씩 보는데, 기준을 보게 되면 왼쪽 보고 난 뒤는 오른쪽이다.
    for C in str:
        if C == V:
            List.append(strings)
            strings=''
        else:
            strings += C
    List.append(strings)
    return List

# split같은 경우는 '111'을 한 문자로 보고 있지만, 내 코드는 '111'을 각각 다른 문자로 보고 있기 때문에
# 이러한 문제가 발생하는 것이라 생각한다.
# 그렇다면 이 문제를 해결하기 위해선, 기준을 한 문자로 보는 방식으로 처리해야 한다.
print(mysplit('AB111DE',))
print('AB111DE'.split())
