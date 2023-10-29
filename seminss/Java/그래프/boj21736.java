package 그래프;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//3:30
public class boj21736 {
    protected static int result=0;
    private static int n;
    private static int m;
    private static char[][] maps;
    private static int[] nx = {1, -1, 0, 0};
    private static int[] ny = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        maps = new char[n][m];

        int doyeon_x=-1;
        int doyeon_y=-1;
        boolean[][] visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                maps[i][j] = line.charAt(j);
                visited[i][j]=false;
                if(maps[i][j]=='I'){
                    doyeon_y=i;
                    doyeon_x=j;
                }
            }
        }

        bfs(List.of(doyeon_x,doyeon_y), visited);
        System.out.print(result>0? result: "TT");
    }

    private static void bfs(List<Integer> coord, boolean[][] visited){
        Queue<List<Integer>> dq = new ArrayDeque<>();
        dq.add(coord);
        visited[coord.get(1)][coord.get(0)]= true;

        while(!dq.isEmpty()){
            List<Integer> pcoord=dq.poll();
            int x = pcoord.get(0);
            int y = pcoord.get(1);
            for(int i=0;i<4;i++){
                int dx=x+nx[i];
                int dy=y+ny[i];
                if(dy<0 || dx<0 || dy>=n || dx>=m){
                    continue;
                }
                if(visited[dy][dx]){
                    continue;
                }
                if(maps[dy][dx]=='X'){
                    continue;
                }
                if(maps[dy][dx]=='P'){
                    result++;
                }
                dq.add(List.of(dx,dy));
                visited[dy][dx]=true;
            }

        }
    }

}
