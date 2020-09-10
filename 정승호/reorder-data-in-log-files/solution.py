class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        log_letter = []
        log_digit = []
        for log in logs:
            if log.split(" ")[1].isdigit():
                log_digit.append(log)
            else :
                log_letter.append(log)
        log_letter.sort(key = lambda x : (x.split()[1:], x.split()[0]))
                
        answer = log_letter + log_digit
        
        return answer
