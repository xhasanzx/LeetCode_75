def palindrome(str):
    left, right = 0, len(str) - 1
    lower_str = str.lower()

    while left <= right:
        if not lower_str[left].isalnum():
            left = left + 1
            continue
        if not lower_str[right].isalnum():
            right = right - 1
            continue

        if lower_str[left] == lower_str[right]:
            left += 1
            right -= 1
        else:
            return None

    return True


if __name__ == "__main__":
    string = "a man ,a plan, a canal: panama"
    print(palindrome(string))
