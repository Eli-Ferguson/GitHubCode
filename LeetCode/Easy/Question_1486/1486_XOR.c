#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int xorOperation(int n, int start){

    int ret = 0;

    for( int i = 0; i < n; i++ )
    {
        ret = ret ^ ( start + ( 2 * i ) );
    }

    return ret;
}

int main()
{
    printf("%d\n", xorOperation( 5, 0) );
    printf("%d\n", xorOperation( 4, 3) );
}

//  Beats 100% Runtime, 0ms
//  Beats 50.94% Memory, 5.5mb