#ifndef IS_PERM_H
#define IS_PERM_H
 

enum METHOD {NAIVE, MAP, SORT};


int is_perm(const char* str, enum METHOD method);

#endif