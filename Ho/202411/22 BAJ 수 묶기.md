```java
package gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class P1744 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] sequence = new int[N];
        boolean[] visited = new boolean[N];

        // 음수는 음수끼리 묶는게 좋지
        for(int i =0;  i < N; i++) {
            sequence[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(sequence);

        long sum = 0;

        // 자연수인 경우 가장 큰 수끼리 묶고
        // 음수인 경우 가장 작은 두개를 곱하고
        // 0은 음수가 짝이 없는 경우 곱하고
        // 아닌 경우 혼자 사용한다.

        int nNumIdx = N;

        for (int i = 0; i < N; i++) {
            if(visited[i]) continue;
            if(i != N-1) {
                if(sequence[i] < 0 && sequence[i + 1] < 0) {
                    visited[i] = true;
                    visited[i + 1] = true;

                    sum += sequence[i] * sequence[i + 1];
                }

                else if(sequence[i] < 0 && sequence[i + 1] == 0) {
                    visited[i] = true;
                    visited[i + 1] = true;
                }

                else if(sequence[i] < 0 && sequence[i + 1] >0) {
                    visited[i] = true;
                    sum += sequence[i];
                }

                if(sequence[i] >= 0) {
                    nNumIdx = i;
                    break;
                }
            }
            else{
                sum += sequence[i];
                visited[i] = true;
            }
        }

        for (int i = N-1; i >= nNumIdx; i--) {
            if(visited[i]) continue;

            if(i == 0 || i == nNumIdx) {
                sum += sequence[i];
                break;
            }

            if(sequence[i] > 0 && sequence[i-1] > 0) {
                visited[i] = true;
                visited[i - 1] = true;
                if(sequence[i] == 1 && sequence[i-1] == 1) {
                    sum += 2;
                    continue;
                }
                else if(sequence[i] > 1 && sequence[i-1] == 1) {
                    sum += sequence[i];
                    sum += sequence[i-1];
                    continue;

                }
                sum += sequence[i] * sequence[i - 1];
            }

            else if(sequence[i] > 0 && sequence[i - 1] == 0) {
                visited[i] = true;
                visited[i - 1] = true;
                sum += sequence[i];
            }
            else if(sequence[i] == 0 && sequence[i - 1] == 0) {
                visited[i] = true;
                visited[i - 1] = true;
            }
        }

        System.out.println(sum);
    }
}

```