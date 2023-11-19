// 23.11.6 11:30 ~ 23.11.6 11:42
import java.util.Scanner;
import java.io.FileInputStream;

class Solution1217
{
    private static StringBuilder sb = new StringBuilder();
    private static int tcNum = 0;

	public static void main(String args[]) throws Exception
	{
		System.setIn(new FileInputStream("input.txt"));
        
        
		Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt())
		{
            tcNum = sc.nextInt();
            int n = sc.nextInt();
            int m = sc.nextInt();
            sb.append("#" + tcNum + " ");
            power(n, m, 0, 1);
		}
        System.out.print(sb.toString());
	}

    private static void power(int n, int m, int r, int tmp) {
        if (r == m) {
            sb.append(tmp + "\n");
            return;
        }
        power(n, m, r + 1, tmp * n);
    }
}
