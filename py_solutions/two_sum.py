def get_two_sum(array, target):
    hashmap = {}
    for i, num in enumerate(array):
        comp = target - num

        if comp in hashmap:
            return [hashmap[comp], i]
        hashmap[num] = i
    return None


if __name__ == "__main__":
    arr = [2, 11, 1, 8, 9]
    print(get_two_sum(arr, 9))
