```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N,M;
	static int[] seg;
	static int[] temp;
	static int size;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		
		size = (int) Math.ceil((Math.log(N)/ Math.log(2))) + 1;
		
		seg = new int[1<<size];
		temp = new int[1<<size];
		int leaf = (1 << (size-1));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for(int i = 0; i < N; i++) {
			seg[leaf + i] = Integer.parseInt(st.nextToken());
		}
		
		// XOR 값을 가진 seg 초기화
		init(1);
		M = Integer.parseInt(br.readLine());
		
		
		for(int i = 0; i < M; i++) {
			//M번 쿼리 받아서 실행하기

			st = new StringTokenizer(br.readLine());
			
			int q = Integer.parseInt(st.nextToken());
			
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			if(q == 1) {
				int k = Integer.parseInt(st.nextToken());
				update(1,0, leaf-1,a,b,k);
			}
			else {
				sb.append(query(1,0,leaf-1,a,b)).append("\n");
			}
		}
		System.out.print(sb);
	}
			
	private static int query(int node, int start, int end, int left, int right) {
		//위에서부터 아래로 확인하면서 선택
		//왼쪽이랑 오른쪽 선택하기
		updateCheck(start, end,node);
		if (right < start || end < left) return 0;
		if (left <= start && end <= right) {
	        return seg[node];
	    }
	    
	    int mid = (start + end) / 2;
	    
	    return query(node * 2, start, mid, left, right) ^ 
	           query(node * 2 + 1, mid + 1, end, left, right);
	}
	
	//node를 업데이트한다.
	// 루트부터 1, N까지 update 구간 left, right
    private static void update(int node,int start,int end,int left,int right,int k) {
    	//현재 노드가 변경된적 있다면 update함 아래구간을 정확하게 체크해야 돼서
        updateCheck(start, end, node);
        
        // 범위를 벗어난 경우
        if(right < start || end < left) return;
        
        if(left <= start && end <= right) {
        	// 선택한 구간을 포함한다면 홀수,짝수 판단
        	// 현재 남은 노드개수 판단해서 홀수면 k 값 업데이트하고 종료
        	if((end - start + 1) % 2 == 1) {
        		seg[node] ^= k;
        	}
        	// 아래에도 값을 전달한다.
        	if(start != end) {
        		temp[node * 2] ^= k;
        		temp[node * 2 + 1] ^= k;
        	}
        	temp[node] = 0;
        	return;
        }
    	
        // 위에서부터 내려가면서 구간잡기 
        int mid = (start + end) / 2;
        update(node * 2 , start, mid, left, right,k);
        update(node * 2 + 1, mid + 1, end, left,right,k);
        
        seg[node] = seg[node * 2] ^ seg[node * 2 + 1];
    }
    
    private static void updateCheck(int s, int e, int node) {
    	//위에서부터 아래로? 
    	if(temp[node] == 0) return;
    	
    	if(s != e) {
    		temp[node * 2] ^= temp[node];
    		temp[node * 2 + 1] ^= temp[node];
    	}
    	// 홀수인 경우
    	if((e - s +1) % 2 == 1) {
    		seg[node] ^= temp[node];
    	}
    	
    	temp[node] = 0;
    }
    
	private static int init(int idx) {
		if(idx >= 1 << (size -1)) {
			return seg[idx];
		}
		//segTree 초기화 XOR 값으로
		seg[idx] = init(idx * 2) ^ init(idx * 2 + 1);
		
		return seg[idx];
	}
}

```