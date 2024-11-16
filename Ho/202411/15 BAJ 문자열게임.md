```java
package gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class P20437 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++) {
            int ansMin = (int) 1e9;
            int ansMax = 0;

            String word = br.readLine();
            int k = Integer.parseInt(br.readLine());

            int[] result = findMinMax(word, k);

            ansMin = Math.min(result[0], ansMin);
            ansMax = Math.max(result[1], ansMax);

            if(result[1] == 0) {
                if(k == 1) {
                    sb.append("1 1\n");
                }
                else{
                    sb.append("-1\n");
                }
            }
            else{
                sb.append(ansMin + " " + ansMax + "\n");
            }
        }
        System.out.println(sb.toString());

    }

    public static int[] findMinMax(String word, int k) {
        int min = (int) 1e9;
        int max = 0;

        Queue[] qArr = new Queue[26];

        for(int i = 0; i < 26; i++) {
            qArr[i] = new LinkedList<>();
        }

        for (int i = 0; i < word.length(); i++) {
            int idx = word.charAt(i) - 'a';

            if(qArr[idx].size() < k) {
                // 가장 앞에 있는 알파벳을 넣는거
                qArr[idx].add(i);
                if (qArr[idx].size() == k) {
//                  동일해지면
                    int len = i - (int) qArr[idx].peek() + 1;
                    min = Math.min(min, len);
                    max = Math.max(max, len);
                }
            }
            else{
                qArr[idx].poll();
                qArr[idx].add(i);
                 int len = i - (int) qArr[idx].peek() + 1;
                min = Math.min(min, len);
                max = Math.max(max, len);
            }

        }

        return new int[] {min, max};
    }
}

```