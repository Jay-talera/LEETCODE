class Solution:
    def minDeletions(self, s: str) -> int:
        
        frequency = [0] * 26
        for char in s:
            frequency[ord(char) - ord('a')] += 1
        
        delete_count = 0
        seen_frequencies = set()
        for i in range(26):
            while frequency[i] and frequency[i] in seen_frequencies:
                frequency[i] -= 1
                delete_count += 1
            
            seen_frequencies.add(frequency[i])
        
        return delete_count