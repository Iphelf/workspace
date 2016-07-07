#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void swap(int *a,int *b)
{
	int t;
	t=*b;
	*b=*a;
	*a=t;
}
int main()
{
	int s[71],i=0;
	srand(time(0));
	for(i;i<=70;i++)
		s[i]=i+1;
	i=70;
	int loop=1;
	while(loop==1){
	puts("-------------------------------\n        STAGE\nFOURTH  THIRD    SECOND  FIRST\n");
	int j=0;
	for(j;j<=49;j++){
		for(i;i>=0;i--)
			swap(&s[i],&s[rand()%70]);
		i=70;
	}
	i=0;
/*	for(i;i<=70;i++){
		if(s[i]==44){	//taech for 44
			swap(&s[i],&s[8]);
		}
		else if(s[i]==45){	//taech for 45
//			swap(&s[i],&s[7]);	//test
			j=0;
			for(j;j<=70;j++){
				if(s[j]==20){
					if(s[7]==45)
						swap(&s[j],&s[6]);
					else if(i==70)
						swap(&s[j],&s[69]);
					else if(i%10==8)
						swap(&s[j],&s[i-1]);
					else
						swap(&s[j],&s[i+1]);
				}
			}
		}
	}
*/	int x=0,y=0,z=0;i=0;
	for(x;x<=6;x++){
		for(y;y<=9;y++){
			if((x==0)&&(y==9))
				continue;
			printf("%3.2i",s[i]);
			i++;
		}
		y=0;
		puts("\n");
	}
	printf("%18.2i%3.2i\n",s[69],s[70]);
	puts("-------------------------------\nIf you want to continue, input integer: 1; \notherwise, input integer:0.");
	scanf("%i",&loop);
	}
	return 0;
}
