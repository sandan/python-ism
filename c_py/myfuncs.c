#include<stdio.h>
#include<string.h>

int greeting(char *name) {
  printf("hello %s\n", name);
  return 0;
}

int add(int x, int y) {
  return x + y;
}

double mult(double x, double y){
  return x * y;
}

double divide(int num, int den, int *rem){
  if (rem != NULL){
    *rem = num % den;
  }
  if (den == 0){
    //error
  }
  return ((double)num / (double)den);
}

double avg(double *arr, int len){

  if (arr && len > 0){
    int i = 0;
    double sum = 0.0;
    for (; i < len; i ++){
      sum += arr[i];
    }
    return sum / len;
  } else {
    printf("[avg][error]: input array empty or length is < 1");
  }
  return -1;
}

int show_double(double *dval){
  printf("dval = %f\n", *dval); //prints up to 6 after decimal
  return 0;
}

// see Kernighan
int replace(char *s, char old, char new){
  int num = 0;
  printf("printing input to replace: %s\n", s);
  printf("printing old: %x\n", old);
  printf("printing new before loop: %x\n", new);

  for (; (s = strchr(s, old)); num++)
    *s++ = new;

  printf("printing new after loop: %x\n", new);
  return num;
}

typedef struct Point{
  double x;
  double y;
} Point;

double slope(Point *p1, Point *p2){
  double rise = p2->y - p1->y;
  double run =  p2->x - p1->x;
  return rise / run;
}

double slope2(Point p1, Point p2){
  double rise = p2.y - p1.y;
  double run =  p2.x - p1.x;
  return rise / run;
}

typedef struct Node{
  double val;
  struct Node *left;
  struct Node *right;
} Node;

// will this conflict with the python class?
// nope.. the one in python ignores this
// and uses the one defined in the py program
// Need to make sure references are consistent between both
typedef struct Cherry{
  double j;
} Cherry;

void show_cherry(Cherry *c){
  // printf("%f\n", c->parent); myfuncs.c:93:21: error: no member named 'parent' in 'struct Cherry'
  printf("%f\n", c->j);
}

void sortArray(int size, int *array){
  register int i, j, temp;
  for(i = 0; i < size; i++){
    for(j=i+1; j < size; j++){
      if (array[i] > array[j]){
        temp = array[i];
        array[i] = array[j];
        array[j] = temp;
      }
    }
  }

}
