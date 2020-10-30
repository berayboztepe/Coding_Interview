#include <stdio.h>
#include <stdlib.h>

#This problem was asked by Microsoft.
#Print the nodes in a binary tree level-wise. 

/*   1
    / \
   2   3
      / \
     4   5
*/
    #For example, the following should print 1, 2, 3, 4, 5.


struct node{
    int key;
    struct node *left;
    struct node *right;


};
struct node* CreateNode(int key){

    struct node* root = (struct node *)malloc(sizeof(struct node));
    root->key = key;
    root->left = root->right = NULL;


    return root;

};

void preorder(struct node* root){
    if(root == NULL) return;

    printf("%d", root->key);
    printf("-\t");
    preorder(root->left);
    preorder(root->right);


}

int main()
{

   struct node* root = CreateNode(1);


   root->left = CreateNode(2);

   root->right = CreateNode(3);

   root->right->left = CreateNode(4);

   root->right->right = CreateNode(5);


    preorder(root);

}
