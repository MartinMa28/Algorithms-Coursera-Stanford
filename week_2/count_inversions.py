class Solution:
    @classmethod
    def merge_and_count_split_inversions(cls, left: list, right: list) -> (list, int):
        length = len(left) + len(right)
        merged = []
        i = 0
        j = 0
        inversions = 0
        for k in range(length):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
                if i == len(left):
                    merged.extend(right[j:])
                    return merged, inversions
            else:
                merged.append(right[j])
                j += 1
                inversions += len(left) - i
                if j == len(right):
                    merged.extend(left[i:])
                    return merged, inversions
        
    def sort_and_count_inversions(self, xs: list) -> (list, int):
        mid_index = len(xs) // 2
        if mid_index == 0:
            # only has one element in the list, already sorted
            return xs, 0
        
        sorted_left, n_left = self.sort_and_count_inversions(xs[:mid_index])
        sorted_right, n_right = self.sort_and_count_inversions(xs[mid_index:])
        sorted_xs, n_split = Solution.merge_and_count_split_inversions(sorted_left, sorted_right)

        return sorted_xs, n_left + n_right + n_split

if __name__ == "__main__":
    solu = Solution()
    test = [6, 5, 4, 3, 2, 1]
    sorted_test, n = solu.sort_and_count_inversions(test)
    print('sorted list: {}, num of inversions: {}'.format(sorted_test, n))