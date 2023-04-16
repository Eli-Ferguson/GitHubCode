#include <stdio.h>
#include <stdlib.h>

void moveZeroes(int* nums, int numsSize)
{
    int idx = 0;

    for( int i = 0; i < numsSize; i++ )
    {
        if( nums[ i ] )
        {
            nums[ idx ] = nums[ i ];
            idx++;
        }
    }

    while( idx < numsSize )
    {
        nums[ idx ] = 0;
        idx++;
    }
}

int main()
{
    int size = 5;
    
    int nums[] = {-4,-1,0,3,10};

    moveZeroes( nums, 5 );

    for( int a = 0; a < size; a++ )
    {
        printf( "%d ", nums[ a ] );
    }printf("\n");

    return 0;
}

//  Beats 97.48% Runtime, 76ms
//  Beats 56.5% Memory, 15.2mb