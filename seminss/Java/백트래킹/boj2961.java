package 브루트포스;

import java.util.Scanner;

public class boj2961 {
    static int N;
    static long res;
    static Food[] foods;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        foods = new Food[N];
        for (int i = 0; i < N; i++) {
            foods[i] = new Food(sc.nextInt(), sc.nextInt());
        }
        res = Integer.MAX_VALUE;
        combination(0, 1, 0, 0); // 신맛은 곱, 쓴맛은 합(bitter)
        System.out.println(res);
    }

    private static void combination(int k, int sMul, int bSum, int cnt) {
        if (k == N) {
            if (cnt == 0) { //sMul과 bSum이 초기값과 같다로 비교하면, 연산 후에도 초기값과 같은 경우를 처리 x
                return;
            }
            res = Math.min(res, Math.abs(sMul - bSum));
            return;
        }
        combination(k + 1, sMul * foods[k].sour, bSum + foods[k].bitter, cnt + 1);
        combination(k + 1, sMul, bSum, cnt);
    }

    static class Food {
        int sour; // 신맛
        int bitter; // 쓴맛

        Food(int s, int b) {
            this.sour = s;
            this.bitter = b;
        }

        @Override
        public String toString() {
            return "Food [bitter=" + bitter + ", sour=" + sour + "]";
        }
    }
}