package 백트레킹;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj17136 {
    static boolean[][] maps;
    static int[] counts = {0, 0, 0, 0, 0};
    static int res;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        maps = new boolean[10][10];
        res = Integer.MAX_VALUE;
        for (int i = 0; i < 10; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 10; j++) {
                if (st.nextToken().equals("1")) {
                    maps[i][j] = true;
                }
            }
        }
        coloring();
        System.out.println(res == Integer.MAX_VALUE ? -1 : res);
    }

    private static void coloring() {
        int x = -1;
        int y = -1;

        L:
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (maps[i][j]) {
                    x = j;
                    y = i;
                    break L;
                }
            }
        }

        if (x == -1 && y == -1) {
            int sum = 0;
            for (int i = 0; i < 5; i++) {
                sum += counts[i];
            }
            res = Math.min(res, sum);
            return;
        }

        // 해당 위치에서 어떤 색종이를 놓을 수 있는지 보기 (+0~4)
        for (int len = 0; len < 5; len++) {
            if (counts[len] == 5) {  //그 길이에 해당하는 색종이 갯수가 충분한지
                continue;
            }
            if (canPut(y, x, len)) {
                fillMaps(y, x, len, false);  //색종이 놓기
                counts[len]++;
                coloring();
                counts[len]--;
                fillMaps(y, x, len, true);
            } else {
                break; //사이즈 문제로 놓을 수 없는 경우는 더 큰 색종이는 어짜피 불가능
            }
        }
    }

    private static void fillMaps(int i, int j, int len, boolean status) {
        int endx = j + len;
        int endy = i + len;
        for (int y = i; y <= endy; y++) {
            for (int x = j; x <= endx; x++) {
                maps[y][x] = status;
            }
        }
    }

    private static boolean canPut(int i, int j, int len) {
        int endx = j + len;
        int endy = i + len;
        //색종이를 놓았을 때 범위를 벗어나는지
        if (endx >= 10 || endy >= 10) {
            return false;
        }
        for (int y = i; y <= endy; y++) {
            for (int x = j; x <= endx; x++) {
                if (!maps[y][x]) {
                    //어짜피 색종이 크기가 더 커지면 불가능
                    return false;
                }
            }
        }
        return true;
    }
}
