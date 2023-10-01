// 23.9.27 08:11 ~ 08:17

import java.util.*;
import java.io.*;

public class Main10870 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] fibonacci = new int[20 + 1];
        fibonacci[1] = 1;
        for (int i = 2; i < 21; i++)
            fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
        System.out.println(fibonacci[n]);
    }
}
