#!/usr/bin/env python
from alneberg.session3 import CourseRepo, repo_dir
from argparse import ArgumentParser
import os

def main(path):
    with repo_dir(path):


if __name__=="__main__":
    parser = ArgumentParser()
    parser.add_argument('path', 
        help='specify absolute path to the course repo')

    
    args = parser.parse_args()
    main(args.path)
