class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a = s[0:len(s)//2]
        b = s[len(s)//2:len(s) + 1]
        c = list(a)
        d = list(b)
        count_1 = 0
        for i in c:
            if i in vowels:
                count_1+=1
        count_2 = 0
        for i in d:
            if i in vowels:
                count_2 +=1
        print(count_1)
        print(count_2)
        return count_1 == count_2
            


        
