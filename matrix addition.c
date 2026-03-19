#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a[10][10], b[10][10], c[10][10];
    int i, j, r1, r2, c1, c2;

    printf("Input the order of both matrices: ");
    scanf("%d %d %d %d", &r1, &c1, &r2, &c2);

    if (r1 != r2 || c1 != c2) {
        printf("Operation is not possible.\n");
        exit(0);
    }

    // Input matrix A
    printf("Enter elements of matrix A:\n");
    for (i = 0; i < r1; i++) {
        for (j = 0; j < c1; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    // Input matrix B
    printf("Enter elements of matrix B:\n");
    for (i = 0; i < r2; i++) {
        for (j = 0; j < c2; j++) {
            scanf("%d", &b[i][j]);
        }
    }

    // Addition
    for (i = 0; i < r1; i++) {
        for (j = 0; j < c1; j++) {
            c[i][j] = a[i][j] + b[i][j];
        }
    }

    // Output result
    printf("Resultant matrix:\n");
    for (i = 0; i < r1; i++) {
        for (j = 0; j < c1; j++) {
            printf("%d ", c[i][j]);
        }
        printf("\n");
    }

    return 0;
}
