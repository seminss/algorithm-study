package 구현;

import java.util.Scanner;

public class boj2446 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int n = sc.nextInt();
        for(int i=0;i<n;i++){
            for(int j=0;j<i;j++){
                sb.append(" ");
            }
            for(int j=1;j<(n-i)*2;j++){
                sb.append("*");
            }
            sb.append("\n");
        }
        for(int i=1;i<n;i++){
            for(int j=0;j<(n-i)-1;j++){
                sb.append(" ");
            }
            for(int j=0;j<=i*2;j++){
                sb.append("*");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
