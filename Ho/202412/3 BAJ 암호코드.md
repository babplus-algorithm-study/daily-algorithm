```java
package gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P2011 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String number = br.readLine();

        if (number.length() == 0 || number.charAt(0) == '0') {
            System.out.println(0);
            return;
        }
        if(number.length() == 1) {
            if(number.charAt(0) == '0'){
                System.out.println(0);
            }
            else{
                System.out.println(1);
            }
            return;
        }

        char[] numbers = number.toCharArray();
        int[] dp = new int[numbers.length + 10];
        boolean flag = false;

        dp[0] = 1;

        // i=1일 때의 처리
        if (numbers[1] == '0') {
            if (numbers[0] == '1' || numbers[0] == '2') {
                dp[1] = 1;
            } else {
                flag = true;
            }
        } else if (numbers[0] == '1' || (numbers[0] == '2' && numbers[1] <= '6')) {
            dp[1] = 2;
        } else {
            dp[1] = 1;
        }

        for(int i = 2; i < numbers.length && !flag; i++) {
            if(numbers[i] == '0') {
                if (numbers[i-1] == '0' || numbers[i-1] > '2') {
                    flag = true;
                    break;
                }
                dp[i] = dp[i-2];
            } else {
                dp[i] = dp[i-1];
                if (numbers[i-1] == '1' || (numbers[i-1] == '2' && numbers[i] <= '6')) {
                    dp[i] = (dp[i] + dp[i-2]) % 1000000;
                }
            }
        }

        if (flag) {
            System.out.println(0);
        } else {
            System.out.println(dp[numbers.length-1]);
        }
    }
}
```