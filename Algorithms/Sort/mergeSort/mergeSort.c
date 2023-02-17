#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int * mergeStep( int * arr1, int arr1Len, int * arr2, int arr2Len)
{
    int * retArr = calloc( arr1Len + arr2Len, sizeof( int ) );

    // printf("%d %d %d\n", arr1[0], arr2[0], arr2[1] );

    int i = 0, j=0, k=0;

    for( ; j < arr1Len && k < arr2Len; i++ )
    {
        printf( "i=%d\n", i );
        printf( "\tarr1[%d]=%d arr2[%d]=%d\n", j, arr1[j], k, arr2[k] );

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

    printf( "i=%d j=%d k=%d\n", i, j, k );

    while( j < arr1Len )
    {
        printf( "i=%d j=%d k=%d\n", i, j, k );
        retArr[i] = arr1[j];
        j++;
        i++;
    }

    while( k < arr2Len )
    {
        printf( "i=%d j=%d k=%d\n", i, j, k );
        retArr[i] = arr1[j];
        j++;
        i++;
    }

    printf("Ret Arr:\n\t");
    for(int i = 0; i < ( arr1Len + arr2Len ); i++ )
    {
        printf( "%d ", retArr[i] );
    } printf("\n");

    return retArr;
}

int * mergeSplit( int * arr, int start, int arrLen )
{

    printf( "Start : %d\nLen : %d\n", start, arrLen );

    if( arrLen == 1 )
    {
        return arr;
    }
    else if( arrLen == 2 )
    {
        if( arr[0] > arr[1] )
        {
            int * ret = calloc( 2, sizeof( int ) );
            ret[0] = arr[1];
            ret[1] = arr[0];
            return ret;
        }
        else
        {
            int * ret = calloc( 2, sizeof( int ) );
            ret[0] = arr[0];
            ret[1] = arr[1];
            return ret;
        }
    }

    int low = start, high = arrLen;
    int mid = ( high - low ) / 2;

    printf( "Low : %d\nMid : %d\nHigh : %d\n\n", low, mid, high);

    int * bottomHalf = mergeSplit( &arr[low], low, mid-low );
    int * topHalf = mergeSplit( &arr[mid], mid, high-mid );

    return mergeStep( bottomHalf, mid-low, topHalf, high-mid );
}

int main()
{
    int arr[3] = {1,3,5};
    int len = 3;

    int arr2[3] = {2,4,6};
    int len2 = 3;

    mergeStep( arr, len, arr2, len2 );

    // mergeSplit( arr, 0, len );

    return 0;
}