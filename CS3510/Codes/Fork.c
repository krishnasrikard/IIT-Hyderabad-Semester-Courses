#include <stdio.h>
#include <sys/types.h> /* Primitive System Data Types */
#include <unistd.h>
#include <sys/wait.h>

int main()
{
	pid_t pid;

	pid = fork();

	if (pid < 0)
	{
		fprintf(stderr, "Fork Failed");
	}

	else if (pid == 0)
	{
		execlp("/bin/ls","ls",NULL);
	}

	else
	{
		wait(NULL);
		printf("Child Complete\n");
	}
}