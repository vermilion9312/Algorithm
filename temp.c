#include <stdio.h>

int main (void)
{
    char changeList[4] = { 25, 10, 5, 1 };
    char testCase = getchar();
    for (int i = 0; i < testCase; i++)
    {
        char change = getchar();
        for (int j = 0; j < sizeof(changeList); j++)
        {
            putchar(change / changeList[j]);
            change %= changeList[j];
        }
    }

    return 0;
}