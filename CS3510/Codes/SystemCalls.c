#define _GNU_SOURCE
#include <unistd.h> //wrapper for syscalls
#include <sys/syscall.h> // loc: /usr/src/include/i386-linux-gnu/bits/syscall.h, defines syscall numbers/Macros
#include <sys/types.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
pid_t tid;
tid = syscall(SYS_gettid); //SYS_gettid does not have glibc wrapper function, so calling syscall directly using "syscall" func; refer mansyscall, man gettid
printf("TID=%d\n", tid);

tid = getpid(); //getpid is wrapper function given in glibc
printf("PID=%d\n", tid);

tid = getppid(); //getppid is wrapper in glibc
printf("PPID=%d\n", tid);

tid = syscall(__NR_getpid); //calling SYSCALL directly
printf("PID=%d\n", tid);

tid = syscall(SYS_getpid); //calling SYSCALL directly
printf("PID=%d\n", tid);

tid = syscall(__NR_getppid); //calling SYSCALL directly
printf("PPID=%d\n", tid);

return 0;
}