// 23.11.08 21:16 ~

import java.util.Scanner;
import java.io.FileInputStream;

class Solution1491
{
    private static StringBuilder sb = new StringBuilder();
    private static final long INF = 9_000_000_000_000_000L;
    private static long min = INF; 
    private static int n;
    private static int a;
    private static int b;

	public static void main(String args[]) throws Exception
	{
		// System.setIn(new FileInputStream("input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
            n = sc.nextInt();
            a = sc.nextInt();
            b = sc.nextInt();
            findSweetSpot();
            sb.append("#" + test_case + " " + min + "\n");
            min = INF;
		}
        System.out.print(sb.toString());
	}

    public static void findSweetSpot() {
        for (int i = 1; i <= n; i++) {
            int j = 1;
            while (i * j <= n) {
                min = Math.min(min, evaluate(i, j++));
            }
        }
    }

    public static long evaluate(int i, int j) {
        return a * Math.abs((long) i - j) + b * Math.abs((long) n - (long) i * j);
    }
}
