int max( int i1, int i2 )
{
    if( i1 > i2 ) return i1;
    else return i2;
}

int maxArea(int* height, int heightSize)
{
    int maxWater = 0, i = 0;
    heightSize--;

    while( i < heightSize )
    {
        if( height[ i ] < height[ heightSize ] )
        {
            maxWater = max( maxWater, height[i] * ( heightSize - i ) );
            i++;
        }
        else
        {
            maxWater = max( maxWater, height[ heightSize ] * ( heightSize - i ) );
            heightSize--;
        }
    }

    return maxWater;

}

// Beats 56.87% Runtime, 96ms
// Beats 24.81% Memory, 12mb