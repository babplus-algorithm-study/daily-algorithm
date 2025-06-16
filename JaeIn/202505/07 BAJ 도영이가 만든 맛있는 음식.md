```python
n = int(input())
ingre = [list(map(int , input().split())) for _ in range(n)]
answer = float('inf')


def dfs(idx , sin, jan ,use):
    global answer

    if idx == n:
        if use == 0:
            return
        diff = abs(sin - jan)
        answer = min(diff , answer)
        return

    # 재료를 사용할 때
    dfs(idx + 1, sin * ingre[idx][0] , jan + ingre[idx][1], use + 1)
    # 사용 인 힐 때
    dfs(idx + 1 , sin , jan , use)



dfs(0 ,1 ,0 , 0)
print(answer)

```

```javascript
let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().trim().split("\n");
let n = Number(input[0]);
let ingre = [];
for (let i = 1; i <= n; i++) {
  ingre.push(input[i].split(" ").map(Number));
}

let answer = 1e9;

function dfs(idx, sin, jan, use) {
  if (idx == n) {
    if (use == 0) return;

    let diff = Math.abs(sin - jan);
    answer = Math.min(answer, diff);
    return;
  }

  dfs(idx + 1, sin * ingre[idx][0], jan + ingre[idx][1], use + 1);
  dfs(idx + 1, sin, jan, use);
}

dfs(0, 1, 0, 0);

console.log(answer);
```
