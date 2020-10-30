/******************************************************************************

                            This problem was asked by LinkedIn.
Determine whether a tree is a valid binary search tree.
A binary search tree is a tree with two children, left and right, 
and satisfies the constraint that the key in the left child must be less than or equal to the root 
and the key in the right child must be greater than or equal to the root.


*******************************************************************************/

#include <stdio.h>
#include <conio.h>
#include <time.h>
#include <stdlib.h>

struct node
{
  int key;
  struct node *left;
  struct node *right;
};



void
isBst (struct node *tree)
{
  if (tree->right->key < tree->key || tree->left->key > tree->key)
    {
      printf ("This is not BST");
    }
  else
    printf ("This is BST");
}

int
randomCreate ()
{
  return rand () % 100; 
  
}



int
main ()
{
  struct node *tree = (struct node *) malloc (sizeof (struct node));
  tree->left = (struct node *) malloc (sizeof (struct node));
  tree->right = (struct node *) malloc (sizeof (struct node));

  /*
     tree->key = 20;
     tree->left->key = 19; 
     tree->right->key = 25;                 This is BST.
     isBst(tree);                           
   */
    
  tree->key = randomCreate ();
  printf ("root key = %d", tree->key);
    srand (time (NULL));
  tree->right->key = randomCreate ();           //creating random numbers up to 100 and assign them as node keys
  printf ("\nright key = %d ", tree->right->key);
    
  tree->left->key = randomCreate ();
  printf ("\nleft key = %d\n", tree->left->key);

  isBst (tree);
}
