package SWEA;

import java.util.Scanner;

//6:20~6:50, D2
public class problem1959 {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            int n = sc.nextInt();
            int m = sc.nextInt();

            int[] arr1 = new int[n];
            int[] arr2 = new int[m];
            for (int i = 0; i < n; i++) {
                arr1[i] = sc.nextInt();
            }
            for (int i = 0; i < m; i++) {
                arr2[i] = sc.nextInt();
            }
            if (n >= m) {
                System.out.printf("#%d %d\n", test_case, solution(arr1, arr2));
                continue;
            }
            System.out.printf("#%d %d\n", test_case, solution(arr2, arr1));
        }
        sc.close();
    }

    private static int solution(int[] lNums, int[] sNums) {
        int result = 0;
        for (int i = 0; i <= lNums.length - sNums.length; i++) {
            int temp = 0;
            for (int j = 0; j < sNums.length; j++) {
                temp += sNums[j] * lNums[i+j];
            }
            result = Math.max(temp, result);
        }
        return result;
    }
}
