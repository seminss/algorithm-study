package SWEA;

import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;

//단순하게 생각하면 되는 문제여따... Step1, 2 나눠서 그냥 하면 됐는데 넘 복잡하게 생각했음..
public class problem1868 {

    private static int N, maps[][];
    private static int[] nx = {1, -1, 0, 0, 1, -1, 1, -1};
    private static int[] ny = {0, 0, 1, -1, 1, 1, -1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            sb.append("#").append(test_case).append(" ");
            N = Integer.parseInt(br.readLine());
            maps = new int[N][N];

            for (int i = 0; i < N; i++) {
                String line = br.readLine();
                for (int j = 0; j < line.length(); j++) {
                    if (line.charAt(j) == '.') {
                        maps[i][j] = 100;
                    } else {
                        maps[i][j] = -1;
                    }
                }
            }

            int answer = 0;

            //Step1 주변에 지뢰 없는 곳부터 누르기
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (isZeroMine(j, i) && (maps[i][j] == 100)) {
                        bfs(j, i);
                        answer++;
                    }
                }
            }

            //Step2 나머지 안눌린데 누르기
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (maps[i][j] == 100) { //
                        bfs(j, i);
                        answer++;
                    }
                }
            }
            sb.append(answer).append("\n");
        }
        System.out.println(sb);
    }

    /*주변에 지뢰있는지 여부 반환하는 메서드*/
    private static boolean isZeroMine(int x, int y) {
        for (int i = 0; i < 8; i++) {
            int dx = x + nx[i];
            int dy = y + ny[i];
            if (dx >= 0 && dy >= 0 && dx < N && dy < N && maps[dy][dx] == -1) {
                return false;
            }
        }
        return true;
    }

    private static void bfs(int startX, int startY) {
        Deque<Point> dq = new LinkedList<>();
        dq.add(new Point(startX, startY));
        maps[startY][startX] = -2; //없어도 문제는 없지만, step2에서 중복 탐색 안하기 위해 탐색했다고 업데이트

        while (!dq.isEmpty()) {
            Point point = dq.poll();
            int x = point.x;
            int y = point.y;

            int mineCnt = 0; //해당 포인트 주변의 지뢰 개수
            for (int i = 0; i < 8; i++) {
                int dx = x + nx[i];
                int dy = y + ny[i];
                if (dx >= N || dy >= N || dx < 0 || dy < 0) {
                    continue;
                }
                if (maps[dy][dx] == -1) {
                    mineCnt++;
                }
            }
            if (mineCnt != 0) {
                maps[y][x] = mineCnt;
            } else {
                for (int i = 0; i < 8; i++) {
                    int dx = x + nx[i];
                    int dy = y + ny[i];
                    if (dx >= N || dy >= N || dx < 0 || dy < 0 || maps[dy][dx] != 100) {
                        continue;
                    }
                    maps[dy][dx] = -2; // 인접 셀도 처리된 셀임을 표시
                    dq.add(new Point(dx, dy));
                }
            }
        }
    }
}
