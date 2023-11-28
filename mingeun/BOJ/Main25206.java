// 11.28 08:52~09:02
import java.io.*;
import java.util.*;

public class Main25206 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double a = 0;
        double b = 0;
        String[] input;
        for (int i = 0; i < 20; i++) {
            input = br.readLine().split(" ");
            if (!input[2].equals("P")) {
                a += Double.parseDouble(input[1]) * score(input[2]);
                b += Double.parseDouble(input[1]);
            }
        }
        System.out.println(a / b);
    }

    private static double score(String grade) {
        if (grade.equals("A+")) {
            return 4.5;
        } else if (grade.equals("A0")) {
            return 4.0;
        } else if (grade.equals("A0")) {
            return 4.0;
        } else if (grade.equals("B+")) {
            return 3.5;
        } else if (grade.equals("B0")) {
            return 3.0;
        } else if (grade.equals("C+")) {
            return 2.5;
        } else if (grade.equals("C0")) {
            return 2.0;
        } else if (grade.equals("D+")) {
            return 1.5;
        } else if (grade.equals("D0")) {
            return 1.0;
        } else {
            return 0.0;
        }
    }
}
