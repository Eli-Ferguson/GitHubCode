char * mergeAlternately(char * word1, char * word2)
{
    int len1 = strlen( word1 );
    int len2 = strlen( word2 );

    int minLen = len1 > len2 ? len2 : len1;
    char * newStr = calloc( len1 + len2 + 1, sizeof( char ) );

    int i = 0, c = 0;
    for( i = 0; i < minLen; i++ )
    {
        newStr[ c ] = word1[ i ];
        newStr[ c+1 ] = word2[ i ];
        c += 2;
    }

    while( i < len1 )
    {
        newStr[ c ] = word1[ i ];
        c++;
        i++;
    }

    while( i < len2 )
    {
        newStr[ c ] = word2[ i ];
        c++;
        i++;
    }

    return newStr;
}

// Beats 100% Runtime, 0ms
// Beats 70.9% Memory, 5.8mb