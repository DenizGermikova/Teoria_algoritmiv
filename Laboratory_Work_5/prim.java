import java.util.*;

public class Main {

    public static void main(String[] args) {
        System.out.println("=== Алгоритм Пріма ===");

        // Створюємо граф (1..8)
        Map<Integer, List<int[]>> g = new HashMap<>();
        for (int i = 1; i <= 8; i++) g.put(i, new ArrayList<>());

        addEdge(g, 1,4,7);
        addEdge(g, 4,2,3);
        addEdge(g, 4,5,9);
        addEdge(g, 1,6,8);
        addEdge(g, 1,3,6);
        addEdge(g, 3,2,1);
        addEdge(g, 3,8,7);
        addEdge(g, 2,6,2);
        addEdge(g, 2,7,4);
        addEdge(g, 6,8,3);
        addEdge(g, 8,7,4);
        addEdge(g, 5,7,5);

        prim(g, 1);
    }

    static void addEdge(Map<Integer, List<int[]>> g, int a, int b, int w) {
        g.get(a).add(new int[]{b, w});
        g.get(b).add(new int[]{a, w});
    }

    static void prim(Map<Integer, List<int[]>> g, int start) {
        Set<Integer> used = new HashSet<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[2]));
        List<int[]> mst = new ArrayList<>();

        used.add(start);
        for (int[] e : g.get(start)) pq.add(new int[]{start, e[0], e[1]});

        while (mst.size() < g.size() - 1) {
            int[] cur = pq.poll();
            if (cur == null) break; // захист на випадок не з'єднаного графа
            if (used.contains(cur[1])) continue;

            mst.add(cur);
            used.add(cur[1]);

            for (int[] e : g.get(cur[1])) {
                if (!used.contains(e[0])) pq.add(new int[]{cur[1], e[0], e[1]});
            }
        }

        int total = 0;
        System.out.println("Ребра МКД (Prim):");
        for (int[] e : mst) {
            System.out.println(e[0] + " - " + e[1] + " : " + e[2]);
            total += e[2];
        }
        System.out.println("Сумарна вага = " + total);
    }
}
