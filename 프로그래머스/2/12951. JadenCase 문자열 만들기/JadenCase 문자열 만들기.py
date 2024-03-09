def JadenCase(sentence):
    words = sentence.split(" ")
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return " ".join(words)    

def solution(s):
    return JadenCase(s)