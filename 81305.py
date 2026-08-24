import sys
sys.setrecursionlimit(100000)

def solution(k, num, links):
    n = len(num)
    has_parent = [False for _ in range(n)]
    for left, right in links:
        if left != -1:
            has_parent[left] = True
        if right != -1:
            has_parent[right] = True

    root = 0
    for i in range(n):
        if not has_parent[i]:
            root = i
            break

    left, right = max(num), sum(num)
    def isAvail(limit):
        cnt = 0
        def dfs(node):
            nonlocal cnt
            children = []
            for child in links[node]:
                if child != -1:
                    children.append(dfs(child))

            curr = num[node]
            if not children:
                return curr

            elif len(children) == 1:
                child = children[0]
                if curr + child <= limit:
                    return curr + child
                else:
                    cnt += 1
                    return curr

            else:
                a, b = sorted(children)
                if curr + a + b <= limit:
                    return curr + a + b
                elif curr + a <= limit:
                    cnt += 1
                    return curr + a
                else:
                    cnt += 2
                    return curr
        dfs(root)
        return cnt + 1 <= k
    while left < right:
        mid = (left + right) // 2
        if isAvail(mid):
            right = mid
        else:
            left = mid + 1
    return left