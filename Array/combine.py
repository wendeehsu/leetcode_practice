from typing import List

def combine(n: int, k: int) -> List[List[int]]:
    def bfs(ans):
        final = []
        for i in range(len(ans)):
            for j in range(ans[i][-1]+1, n+1):
                final += [ans[i] + [j]]
        return final

    ans = []
    while k > 0:
        print("k =", k)
        if len(ans) == 0:
            for i in range(1,n+1):
                ans += [[i]]
        else:
            ans = bfs(ans)
        k -= 1
        print("ans ->", ans)
    return ans

n = 5
k = 3
print(combine(n,k))