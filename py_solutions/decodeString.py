class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        stack = []
        number = ""
        string = ""
        for ch in s:
            if ch.isdigit():
                number += ch
            elif ch == "[":
                if string:
                    stack.append(string)
                    string = ""
                stack.append(number)
                print("number before resetting: ", number)
                number = ""
            elif ch == ']':
                print(stack)
                num = stack.pop()
                print(f"{string} * {num}")
                stack.append(string*int(num))
                print("string after resetting: ", string)
                string = ""
            elif ch.isalpha():
                string += ch
        print(stack)
        return "".join(stack)


if __name__ == '__main__':
    s = Solution()
    print("3[a] ==> ", s.decodeString("3[a]"))
    print("3[a]2[bc] ==> ", s.decodeString("3[a]2[bc]"))
    print("3[a2[c]] ==> ", s.decodeString("3[a2[c]]"))