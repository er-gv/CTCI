#ifndef IS_UNIQUE_H
#define IS_UNIQUE_H
 

enum METHOD {NAIVE, MAP, SORT};


int is_unique(const char* str, enum METHOD method);

#endif