#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int value;
    struct node *next;
} node;

node *pushNode( node *head, node *newNode );
node *appendNode( node *head, node *newNode );
node *createNode();

node *removeNodeByValue( node *head, int value );
node *removeNodeByIndex( node *current, int idx );

int getUserVal();

void printLL( node *head );
void freeNode( node *NODE );

int main()
{
    node *head = malloc( sizeof( node ) );
    head->next = NULL;
    head->value = 0;

    printLL( head );

    node *newNode = createNode();
    appendNode( head, newNode );

    printLL( head );

    node *newNode2 = createNode();
    head = pushNode( head, newNode2 );

    printLL( head );

    int valueToRemove = getUserVal();
    // head = removeNodeByValue( head, valueToRemove );
    head = removeNodeByIndex( head, valueToRemove );

    printLL( head );

    return 0;
}

node *createNode()
{
    int userVal = getUserVal();

    node *newNode = ( node *)malloc( sizeof ( node ) );
    newNode->value = userVal;
    newNode->next = NULL;

    return newNode;
}

node *pushNode( node *head, node *newNode )
{
    newNode->next = head;
    return newNode;
}

node *appendNode( node *head, node *newNode )
{
    // O(n) operation for a single linked list

    node *tmp = head;

    while( tmp->next != NULL )
    {
        tmp = tmp->next;
    }

    tmp->next = newNode;
    return head;
}

node *removeNodeByValue( node *current, int value )
{

    if( current->value == value )
    {
        printf( "\tValue %d removed from Linked List\n", value );

        node *ret = current->next;
        freeNode( current );

        return ret;
    }

    node *head = current;
    node *prev = head->next;

    printf( "Target Val = %d\n", value );

    while( current != NULL )
    {
        if( current->value == value )
        {
            printf( "\tValue %d removed from Linked List\n", value );
            prev->next = current->next;
            freeNode( current );
            return head;
        }

        prev = current;
        current = current->next;
    }

    printf( "\tValue %d not in Linked List\n", value );
    return head;
}

node *removeNodeByIndex( node *current, int idx )
{

    if( idx == 0 )
    {
        printf( "\tValue %d removed from Linked List\n", idx );

        if( current == NULL || current->next == NULL )
        {
            return NULL;
        }
        else
        {
            node *ret = current->next;
            freeNode( current );

            return ret;
        }
    }

    node *head = current;
    node *prev = head;
    current = current->next;

    for( int i = 1; current != NULL && i <= idx; i++ )
    {
        if( i == idx )
        {
            prev->next = current->next;
            freeNode( current );
            return head;
        }
        prev = current;
        current = current->next;
    }

    printf( "\tValue %d not in Linked List\n", idx );
    return head;
}

int getUserVal()
{
    int userVal;
    printf( "Enter a Value: " );
    scanf( "%d", &userVal);

    return userVal;
}

void printLL( node *head )
{
    while( head->next != NULL )
    {
        printf( "%d -> ", head->value );
        head = head->next;
    }
    printf( "%d\n", head->value );
}

void freeNode( node *NODE )
{
    // NODE->value = NULL;
    NODE ->next = NULL;
    free( NODE );
}