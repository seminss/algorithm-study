package 브루트포스;

import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.lang.Math.abs;

//9:41 ~ 10:35

/**
 * 0~9가 있고 고장난 번호가 있으면 해당 숫자는 입력 못함
 * 누를 수 있는 번호로 N에 최대한 근접한 숫자를 누르고, (1회)
 * 그다음 +를 누르던지, -를 누르던지 한다. (+-당 1회)
 * 0에서는 더이상 아래로 내려가지 못하고, 최대 채널은 500,000이다.
 * 수빈이는 현재 100이다.
 */
public class boj1107 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int result;
    private static int N, M;
    private static List<Integer> numbers = new ArrayList<>(Arrays.asList(0, 1, 2, 3, 4, 5, 6, 7, 8, 9));

    public static void main(String[] args) throws IOException {
        String goal = br.readLine();
        N = Integer.parseInt(goal);
        M = Integer.parseInt(br.readLine());
        if (M > 0) {
            st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                numbers.remove(Integer.valueOf(st.nextToken()));
            }
        }
        result = abs(N - 100); //현재 위치
        int startDigit = Math.max(goal.length() - 1, 1);
        //자리수를 하나 작은거, 같은거, 하나 큰 거까지만 보기
        for (int s = startDigit; s <= goal.length() + 1; s++) {
            int[] arr = new int[s];
            repeatedPermutation(s, 0, arr);
        }
        System.out.println(result);
    }

    private static void repeatedPermutation(int s, int cnt, int[] arr) { // 중복 순열
        if (cnt == s) {
            int candidateNum = createNumber(arr);
            result = Math.min(abs(N - candidateNum) + arr.length, result);
            return;
        }
        for (int i = 0; i < numbers.size(); i++) {
            arr[cnt] = numbers.get(i);
            repeatedPermutation(s, cnt + 1, arr);
        }
    }

    private static int createNumber(int[] arr) {
        int number = 0;
        int digit = 1;
        for (int i = 0; i < arr.length; i++) {
            number += arr[i] * digit;
            digit = digit * 10;
        }
        return number;
    }
}
