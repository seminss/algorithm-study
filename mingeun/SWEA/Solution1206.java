// 23.11.17 22:55~23:40

import java.util.*;
import java.io.*;

class Solution1206
{
    private static int N;
    private static int[] buildings;
    private static StringBuilder sb = new StringBuilder();

	public static void main(String args[]) throws Exception
	{
		System.setIn(new FileInputStream("input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = 10;

		for(int test_case = 1; test_case <= T; test_case++)
		{
            N = Integer.parseInt(br.readLine());
            buildings = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            sb.append(String.format("#%d %d\n",
                test_case, countProspectRightSecuredHousHolds()));
		}
        System.out.print(sb.toString());
	}

    private static int countProspectRightSecuredHousHolds() {
        int count = 0;
        for (int i = 0; i < buildings.length; i++) {
            if ( i == 0) {
                count += Math.min(
                    (buildings[i] - buildings[i + 1] < 0) ? 0 : buildings[i] - buildings[i + 1],
                    (buildings[i] - buildings[i + 2] < 0) ? 0 : buildings[i] - buildings[i + 2]);
            } else if( i == buildings.length - 1 ) {
                count += Math.min(
                    (buildings[i] - buildings[i - 1] < 0) ? 0 : buildings[i] - buildings[i - 1],
                    (buildings[i] - buildings[i - 2] < 0) ? 0 : buildings[i] - buildings[i - 2]);
            } else if( i == 1 ) {
                count += Math.min(
                    Math.min(
                        (buildings[i] - buildings[i + 1] < 0) ? 0 : buildings[i] - buildings[i + 1],
                        (buildings[i] - buildings[i + 2] < 0) ? 0 : buildings[i] - buildings[i + 2]),
                    (buildings[i] - buildings[i - 1] < 0) ? 0 : buildings[i] - buildings[i - 1]
                );
            } else if( i == buildings.length - 2 ) {
                count += Math.min(
                    Math.min(
                        (buildings[i] - buildings[i + 1] < 0) ? 0 : buildings[i] - buildings[i + 1],
                        (buildings[i] - buildings[i - 2] < 0) ? 0 : buildings[i] - buildings[i - 2]),
                    (buildings[i] - buildings[i - 1] < 0) ? 0 : buildings[i] - buildings[i - 1]
                );
            } else {
                count += Math.min(
                    Math.min(
                        (buildings[i] - buildings[i - 1] < 0) ? 0 : buildings[i] - buildings[i - 1],
                        (buildings[i] - buildings[i - 2] < 0) ? 0 : buildings[i] - buildings[i - 2]),
                    Math.min(
                        (buildings[i] - buildings[i + 1] < 0) ? 0 : buildings[i] - buildings[i + 1],
                        (buildings[i] - buildings[i + 2] < 0) ? 0 : buildings[i] - buildings[i + 2])
                );
            }
        }
        return count;
    }
}
