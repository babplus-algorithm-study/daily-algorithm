```java
import java.io.*;
import java.util.*;

public class Main {
	
	
	static int[] failure;
	static int count = 0;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        
        String a = br.readLine();
        a += a.substring(0, a.length() - 1);
        String b = br.readLine();
        
        char[] ac = a.toCharArray();
        char[] bc = b.toCharArray();
        
        failure = new int[ac.length];
        
        failureFunction(bc);
        kmp(ac, bc);
        System.out.println(count);
    }
    
    public static void failureFunction(char[] s) {
    	int p = 0;
    	
    	for(int idx = 1; idx < s.length; idx++) {
    		
    		while(p != 0  && s[idx] != s[p]) {
    			p = failure[p - 1];
    		}
    		
    		if(s[idx] == s[p]) {
    			p++;
    			failure[idx] = p;
    		}
    	}
    	
    }
    
    public static void kmp(char[] s1, char[] s2) {
    	
    	int p = 0;
    	
    	for(int idx = 0; idx < s1.length; idx++) {
    		
    		while(p != 0 && s1[idx] != s2[p]) p = failure[p - 1];
    		
    		if(s1[idx] == s2[p]) {
    			if(p == s2.length - 1) {
    				count++;
    				p = failure[p];
    			} else {
    				p++;
    			}
    		}
    	}
    }
    
    
    
    

}
```
