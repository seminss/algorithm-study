// 23.9.28 08:40 ~

import java.util.*;
import java.io.*;

public class Main9655 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        /*
         *  1  2  3  4
         * SK CY SK CY 
         */
        System.out.println((n % 2 == 0) ? "CY" : "SK");

        br.close();
    }
}
