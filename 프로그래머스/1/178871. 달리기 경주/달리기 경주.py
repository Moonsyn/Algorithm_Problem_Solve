from collections import Counter

def solution(players, callings):
    answer = [0 for _ in range(len(players))]
    ranking = {}
    for i in range(len(players)):
        ranking[players[i]] = i
    
    for call in callings:
        called_rank = ranking[call]
        ranking[call] -= 1
        ranking[players[ranking[call]]] += 1
        
        players[called_rank], players[called_rank-1] = players[called_rank-1], players[called_rank]
    
    for key in ranking.keys():
        answer[ranking[key]] = key
    
    return answer