#include <stdio.h>
#include <stdlib.h>

int searchInsert(int* nums, int numsSize, int target)
{
    if( nums[0] >= target ) return 0;
    else if( nums[numsSize - 1] < target ) return numsSize;

    int bottom = 0;
    numsSize--;
    int mid = numsSize / 2;

    while( bottom <= numsSize )
    {
        if( nums[ mid ] == target ) return mid;
        else if( nums[ mid ] > target ) numsSize = mid-1;
        else bottom = mid+1;

        mid = ( bottom + numsSize ) / 2;
    }
    return mid+1;
}

int main()
{
    int nums[7] = {-1,0,3,5,9,12};
    int searchInsertResult = searchInsert( nums, 6, 9);

    printf( "Insert Where: %d", searchInsertResult );

    return 0;
}

//  Beats 91.21% Runtime, 3ms
//  Beats 81.88% Memory, 6mb