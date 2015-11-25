#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def main():
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'), )

	STATIC_ROOT = os.path.join(BASE_DIR, 'static')
	STATIC_URL = '/static/'
	print "BASE_DIR", BASE_DIR
	print "TEMPLATE_DIRS", TEMPLATE_DIRS


if __name__ == '__main__':
	main()