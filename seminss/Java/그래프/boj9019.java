package 그래프;
//11:57 ~1:05, 풀이 참고

import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

/**
 * D,S,L,R
 * 레지스터에 저장된 n을 다음과 같이 변환한다.
 * n의 네 자릿수를 d1, d2, d3, d4
 * D: D 는 n을 두 배로 바꾼다.
 * 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다.
 * 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
 * S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다.
 * n이 0 이라면 9999 가 대신 레지스터에 저장된다.
 * L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다.
 * 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
 * R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다.
 * 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
 * 무조건 n은 4자리수
 */
public class boj9019 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(br.readLine());
        for (int testCase = 0; testCase < T; testCase++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            dslr(A, B);
        }
    }

    private static void dslr(int a, int b) {
        Deque<Integer> dq = new ArrayDeque<>();
        boolean[] visited = new boolean[10000];
        String[] history = new String[10000];

        dq.add(a);
        visited[a] = true;
        Arrays.fill(history, "");
        while (!dq.isEmpty() && !visited[b]) {
            int num = dq.poll();

            int D = d(num);
            int S = s(num);
            int L = l(num);
            int R = r(num);

            if (!visited[D]) {
                dq.add(D);
                visited[D] = true;
                history[D] = history[num] + "D"; //지금까지 온 커맨드+새 커맨드
            }

            if (!visited[S]) {
                dq.add(S);
                visited[S] = true;
                history[S] = history[num] + "S";
            }

            if (!visited[L]) {
                dq.add(L);
                visited[L] = true;
                history[L] = history[num] + "L";
            }

            if (!visited[R]) {
                dq.add(R);
                visited[R] = true;
                history[R] = history[num] + "R";
            }
        }
        System.out.println(history[b]); // b를 방문하자 마자 탈출 -> 가장 적은 커맨드 사용
    }

    private static int d(int num) {
        int goal = num * 2;
        return goal > 9999 ? goal % 10000 : goal;
    }

    private static int s(int num) {
        int goal = num - 1;
        return num == 0 ? 9999 : goal;
    }

    private static int l(int num) { //n이 무조건 4자리라 가능한 연산
        return (num % 1000) * 10 + num / 1000;
    }

    private static int r(int num) {
        return (num % 10) * 1000 + num / 10;
    }
}
