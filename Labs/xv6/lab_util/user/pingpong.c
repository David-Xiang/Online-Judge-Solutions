#include "kernel/types.h"
#include "user/user.h"

int
main(int argc, char *argv[])
{
  int ppc[2], pcp[2]; // parent -> child, child -> parent
  pipe(ppc);
  pipe(pcp);
  if(fork() != 0) {
    // parent
    // not necessary, but a good habit to close unused fds
    // close(pcp[1]);
    // close(ppc[0]);
    write(ppc[1], "", 1);
    char p;
    read(pcp[0], &p, 1);
    printf("%d: received pong\n", getpid());
    // close(pcp[0]);
    // close(ppc[1]);
  } else {
    // child
    // close(pcp[0]);
    // close(ppc[1]);
    char p;
    read(ppc[0], &p, 1);
    printf("%d: received ping\n", getpid());
    write(pcp[1], "", 1);
    // close(ppc[0]);
    // close(pcp[1]);
  }
  exit(0);
}
