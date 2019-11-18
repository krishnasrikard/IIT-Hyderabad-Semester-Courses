#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>
/* Primitive System Data Types */

int main(int argc, char **argv)
{

char *myName = argv[0];
int cpid = fork();

if (cpid == 0)
{ //Child
	sleep(5); //sleeps for 5 secs
	printf("My pid: %d I am a child of %s My parent pid: %d\n", getpid(), myName, getppid());
	exit(0);
}

else
{ //Parent
	printf("My pid: %d My child’s pid: %d\n",getpid(),cpid);
	exit(0);
}

