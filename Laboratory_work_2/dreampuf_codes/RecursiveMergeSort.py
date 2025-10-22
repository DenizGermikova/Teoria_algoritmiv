digraph RecursiveMergeSort {
    rankdir=TB;
    node [shape=rect, style="filled,rounded", fontname="Arial", fontsize=11, fillcolor="#E6F2FF", color="#7FA6C1"];

    // Головний виклик
    start [label="Початковий виклик\n[41, 52, 47, 65, 95, 38, 15, 50, 99]", shape=rect, fillcolor="#FFF5CC", color="#D1A000"];

    // Розділення
    subgraph cluster_split {
        label="Етап розділення";
        color="#B3CDE0";

        l1 [label="[41, 52, 47, 65, 95]"];
        r1 [label="[38, 15, 50, 99]"];

        l2a [label="[41, 52, 47]"];
        l2b [label="[65, 95]"];
        r2a [label="[38, 15]"];
        r2b [label="[50, 99]"];

        l3a1 [label="[41]"];
        l3a2 [label="[52]"];
        l3a3 [label="[47]"];
        l3b1 [label="[65]"];
        l3b2 [label="[95]"];
        r3a1 [label="[38]"];
        r3a2 [label="[15]"];
        r3b1 [label="[50]"];
        r3b2 [label="[99]"];
    }

    // Етап злиття
    subgraph cluster_merge {
        label="Етап злиття";
        color="#B3E6B3";

        m1 [label="[41,52,47] → [41,47,52]"];
        m2 [label="[65,95] → [65,95]"];
        m3 [label="[38,15] → [15,38]"];
        m4 [label="[50,99] → [50,99]"];

        left_merge [label="[41,47,52,65,95]"];
        right_merge [label="[15,38,50,99]"];

        final [label="[15,38,41,47,50,52,65,95,99]", fillcolor="#D8FAD8", color="#6DB36D"];
    }

    // connections
    start -> l1 [label="ліва частина"];
    start -> r1 [label="права частина"];

    // left splits
    l1 -> l2a;
    l1 -> l2b;
    l2a -> l3a1;
    l2a -> l3a2;
    l2a -> l3a3;
    l2b -> l3b1;
    l2b -> l3b2;

    // right splits
    r1 -> r2a;
    r1 -> r2b;
    r2a -> r3a1;
    r2a -> r3a2;
    r2b -> r3b1;
    r2b -> r3b2;

    // merges
    l2a -> m1;
    l2b -> m2;
    r2a -> m3;
    r2b -> m4;

    m1 -> left_merge;
    m2 -> left_merge;
    m3 -> right_merge;
    m4 -> right_merge;

    left_merge -> final;
    right_merge -> final;
}
