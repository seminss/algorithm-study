package SWEA;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

//7:57~8:19
public class problem1974 {
    private static final int SUDOKU_SIZE = 9;
    private static final int MINI_SIZE = 3;

    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            int maps[][] = new int[SUDOKU_SIZE][SUDOKU_SIZE];
            for (int i = 0; i < SUDOKU_SIZE; i++) {
                for (int j = 0; j < SUDOKU_SIZE; j++) {
                    maps[i][j] = sc.nextInt();
                }
            }
            System.out.printf("#%d %d\n", test_case, solution(maps));
        }
    }

    private static int solution(int[][] maps) {
        for (int i = 0; i < SUDOKU_SIZE; i++) {
            Set<Integer> width = new HashSet<>();
            Set<Integer> height = new HashSet<>();
            for (int j = 0; j < SUDOKU_SIZE; j++) {
                width.add(maps[i][j]);
                height.add(maps[j][i]);
            }
            if (height.size() != SUDOKU_SIZE || width.size() != SUDOKU_SIZE) {
                return 0;
            }
        }
        for (int I = 0; I < SUDOKU_SIZE; I = I + MINI_SIZE) {
            for (int J = 0; J < SUDOKU_SIZE; J = J + MINI_SIZE) {
                int size = getNonDuplicateNumbers(I, J, maps);
                if (size != SUDOKU_SIZE) {
                    return 0;
                }
            }
        }
        return 1;
    }

    private static int getNonDuplicateNumbers(int I, int J, int[][] maps) {
        Set<Integer> miniMap = new HashSet<>();
        for (int i = I; i < I + MINI_SIZE; i++) {
            for (int j = J; j < J + MINI_SIZE; j++) {
                miniMap.add(maps[i][j]);
            }
        }
        return miniMap.size();
    }
}
