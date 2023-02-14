#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define Upper(c) ( ( 97 <= (c) && (c) <= 122) ? (c) - 32 : (c) )

int getStringLength( char * s )
{
    int stringLen;

    for( stringLen = 0; *s != '\0'; s++ )
    {
        if( *s != '-' )
        {
            stringLen++;
        }
    }
    return stringLen;
}

char * licenseKeyFormatting( char * s, int k )
{
    int origianlLen = strlen(s);
    int len = getStringLength( s );

    int remainder = len % k;

    int numberOfDashes = (len-1) / k;

    int newLen = len + numberOfDashes;

    char * tmpS = (char *)calloc( newLen + 1, sizeof(char) );
    tmpS[newLen] = '\0';

    for( int newI = newLen-1, oldI = origianlLen-1, charsAdded = 1; charsAdded <= len; )
    {
        if( s[oldI] != '-' )
        {             
            if( charsAdded % k != 0 || charsAdded == len )
            {
                tmpS[newI] = Upper( s[oldI] );
                newI--;
                oldI--;
            }
            else
            {
                tmpS[newI] = Upper( s[oldI] );
                newI--;
                tmpS[newI] = '-';

                newI--;
                oldI--;
            }

            charsAdded++;            
        }
        else
        {
            oldI--;
        }
    }

    return tmpS;
}

int main()
{
    char * answer = licenseKeyFormatting( "5F3Z-2e-9-w", 4 );
    printf("%s\n", answer);

    char * answer2 = licenseKeyFormatting( "2-5g-3-J", 2 );
    printf("%s\n", answer2);

    return 0;
}

//  Beats 76.92% Runtime, 3ms
//  Beats 79.48% Memory, 6.5mb