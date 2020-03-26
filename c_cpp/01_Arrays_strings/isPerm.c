#include "isPerm.h"
#include <stdlib.h>
#include <string.h>

static const unsigned int CHARSET_SIZE = 256u;
static int is_perm_by_map(const char* str1, const char* str2);
static int is_unique_by_sort(const char* str1, const char* str2);
static int is_unique_naive(const char* str1, const char* strs);
int comp (const void * elem1, const void * elem2) ;

int is_perm(const char* str1, const char* str2, enum METHOD method){

	int result = 0;
	switch(method){
		case MAP:
		result = is_perm_by_map(str1, str2);
		break;

		case SORT:
		result = is_perm_by_sort(str1, str2);
		break;

		case NAIVE:
		default:
		result = is_perm_naive(str1, str2);
	}
	return (0==result);
}

int is_perm_naive(const char* str1, const char* str2){
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

int is_perm_by_sort(const char* str1, const char* str2){
	char* p;
	if(!*str) return 0;
	qsort ((void*)str, sizeof(char), strlen(str), comp);
	for(p = str+1; *p; *p != *(p-1));
	return (int)*p; 
}


int is_perm_by_map(const char* str1, const char* str2){
	int map[CHARSET_SIZE];
	memset(map, 0, sizeof(map));
	char* p = str;
	while(*p && 0==map[*p]){
		map[*p] = 1;
	}
	return (int)(!(*p));
}