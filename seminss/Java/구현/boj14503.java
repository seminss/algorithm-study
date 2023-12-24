package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 청소기는 바라보는 방향이 있고, 이 방향은 동서남북 중 하나
 * 방 한 칸의 좌표 : (r,c)
 * 가장 북쪽 줄 가장 서쪽 칸 : (0,0)
 * 가장 남쪽 줄 가장 동쪽 칸 : (n-1,m-1)
 * (r,c)는 북쪽에서 (r+1)번째 있는 줄의 서쪽에서 (c+1)번째 칸을 가리킨다.
 */
public class boj14503 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int[][] maps;
    private static boolean[][] visited;
    private static int[] dx = {0, 1, 0, -1};
    private static int[] dy = {-1, 0, 1, 0};
    private static int result = 1;
    private static int m, n, r, c, d;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        maps = new int[n][m];
        visited = new boolean[n][m];

        st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken()); // 0:북, 1:동, 남:2, 서:3

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        cleanUp(r, c, d);
        System.out.println(result);
    }

    //북->서->남->동 (d+3)%4
    //0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)
    private static void cleanUp(int r, int c, int d) {
        visited[r][c] = true;

        for (int i = 0; i < 4; i++) { //d의 방향 기준 반시계로 4방향 돌아야 함
            d = (d + 3) % 4;
            int nx = c + dx[d];
            int ny = r + dy[d];
            if (ny < 0 || ny >= n || nx < 0 || nx >= m) {
                continue;
            }
            if (maps[ny][nx] == 0 && !visited[ny][nx]) {
                cleanUp(ny, nx, d);
                result++;
                return; // 복귀 도중 다른 곳을 청소 하지 않도록
            }
        }

        //반시계로 돌 때마다 청소가 다 되어 있음 or 벽임
        int b = (d + 2) % 4;
        int bx = c + dx[b];
        int by = r + dy[b];
        if (by >= 0 && by < n && bx >= 0 && bx < m && maps[by][bx] != 1) {
            cleanUp(by, bx, d); //원래 방향 유지
        }
    }
}
