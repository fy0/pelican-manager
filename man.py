#!/usr/bin/env python
#coding:utf-8

import os
import click
from datetime import datetime
from collections import OrderedDict

contents = OrderedDict()

@click.command()
def lst():
    """ 列出当前文章 """
    for k, v in contents.items():
        click.echo('[%s] %s'% (k, v[1]))

@click.command()
@click.option('--name', default=None, help=u'文件名格式："数字.助记.rst" 助记非必须')
def new(name):
    """ 新文章 """
    key = ('%3d'% (int(contents.keys()[-1]) + 1)).replace(' ', '0')
    if name:
        fn = '%s.%s.rst' % (key, name)
    else:
        fn = '%s.rst' % key

    t = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M')
    tmpl = '''标题
##############

:date: %s 
:author: fy
:category: 综合
:tags: ...
:summary: ...'''
    open(fn, 'w+').write(tmpl % t)
    click.echo('完成:%s' % fn)


@click.command()
def rm():
    """ 删除文章 """
    pass


@click.command()
def sort():
    """ 顺序重排 """
    pass

@click.group()
def cli():
    info = {}
    global contents
    for i in os.listdir('.'):
        if i.endswith('.rst'):
            info[i[:3]] = [i, open(i).readline()[:-1]]
    contents = OrderedDict(sorted(info.items(), key=lambda x:int(x[0])))

def init():
    info = {}
    global contents
    for i in os.listdir('.'):
        if i.endswith('.rst'):
            info[i[:3]] = [i, open(i).readline()[:-1]]
    contents = OrderedDict(sorted(info.items(), key=lambda x:int(x[0])))

cli.add_command(lst)
cli.add_command(new)
cli.add_command(rm)
cli.add_command(sort)

if __name__ == '__main__':
    cli()

