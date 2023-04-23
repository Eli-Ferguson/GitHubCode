/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** buildArray(int* target, int targetSize, int n, int* returnSize)
{
    char ** stack = calloc( targetSize*2, sizeof( char * ) * 4 );
    int stackSize = 0;

    for( int i = 0, j = 0; j < targetSize; i++ )
    {
        if( i+1 == target[ j ] )
        {
            stack[ stackSize ] = "Push";
            stackSize++;
            j++;
        }
        else
        {
            stack[ stackSize ] = "Push";
            stackSize++;
            stack[ stackSize ] = "Pop";
            stackSize++;
        }
    }

    *returnSize = stackSize;

    return stack;
}

// Beats 100% Runtime, 0ms
// Beats 45.45% Memory, 6.2mb