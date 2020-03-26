CC := gcc
FLAGS := -Wall -std=c99

clean:
	rm -f *.o *.out *.gch

all: is_unique is_perm is_palindrom_perm

is_palindrom_perm: palindrom_perm.c
	$(CC) $(FLAGS) -c $?
	$(CC) $(FLAGS) palindrom_perm.o  -o $@.so

is_unique: isUnique isUniqueTester
	$(CC) $(FLAGS) $(addsuffix .o, $?)  -o $@.out

isUnique: isUnique.c isUnique.h
	$(CC) $(FLAGS) -c $@.c

isUniqueTester: isUniqueTester.c isUnique.c 
	$(CC) $(FLAGS) -c $@.c

is_perm: isUnique isUniqueTester 
	$(CC) $(FLAGS) $(addsuffix .o, $?)  -o $@.out

isPerm: isPerm.c isPerm.h
	$(CC) $(FLAGS) -c $@.c

isPermTester: isPermTester.c isPerm.c 
	$(CC) $(FLAGS) -c $@.c