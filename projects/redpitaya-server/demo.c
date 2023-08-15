#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

int ITERS = 50;

FILE *fp;
FILE *fp2;

// generate random x,y,bool values
char *generateValues(int ITERS) {
  int x, y, NUM = time(NULL), RND;
  char *result = (char *)malloc(1024 * sizeof(char));
  char temp[50];

  if (result == NULL) {
    fprintf(stderr, "Memory allocation error");
    exit(1);
  }

  result[0] = '\0';  // Initialize an empty string
  printf("Running on Num: %d\n", NUM);

  for (x = 0; x <= ITERS; x++) {
    for (y = 0; y <= ITERS; y++) {
      NUM = ((NUM * 1103245 + 12345) % 65536);
      NUM = (NUM / 100);
      RND = NUM % 2;

      snprintf(temp, sizeof(temp), "%d,%d,%d\n", x, y, RND);
      strcat(result, temp);
    }
  }

  return result;
}

// generate x,(sqrtX + jitter) values
int *calculateLoss(char *values) {
  int *result = (int *)malloc(1024 * sizeof(int));
  char *token;
  char *temp;
  int x, y, RND, i = 0;

  if (result == NULL) {
    fprintf(stderr, "Memory allocation error");
    exit(1);
  }

  token = strtok(values, "\n");
  while (token != NULL) {
    temp = strdup(token);
    x = atoi(strtok(temp, ","));
    y = atoi(strtok(NULL, ","));
    RND = atoi(strtok(NULL, ","));

    if (RND == 1) {
      result[i] = x + (rand() % 10);
    } else {
      result[i] = x;
    }

    i++;
    token = strtok(NULL, "\n");
  }

  return result;
}

int main() {
  time_t t;
  char *DATA_FILE = "./data/send.txt";
  char *LOSS_FILE = "./data/loss.txt";

  srand((unsigned)time(&t));

  while (1) {
    fp = fopen(DATA_FILE, "w");
    fp2 = fopen(LOSS_FILE, "a");

    char *values = generateValues(ITERS);
    fprintf(fp, "%s", values);

    char *loss = calculateLoss(values);
    fprintf(fp2, "%s", loss);

    free(values);
    fclose(fp);

    sleep(1);
  }

  return 0;
}
