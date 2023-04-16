#include <stdio.h>
#include <stdlib.h>

void reverse( int * arr, int start, int end )
{
    int save;
    while( start < end )
    {
        save = arr[ start ];
        arr[ start ] = arr[ end ];
        arr[ end ] = save;

        start++;
        end--;
    }
}

void rotate(int* nums, int numsSize, int k)
{
    k = k % numsSize;
    if (k == 0 || numsSize == 1) return; 
    
    reverse( nums, 0, numsSize-1 );
    reverse( nums, 0, k-1 );
    reverse( nums, k, numsSize-1 );
}

int main()
{
    int size = 5;
    
    int nums[] = {-4,-1,0,3,10};

    rotate( nums, 5, 3 );

    for( int a = 0; a < size; a++ )
    {
        printf( "%d ", nums[ a ] );
    }printf("\n");

    return 0;
}

//  Beats 93.63% Runtime, 113ms
//  Beats 97.43% Memory, 22mb