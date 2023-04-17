#include <stdio.h>
#include <stdlib.h>

void reverse( char * s, int pt1, int pt2 )
{
    while( pt1 < pt2 )
    {
        char save = s[ pt1 ];
        s[ pt1 ] = s[ pt2 ];
        s[ pt2 ] = save;

        pt1++;
        pt2--;
    }
}

char * reverseWords(char * s)
{
    int start = 0, end = 0;
    int beg = 1;

    for( int i = 0; s[ i ] != '\0'; i++ )
    {
        if( s[ i ] != ' ' && beg )
        {
            start = i;
            end = i;
            beg = 0;
        }
        else if( s[ i ] != ' ' && !beg )
        {
            end = i;
        }
        else if( s[ i ] == ' ' && !beg )
        {
            reverse( s, start, end );
            beg = 1;
        }
    }

    reverse( s, start, end );

    return s;
}

int main()
{
    int size = 5;
    char * s = calloc( size, sizeof( char ) );
    s[0] = 'h';
    s[1] = 'e';
    s[2] = 'l';
    s[3] = 'l';
    s[4] = 'o';

    for( int i = 0; i < size; i++ ) { printf("%c ", s[ i ] ); }
    printf("\n");

    s = reverseWords( s );

    for( int i = 0; i < size; i++ ) { printf("%c ", s[ i ] ); }
    printf("\n");

    return 0;
}

//  Beats 60.86% Runtime, 8ms
//  Beats 94.19% Memory, 6.8mb