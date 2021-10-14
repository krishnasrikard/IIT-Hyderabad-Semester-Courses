#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

struct Node{
    int data;
    struct Node *next;
    struct Node *down;
};

// Fucntion to create a vector
struct Node *CreateVector(int n){
	struct Node *head, *temp;
	head = (struct Node*)malloc(sizeof(struct Node));
	temp = head;

	for(int j=1;j<n;j++){
		temp->next = (struct Node*)malloc(sizeof(struct Node));
		if (j != n-1)
			temp = temp->next;	
	}
	return head;
}

// Function to check collinearity
void Check_Collinearity(struct Node *head, int n, int m){
	struct Node *temp1, *temp2, *temp3, *temp4;

	// Variable to verify points are coliinear or not
	bool c = true;
	
	// CA = (lambda)BA 
	double lambda = 0, test = 0;
	
	// Reassigning Pointers for propagation to comapre vectors
	temp1 = head;
	temp2 = head->down;
	temp3 = head->down;

	for(int i=2;i<m;i++){
		// Pointer that moves along row
		temp3 = temp3->down;

		// Pointers that move along columns
		temp1 = head;
		temp2 = head->down;
		temp4 = temp3;

		for(int j=0;j<n;j++){
			if (j==0){
				if (temp2->data - temp1->data == 0) lambda = (temp4->data - temp1->data)/(pow(10,-6));
				else lambda = (temp4->data - temp1->data)/(temp2->data - temp1->data);
			}
			else{
				temp1 = temp1->next;
				temp2 = temp2->next;
				temp4 = temp4->next;

				// Comparing each component of CA and BA.
				if (temp2->data - temp1->data == 0) test = (temp4->data - temp1->data)/(pow(10,-6));
				else test = (temp4->data - temp1->data)/(temp2->data - temp1->data);

				// When the component CA and BA lie on same plane, then consider lambda to be the factor for points that doesn't lie on that plane,
				if (lambda == 0) lambda = test;

				// When they don't lie on same plane and are not a multiple
				if (test != lambda && test != 0){
					c = false;
					break;
				}
			}
		}
		if (c == false) break;
	}

	if (c) printf("Points are collinear.\n");
	else printf("Points are not collinear.\n");
}

int main(){
	// No.of dimensions of the vector
	int n;
	scanf("%d", &n);

	// No.of data points
	int m;
 	scanf("%d", &m);

	// Initializing Pointers
	struct Node *head, *temp1, *temp2, *temp3, *temp4;
	head = CreateVector(n); // (struct Node*)malloc(sizeof(struct Node));

	// Creating a Matrix formed using Pointers with m-rows and n-columns.
	for(int i=0;i<m;i++){
		if (i==0){
			temp1 = head;
			temp2 = temp1;
		}
		else{
			temp1->down = CreateVector(n); // (struct Node*)malloc(sizeof(struct Node));
			temp2 = temp1->down;
			temp1 = temp2;
		}
		for(int j=0;j<n;j++){
			if(j==n-1){
				scanf("%d", &temp2->data);
			}
			else{
				scanf("%d", &temp2->data);
				// temp2->next = (struct Node*)malloc(sizeof(struct Node));
				temp2 = temp2->next;
			}
		}
	}
	Check_Collinearity(head, n, m);
}