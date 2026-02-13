class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        available_chars = Counter(chars)
        total_length = 0
        
        for word in words:
            word_count = Counter(word)
            
            is_good = True
            for char, count in word_count.items():
                if available_chars[char] < count:
                    is_good = False
                    break
            
            if is_good:
                total_length += len(word)
                
        return total_length
