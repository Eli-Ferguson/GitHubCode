#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void arrPrint( int * arr, int len )
{
    printf("[ ");
    for(int i = 0; i < len; i++ )
    {
        printf( "%d ", arr[i] );
    } printf("]\n");
}

int * mergeStep( int * arr1, int arr1Len, int * arr2, int arr2Len)
{
    int * retArr = calloc( arr1Len + arr2Len, sizeof( int ) );

    int i = 0, j=0, k=0;

    for( ; j < arr1Len && k < arr2Len; i++ )
    {
        if( arr1[j] < arr2[k] )
        {
            retArr[i] = arr1[j];
            j++;
        }
        else
        {
            retArr[i] = arr2[k];
            k++;
        }
    }

    while( j < arr1Len )
    {
        retArr[i] = arr1[j];
        j++;
        i++;
    }

    while( k < arr2Len )
    {
        retArr[i] = arr2[k];
        k++;
        i++;
    }

    return retArr;
}

int * mergeSort( int * arr, int arrLen )
{
    int low = 0, high = arrLen;
    int mid = ( high - low ) / 2;

    if( arrLen == 1 )
    {
        return arr;
    }

    int * bottomHalf = mergeSort( &arr[low], mid-low );

    int * topHalf = mergeSort( &arr[mid], high-mid );

    return mergeStep( bottomHalf, mid-low, topHalf, high-mid );
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    
    int* retArr = malloc( 2 * sizeof( int ) );

    int * sorted = mergeSort( nums, numsSize );

    int i = 0;
    int j = numsSize-1;

    while( i < j )
    {
        if( sorted[i] + sorted[j] == target ){break;}
        else if( sorted[i] + sorted[j] < target ) {i++;}
        else if( sorted[i] + sorted[j] > target ) {j--;}
    }

    int indexOfI=-1, indexOfJ=-1;

    for( int idx = 0; idx < numsSize; idx++ )
    {
        if( nums[idx] == sorted[i] && idx != indexOfJ && indexOfI == -1)
        {
            indexOfI = idx;
        }
        if( nums[idx] == sorted[j] && idx != indexOfI && indexOfJ == -1)
        {
            indexOfJ = idx;
        }
    }

    *returnSize = 2;
    retArr[0] = indexOfI;
    retArr[1] = indexOfJ;

    return retArr;
}

int main()
{
    int arr[4] = {2,7,11,15};
    int returnSize[2];

    int * retArr = twoSum( arr, 4, 9, returnSize );

    printf( "{%d, %d}\n", retArr[0], retArr[1] );

    return 0;
}

//  Beats 92.94% Runtime, 18ms
//  Beats 5.12% Memory, 18.5mb