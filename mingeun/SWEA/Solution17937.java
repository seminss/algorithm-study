// 23.11.17 22:22~22:46

import java.util.Scanner;
import java.io.FileInputStream;

class Solution17937
{
	public static void main(String args[]) throws Exception
	{
		System.setIn(new FileInputStream("input.txt"));

		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/

		for(int test_case = 1; test_case <= T; test_case++)
		{
            String a = sc.next();
            String b = sc.next();
            System.out.println(String.format("#%d %s", test_case, gcdInRange(a, b)));
		}
	}

    /**
     * n n+1 n+2 n+3 ... n
     */

    private static String gcdInRange(String s, String e) {
        if (s.equals(e))
            return s;
        return "1";
    }

    private static long gcd(int a, int b) {
        if ( b == 0 )
            return a;
        return gcd( b, b % a );
    }
}
