package 동적계획법;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj11660 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] sums = new int[N + 1][N + 1];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                sums[i][j] = sums[i][j - 1] + sums[i - 1][j] - sums[i - 1][j - 1] + Integer.parseInt(st.nextToken());
            }
        }
        for (int cnt = 0; cnt < M; cnt++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken()); //1
            int y1 = Integer.parseInt(st.nextToken()); //2
            int x2 = Integer.parseInt(st.nextToken()); //1
            int y2 = Integer.parseInt(st.nextToken()); //2
            int res;
            //(x, y)는 x행 y열을 의미한다.
            res = sums[x2][y2] - sums[x1 - 1][y2] - sums[x2][y1 - 1] + sums[x1 - 1][y1 - 1];
            sb.append(res).append("\n");
        }
        System.out.println(sb);
    }
}