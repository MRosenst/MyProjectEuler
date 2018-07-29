#include <stdio.h>

int main()
{
    int count = 0;
    for (int i = 0; i <= 200; i++) {
    for (int j = 0; j <= 100; j++) {
    for (int k = 0; k <= 40; k++)  {
    for (int l = 0; l <= 20; l++)  {
    for (int m = 0; m <= 10; m++)  {
    for (int n = 0; n <= 4; n++)   {
    for (int o = 0; o <= 2; o++)   {
    for (int p = 0; p <= 1; p++)   {
        //printf("[%d %d %d %d %d %d %d %d count=%d]\n", i,j,k,l,m,n,o,p, count);
        if (i + 2*j + 5*k + 10*l + 20*m + 50*n + 100*o + 200*p == 200) {
            printf("(%d,%d,%d,%d,%d,%d,%d,%d)\n", i,j,k,l,m,n,o,p);
            count++;
    }}}}}}}}}

    printf("Count: %d\n", count);

    return 0;
}
