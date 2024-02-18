package 그래프;

import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * Stack : 116700KB, 820ms
 * LinkedList : 206904KB, 488ms
 */
public class boj16234 {
    static int N, L, R, maps[][];
    static boolean visited[][], didMoved;
    static List<Point> countries = new LinkedList<>();
    //static Stack<Point> countries = new Stack<>();
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken()); //인구 차이가 L명 이상
        R = Integer.parseInt(st.nextToken()); //R명 이하
        maps = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int cnt = 0;
        while (true) {
            didMoved = false;
            visited = new boolean[N][N]; // 한 턴 연산 이후 다음 턴에서 중복 연산 하는 문제 방지
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (!visited[i][j]) {
                        countries.add(new Point(j, i));
                        visited[i][j] = true;
                        int sum = dfs(j, i);
                        int avg = sum / countries.size();
                        //while (!countries.isEmpty()) {
                        //    Point p = countries.pop();
                        //    maps[p.y][p.x] = avg;
                        //}
                        for (int c = countries.size() - 1; c >= 0; c--) { // remove는 뒤에서부터
                            Point p = countries.remove(c);
                            maps[p.y][p.x] = avg;
                        }
                    }
                }
            }
            if (!didMoved) {
                break;
            }
            cnt++;
        }
        System.out.println(cnt);
    }

    private static int dfs(int x, int y) {
        int sum = maps[y][x]; //더이상 연합 생성 불가하다면 이 상태 그대로 자기 인구만 리턴 하면 됨
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= N || ny >= N || nx < 0 || ny < 0) {
                continue;
            }
            if (visited[ny][nx]) {
                continue;
            }
            if (Math.abs(maps[ny][nx] - maps[y][x]) >= L && Math.abs(maps[ny][nx] - maps[y][x]) <= R) {
                countries.add(new Point(nx, ny));
                visited[ny][nx] = true;
                sum += dfs(nx, ny);
                didMoved = true;
            }
        }
        return sum;
    }
}
