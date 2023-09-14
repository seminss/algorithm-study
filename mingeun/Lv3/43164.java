// 23.9.14 13:37 ~ 13:58
import java.util.*;

class Solution {
    private static final int D = 0;
    private static final int A = 1;
    private List<String> routes;
    
    public String[] solution(String[][] tickets) {
        routes = new ArrayList<>(tickets.length + 1);
        searchAnswer(tickets);
        return selectOneRoute();
    }
    
    private void searchAnswer(String[][] tickets) {
        boolean[] usedTicket = new boolean[tickets.length];
        dfs(tickets, "ICN", usedTicket, 0, "ICN");
    }
    
    private int dfs(String[][] tickets, String dept, 
                   boolean[] used, int depth, String route) {
        if (depth == tickets.length) {
            routes.add(route);
            return 0;
        }
        for (int i = 0; i < tickets.length; i++) {
            if (tickets[i][D].equals(dept) && !used[i]) {
                used[i] = true;
                dfs(tickets, tickets[i][A], used, depth + 1, 
                    route + " " + tickets[i][A]);
                used[i] = false;
            }
        }
        return 0;
    }
    
    private String[] selectOneRoute() {
        Collections.sort(routes);
        return routes.get(0).split(" ");
    }
}
