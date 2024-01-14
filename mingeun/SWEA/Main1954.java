// 22:50 ~ 23:24
import java.util.Scanner;
import java.io.FileInputStream;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Main1954 {
    private static StringBuilder sb = new StringBuilder();
    private static int[][] snail;
    private static int n;

	public static void main(String args[]) throws Exception
	{
        System.setIn(new FileInputStream("input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
            n = sc.nextInt();
            snail = new int[n][n];
            markSnail();
            System.out.println("#" + test_case);
            printSnail();
		}
	}

    /**
     * 1 2 3
     * 8 9 4
     * 7 6 5
     */
    private static int X = 0;
    private static int Y = 1;

    private static void markSnail() {
        int mark = 1;
        int x = 0;
        int y = 0;
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int d = 0;
        while (mark <= n * n) {
            snail[x][y] = mark++;
            int xn = x + directions[d][X];
            int yn = y + directions[d][Y];
            if (endOfSide(xn, yn)) {
                d = (d + 1) % 4;
                x += directions[d][X];
                y += directions[d][Y];
            } else {
                x = xn;
                y = yn;
            }
        }

    }

    private static boolean endOfSide(int x, int y) {
        if (x >= 0 && x < n && y >= 0 && y < n && snail[x][y] == 0)
            return false;
        return true;
    }

    private static void printSnail() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sb.append(snail[i][j] + " ");
            }
            sb.append("\n");
        }
        System.out.print(sb.toString());
        sb.setLength(0);
    }
}
