#!/usr/bin/python2.7
# coding=utf-8
import json
import os

jsonData = raw_input('please input your json data:')
testJson = {}
testJson = json.loads(jsonData)

formateData = json.dumps(testJson, ensure_ascii=False, sort_keys=True, indent=2, separators=(',', ": "))
print formateData
