#include <unistd.h>
#include <sys/syscall.h>
#include <errno.h>
#include <stdio.h>

int main()
{
	int rc;

	rc = syscall(SYS_chmod, "/etc/passwd", 0044);

	if (rc == -1)
		fprintf(stderr, "chmod failed, errno = %d\n", errno);
}