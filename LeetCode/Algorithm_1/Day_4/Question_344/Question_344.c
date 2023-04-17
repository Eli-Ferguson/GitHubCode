#include <stdio.h>
#include <stdlib.h>

void reverseString(char* s, int sSize)
{
    int pt1 = 0;
    sSize--;

    while( pt1 < sSize )
    {
        char save = s[ pt1 ];

        s[ pt1 ] = s[ sSize ];
        s[ sSize ] = save;

        pt1++;
        sSize--;
    }
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

    reverseString( s, size );

    for( int i = 0; i < size; i++ ) { printf("%c ", s[ i ] ); }
    printf("\n");

    return 0;
}

//  Beats 93.48% Runtime, 47ms
//  Beats 92.26% Memory, 12.2mb