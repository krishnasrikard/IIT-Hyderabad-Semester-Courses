#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

int main()
{
	pid_t pid1,pid2;
	int i=1,status;

	pid1 = fork();

	if (pid1 == 0)
	{
		while(1)
		{
			fprintf(stdout,"In child: Iteration: %d\n",i++);
			fprintf(stdout,"Sleep for fork-1 will be Executed Next. My PID: %d\n",getpid());
			sleep(1);
			fprintf(stdout,"Sleep for fork-1 Executed.\n");
		}
	}

	else
	{		
		pid2 = fork();
		if (pid2 == 0)
		{
			fprintf(stdout,"Sleep for fork-2 will be Executed Next. My PID: %d\n",getpid());
			sleep(10);
			fprintf(stdout,"Sleep for fork-2 Executed.\n");
			fprintf(stdout,"Killing Process-1.\n");
			kill (pid1,SIGTERM);
			fprintf(stdout,"Process-1 Killed.\n");
			fprintf(stdout,"Sleep for fork-2 will be Executed Next. My PID: %d\n",getpid());
			sleep(10);
			fprintf(stdout,"Sleep for fork-2 Executed.\n");
		}

		else
		{
			fprintf(stdout,"Waiting for Process-1 and Process-2 to terminate.\n");
			waitpid(pid2,&status,0);
			exit(0);
		}
	}

	
}