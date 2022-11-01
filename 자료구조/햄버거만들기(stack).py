def solution(ingredient):
    answer = 0 
    ingredients = []
    for i in ingredient:
        ingredients.append(i)
        if ingredients[-4:] == [1,2,3,1]:
            ingredients.pop()
            ingredients.pop()
            ingredients.pop()
            ingredients.pop()
            answer +=1
        
    return answer
