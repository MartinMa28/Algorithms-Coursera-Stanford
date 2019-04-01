class Solution:
    @classmethod
    def merge(cls, left: list, right: list) -> list:
        if len(left) == 0:
            return right
        elif len(right) == 0:
            return left
        
        # note that slice is not bounding checked, so it's safe to use slice for a non-exist element
        # Therefore, I use [1:] to pick up the sub-array except for the first element, even if there is
        # only one element. By contrast, '[1]' will cause index out of range error.
        if left[0] < right[0]:
            return [left[0]] + Solution.merge(left[1:], right)
        else:
            return [right[0]] + Solution.merge(left, right[1:])

    @classmethod
    def merge_2(cls, left: list, right: list) -> list:
        if len(left) == 0:
            return right
        elif len(right) == 0:
            return left
        
        if left[0] < right[0]:
            temp = [left[0]]
            temp.extend(cls.merge_2(left[1:], right))
            return temp
        else:
            temp = [right[0]]
            temp.extend(cls.merge_2(left, right[1:]))
            return temp

    @classmethod
    def merge_non_iterative(cls, left: list, right: list) -> list:
        length = len(left) + len(right)
        output = list()
        i = 0
        j = 0
        for k in range(0, length):
            if left[i] < right[j]:
                output.append(left[i])
                i += 1
                if i == len(left):
                    output.extend(right[j:])
                    return output
            else:
                output.append(right[j])
                j += 1
                if j == len(right):
                    output.extend(left[i:])
                    return output
    
    
    def merge_sort(self, xs: list) -> list:
        mid_index = int(len(xs) / 2)
        if mid_index < 1:
            # only has one or zero number, it's already sorted, returns itself
            return xs
        else:
            # at least, has two numbers, invoke the merge sort function by recursion
            return Solution.merge_non_iterative(self.merge_sort(xs[:mid_index]), self.merge_sort(xs[mid_index:]))


if __name__ == "__main__":
    solu = Solution()
    test = [5, 3, 7, 9, 8, 6, 1, 2, 4, 0]
    sort = solu.merge_sort(test)
    print(sort)

