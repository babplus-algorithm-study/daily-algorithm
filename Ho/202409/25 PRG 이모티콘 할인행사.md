```java
class Solution {
    static int size;
    static int[] percents = {10,20,30,40};
    static int[] curSales;
    static int[][] copyUsers;
    static int[] copyEmotis;
    static int[] ans = new int[2];

    public int[] solution(int[][] users, int[] emoticons) {
        int[] answer = {0,0};
        ans[0] = 0;
        ans[1] = 0;
        size = emoticons.length;
        curSales = new int[size];

        copyUsers = new int[users.length][2];

        for(int i = 0; i < users.length; i++) {
            copyUsers[i][0] = users[i][0];
            copyUsers[i][1] = users[i][1];
        }
        // 이모티콘 할인율은 10,20,30,40
        copyEmotis = new int[emoticons.length];
        for(int i = 0; i < size; i++) {
            copyEmotis[i] = emoticons[i];
        }

        backtracking(0);

        answer[0] = ans[0];
        answer[1] = ans[1];
        return answer;
    }

    public void backtracking(int depth) {
        if(depth == size) {
            calBuyPrice();
            return;
        }


        for(int i = 0; i < 4; i++ ) {
            curSales[depth] = percents[i];
            backtracking(depth + 1);
        }
    }

    public void calBuyPrice() {
        int kakaoPlusCnt = 0;
        int salePrice = 0;
        for(int i = 0; i < copyUsers.length; i++) {
            int sumPrice = 0;
            for(int j = 0; j < copyEmotis.length; j++) {
                if(canBuy(curSales[j], copyUsers[i][0])) {
                    int price = copyEmotis[j] * (100 - curSales[j]) / 100;
                    sumPrice += price;
                }
            }
            if(sumPrice >= copyUsers[i][1]) {
                // 카카오 플러스 가입해야하는 경우
                kakaoPlusCnt++;
                continue;
            }
            salePrice += sumPrice;
        }

        if(ans[0] < kakaoPlusCnt) {
            ans[0] = kakaoPlusCnt;
            ans[1] = salePrice;
        }

        if(ans[0] == kakaoPlusCnt && ans[1] < salePrice) {
          ans[1] = salePrice;
        }
    }

    public boolean canBuy(int sale, int userSale) {
        return sale >= userSale;
    }
}
```