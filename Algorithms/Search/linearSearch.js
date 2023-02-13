
list = []
for( let i = 0; i < 100; i++ ) list.push( Math.round( Math.random() * 100 ) )

function linearSearch( list, target )
{
    for( let i = 0; i < list.length; i++ )
    {
        if( list[i] == target ) return true
    }

    return false
}

console.log( list )
console.log( linearSearch( list , target=10) )