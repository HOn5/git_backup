##
#   remove minimum value
#

def removeMin(values):
    minValue = values[0]

    #최소값 찾아서 변수 재정의 
    for index in range(1, len(values)):
        if values[index] < minValue:
            minValue = values[index]

    #저장된 변수에 대응하는 인덱스 찾아서 리스트 맨 뒤로 보낸 뒤 슬라이싱
    for index in range(len(values)):
        if minValue == values[index]:
            LASTINDEX = len(values) - 1
            values[index], values[LASTINDEX] = values[LASTINDEX], values[index]
            
            result = values[:LASTINDEX]
            break

    return result


listValues = list(map(int, input("Please, enter numbers: ").split()))
resultList = removeMin(listValues)
print(resultList)
