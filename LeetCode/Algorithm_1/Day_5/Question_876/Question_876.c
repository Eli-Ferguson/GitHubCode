#include <stdio.h>
#include <stdlib.h>


// Definition for singly-linked list.
struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode* middleNode(struct ListNode* head)
{
    struct ListNode * mid = head;

    for( int i = 0; head != NULL; i++ )
    {
        if( i % 2 )
        {
            head = head->next;
            mid = mid-> next;
        }
        else
        {
            head = head->next;
        }
    }

    return mid;
}

void addNode( struct ListNode  * head, int val )
{
    while( head->next != NULL )
    {
        head = head->next;
    }
    struct ListNode * newNode = malloc( sizeof( struct ListNode ) );
    newNode->val = val;
    newNode->next = NULL;
    
    head->next = newNode;
}

int main()
{
    int len = 8;
    
    struct ListNode * head = malloc( sizeof( struct ListNode ) );
    head->val = 0;
    head->next = NULL;

    for( int i = 1; i < len; i++ )
    {
        addNode( head, i );
    }    


    struct ListNode * tmp = malloc( sizeof( struct ListNode ) );    
    tmp = head;

    for( int i = 0; tmp != NULL; i++ )
    {
        printf("%d -> ", tmp->val );
        tmp = tmp->next;
    }printf("NULL\n");

    printf("Middel Node Value = %d\n", middleNode( head )->val );

    return 0;
}

//  Beats 100% Runtime, 0ms
//  Beats 40.27% Memory, 6mb