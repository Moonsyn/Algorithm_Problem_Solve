def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    
    id_index = {}
    report_by = {}
    
    for i in range(len(id_list)):
        id = id_list[i]
        id_index[id] = i
        
    for r in report:
        reporter, reported = map(str, r.split(" "))
        if reported not in report_by:
            report_by[reported] = set([reporter])
        else:
            report_by[reported].add(reporter)
    
    for reported in report_by:
        if len(report_by[reported]) < k:
            continue
        for key in report_by[reported]:
            answer[id_index[key]] += 1
    
    return answer