class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize the result variable
        res = 0
        
        # Define the values of Roman numerals
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Loop through the Roman numeral string except the last character
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                # If the current value is smaller than the next one, subtract it
                res -= roman[s[i]]
            else:
                # Otherwise, add the current value
                res += roman[s[i]]
        
        # Add the last character's value (since it's never compared in the loop)
        res += roman[s[-1]]
        
        return res
        