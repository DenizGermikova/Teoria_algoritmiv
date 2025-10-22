digraph IterativeMergeSort {
    rankdir=TB;
    node [shape=rect, style=filled, fontname="Arial", fontsize=11];

    start [label="Початковий масив\n[41, 52, 47, 65, 95, 38, 15, 50, 99]", fillcolor="#FFD580"];

    // --- Pass 1 ---
    p1a [label="Злиття [41] та [52]\n[41, 52]", fillcolor="#B4E197"];
    p1b [label="Злиття [47] та [65]\n[47, 65]", fillcolor="#B4E197"];
    p1c [label="Злиття [95] та [38]\n[38, 95]", fillcolor="#B4E197"];
    p1d [label="Злиття [15] та [50]\n[15, 50]", fillcolor="#B4E197"];
    p1e [label="[99]", fillcolor="#B4E197"];

    // --- Pass 2 ---
    p2a [label="Злиття [41, 52] та [47, 65]\n[41, 47, 52, 65]", fillcolor="#A1DD70"];
    p2b [label="Злиття [38, 95] та [15, 50]\n[15, 38, 50, 95]", fillcolor="#A1DD70"];
    p2c [label="[99]", fillcolor="#A1DD70"];

    // --- Pass 3 ---
    p3a [label="Фінальне злиття [41, 47, 52, 65]\nта [15, 38, 50, 95]\n[15, 38, 41, 47, 50, 52, 65, 95, 99]", fillcolor="#6CC24A"];

    // --- Sorted ---
    sorted [label="Відсортований масив\n[15, 38, 41, 47, 50, 52, 65, 95, 99]", fillcolor="#C5F5A5"];

    // --- connections ---
    start -> p1a -> p2a;
    start -> p1b -> p2a;
    start -> p1c -> p2b;
    start -> p1d -> p2b;
    start -> p1e -> p2c;
    p2a -> p3a;
    p2b -> p3a;
    p2c -> p3a;
    p3a -> sorted;
}
