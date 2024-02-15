package 백트레킹;

import java.util.Scanner;

public class boj2023 {
    static int res = 0;
    static int N;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        combi(2);
        combi(3);
        combi(5);
        combi(7);
    }

    public static void combi(int num) {
        for (int i = 2; i < Math.sqrt(num) + 1; i++) {
            if (i != num && num % i == 0) {
                return;
            }
        }
        if (num >= Math.pow(10, N - 1) && num <= Math.pow(10, N) - 1) {
            System.out.println(num);
            return;
        }
        for (int i = 1; i <= 9; i++) {
            combi(num * 10 + i);
        }
    }
}