#!/usr/bin/python
import json, sys, hashlib, fractions, primefac

#https://brilliant.org/wiki/extended-euclidean-algorithm/
#https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Modular_inverse
def usage():
    print """Usage:
    python find_waldo.py student_id (i.e., qchenxiong3)"""
    sys.exit(1)

#TODO -- n1 and n2 share p or q? p
def is_waldo(n1, n2):
    result = False
    #your code start here
    if fractions.gcd(n1, n2) > 1:
        result = True
    #your code ends here
    return result
#TODO -- get private key of n1
def get_private_key(n1, n2, e):
    d = 0
    e = 0x10001
    p = fractions.gcd(n1,n2)
    q = n1 / p
    #your code starts here
    mod = (p-1)*(q-1)
    def exgcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = exgcd(b%a,a)
        return (g, x - (b//a) * y, y)
    def modinv(a, m):
        g, x, y = exgcd(a, m)
        if g != 1:
            raise Exception('ModInv null')
        return x%m
    d = (modinv(e,mod))
    #your code ends here
    return d

def main():
    if len(sys.argv) != 2:
        usage()

    all_keys = None
    with open("keys4student.json", 'r') as f:
        all_keys = json.load(f)

    name = hashlib.sha224(sys.argv[1].strip()).hexdigest()
    if name not in all_keys:
        print sys.argv[1], "not in keylist"
        usage()

    pub_key = all_keys[name]
    n1 = int(pub_key['N'], 16)
    e = int(pub_key['e'], 16)
    d = 0
    waldo = "dolores"

    print "your public key: (", hex(n1).rstrip("L"), ",", hex(e).rstrip("L"), ")"

    for classmate in all_keys:
        if classmate == name:
            continue
        n2 = int(all_keys[classmate]['N'], 16)

        if is_waldo(n1, n2):
            waldo = classmate
            d = get_private_key(n1, n2, e)
            break
    
    print "your private key: ", hex(d).rstrip("L")
    print "your waldo: ", waldo


if __name__ == "__main__":
    main()
