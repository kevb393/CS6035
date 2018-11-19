#!/usr/bin/python
import sys, hashlib

def usage():
    print """usage: python get_name_hash.py student_id
    for example:
    python get_name_hash.py qchenxiong3"""
    sys.exit(1)

if len(sys.argv) != 2:
    usage()

print hashlib.sha224(sys.argv[1]).hexdigest()
