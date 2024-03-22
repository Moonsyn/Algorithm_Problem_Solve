def solution(jobs):
    answer = 0
    length = len(jobs)
    
    jobs.sort(key=lambda x: x[0])
    
    waits = []
    operating = []
    time = jobs[0][0]
    
    while len(waits) > 0 or len(jobs) > 0:
        for wait in waits:
            wait[2] += 1
            
        while jobs:
            if jobs[0][0] <= time:
                job = jobs.pop(0)
                job.append(job[1])  # [0,1,1]
                waits.append(job)
            else:
                break
                
        if len(operating) > 0:
            operating[1] -= 1
        
        if (len(operating) == 0 or operating[1] <= 0) and len(waits) > 0:
            waits.sort(key=lambda x:x[1])
            operating = waits.pop(0)
            answer += operating[2]
        
        time += 1
    
    return answer // length