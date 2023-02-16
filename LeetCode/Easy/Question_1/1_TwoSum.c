#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    
    int* retArr = malloc( 2 * sizeof( int ) );

    for( int i = 0; i < numsSize; i++ )
    {
        for( int j = i+1; j < numsSize; j++ )
        {
            if( ( nums[i] + nums[j] ) == target )
            {                
                *returnSize = 2;
                retArr[0] = i;
                retArr[1] = j;

                return retArr;
            }
        }
    }

    *returnSize = 0;
    return retArr;
}

int main()
{
    int arr[3] = {1,2,3};
    int returnSize[2];

    int * retArr = twoSum( arr, 3, 5, returnSize );

    printf( "{%d, %d}\n", retArr[0], retArr[1] );

    return 0;
}

//  Beats 57.27% Runtime, 139ms
//  Beats 48.47% Memory, 6.5mb