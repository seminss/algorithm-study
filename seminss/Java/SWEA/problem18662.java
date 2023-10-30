package SWEA;

import java.util.Scanner;

public class problem18662 {
    public static void main(String[] args) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();
        sc.nextLine();
        for(int test_case = 1; test_case <= T; test_case++)
        {
            //b-a = c-b
            String[] numbers = sc.nextLine().split(" ");
            int a = Integer.parseInt(numbers[0]);
            int b = Integer.parseInt(numbers[1]);
            int c = Integer.parseInt(numbers[2]);

            //a를 바꾸기
            double xa = Math.abs(2*b-c-a);
            //b를 바꾸기
            double xb = Math.abs((a+c) /2.0-b);
            //c를 바꾸기
            double xc = Math.abs(2*b-a-c);

            double x = Math.min(xa,xb);
            x = Math.min(x,xc);

            System.out.printf("#%d %.1f%n",test_case,x);
        }
    }
}
