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

    printf("Partial Arr:\t");
    arrPrint( retArr, arr1Len+arr2Len );

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

int main()
{
    int arr[9] = {27, 43, 45, 76, 12, 84, 101, 8, 19};
    int len = 9;

    int * sorted = mergeSort( arr, len );
    printf("Final Array:\t");
    arrPrint( sorted, len );

    return 0;
}