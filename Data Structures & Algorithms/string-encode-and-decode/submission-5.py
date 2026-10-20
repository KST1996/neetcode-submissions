class Solution:

    def encode_word(self, word: str) -> str:
        return "a".join([str(ord(ch)) for ch in word])
        
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "E"
        return "z".join([self.encode_word(word) for word in strs])

    def decode_word(self, word: str) -> str:
        if not word:
            return ""
        return "".join(chr(int(c)) for c in word.split("a"))

    def decode(self, s: str) -> List[str]:
        if s=="E":
            return []
        return [self.decode_word(word) for word in s.split("z")]
