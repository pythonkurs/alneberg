import os
class CourseRepo(object):
    
    def __init__(self, surname):
        self.required = [".git", 
                         "setup.py", 
                         "README.md",
                         "scripts/getting_data.py", 
                         "scripts/check_repo.py",
                         "%s/__init__.py" % surname,
                         "%s/session3.py" % surname]
    
    @property
    def surname(self):
        return self.required[-1].split('/')[0]

    @surname.setter
    def surname(self, value):
        self.required = [".git",
                         "setup.py",
                         "README.md",
                         "scripts/getting_data.py",
                         "scripts/check_repo.py",
                         "%s/__init__.py" % value,
                         "%s/session3.py" % value]


    def check(self):
        mi_b = True
        for path in self.required:
            mi_b = mi_b and os.path.exists(path)
        return mi_b
