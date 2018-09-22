import numpy
class Solutiom(object):
    def roman(self, s):
        rome = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        maxsize=1
        for i in range (len(s)-1,-1,-1):
            if rome[s[i]]>=maxsize:
                sum=sum+rome[s[i]]
                maxsize=rome[s[i]]
            else:
                sum=sum-rome[s[i]]
        return sum
a=Solutiom.roman(Solutiom,"XL")
print(a)

