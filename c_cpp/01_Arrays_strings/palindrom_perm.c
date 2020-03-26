#include "palindrom_perm.h"

#include <string.h>

const int CHARSET_SIZE = 256;
int is_palindrome_perm(const char* str){
	int counters[CHARSET_SIZE];
	memset(counters, 0, sizeof(counters));
	int odds =0;
	while(*str){
		++counters[(int)*str];
		++str;
	}
	for(int i=0; i<CHARSET_SIZE && 2>(odds = counters[i]%2); ++i);
	return (odds<2? 0:1);
}

int main(void){ return 0;}

