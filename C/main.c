#include<stdio.h>

//#define VERSION 2

int main()
{
#ifdef VERSION
    printf("Version %d is compiled.\n", VERSION);
#else
    printf("No version defined.\n");
#endif

    return 0;
}
