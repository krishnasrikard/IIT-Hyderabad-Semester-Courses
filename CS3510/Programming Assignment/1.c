/*******************************************************************
 *
 * 	1.c - For the given Operating Systems Coding Assignment
 *
 *	
 *	Utility - This code created 2 Child Processes and performs
 *	          Kill and Sleep Operations
 *
 */

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

	if (pid1 == 0)  { /* First Child Process created -- Process-1 */
			while(1)  {
					fprintf(stdout,"In Child: Iteration: %d\n",i++);		
					fprintf(stdout,"Sleep for fork-1. fork-1 PID: %d\n",getpid());
					sleep(1);																	// Process-1 goes to sleep for 1 sec																
					fprintf(stdout,"Sleep for fork-1 completed.\n");
			}
	}

	else  {		
			pid2 = fork();
			if (pid2 == 0)  {/* Second Child Process created -- Process-2 */
					fprintf(stdout,"Sleep for fork-2. fork-2 PID: %d\n",getpid());
					sleep(10);																	// Process-2 goes to sleep for 10 seconds
					fprintf(stdout,"Sleep for fork-2 completed.\n");
					fprintf(stdout,"Killing Process-1.\n");
					kill (pid1,SIGTERM);														// Process-2 sends signal to terminate Process-1
					fprintf(stdout,"Process-1 Killed.\n");
					fprintf(stdout,"Sleep for fork-2. fork-2 PID: %d\n",getpid());
					sleep(10);																	// Process-1 goes to sleep for 10 seconds
					fprintf(stdout,"Sleep for fork-2 completed.\n");
			}

			else {/* Parent Process */
					fprintf(stdout,"Waiting for Process-1 and Process-2 to terminate.\n");
					waitpid(pid2,&status,0);													// Waiting for Process-2 to complete
					exit(0);
			}
	}
}