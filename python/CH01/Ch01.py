def is_unique(string, algorithm=None):

    def is_unique_by_map(s):
        map = {}
        for c in s:
            if c in map:
                return False
            map[c] = True

        return True

    def is_unique_by_sort(s):
        if len(s) is 0:
            return True
        chars = sorted(s)
        #print (chars, s)
        return all(chars[c-1]!=chars[c] for c in range(1, len(chars)))
       

    def is_unique_by_brute_force(s):
        if len(s) is 0:
            return True
        for c in range(len(s)):
            for d in range(c+1, len(s)):
                if s[c] == s[d]:
                    return False
        return True


    mapper = {"map": is_unique_by_map, "sort": is_unique_by_sort}
    if algorithm in mapper:
        return mapper[algorithm](string)

    return is_unique_by_brute_force(string)


def is_palindrome(s1, s2, algo=None):

    def is_palindrome_by_map(s1, s2):
        dict1, dict2 = {}, {}
        for c in s1:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1

        for c in s2:
            if c in dict2:
                dict2[c] += 1
            else:
                dict2[c] = 1
        print (dict1, dict2)
        return 0==cmp(dict1, dict2)

    def is_palindrome_by_sort(s1, s2):
        chars1 = [ch for ch in s1]
        chars2 = [ch for ch in s2]
        chars1.sort()
        chars2.sort()
        return 0==cmp(chars1, chars2)

    def is_palindrome_by_depleting(s1, s2):
        for c in s1:
            if len(s2) >0:
                if c not in s2:
                    return False
                else:
                    s2 = s2.replace(c, '', 1)
            else:
                return False
        return s2 == ""

    mapper = {"map": is_palindrome_by_map, "sort": is_palindrome_by_sort}
    if algo in mapper:
        return mapper[algo](s1, s2)

    else:
        return is_palindrome_by_depleting(s1, s2)


def URLify(string):
    import re
    return re.sub(r"[ ]+", "%20", string)


def perm_of_palindrome(s):

    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    return reduce(lambda x, sum: x + sum, map(lambda e: 1 if dict[e] % 2 == 1 else 0, dict)) <= 2


def one_away(s1, s2):
    if s1 == s2:
        return True
    indices = [c for c in range(len(s1))]
    if any(map(lambda idx:(s2 == s1[:idx]+s1[idx+1:]), indices)) or s1 == s2[:-1] \
        or \
        any(map(lambda idx:(s1 == s2[:idx]+s2[idx+1:]), indices)) or s2 == s1[:-1]:
        return True


    return len(s1) == len(s2) and reduce(lambda x, y: x+y, map(lambda i: 1 if s1[i] != s2[i] else 0, [idx for idx in range(len(s2))])) <= 1


def string_compression(s):
    l = len(s)
    if 0 == l:
        return s

    counter = 1
    letter = s[0]
    result = ""
    for c in range(1, l):
        if letter == s[c]:
            counter += 1
        else:
            result += letter
            result += str(counter)
            letter = s[c]
            counter = 1

    result += letter
    result += str(counter)

    return result if len(result) < len(s) else s


def one_away_tester():

    def expected(method, params, result):
        #print (params, method(*params))
        return result == method(*params)

    print(expected(one_away, ["pale", "ale"], True))
    print(expected(one_away, ["pale", "gale"], True))
    print(expected(one_away, ["pale", "bake"], False))
    print(expected(one_away, ["pale", "paler"], True))
    print(expected(one_away, ["pale", "player"], False))
    print(expected(one_away, ["pale", "pa"], False))
    print(expected(one_away, ["pale", "pal"], True))


class Matricia:
    m = []
    cols = 0
    rows = 0

    def __init__(self, rows, cols):
        self.cols = cols
        self.rows = rows
        self.m = [[-1 for x in range(cols)] for r in range(rows)]

    def rand_fill(self, max=4):
        import random
        random.seed()
        for r in range(self.rows):
            for c in range(self.cols):
                self.m[r][c] = random.randint(0, max)

    def rand_spawn_zeros(self):
        import random
        import math

        random.seed()
        s = self.cols * self.rows

        for k in range(int(math.sqrt(s)), s/2):
            c = random.randint(0, self.cols)
            r = random.randint(0, self.rows)
            self.m[r][c] = 0

    def print_mat(self):
        for i in range(self.rows):
            print self.m[i]
        print

    def zero_matrix(self):
        zeros = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self.m[r][c] is 0:
                    zeros.append((r, c))

        for z in zeros:
            for i in range(self.cols):
                self.m[z[0]][i] = 0
            for i in range(self.rows):
                self.m[i][z[0]] = 0

    def make_transpose(self):

        trans = []
        for c in range(self.cols):
            row = []
            for r in range(self.rows):
                row.append(self.m[r][c])
            trans.append(row)
        self.m = trans
        self.cols, self.rows = self.rows, self.cols

    def rotate_right(self):
        n = self.rows - 1
        left = 0
        right = n-1
        for k in range(n/2):
            corner = self.m[k][k]
            print ("n: ", n, "k: ", k, 'left: ', left, 'right: ', right, range(left, right))
            for i in range(left, right):
                self.m[i+k][left] = self.m[i+k+1][left]

            for i in range(left, right):
                self.m[right-k][i] = self.m[right-k][i+1]

            for i in range(left, right):
                self.m[n-i-1][right] = self.m[n-i-2][right]

            for i in range(left, right):
                self.m[left+k][n-k-i-1] = self.m[left+k][n-k-i-2]

            self.m[k][k+1] = corner
            left += 1
            right -=1

    def rotate(self):
        if self.cols != self.rows:
            self.make_transpose()
        else:
            self.rotate_right()

    def zero_mat(self):
        zeros = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self.m[r][c] is 0:
                    zeros.append((r, c))

        for z in zeros:
            for i in range(self.cols):
                self.m[z[0]][i] = 0
            for i in range(self.rows):
                self.m[i][z[1]] = 0


def test_zero_matrix(rows, cols):

    mat = Matricia(rows, cols)
    mat.print_mat()
    mat.rand_fill(5)
    mat.print_mat()

    mat.rotate()
    mat.print_mat()


def tester():
    print("compressing the empty string yiels "+string_compression(""))
    print("compressing abcd yiels " + string_compression("abcd"))
    print("compressing aaaabbcccccddaeefggg yiels " + string_compression("aaaabbcccccddaeefggg"))


    print("calling is _palindrome(\"you go glen coco\", \"you go glen coco\", \"map\") should return true, returns " + str(is_palindrome(
        "you go glen coco", "you go glen coco", "map")))
    print("calling is_palindrome(\"regina\", \"inareg\", \"sort\") should return true, returns " + str(is_palindrome(
        "regina", "inareg", "sort")))
    print("calling is_palindrome(\"regina! regina! regina!\", \"regina\") should return false, returns " + str(is_palindrome(
        "regina! regina! regina!", "regina" )))
    print("calling is_palindrome(\"regina\", \"george\", \"map\") should return false, returns " + str(is_palindrome(
        "regina", "george", "map")))

    one_away_tester()
    test_zero_matrix(6, 3)


#tester()

for x in range(9):
    test_zero_matrix(x,x)




