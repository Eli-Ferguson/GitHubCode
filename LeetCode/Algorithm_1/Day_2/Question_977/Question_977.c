#include <stdio.h>
#include <stdlib.h>

int* sortedSquares(int* nums, int numsSize, int* returnSize)
{
    int * retArr = malloc( numsSize * sizeof(int) );

    int beg = 0;
    int end = numsSize-1;
    int i = numsSize-1;

    while( beg <= end )
    {        
        if( nums[ beg ] * nums[ beg ] >= nums[ end ] * nums[ end ] )
        {
            retArr[ i ] = nums[ beg ] * nums[ beg ];
            beg++;
        }
        else
        {
            retArr[ i ] = nums[ end ] * nums[ end ];
            end--;
        }
        
        i--;
    }

    *returnSize = numsSize;
    return retArr;
}

int main()
{
    int size = 5;
    
    // Note as per the problem this list is sorted in non descending order
    int nums[] = {-4,-1,0,3,10};

    int * result = sortedSquares( nums, size, size );

    for( int a = 0; a < size; a++ )
    {
        printf( "%d ", result[ a ] );
    }printf("\n");

    return 0;
}

//  Beats 96.84% Runtime, 112ms
//  Beats 58.74% Memory, 20.1mb