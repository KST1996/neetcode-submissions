class Solution:

    # def encode_word(self, word: str) -> str:
    #     return "a".join([str(ord(ch)) for ch in word])
        
    def encode(self, strs: List[str]) -> str:
        # if not strs:
        #     return "E"
        # return "z".join([self.encode_word(word) for word in strs])
        encoded = ""
        for word in strs:
            encoded+=str(len(word))+"_"+word
        return encoded

    # def decode_word(self, word: str) -> str:
    #     if not word:
    #         return ""
    #     return "".join(chr(int(c)) for c in word.split("a"))

    def decode(self, s: str) -> List[str]:
        # if s=="E":
        #     return []
        # return [self.decode_word(word) for word in s.split("z")]
        if not s:
            return []
        ans=[]
        i=0
        # print(s)
        start=0
        while i<len(s):
            while s[i]!='_':
                i+=1
            length=int(s[start:i])
            if length==0:
                ans.append("")
            else:
                ans.append(s[i+1:i+length+1])
            i+=length+1
            start=i
        return ans





