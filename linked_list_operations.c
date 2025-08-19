#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node *next;
};

struct Node* create_ll(struct Node* start){
    int iter;
    struct Node *ptr;
    printf("enter no. of nodes u want to make : ");
    scanf("%d", &iter);
    for(int i=0;i<iter; i++){
        int data;
        printf("enter data: ");
        scanf("%d",&data);
        struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode -> data = data;
        if (start == NULL){
            newNode -> next = NULL;
            start = newNode;
            ptr = start;
        }
        else {
            ptr -> next = newNode;
            newNode -> next = NULL;
            ptr = ptr -> next;
        }
    }
    return start;
}

void display(struct Node* start){
    struct Node *ptr = start;
    printf("LL display data: \nStart  ");
    while (ptr != NULL){
        printf("-> %d ", ptr -> data);
        ptr = ptr -> next;
    }
    printf("\n");
}

struct Node* insert_beg(struct Node* start){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    int data;
    printf("enter value : ");
    scanf("%d", &data);
    newNode -> data = data;
    newNode -> next = start;
    start = newNode;
    return start;

}

struct Node* insert_end(struct Node* start){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    struct Node* ptr;
    int data;
    printf("enter value : ");
    scanf("%d", &data);
    newNode -> data = data;
    newNode -> next = NULL;
    ptr = start;
    while (ptr -> next != NULL){
        ptr = ptr -> next;
    }
    ptr -> next = newNode;
    return start;
}

struct Node* insert_pos(struct Node* start){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    struct Node* ptr = start;
    struct Node* preptr = start;
    int data, post;
    printf("enter value : ");
    scanf("%d", &data);
    newNode -> data = data;
    printf("enter postion to enter newnode : ");
    scanf("%d",&post);
    if (post == 0) {
        newNode -> next = start;
        return newNode;
    }
    ptr = preptr = start;
    for (int i=0; i<post; i++){
        preptr = ptr;
        ptr = ptr -> next;
    }
    preptr -> next = newNode;
    newNode -> next = ptr;
    return start;
}

struct Node* delete_beg(struct Node * start){
    struct Node* ptr = start;
    start = start -> next;
    free (ptr);
    printf("\nFirst node deleted successfully...\n");
    return start;

}

struct Node* delete_end(struct Node* start){
    struct Node* ptr, *preptr;
    ptr = start;
    while (ptr -> next != NULL){
        preptr = ptr;
        ptr = ptr -> next;
    }
    preptr -> next = NULL;
    free (ptr);
    return start;
}

struct Node* delete_pos(struct Node* start){
    int post;
    struct Node* delptr , *ptr;
    ptr = start;
    printf("enter position to delete :");
    scanf("%d",&post);
    for (int i=0; i<post-1; i++){
        ptr = ptr -> next;
    }
    delptr = ptr -> next;
    ptr -> next = ptr -> next -> next;
    free (delptr);
    return start;
}

int main(){
    int option;
    struct Node *start = NULL;
    do{
        printf("...MAIN MENU...\n1. CREATE LL\n2. DISPLAY LL\n3. INSERT AT BEGINNING \n4.INSERT AT END\n5. INSERT AT POSITION \n6. DELETE AT BEGINNING\n7.DELETE AT END\n8. DELETE AT POSITION\n-1.. Exit\n");
        scanf("%d",&option);
        switch (option){
            case 1 : {
                start = create_ll(start);
                break;
            }
            case 2: {
                display(start);
                break;
            }
            case 3 :{
                start = insert_beg(start);
                break;
            }
            case 4 :{
                start = insert_end(start);
                break;
            }
            case 5: {
                start = insert_pos(start);
                break;
            }
            case 6: {
                start = delete_beg(start);
                break;
            }
            
            case 7 :{
                start = delete_end(start);
                break;
            }
            case 8 :{
                start = delete_pos(start);
                break;
            }
        }
    } while (option!=-1);
}
