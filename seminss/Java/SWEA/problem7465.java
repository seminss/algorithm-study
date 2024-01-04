import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int n, m;
    static boolean[] visited;
    static ArrayList<Integer>[] arr;

    public static void main(String args[]) throws IOException {
        int T = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case <= T; test_case++) {
            sb.append("#").append(test_case).append(" ");
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken()); //사람 수
            m = Integer.parseInt(st.nextToken()); //관계 수
            arr = new ArrayList[n+1];
            visited = new boolean[n + 1];

            int result = 0;
            for(int i=0;i<=n;i++){
                arr[i] = new ArrayList<>();
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int key = Integer.parseInt(st.nextToken());
                int value = Integer.parseInt(st.nextToken());
                arr[key].add(value);
                arr[value].add(key);
            }
            for (int i = 1; i <= n; i++) {
                if (!visited[i]) {
                    bfs(arr, visited, i);
                    result++;
                }
            }
            sb.append(result).append("\n");
        }
        System.out.println(sb);
    }

    private static void bfs(ArrayList[] arr, boolean[] visited, int num) {
        Queue<Integer> dq = new LinkedList<>();
        dq.add(num);
        visited[num]=true;

        while(!dq.isEmpty()){
            num=dq.poll();
            for(int i=0;i<arr[num].size();i++){
                int friend= (int) arr[num].get(i);
                if(!visited[friend]){
                    dq.add(friend);
                    visited[friend]=true;
                }
            }
        }
    }
}