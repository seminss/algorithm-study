package 그래프.dfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj2668 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int n;
    private static int[] list;
    private static Set<Integer> result = new HashSet<>();


    public static void main(String args[]) throws IOException {
        n= Integer.parseInt(br.readLine());
        list = new int[n+1];
        for (int i=1;i<n+1;i++)
            list[i]=Integer.parseInt(br.readLine());
        for(int i=1;i<n+1;i++){
            dfs(i,new boolean[n+1],i);
        }
        List<Integer> sortedResult = new ArrayList<>(result);
        Collections.sort(sortedResult);
        System.out.println(sortedResult.size());
        for (int num : sortedResult) {
            System.out.println(num);
        }
    }
    private static void dfs(int u,boolean[] visited,int start) {
        if(list[u]==start)
            result.add(start);
        if(!visited[list[u]]){
            visited[list[u]] =true;
            dfs(list[u],visited,start);
        }
    }
}
