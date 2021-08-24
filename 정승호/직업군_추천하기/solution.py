def solution(table, languages, preference):
    answer = []
    new_table = sorted([list(t.split()) for t in table], key=lambda x : x[0])
    preference_table = {n : new_table[n][0] for n in range(len(new_table))}
    
    for i in range(len(preference_table)):
        total = 0
        for lang, pref in zip(languages, preference):
            if lang in new_table[i]:
                total += (6 - new_table[i].index(lang)) * pref
        answer.append(total)
    return preference_table[answer.index(max(answer))]

