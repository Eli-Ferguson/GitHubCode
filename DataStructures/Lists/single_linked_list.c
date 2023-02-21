#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int value;
    struct node *next;
} node;

node *removeNode( node *head, int value )
{
    node *prev = head;

    while( head->next != NULL )
    {
        if( head->value == value )
        {
            prev->next = head->next;
        }
    }

    return head;
}

node *pushNode( node *head, node *newNode );
node *appendNode( node *head, node *newNode );
node *createNode();
void printLL( node *head );

int main()
{
    node *head;
    head->next = NULL;
    head->value = 0;

    printLL( head );

    node *newNode = createNode();
    appendNode( head, newNode );

    printLL( head );

    node *newNode2 = createNode();
    head = pushNode( head, newNode2 );

    printLL( head );

    return 0;
}

node *createNode()
{
    int userVal;
    printf( "Enter A Value: " );
    scanf( "%d", &userVal );

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

void printLL( node *head )
{
    while( head->next != NULL )
    {
        printf( "%d -> ", head->value );
        head = head->next;
    }
    printf( "%d\n", head->value );
}