#include <stdio.h>
int main(){
	int A[2]={-2,4},B[2]={3,-1},C[2]={-1,0},D[2]={1,2},E[2]={-3,-5};
	FILE *ptr;
	ptr=fopen("data.txt","w");
	for (int i=0;i<=1;i++){

	fprintf(ptr, "%d ",A[i]);
	}
	fprintf(ptr,"\n");
	for (int i=0;i<=1;i++){
                
        fprintf(ptr, "%d ",B[i]);
        }
	fprintf(ptr,"\n");
	for (int i=0;i<=1;i++){
                
        fprintf(ptr, "%d ",C[i]);
        }
	fprintf(ptr,"\n");

	for (int i=0;i<=1;i++){
                
        fprintf(ptr, "%d ",D[i]);
        }
	fprintf(ptr,"\n");
        for (int i=0;i<=1;i++){
                
        fprintf(ptr, "%d ",E[i]);
        }
	fprintf(ptr,"\n");
        return 0;
}
