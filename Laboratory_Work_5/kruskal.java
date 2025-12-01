import java.util.*;

public class Main {

    static class Edge {
        int u, v, w;
        Edge(int u, int v, int w) { this.u = u; this.v = v; this.w = w; }
    }

    public static void main(String[] args) {
        System.out.println("=== Алгоритм Крускала ===");

        List<Edge> edges = new ArrayList<>();

        edges.add(new Edge(1,4,7));
        edges.add(new Edge(4,2,3));
        edges.add(new Edge(4,5,9));
        edges.add(new Edge(1,6,8));
        edges.add(new Edge(1,3,6));
        edges.add(new Edge(3,2,1));
        edges.add(new Edge(3,8,7));
        edges.add(new Edge(2,6,2));
        edges.add(new Edge(2,7,4));
        edges.add(new Edge(6,8,3));
        edges.add(new Edge(8,7,4));
        edges.add(new Edge(5,7,5));

        kruskal(edges, 8);
    }

    static void kruskal(List<Edge> edges, int n) {
        edges.sort(Comparator.comparingInt(e -> e.w));

        int[] parent = new int[n+1];
        for (int i = 1; i <= n; i++) parent[i] = i;

        List<Edge> mst = new ArrayList<>();

        for (Edge e : edges) {
            if (find(parent, e.u) != find(parent, e.v)) {
                union(parent, e.u, e.v);
                mst.add(e);
                if (mst.size() == n - 1) break;
            }
        }

        int total = 0;
        System.out.println("Ребра МКД (Kruskal):");
        for (Edge e : mst) {
            System.out.println(e.u + " - " + e.v + " : " + e.w);
            total += e.w;
        }
        System.out.println("Сумарна вага = " + total);
    }

    static int find(int[] p, int x) {
        if (p[x] == x) return x;
        return p[x] = find(p, p[x]);
    }

    static void union(int[] p, int a, int b) {
        a = find(p, a);
        b = find(p, b);
        p[b] = a;
    }
}
