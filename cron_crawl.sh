#!/bin/bash

export DJANGO_SETTINGS_MODULE=lescraper.settings 
python3 manage.py import_crawlresults
