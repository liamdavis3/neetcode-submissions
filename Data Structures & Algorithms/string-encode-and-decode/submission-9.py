class Solution:

    def encode(self, strs: List[str]) -> str: 
        if not strs:
            return "blank"  
        encoded_string = "-".join(strs)
        print(encoded_string)
        return encoded_string
        
    def decode(self, s: str) -> List[str]:
        if s == "blank":
            return []
        decoded_strs = s.split("-")
        return decoded_strs
