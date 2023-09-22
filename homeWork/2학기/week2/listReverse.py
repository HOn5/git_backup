##
#   normal list to reverse list
#

def reverseList(values):
    HALFINDEX = len(values) // 2

    #리스트 길이 절반만큼 for문 돌려서 자리 바꿔주기
    for index in range(HALFINDEX):
        values[index], values[-(index+1)] = values[-(index+1)], values[index]

    return values


listValues = list(map(int, input("Please, enter numbers: ").split()))

print(listValues)

result = reverseList(listValues)
print("="*15,"reverse list", "="*15)
print(result)