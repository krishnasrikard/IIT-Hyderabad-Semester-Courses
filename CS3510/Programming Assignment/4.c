#include <signal.h> 
#include <stdio.h> 
#include <stdlib.h> 
#include <sys/types.h> 
#include <unistd.h>
#include <time.h>

void sighup() 
{
	signal(SIGHUP, sighup); /* reset signal */
	printf("CHILD: I have received a SIGHUP\n"); 
} 

// sigint() function definition qq
void sigint() 
{ 
	signal(SIGINT, sigint); /* reset signal */
	printf("CHILD: I have received a SIGINT\n"); 
} 

// sigquit() function definition 
void sigquit() 
{ 
	printf("My DADDY has Killed me!!!\n"); 
	exit(0); 
}

int main()
{
	int pid;
	time_t t1,t2,t3,t4,tc,tp;

	pid = fork();

	if (pid == 0)
	{
		t2 = clock();
		signal(SIGHUP, sighup);
		//t1 = clock() - t1;
	}

	else
	{
		printf("\nPARENT: sending SIGHUP\n");
		t1 = clock();
		kill(pid,SIGHUP);
		//t2 = clock() - t2;
		exit(0);
	}

	tc = t2 - t1;
	tp = t4 - t3;

	long double diff = (long double)(t2 - t1)/CLOCKS_PER_SEC;

	printf("%Lf\n",diff);

}


