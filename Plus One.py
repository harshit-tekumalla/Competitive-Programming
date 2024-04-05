class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''if len(digits)>1:
            if digits[-1] == 9:
                digits[-2]+=1
                digits[-1] = 0
                return''' 
        number = ''
        for i in digits:
            number+=str(i)
        int_num = int(number)
        a = str(int_num + 1)
        #b=list(a)
        c=[]
        for i in list(a):
            k = int(i)
            c.append(k)
        return c
                
                
        
