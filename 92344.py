def solution(board, skill):
    n, m = len(board), len(board[0])
    psum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for t, r1, c1, r2, c2, degree in skill:
        value = -degree if t == 1 else degree
        psum[r1][c1] += value
        psum[r1][c2 + 1] -= value
        psum[r2 + 1][c1] -= value
        psum[r2 + 1][c2 + 1] += value
    answer = 0
    
    # 가로축 계산
    for i in range(n + 1):
        for j in range(1, m + 1):
            psum[i][j] += psum[i][j - 1]
            
    # 세로축 계산
    for j in range(m + 1):
        for i in range(1, n + 1):
            psum[i][j] += psum[i - 1][j]
            
    for i in range(n):
        for j in range(m):
            total = board[i][j] + psum[i][j]
            if total > 0: answer += 1
    return answer