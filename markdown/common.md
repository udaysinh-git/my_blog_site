# Essentials
---

## 1. Linear Search Algorithm

### C Code:
```c
#include <stdio.h>

int linear_search(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

int main() {
    int arr[] = {2, 3, 4, 10, 40};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 10;
    int result = linear_search(arr, n, target);
    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found\n");
    }
    return 0;
}
```

### Pseudocode:
```
function LinearSearch(array, target):
    for i from 0 to length(array) - 1:
        if array[i] == target:
            return i
    return -1
```

---

## 2. Bubble Sort Algorithm

### C Code:
```c
#include <stdio.h>

void bubble_sort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    bubble_sort(arr, n);
    printf("Sorted array: \n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

### Pseudocode:
```
function BubbleSort(array):
    for i from 0 to length(array) - 1:
        for j from 0 to length(array) - i - 2:
            if array[j] > array[j + 1]:
                swap(array[j], array[j + 1])
```

---

## 3. Insertion Sort Algorithm

### C Code:
```c
#include <stdio.h>

void insertion_sort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    insertion_sort(arr, n);
    printf("Sorted array: \n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

### Pseudocode:
```
function InsertionSort(array):
    for i from 1 to length(array) - 1:
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
```

---

## 4. Selection Sort Algorithm

### C Code:
```c
#include <stdio.h>

void selection_sort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        int min_idx = i;
        for (int j = i+1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    selection_sort(arr, n);
    printf("Sorted array: \n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

### Pseudocode:
```
function SelectionSort(array):
    for i from 0 to length(array) - 2:
        min_idx = i
        for j from i + 1 to length(array) - 1:
            if array[j] < array[min_idx]:
                min_idx = j
        swap(array[i], array[min_idx])
```

---

## 5. Binary Search Algorithm

### C Code:
```c
#include <stdio.h>

int binary_search(int arr[], int low, int high, int target) {
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            return mid;
        }
        if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}

int main() {
    int arr[] = {2, 3, 4, 10, 40};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 10;
    int result = binary_search(arr, 0, n - 1, target);
    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found\n");
    }
    return 0;
}
```

### Pseudocode:
```
function BinarySearch(array, target):
    low = 0
    high = length(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        else if array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

---
## 6. Merge Sort Algorithm

Merge Sort is a divide-and-conquer algorithm that divides the array into smaller subarrays, sorts them, and then merges the sorted subarrays.

### C Code
```c
#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];

    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void merge_sort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        merge_sort(arr, l, m);
        merge_sort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr) / sizeof(arr[0]);

    merge_sort(arr, 0, arr_size - 1);

    printf("Sorted array: \n");
    for (int i = 0; i < arr_size; i++)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}
```

### Pseudocode
1. Divide the array into two halves recursively.
2. Sort each half using the same process.
3. Merge the two sorted halves into a single sorted array.

---

## 7. Quick Sort Algorithm

Quick Sort is another divide-and-conquer algorithm. It selects a pivot element and partitions the array around the pivot.

### C Code
```c
#include <stdio.h>

void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quick_sort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quick_sort(arr, low, pi - 1);
        quick_sort(arr, pi + 1, high);
    }
}

int main() {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    quick_sort(arr, 0, n - 1);
    printf("Sorted array: \n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}
```

### Pseudocode
1. Select a pivot element.
2. Partition the array into elements less than the pivot and greater than the pivot.
3. Recursively apply Quick Sort to the subarrays.

---

## 8. Strassen’s Matrix Multiplication Algorithm (2x2)

Strassen’s algorithm multiplies two matrices faster than the standard matrix multiplication algorithm.

### C Code
```c
#include <stdio.h>

void strassen_multiply(int A[2][2], int B[2][2], int C[2][2]) {
    int M1 = (A[0][0] + A[1][1]) * (B[0][0] + B[1][1]);
    int M2 = (A[1][0] + A[1][1]) * B[0][0];
    int M3 = A[0][0] * (B[0][1] - B[1][1]);
    int M4 = A[1][1] * (B[1][0] - B[0][0]);
    int M5 = (A[0][0] + A[0][1]) * B[1][1];
    int M6 = (A[1][0] - A[0][0]) * (B[0][0] + B[0][1]);
    int M7 = (A[0][1] - A[1][1]) * (B[1][0] + B[1][1]);

    C[0][0] = M1 + M4 - M5 + M7;
    C[0][1] = M3 + M5;
    C[1][0] = M2 + M4;
    C[1][1] = M1 - M2 + M3 + M6;
}

int main() {
    int A[2][2] = {{1, 2}, {3, 4}};
    int B[2][2] = {{5, 6}, {7, 8}};
    int C[2][2];

    strassen_multiply(A, B, C);

    printf("Result matrix: \n");
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

### Pseudocode
1. Calculate seven intermediate products using matrix addition and subtraction.
2. Combine the results to form the final product matrix.

---
## 9. Knapsack Problem (0/1 Knapsack)

The 0/1 Knapsack problem is a combinatorial optimization problem where you are given weights, values of items, and a maximum capacity. The goal is to maximize the total value without exceeding the capacity.

### C Code
```c
#include <stdio.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

void knapsack(int W, int wt[], int val[], int n) {
    int K[n + 1][W + 1];

    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (i == 0 || w == 0)
                K[i][w] = 0;
            else if (wt[i - 1] <= w)
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
            else
                K[i][w] = K[i - 1][w];
        }
    }

    printf("Maximum value: %d\n", K[n][W]);

    printf("Selected items: ");
    int w = W;
    for (int i = n; i > 0 && K[i][w] > 0; i--) {
        if (K[i][w] != K[i - 1][w]) {
            printf("%d ", i - 1);
            w -= wt[i - 1];
        }
    }
    printf("\n");
}

int main() {
    int val[] = {60, 100, 120};
    int wt[] = {10, 20, 30};
    int W = 50;
    int n = sizeof(val) / sizeof(val[0]);

    knapsack(W, wt, val, n);
    return 0;
}
```

### Pseudocode
1. Initialize a table to store maximum values for subproblems.
2. Use dynamic programming to fill the table:
   - If the weight of the current item exceeds the capacity, exclude it.
   - Otherwise, include or exclude it, taking the maximum value.
3. Backtrack to find the selected items.

---

## 10. Graph Coloring Problem

The Graph Coloring problem assigns colors to vertices of a graph so that no two adjacent vertices share the same color.

### C Code
```c
#include <stdbool.h>
#include <stdio.h>

#define V 4

bool is_safe(int v, bool graph[V][V], int color[], int c) {
    for (int i = 0; i < V; i++)
        if (graph[v][i] && color[i] == c)
            return false;
    return true;
}

bool graph_coloring_util(bool graph[V][V], int m, int color[], int v) {
    if (v == V)
        return true;

    for (int c = 1; c <= m; c++) {
        if (is_safe(v, graph, color, c)) {
            color[v] = c;

            if (graph_coloring_util(graph, m, color, v + 1))
                return true;

            color[v] = 0;
        }
    }

    return false;
}

bool graph_coloring(bool graph[V][V], int m) {
    int color[V] = {0};

    if (!graph_coloring_util(graph, m, color, 0)) {
        printf("Solution does not exist.\n");
        return false;
    }

    printf("Solution exists: Following are the assigned colors:\n");
    for (int i = 0; i < V; i++)
        printf("Vertex %d -> Color %d\n", i, color[i]);
    return true;
}

int main() {
    bool graph[V][V] = {
        {0, 1, 1, 1},
        {1, 0, 1, 0},
        {1, 1, 0, 1},
        {1, 0, 1, 0},
    };
    int m = 3;

    graph_coloring(graph, m);
    return 0;
}
```

### Pseudocode
1. Start with the first vertex and try to assign a color.
2. Check if the color assignment violates constraints.
3. Recursively assign colors to the next vertices.
4. Backtrack if no valid color is found.

---

## 11. N-Queen Problem

The N-Queen problem places N queens on an N×N chessboard so that no two queens threaten each other.

### C Code
```c
#include <stdbool.h>
#include <stdio.h>
#define N 8

void print_solution(int board[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            printf("%d ", board[i][j]);
        printf("\n");
    }
}

bool is_safe(int board[N][N], int row, int col) {
    for (int i = 0; i < col; i++)
        if (board[row][i])
            return false;

    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;

    for (int i = row, j = col; j >= 0 && i < N; i++, j--)
        if (board[i][j])
            return false;

    return true;
}

bool solve_nq_util(int board[N][N], int col) {
    if (col >= N)
        return true;

    for (int i = 0; i < N; i++) {
        if (is_safe(board, i, col)) {
            board[i][col] = 1;

            if (solve_nq_util(board, col + 1))
                return true;

            board[i][col] = 0;
        }
    }

    return false;
}

void solve_nq() {
    int board[N][N] = {0};

    if (!solve_nq_util(board, 0)) {
        printf("Solution does not exist.\n");
        return;
    }

    print_solution(board);
}

int main() {
    solve_nq();
    return 0;
}
```

### Pseudocode
1. Start with the first column.
2. Place a queen in a safe row of the column.
3. Recursively try to place queens in the subsequent columns.
4. Backtrack if a solution is not possible.

---
## 12. Travelling Salesman Problem (TSP)

The Travelling Salesman Problem is a classic optimization problem where a salesman must visit a set of cities, each only once, and return to the starting city while minimizing the total travel cost.

### Problem Statement
Given a cost matrix where `cost[i][j]` represents the cost of traveling from city `i` to city `j`, find the minimum cost to complete the tour.

### Solution using Dynamic Programming (Held-Karp Algorithm)

#### C Code
```c
#include <stdio.h>
#include <limits.h>

#define MAX 100
#define INF INT_MAX

int tsp(int graph[MAX][MAX], int n) {
    int dp[1 << n][n];
    for (int i = 0; i < (1 << n); i++)
        for (int j = 0; j < n; j++)
            dp[i][j] = INF;

    dp[1][0] = 0;

    for (int mask = 1; mask < (1 << n); mask++) {
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                for (int j = 0; j < n; j++) {
                    if (mask & (1 << j) && j != i && graph[j][i] != INF) {
                        dp[mask][i] = 
                            dp[mask][i] < dp[mask ^ (1 << i)][j] + graph[j][i]
                            ? dp[mask][i]
                            : dp[mask ^ (1 << i)][j] + graph[j][i];
                    }
                }
            }
        }
    }

    int min_cost = INF;
    for (int i = 1; i < n; i++) {
        if (graph[i][0] != INF) {
            min_cost = min_cost < dp[(1 << n) - 1][i] + graph[i][0]
                       ? min_cost
                       : dp[(1 << n) - 1][i] + graph[i][0];
        }
    }

    return min_cost;
}

int main() {
    int n = 4;
    int graph[MAX][MAX] = {
        {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0}
    };

    int result = tsp(graph, n);
    printf("The minimum cost of the tour is: %d\n", result);
    return 0;
}
```

### Pseudocode
1. Initialize a DP table `dp[mask][i]`:
   - `mask` represents the set of visited cities.
   - `i` is the current city.
2. Set the base case: `dp[1 << i][i] = cost[0][i]`.
3. For each subset of cities (`mask`), update the cost for visiting a new city.
4. Calculate the minimum cost to return to the starting city.
5. Return the minimum cost.

---
