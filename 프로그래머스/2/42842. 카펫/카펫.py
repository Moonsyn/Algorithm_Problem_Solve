def solution(brown, yellow):
    answer = []
    for w in range((brown+4)//4, (brown+4)//2):
        h = (brown+4)//2 - w
        if w*h - brown == yellow:
            if w >= h:
                answer = [w,h]
            else:
                answer = [h,w]
            break
    
    return answer