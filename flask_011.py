import flask
import os
def safe_jinja(s):
    s = s.replace('(', '').replace(')', '')
    blacklist = ['config', 'self']
    return ''.join(['{{% set {}=None%}}'.format(c) for c in blacklist]) + s
print(safe_jinja("(asd)"))
