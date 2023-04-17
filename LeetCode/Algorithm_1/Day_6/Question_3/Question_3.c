#include <stdio.h>
#include <stdlib.h>

int hasRepeat( char * s, int start, int end, char test )
{
    while( start < end )
    {
        if( s[ start ] == test ) return 1;
        start++;
    }

    return 0;
}

int lengthOfLongestSubstring(char * s)
{
    int start = 0, end = 0, longest = 0;

    while( s[ end ] != '\0' )
    {
        if( !hasRepeat( s, start, end, s[ end ] ) )
        {
            if( ( end - start ) >= longest ) longest++;
            end++;
        }
        else
        {
            start++;
        }
    }

    return longest;
}

int main()
{
    printf("Longest SubString No Repeat Chars: %d\n", lengthOfLongestSubstring( "abcabcbb" ) );

    return 0;
}

//  Beats 43.47% Runtime, 3ms
//  Beats 99.13% Memory, 5.7mb