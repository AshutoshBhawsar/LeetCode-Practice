class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        def backtrack(combination, remaining_digits):
            if not remaining_digits:
                result.append(combination)
                return

            current_digit = remaining_digits[0]
            letters = digit_to_letters[current_digit]

            for letter in letters:
                backtrack(combination + letter, remaining_digits[1:])

        result = []
        backtrack('', digits)
        return result

