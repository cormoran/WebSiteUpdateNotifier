#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import os.path
import codecs
import difflib
from escape_sequence import * 


class WebPage:
    def __init__(self,name,url):
        self.name = name
        self.url  = url

        
    def get_html(self):
        try:
            response = urllib.request.urlopen(self.url)
        except:
            return None
        charset = 'utf-8'   #TODO : detection
        byte_html = response.read()
        try:
            #codecs.lookup(charset)
            html = byte_html.decode(charset,'replace')
        except:
            print(em('Failed to Detect Encoding at ') + self.url)
            html = None
        return html

    
    def parse(self,html):
        raise NotImplementedError

    
    def beautify(self,parsed):
        raise NotImplementedError

    
        
class Logger:
    def __init__(self,name,log_dir = './log'):
        self.name = name
        self.log_dir = log_dir

    def __load_log(self):
        path = self.log_dir + '/' + self.name
        return  open(path,'r').read() if os.path.exists(path) else ""

    
    def write_log(self,new_data):
        if not os.path.exists(self.log_dir):
            os.mkdir(self.log_dir)
            print(em('Log Directory : '+ self.log_dir +' not found.Created directory.'))
        path = self.log_dir + '/' + self.name
        open(path,'w').write(new_data)

        
    def get_updated(self,new_data):
        old_data = self.__load_log()
        ret =''
        if old_data != new_data :
            d = difflib.Differ()
            diff = list(d.compare(old_data.splitlines(),new_data.splitlines()))
            new_diff = []
            for line in diff:
                if line.startswith('+ '):
                    new_diff.append(line[2:])
            ret =  '\n'.join(new_diff)
            if ret == None:
                ret = ''

        is_updated = True if len(ret)>0 else False
        return is_updated , ret
    
    

class UpdateChecker(WebPage,Logger):
    def __init__(self,name,url):
        WebPage.__init__(self,name,url)
        Logger.__init__(self,name)
        self.name = name
        self.url = url
        
    def check_update(self,save_log = True):
        html = self.get_html()
        if html == None:
            print(em("Failed to get html")+" at "+self.url)
            return False , ''
        
        parsed = self.parse(html)
        is_updated,updates = self.get_updated(parsed)
        ret =''
        if is_updated :
            if save_log: self.write_log(parsed)
            ret  = 'サイト:\r\n %s \r\n' % self.name
            ret += 'URL   :\r\n %s \r\n' % self.url
            ret += '更新情報  :\r\n'
            ret += self.beautify(updates)
        
        return is_updated , ret
