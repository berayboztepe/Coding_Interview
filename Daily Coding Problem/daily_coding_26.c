####This problem was asked by Google.
####Given a singly linked list and an integer k, remove the kth last element from the list. 
###k is guaranteed to be smaller than the length of the list.
##The list is very long, so making more than one pass is prohibitively expensive.
#Do this in constant space and in one pass.



#include <stdio.h>
#include <stdlib.h>

struct node{
    int key;
    struct node *next;
};
typedef struct node node;


node* CreateNode(int key){

    node* n = (node *)malloc(sizeof(node));
    n->key = key;
    n->next =  NULL;


    return n;

};

node* delete_node(node** n, int k){
    node * iter = *n;
    int counter = 0;
    while(iter != NULL ){
        counter++;
        iter = iter->next;
    }
    if(k > counter || k < 1){
        printf("\nk is greater or smaller than the list range!\n");
        printf("Nothing has changed\n");
        return;
    }

    iter = *n;
    if((counter-1-k) == -1){
        (*n) = (*n)->next;
        free(iter);
        return n;
    }

    for(int i = 0; i < (counter-1-k);i++){
            iter = iter->next;
        }

    node* temp = iter->next;
    iter->next = temp->next;
    temp->next = NULL;
    free(temp);

    return n;

}

void print(node* n){
    printf("List is = ");
    while(n != NULL){
        printf(" %d ", n -> key);
        n = n -> next;
    }

    printf("\n");


}

int main()
{

   node* n = CreateNode(1);


   n->next = CreateNode(2);

   n->next->next = CreateNode(3);

   n->next->next->next = CreateNode(4);

   n->next->next->next->next = CreateNode(5);

   printf("Write a number :");
   int k ;
   scanf("%d", &k);


    delete_node(&n, k);
    print(n);

}
