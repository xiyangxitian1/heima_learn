#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : manage.py
# Author: MuNian
# Date  : 2019-12-03

from flask import Flask, render_template

# 基于app
# __name__ ---> 文件名称
app = Flask(__name__)


@app.route('/')
def index():
    return  render_template('day1.html')


if __name__ == '__main__':
    app.run()

