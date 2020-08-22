def kthGrammar(n,k):
    if n==1:
        return 0
    if (k%2==0):
        return 1 if kthGrammar(n-1,k/2)==0 else 0
    else:
        return 0 if kthGrammar(n-1,(k+1)/2)==0 else 1

print(kthGrammar(1,1))
print(kthGrammar(2,1))
print(kthGrammar(2,2))
print(kthGrammar(4,5))


