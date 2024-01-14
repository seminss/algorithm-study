// 23.11.24 14:40~16:00

import java.io.*;
import java.util.*;

public class Main16954 {

    private static final int EMPTY = 0;
    private static final int WALL = 1;
    private static final int MOVED = 2;
    private static final int X = 0;
    private static final int Y = 1;
    private static int n = 8;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            String row = br.readLine();
            for (int j = 0; j < n; j++) {
                board[i][j] = row.charAt(j) == '#' ? WALL : EMPTY;
            }
        }

        try {
            dfs(board, new int[] {n - 1, 0});
            System.out.println(0);
        } catch (ReachableException e) {
            System.out.println(1);
        }

    }

    private static void dfs(int[][] board, int[] pos) throws ReachableException {
        // printBoard(board);
        if (countWalls(board) == 0) {
            throw new ReachableException();
        }
        int[][] d = {{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}, {0, 0}};
        for (int i = 0; i < d.length; i++) {
            int xn = pos[X] + d[i][X];
            int yn = pos[Y] + d[i][Y];
            int npos[] = new int[] {xn, yn};
            if (canMoveTo(xn, yn, board)) {
                try {
                    int[][] movedBoard = wallsMovedBoard(board, npos);
                    dfs(movedBoard, npos);
                } catch (GameOverException e) {
                    continue;
                }
            }
        }
    }

    private static void printBoard(int[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    private static int countWalls(int[][] board) {
        int count = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                if (board[i][j] == WALL)
                    count++;
            }
        }
        return count;
    }

    private static int[][] wallsMovedBoard(int[][] board, int[] pos) throws GameOverException {
        int[][] movedBoard = copy2DSquareIntArray(board);
        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j < n; j++) {
                if (movedBoard[i][j] == WALL && i == n - 1) {
                    movedBoard[i][j] = EMPTY;
                } else if (movedBoard[i][j] == WALL) {
                    movedBoard[i][j] = EMPTY;
                    if (i + 1 == pos[X] && j == pos[Y]) {
                        throw new GameOverException();
                    }
                    movedBoard[i + 1][j] = WALL;
                }
            }
        }
        return movedBoard;
    }

    private static boolean canMoveTo(int x, int y, int[][] board) {
        return (x > -1 && x < n && y > -1 && y < n && board[x][y] == EMPTY);
    }

    private static int[][] copy2DSquareIntArray(int[][] source) {
        int[][] copy = new int[source.length][source.length];
        for (int i = 0; i < source.length; i++) {
            for (int j = 0; j < source.length; j++) {
                copy[i][j] = source[i][j];
            }
        }
        return copy;
    }

    private static class GameOverException extends RuntimeException {  }
    private static class ReachableException extends RuntimeException {  }
}
