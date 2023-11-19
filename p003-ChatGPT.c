//The prime factors of 13195 are 5, 7, 13 and 29.
//What is the largest prime factor of the number 600851475143?

#include <stdio.h>
#include <math.h>

long largestPrimeFactor(long n) {
    long maxPrime = -1;

    // Divide out the 2s
    while (n % 2 == 0) {
        maxPrime = 2;
        n /= 2;
    }

    // At this point, n must be odd. Starting from 3, check for prime factors
    for (long i = 3; i <= sqrt(n); i += 2) {
        while (n % i == 0) {
            maxPrime = i;
            n = n / i;
        }
    }

    // If n is a prime number greater than 2
    if (n > 2) {
        maxPrime = n;
    }

    return maxPrime;
}

int main() {
    long number = 600851475143;
    printf("The largest prime factor of %ld is %ld\n", number, largestPrimeFactor(number));
    return 0;
}
