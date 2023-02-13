
function bubbleSort( list, ascending=true )
{
    console.log( 'List Pre Sort:\n', list )

    for( let i = 0; i <= list.length - 1; i++ )
    {
        for( let j = 0; j <= list.length - 2; j++ )
        {
            num1 = list[ j ]
            num2 = list[ j + 1 ]

            if( ( num1 >= num2 && ascending ) || ( num1 <= num2 && !ascending ) )
            {
                list[ j + 1 ] = num1
                list[ j ] = num2
            }

        }
    }

    console.log( 'List Post Sort:\n', list )
}

list = []
for( let i = 0; i < 100; i++ ) list.push( Math.round( Math.random() * 100 ) )

// Set Bool to false for descending sort
bubbleSort( list, true )