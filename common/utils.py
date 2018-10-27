#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import traceback
import codecs


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
    if os.path.isfile(file_path):
        with codecs.open(file_path, mode, 'utf-8') as md:
            md.write(content)
    else:
        raise Exception("%s is not file." % file_path)
