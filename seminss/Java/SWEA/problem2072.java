package SWEA;

import java.io.IOException;
import java.util.Scanner;

public class problem2072 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        sc.nextLine();
        for(int test_case = 1; test_case <= T; test_case++)
        {
            String[] numbers = sc.nextLine().split(" ");
            int result = 0;
            for (String numStr : numbers){
                int num = Integer.parseInt(numStr);
                if(num%2==1){
                    result +=num;
                }
            }
            System.out.println("#"+test_case+" "+result);
        }
        sc.close();
    }
}
