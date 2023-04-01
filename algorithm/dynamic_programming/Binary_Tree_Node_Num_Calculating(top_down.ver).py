def count_trees(n):
    # 이미 계산한 값은 memo에 저장하여 중복 계산을 방지합니다.
    memo = [0] * (n + 1)
    memo[0] = 1

    return count_trees_helper(n, memo)


def count_trees_helper(n, memo):
    if memo[n] > 0:
        # 이미 계산한 값이라면 그대로 반환합니다.
        return memo[n]

    # dp[i]를 계산하기 위해 이진트리의 루트 노드를 선택하는 모든 경우에 대해 왼쪽 서브트리와 오른쪽 서브트리의 이진트리 개수를 곱한 값을 더해줍니다.
    for i in range(n):
        memo[n] += count_trees_helper(i, memo) * count_trees_helper(n - i - 1, memo)

    return memo[n]

print(count_trees(23))