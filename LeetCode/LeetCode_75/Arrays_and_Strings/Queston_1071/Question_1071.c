int isDivisor( char * str, char * divisor, int divisorLen )
{
    for( int i = 0, d = 0; str[ i ] != '\0'; i++ )
    {
        if( str[ i ] != divisor[ d ] ) return 0;

        if( d == divisorLen ) d = 0;
        else d++;
    }
    return 1;
}

char * gcdOfStrings(char * str1, char * str2)
{
    int strlen1 = strlen( str1 );
    int strlen2 = strlen( str2 );

    int maxSize = strlen1 > strlen2 ? strlen2 : strlen1;
    char * test = calloc( maxSize + 1, sizeof( char ) );

    int divisor = 0;
    for( int i = 0; str1[ i ] != '\0' && str2[ i ] != '\0' && str1[ i ] == str2[ i ]; i++ )
    {
        test[ i ] = str1[ i ];

        if(
            strlen1 % ( i + 1 ) == 0 &&
            strlen2 % ( i + 1 ) == 0 &&
            isDivisor( str1, test, i ) == 1 &&
            isDivisor( str2, test, i ) == 1
        )
        {
            divisor = i+1;
        }

    }

    char * ret = calloc( divisor + 1, sizeof( char ) );
    
    for( int i = 0; i < divisor; i++ ) ret [ i ] = test[ i ];

    return ret;
}

// Beats 100% Runtime, 0ms
// Beats 14.29% Memory, 6.1mb