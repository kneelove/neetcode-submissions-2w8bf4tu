class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str=""
        for each in strs:
            encoded_str+=str(len(each))+"^"+each
        print(encoded_str)
        return encoded_str


    def decode(self, s: str) -> List[str]:
        counter=0
        result=[]
        length=""
        while counter<len(s):
            if(s[counter])!="^":
                length+=s[counter]
                counter+=1
            if(s[counter])=="^":
                result.append(s[counter+1:(counter+1+int(length))])
                counter=counter+1+int(length)
                length=""

        return result

           

                
           
        return result
        
