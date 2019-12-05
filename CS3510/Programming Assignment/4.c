/*******************************************************************
 *
 * 	4.c - For the given Operating Systems Coding Assignment
 *
 *	
 *	Utility - This code created 2 Processes measures
 *	          Context Switch Time
 *
 */

#include <signal.h> 
#include <stdio.h> 
#include <stdlib.h> 
#include <sys/types.h> 
#include <unistd.h>
#include <time.h>

void SighUp()  {
	  // signal(SIGHUP, SighUp); /* reset signal */
	  printf("CHILD: I have received a SIGHUP\n");
} 

int main()  {
		
	for(int i=0;i<8;i++)  {/*Loop executes 8-times and Prints Time for Context Switch */
    		pid_t pid;											// To store ID of Parent
    		time_t t1,t2,tc;									// Variables are used to measure time.

   			pid = fork();										// Creating a Child Process

  			if (pid == 0)  {/* Child Process created*/
      				t2 = clock();								// Storing Time-Stamp
      				signal(SIGHUP, SighUp);						// Sending Signal can calling Function
      				//t1 = clock() - t1;
   			}

   			else  {/* Parent Process created*/	
      				printf("\nPARENT: sending SIGHUP\n");
      				t1 = clock();								// Storing Time-Stamp
      				kill(pid,SIGHUP);							// Sending Signal to kill Child Process
      				//t2 = clock() - t2;
   					exit(0);
  			}

  			tc = t2 - t1;

  			long double diff = (long double)(tc)/CLOCKS_PER_SEC; 
  			printf("Time for Context Switch is %Lf\n",diff);
	}
}