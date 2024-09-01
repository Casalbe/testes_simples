#include <stdio.h>

int isFibonacci(int n) {
    int a = 0, b = 1, c = 0;

    while (c < n) {
        c = a + b;
        a = b;
        b = c;
    }

    return c == n || n == 0;
}

int main() {
    int num;

    printf("Informe um numero: ");
    scanf("%d", &num);

    if (isFibonacci(num)) {
        printf("%d pertence à sequência de Fibonacci.\n", num);
    } else {
        printf("%d não pertence à sequência de Fibonacci.\n", num);
    }

    return 0;
}
