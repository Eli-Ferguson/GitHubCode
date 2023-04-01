#include <stdio.h>

// Definition for singly-linked list.
struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode *cpyHeadA = headA;
    struct ListNode *cpyHeadB = headB;

    int aLen = 0;
    int bLen = 0;

    while( cpyHeadA != NULL )
    {
        aLen++;
        cpyHeadA = cpyHeadA->next;
    }

    while( cpyHeadB != NULL )
    {
        bLen++;
        cpyHeadB = cpyHeadB->next;
    }

    int lenDiff = aLen - bLen;
    cpyHeadA = headA;
    cpyHeadB = headB;

    while( lenDiff > 0 )
    {
        cpyHeadA = cpyHeadA->next;
        lenDiff--;
    }

    while( lenDiff < 0 )
    {
        cpyHeadB = cpyHeadB->next;
        lenDiff++;
    }

    while( cpyHeadA )
    {
        if( cpyHeadA == cpyHeadB )
        {
            return cpyHeadA;
        }

        cpyHeadA = cpyHeadA->next;
        cpyHeadB = cpyHeadB->next;
    }
    
    return NULL;
}

//  Beats 78.15% Runtime, 38ms
//  Beats 57.12% Memory, 13.9mb