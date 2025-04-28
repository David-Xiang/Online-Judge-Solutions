#include "kernel/param.h"
#include "kernel/types.h"
#include "user/user.h"

#define BUFSIZE 500
#define ARGSIZE 10

void
run_in_child(int argc, char *argv[], char *line)
{
  char *cmd[MAXARG] = {0};
  int child_argc = 0;
  for(; child_argc < argc - 1; ++child_argc) {
    cmd[child_argc] = malloc(ARGSIZE);
    strcpy(cmd[child_argc], argv[child_argc + 1]);
  }

  int len = strlen(line);
  int arg_start = 0;
  for(int i = 0; i < len + 1; ++i) {
    if(i == len || line[i] == ' ') {
      if(arg_start == i) { // ignore following spaces
        ++arg_start;
        continue;
      }
      line[i] = '\0';
      cmd[child_argc] = malloc(ARGSIZE);
      strcpy(cmd[child_argc++], line + arg_start);
      arg_start = i + 1;
    }
  }

  if(fork() == 0) {
    exec(cmd[0], cmd);
  } else {
    for(int i = 0; i < child_argc; ++i) {
      free(cmd[i]); // remember to free allocated memory
    }
    wait(0);
  }
}

int
main(int argc, char *argv[])
{
  char buf[BUFSIZE];
  char *buf_p = buf;
  memset(buf, 0, BUFSIZE);
  char tmp;

  while(1) {
    int ret = read(0, &tmp, 1);
    if(!ret) {
      if(buf_p - buf > 0) {
        run_in_child(argc, argv, buf);
      }
      break;
    } else if(tmp == '\n') {
      run_in_child(argc, argv, buf);
      memset(buf, 0, BUFSIZE);
      buf_p = buf;
    } else {
      *buf_p++ = tmp;
    }
  }
  exit(0);
}
