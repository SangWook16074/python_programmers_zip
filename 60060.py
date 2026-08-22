


def solution(words, queries):
    
    def lower_bound(array, target):
        left = 0
        right = len(array)

        while left < right:
            mid = (left + right) // 2

            if array[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left


    def upper_bound(array, target):
        left = 0
        right = len(array)

        while left < right:
            mid = (left + right) // 2

            if array[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return left


    def count(array, left_value, right_value):
        left_index = lower_bound(array, left_value)
        right_index = upper_bound(array, right_value)

        return right_index - left_index
    
    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]

    # 길이에 따라 분류
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    # 이진 탐색을 위해 정렬
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    answer = []

    for query in queries:
        if query[0] != '?':
            # fro?? → froaa ~ frozz
            left_value = query.replace('?', 'a')
            right_value = query.replace('?', 'z')

            result = count_by_range(
                array[len(query)],
                left_value,
                right_value,
            )

        else:
            # ????o → o????
            reversed_query = query[::-1]

            left_value = reversed_query.replace('?', 'a')
            right_value = reversed_query.replace('?', 'z')

            result = count(
                reversed_array[len(query)],
                left_value,
                right_value,
            )

        answer.append(result)

    return answer