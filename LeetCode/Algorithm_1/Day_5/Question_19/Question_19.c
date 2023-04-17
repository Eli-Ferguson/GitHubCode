#include <stdio.h>
#include <stdlib.h>


// Definition for singly-linked list.
struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode* removeNthFromEnd(struct ListNode* head, int n)
{
    struct ListNode * pt1 = head;
    struct ListNode * pt2 = head;

    for( int i = 0; pt2->next != NULL; i++ )
    {
        if( n > 0 )
        {
            pt2 = pt2->next;
            n--;
        }
        else
        {
            pt2 = pt2->next;
            pt1 = pt1->next;
        }
    }

    if( n > 0 )
    {
        head = head->next;
        return head;
    }

    if( pt1->next != NULL )
    {
        if( pt1->next->next != NULL )
        {
            pt1->next = pt1->next->next;
        }
        else
        {
            pt1->next = NULL;
        }
    }
    else
    {
        return NULL;
    }

    return head;
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

    tmp = removeNthFromEnd( head, 3 );

    for( int i = 0; tmp != NULL; i++ )
    {
        printf("%d -> ", tmp->val );
        tmp = tmp->next;
    }printf("NULL\n");

    return 0;
}

//  Beats 43.47% Runtime, 3ms
//  Beats 99.13% Memory, 5.7mb