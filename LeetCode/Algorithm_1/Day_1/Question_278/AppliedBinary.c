#include <stdio.h>
#include <stdlib.h>

int firstBadVersion(int n)
{
    long int bottom = 0;
    long int mid = n / 2;
    long int top = n;

    while( bottom != top )
    {
        if( isBadVersion(mid) ) top = mid;
        else bottom = mid+1;

        mid = (bottom + top) / 2;
    }

    return mid;
}

// No Main Available as LeetCode uses outside functions to verify isBadVersion
// You can copy this function into question 278 to test with no edits to the code

//  Beats 100% Runtime, 0ms
//  Beats 69.4% Memory, 5.4mb