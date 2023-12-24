package 문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//11:22~11:28
public class boj5525 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int result = 0;
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        char[] arr = br.readLine().toCharArray();
        int temp = 0;

        for (int i = 1; i < M - 1; ) {
            if (arr[i - 1] == 'I' && arr[i] == 'O' && arr[i + 1] == 'I') {
                temp++;
                if (temp == N) {
                    result++;
                    temp--;
                }
                i = i + 2;
                continue;
            }
            temp = 0;
            i = i + 1;
        }
        System.out.println(result);
    }
}
