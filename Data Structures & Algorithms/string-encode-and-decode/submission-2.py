class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        string_sizes = []
        
        for s in strs:
            string_sizes.append(str(len(s)))
            string_sizes.append("&")
            string_sizes.append(s)

        return "".join(string_sizes)
        

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "&":
                j += 1
            
            num_of_ltrs = int(s[i : j])

            res.append(s[j + 1 : j + 1 + num_of_ltrs])
            i = j + 1 + num_of_ltrs
        
        return res