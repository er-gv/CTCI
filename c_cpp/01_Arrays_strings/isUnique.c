#include "isUnique.h"
#include <stdlib.h>
#include <string.h>

static const unsigned int CHARSET_SIZE = 256u;
static int is_unique_by_map(const char* str);
static int is_unique_by_sort(const char* str);
static int is_unique_naive(const char* str);
int comp (const void * elem1, const void * elem2) ;

int is_unique(const char* str, enum METHOD method){

	int result = 0;
	switch(method){
		case MAP:
		result = is_unique_by_map(str);
		break;

		case SORT:
		result = is_unique_by_sort(str);
		break;

		case NAIVE:
		default:
		result = is_unique_naive(str);
	}
	return (0==result);
}

int is_unique_naive(const char* str){
	int len = strlen(str);
	if(0==len) return 0;
	for(int i=0; i<len; ++i)
		for(int j=i+1; j<len; ++j)
			if(str[i]==str[j])
				return 1;
	return 0; 
}

int comp (const void * elem1, const void * elem2) {
    char f = *((char*)elem1);
    char s = *((char*)elem2);
    if (f > s) return  1;
    if (f < s) return -1;
    return 0;
}

int is_unique_by_sort(const char* str){
	char* p;
	if(!*str) return 0;
	qsort ((void*)str, sizeof(char), strlen(str), comp);
	for(p = str+1; *p; *p != *(p-1));
	return (int)*p; 
}


int is_unique_by_map(const char* str){
	int map[CHARSET_SIZE];
	memset(map, 0, sizeof(map));
	char* p = str;
	while(*p && 0==map[*p]){
		map[*p] = 1;
	}
	return (int)(!(*p));
}