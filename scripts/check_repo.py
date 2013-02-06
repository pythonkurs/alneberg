#!/usr/bin/env python
from alneberg.session3 import CourseRepo, repo_dir
from argparse import ArgumentParser
import os

def main(path):
    if path[-1] == "/":
        path = path[0:-1]
    (base_path,repo) = os.path.split(path)

    with repo_dir(path):
        cr = CourseRepo(repo)
        if cr.check():
            print "PASS!"
        else:
            print "FAIL!"
        

if __name__=="__main__":
    parser = ArgumentParser()
    parser.add_argument('path', 
        help='specify absolute path to the course repo')

    
    args = parser.parse_args()
    main(args.path)
