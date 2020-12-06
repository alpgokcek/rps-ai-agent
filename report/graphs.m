clear all; clc;
size = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000];
nlgn = [0.000308,
0.000143,
0.000365,
0.001293,
0.002357,
0.014938,
0.029693,
0.275072,
0.327912];

n = [0.000025,
0.000028,
0.000043,
0.000088,
0.000232,
0.000993,
0.001529,
0.011182,
0.018655,
    ];

n2 = [0.000024,
0.000173,
0.000558,
0.011872,
0.048077,
1.120954,
4.944334,
132.476787,
559.559621,
    ];

plot(size, nlgn,'LineWidth',2, 'DisplayName','O(nlgn)')
title("O(n), O(nlgn) and O(n^2) comparison"); xlabel("Array Size"); ylabel("Time (sec)")
hold on 
plot(size, n,'LineWidth',2,'DisplayName','O(n)')
plot(size, n2,'LineWidth',2,'DisplayName','O(n^2)')
hold off
legend()