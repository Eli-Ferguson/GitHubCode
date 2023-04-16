#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize)
{
    int * retArr = calloc( 2, sizeof(int) );
    int bottom = 0;
    int top = numbersSize-1;
    int mid = ( top + bottom ) / 2;

    while( top != bottom )
    {
        if( numbers[ bottom ] + numbers[ top ] == target ) 
        {
            break;
        }

        // First two conditions check to see if we can use binary search
        // to cut the top half or bottom half
        // else proceed like normal
        if( numbers[ bottom ] + numbers[ mid ] >= target )
        {
            top = mid;
        }
        else if( numbers[ mid ] + numbers[ top ] <= target )
        {
            bottom = mid;
        }
        else if( numbers[ bottom ] + numbers[ top ] < target )
        {
            bottom++;
        }
        else
        {
            top--;
        }

        mid = ( top + bottom ) / 2;
    }

    *returnSize = 2;
    retArr[0] = bottom+1;
    retArr[1] = top+1;

    return retArr;
}

int main()
{
    int size = 5;
    
    int * nums = calloc( size, sizeof(int) );
    for( int i = 0; i < size; i++ ) nums[i] = i;

    int ret;
    int * retArr = twoSum( nums, 5, 7, &ret);

    printf("retArr = [%d, %d]\n", retArr[0], retArr[1] );

    return 0;
}

//  Beats 97.93% Runtime, 10ms
//  Beats 7.97% Memory, 7.5mb