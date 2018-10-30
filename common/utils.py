#!/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs
import requests
import sys
import traceback


def import_class(import_str):
    mod_str, _sep, class_str = import_str.rpartition('.')
    __import__(mod_str)
    try:
        return getattr(sys.modules[mod_str], class_str)
    except AttributeError:
        raise ImportError('Class %s cannot be found (%s)' %
                          (class_str,
                           traceback.format_exception(*sys.exc_info())))


def write_content_to_file(content, file_path, mode='wb+'):
    with codecs.open(file_path, mode, 'utf-8') as md:
        md.write(content)


def get_content_by_url(url):
    r = requests.get(url)
    if r.status_code == 200:
        print 'get %s success.' % url
        return r.json()
    else:
        print 'get %s error.' % url
