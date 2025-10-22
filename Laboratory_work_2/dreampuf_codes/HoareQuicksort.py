digraph HoareQuicksort {
    rankdir=TB;
    node [shape=rect, fontname="Arial", fontsize=11, style="rounded,filled", fillcolor="#FFFFFF"];

    main [label="Основний виклик\n[41, 52, 47, 65, 95, 38, 15, 50, 99]\nl=0, r=8"];

    subgraph cluster_left {
        label="Лівий підмасив";
        color=black;
        fontname="Arial";
        fontsize=11;


        L1 [label="[99, 52, 47, 65, 95, 38]\nl=0, r=5"];
        L2 [label="[38, 52, 47, 65, 95]\nl=0, r=4"];
        L3a [label="[38]\nl=0, r=0"];
        L3b [label="[52, 47, 65, 95]\nl=1, r=4"];
        L4a [label="[47, 52]\nl=1, r=2"];
        L4b [label="[65, 95]\nl=3, r=4"];
        L5a [label="[47]\nl=1, r=1"];
        L5b [label="[52]\nl=2, r=2"];
        L5c [label="[65]\nl=3, r=3"];
        L5d [label="[95]\nl=4, r=4"];
    }

    subgraph cluster_right {
        label="Правий підмасив";
        color=black;
        fontname="Arial";
        fontsize=11;

        R1 [label="[50, 99]\nl=6, r=8"];
        R2a [label="[50]\nl=6, r=6"];
        R2b [label="[99]\nl=8, r=8"];
    }

    // --- Connections ---
    main -> L1;
    main -> R1;
    L1 -> L2;
    L2 -> L3a;
    L2 -> L3b;
    L3b -> L4a;
    L3b -> L4b;
    L4a -> L5a;
    L4a -> L5b;
    L4b -> L5c;
    L4b -> L5d;
    R1 -> R2a;
    R1 -> R2b;

    // --- Sorted result ---
    sorted [label="Фінальний відсортований масив\n[15, 38, 41, 47, 50, 52, 65, 95, 99]"];
    R2b -> sorted;
}
