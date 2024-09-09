class Solution():
    '''
        Brute Force (pseudo code)
        - setup object
        - loop through chars, adding keys and incrementing values of duplicate keys
        - convert to string, then return length
    '''
    def compress(self, chars: list[str]) -> int:
        dictionary = {}
        for char in chars:
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
        
        arr = []
        for key, value in dictionary.items():
            arr.append(key)
            if value > 1:
                arr.extend(str(value))
        chars = arr
        return len(arr)
    
    '''
        Requirement: space O(1)
        - setup variable to hold char, index, count
        - first pass, when a new char is found, switch to new char, else convert str to one
    '''
    def compress_space(self, chars: list[str]) -> int:
        write_index = 0  # Where to write the compressed result
        read_index = 0  # Pointer to read through the input characters
        
        while read_index < len(chars):
            current_char = chars[read_index]  # Character being processed
            count = 0  # Count occurrences of the current character
            
            # Count the number of consecutive occurrences of current_char
            while read_index < len(chars) and chars[read_index] == current_char:
                read_index += 1
                count += 1
            
            # Write the character to the compression position
            chars[write_index] = current_char
            write_index += 1
            
            # If the count is greater than 1, write the count as individual digits
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1

        chars = chars[0:write_index]
        return write_index

if __name__ == "__main__":
    test = Solution()
    # print(test.compress(["a", "a", "b", "b", "c", "c", "c"]))
    # print(test.compress(["a"]))
    # print(test.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
    print(test.compress_space(["a", "a", "b", "b", "c", "c", "c"]))
    print(test.compress_space(["a"]))
    print(test.compress_space(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))

    # What I learned
    # - if you have to change a list when it is in loop, try not to change its length, keep track of the changes using a var