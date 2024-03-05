package 구현;

import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.List;

public class boj19236 {

    static class Fish implements Comparable<Fish> {
        int x, y, dir, num;
        boolean died;

        public Fish(int x, int y, int num, int dir, boolean died) {
            this.x = x;
            this.y = y;
            this.dir = dir; //방향
            this.num = num;
            this.died = died;
        }

        public int compareTo(Fish o) {
            return Integer.compare(this.num, o.num);
        }

    }

    // 1:↑, 2:↖, 3:←, 4:↙, 5:↓, 6:↘, 7:→, 8:↗
    static int[] dx = {0, -1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dy = {0, 0, -1, -1, -1, 0, 1, 1, 1};
    static Fish[][] maps = new Fish[4][4];
    static int Ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        for (int i = 0; i < 4; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; j++) {
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                maps[i][j] = new Fish(i, j, a, b, false);
            }
        }

        Ans = 0;
        maps[0][0].died = true;
        go(maps, 0, 0, maps[0][0].dir);
        System.out.println(Ans);
    }

    private static void go(Fish[][] maps, int sharkX, int sharkY, int sharkD) {
        Fish[][] copy = copyMaps(maps);
        moveFishes(copy, sharkX, sharkY);
        List<Point> cand = getCandidate(copy, sharkX, sharkY, sharkD);
        if (cand.isEmpty()) {
            Ans = Math.max(Ans, getResult(copy));
        }
        for (Point p : cand) {
            copy[p.x][p.y].died = true;
            go(copy, p.x, p.y, copy[p.x][p.y].dir);
            copy[p.x][p.y].died = false;
        }
    }

    /**
     * 죽은 애들 빼구 남은 물고기 중에서 번호가 작은 물고기부터 이동한다.
     * 상어가 있거나 공간의 경계를 넘지 않으면, 바라보고 있는 방향에 있는 물고기와 교체를 하면 된다.
     * 죽은 물고기는 빈 칸으로 취급 하면 됨.
     * 이동할 수 없다면 45도 회전 시키며 이동할 수 있는 칸을 찾는다.
     * 8방을 전부 봤는데도 이동할 수 없으면 패스
     */
    private static void moveFishes(Fish[][] maps, int sharkX, int sharkY) {
        PriorityQueue<Fish> pq = new PriorityQueue<>();
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (maps[i][j].died) {
                    continue;
                }
                pq.add(maps[i][j]);
            }
        }
        while (!pq.isEmpty()) {
            Fish f = pq.poll();
            int nd = f.dir - 1;
            for (int cnt = 0; cnt < 7; cnt++) {
                nd += 1;
                nd = nd == 9 ? 1 : nd;
                int nx = f.x + dx[nd];
                int ny = f.y + dy[nd];
                if (nx == f.x && ny == f.y) {
                    continue;
                }
                if (nx == sharkX && ny == sharkY) {
                    continue;
                }
                if (nx >= 4 || ny >= 4 || nx < 0 || ny < 0) {
                    continue;
                }
                //두 물고기 swap
                Fish temp = maps[f.x][f.y];
                maps[f.x][f.y] = maps[nx][ny];
                maps[nx][ny] = temp;

                //속성 업데이트
                maps[f.x][f.y].x = f.x;
                maps[f.x][f.y].y = f.y;
                maps[nx][ny].x = nx;
                maps[nx][ny].y = ny;
                maps[nx][ny].dir = nd;



                break;
            }
        }
    }

    private static List<Point> getCandidate(Fish[][] maps, int x, int y, int d) {
        List<Point> cand = new ArrayList<>();
        for (int cnt = 1; cnt <= 3; cnt++) {
            int nx = x + dx[d] * cnt;
            int ny = y + dy[d] * cnt;
            if (nx >= 4 || ny >= 4 || nx < 0 || ny < 0) {
                break;
            }
            if (maps[nx][ny].died) {
                continue;
            }
            cand.add(new Point(nx, ny));
        }
        return cand;
    }

    private static int getResult(Fish[][] maps) {
        int sum = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (maps[i][j].died) {
                    sum += maps[i][j].num;
                }
            }
        }
        return sum;
    }

    private static Fish[][] copyMaps(Fish[][] maps) {
        Fish[][] copy = new Fish[4][4];
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                Fish fish = maps[i][j];
                copy[i][j] = new Fish(fish.x, fish.y, fish.num, fish.dir, fish.died);
            }
        }
        return copy;
    }
}
