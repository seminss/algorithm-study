// 23.11.8 08:20 ~ 08:40
import java.util.*;
import java.io.FileInputStream;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution1221
{
    static String tcNum ;
    static int tcLength;
    static Map<String, Integer> order = new HashMap<String, Integer>();
    static StringBuilder sb = new StringBuilder();
    static String[] input;

	public static void main(String args[]) throws Exception
	{
        order.put("ZRO", 0);
        order.put("ONE", 1);
        order.put("TWO", 2);
        order.put("THR", 3);
        order.put("FOR", 4);
        order.put("FIV", 5);
        order.put("SIX", 6);
        order.put("SVN", 7);
        order.put("EGT", 8);
        order.put("NIN", 9);

		System.setIn(new FileInputStream("input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
            sc.next();
            tcLength = sc.nextInt();
            input = new String[tcLength];
            for (int i = 0; i < tcLength; i++) {
                input[i] = sc.next();
            }
            Arrays.sort(input, (s1, s2) -> order.get(s1) - order.get(s2));
            sb.append("#" + test_case + "\n");
            for (int i = 0; i < tcLength; i++) {
                sb.append(input[i] + " ");
            }
		}
        System.out.println(sb.toString());
	}
}
