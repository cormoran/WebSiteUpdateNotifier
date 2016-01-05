#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from update_checker import *


class KuCs(UpdateChecker):

    def __init__(self):
        name = '情報知能工学科掲示板'
        url  = 'http://www.csi.kobe-u.ac.jp/cs/site/student/kyougaku.html'
        UpdateChecker.__init__(self,name,url)

    def parse(self, html):
        head = '<textarea name="textarea" cols="90" rows="15">'
        tail = '</textarea>'
        st = html.find(head) + len(head)
        html = html[st:]
        ed = html.find(tail)
        html = html[:ed]
        return html

    def beautify(self, parsed):
        return parsed


class KuCommon(UpdateChecker):

    def __init__(self):
        name = '国際教養教育院掲示板'
        url  = 'http://www.iphe.kobe-u.ac.jp/zengaku.htm#'
        UpdateChecker.__init__(self,name,url)

    def parse(self, html):
        head = '<article class="news">'
        tail = '</article>'
        st = html.find(head) + len(head)
        html = html[st:]
        ed = html.find(tail)
        html = html[:ed]

        return html

    def beautify(self, parsed):

        matches = re.findall(
            '<dt>(.*[^>])</dt>.*[^<]<a.*[^>]>(.*[^<])</a>', parsed)
        ret = ''
        for match in matches:
            ret += match[0] + ' ' + match[1] + '\r\n'

        return ret


class KuCsKyuko(UpdateChecker):

    def __init__(self):
        name = '情報知能工学科休講掲示板'
        url = 'http://www.csi.kobe-u.ac.jp/cs/site/student/kyuukou-hoko.html'
        UpdateChecker.__init__(self, name, url)

    def parse(self, html):
        head = '<!-- contents -->'
        tail = '<!-- /contents -->'
        st = html.find(head) + len(head)
        html = html[st:]
        ed = html.find(tail)
        html = html[:ed]

        return html

    def beautify(self, parsed):
        return parsed


class KuEng(UpdateChecker):

    def __init__(self):
        name = '工学部掲示板'
        url = 'http://www.office.kobe-u.ac.jp/eng-ofc/kym/student.html'
        UpdateChecker.__init__(self, name, url)

    def parse(self, html):
        head = '<!--▼中央　記事エリア部分はじまり -->'
        tail = '<!--▲中央　記事エリア部分終わり -->'
        st = html.find(head) + len(head)
        html = html[st:]
        ed = html.find(tail)
        html = html[:ed]

        return html

    def beautify(self, parsed):
        return parsed
