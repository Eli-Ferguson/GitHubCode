#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * licenseKeyFormatting(char * s, int k){

    int originalLen = 0;

    for( int i = 0; s[i] != '\0'; i++ )
    {
        ( s[i] != '-' ) ? originalLen++ : originalLen;
    }

    char * tmpS = (char *)calloc( originalLen, sizeof( char ) );

    for( int idx = 0, i = 0; s[idx] != '\0'; idx++ )
    {
        if( s[idx] != '-' )
        {
            tmpS[i] = s[idx];
            i++;
        }
    }

    s = (char *)malloc( sizeof( tmpS ) );
    memcpy( &s, &tmpS, sizeof( tmpS ) );

    int numberOfDashes = ( originalLen % k == 0 ) ? (originalLen / k) - 1 : originalLen / k;
    tmpS = (char *)calloc( originalLen + numberOfDashes, sizeof( char ) );
    
    int len = originalLen + numberOfDashes;

    for( int j = len-1, i = originalLen-1; j >= 0; i--, j-- )
    {
        if( ( (originalLen-(i)) % k != 0 ) || ( j == 0 ) )
        {
            tmpS[ j ] = s[ i ];
        }
        else
        {
            tmpS[ j ] = s[ i ];
            j--;
            tmpS[ j ] = '-';
        }

    }
    return tmpS;
}

int main()
{
    char * answer = licenseKeyFormatting( "5F3Z-2e-9-w", 4 );
    for( int i = 0; answer[i] != '\0' ; i++ ){printf("%c", answer[i] );} printf("\n");

    char * answer2 = licenseKeyFormatting( "2-5g-3-J", 2 );
    for( int i = 0; answer2[i] != '\0' ; i++ ){printf("%c", answer2[i] );} printf("\n");

    return 0;
}