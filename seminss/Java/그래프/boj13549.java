package 그래프;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj13549 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static Queue<Integer> dq = new ArrayDeque<>();

    public static void main(String args[]) throws IOException {
         st = new StringTokenizer(br.readLine());
         int n = Integer.parseInt(st.nextToken());
         int k = Integer.parseInt(st.nextToken());
         int inf =  100000;
         int[] tmp = new int[inf+1];
         Arrays.fill(tmp,0);
         dq.add(n);
         while (!dq.isEmpty()){
             int t = dq.poll();
             if(t==k){
                 System.out.println(tmp[t]);
                 break;
             }
             for (Integer i : List.of(t - 1, t + 1, t * 2)) {
                 if (inf >= i && i>=0 && 0 == tmp[i]){
                     tmp[i]=tmp[t]+1;
                     dq.add(i);
                 }
             }
         }
    }
}
