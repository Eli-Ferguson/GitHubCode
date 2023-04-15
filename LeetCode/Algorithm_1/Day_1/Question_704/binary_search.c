#include <stdio.h>
#include <stdlib.h>

int search(int* nums, int numsSize, int target)
    {
        int bottom = 0;
        numsSize--;

        while( bottom <= numsSize )
        {
            int mid = ( numsSize + bottom ) / 2;

            if( nums[mid] == target ) return mid;
            else if( nums[mid] > target ) numsSize = mid-1;
            else bottom = mid+1;
        }

        return -1;
    }

int main()
{
    int nums[7] = {-1,0,3,5,9,12};
    int searchResult = search( nums, 6, 9);

    printf( "Search Returns: %d", searchResult );

    return 0;
}

//  Beats 74.86% Runtime, 38ms
//  Beats 96.85% Memory, 7mb