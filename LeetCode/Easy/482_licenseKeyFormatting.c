#include <stdio.h>

char * licenseKeyFormatting(char * s, int k){

    int j = 0;

    char * tmpS = (char *)malloc( sizeof( s ) );

    for( int i = 0; s[i] != NULL; i++ )
    {
        printf("s[%d] = %c", i, s[i] );

        printf(s[i] == '-' ? " True\n" : " False\n" );

        if( s[i] != '-' )
        {
            tmpS[j] = s[i];
            j++;
        }
    }

    // free( s );
    char * s = tmpS;
    // free( tmpS );

    int len = j - 1;

    for( len; len >= 0; len-- )
    {
        len % k != 0 ? printf("%c", s[len] ) : len == 0 ? printf("%c", s[len] ) : printf("%c-", s[len] );
    }
}

int main()
{
    licenseKeyFormatting( "5F3Z-2e-9-w", 4 );

    return 0;
}