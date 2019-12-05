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

int main()
{
  for(int i=0;i<8;i++)
  {
      int pid;
      time_t t1,t2,t3,t4,tc,tp;

      pid = fork();

      if (pid == 0)  {
          t2 = clock();
          signal(SIGHUP, sighup);
          //t1 = clock() - t1;
      }

      else  {
          printf("\nPARENT: sending SIGHUP\n");
          t1 = clock();
          kill(pid,SIGHUP);
          //t2 = clock() - t2;
          exit(0);
      }

      tc = t2 - t1;

      long double diff = (long double)(tc)/CLOCKS_PER_SEC; 
      printf("Time for Context Switch is %Lf\n",diff);
  }
}