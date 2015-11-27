#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
import email
import email.mime.text
import argparse
import twitter

from sites import *
from escape_sequence import *


def send_ku_mail(user, password, subject, body, addr_to=None):
    addr = user + '@stu.kobe-u.ac.jp'
    if addr_to == None:
        addr_to = addr

    msg = email.mime.text.MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = addr
    msg['To'] = addr_to
    msg['Date'] = email.utils.formatdate()

    smtp = smtplib.SMTP_SSL('smtp.kobe-u.ac.jp', 465)
    smtp.ehlo()
    smtp.login(addr, password)
    smtp.sendmail(addr, [addr_to], msg.as_string())
    smtp.quit()
    print('send succeeded to ' + addr_to)


def send_twitter(APP_NAME, CONSUMER_KEY, CONSUMER_SECRET, tweet):
    MY_TWITTER_CREDS = os.path.expanduser('./twitter_id')

    if not os.path.exists(MY_TWITTER_CREDS):
        twitter.oauth_dance(APP_NAME, CONSUMER_KEY,
                            CONSUMER_SECRET, MY_TWITTER_CREDS)
        print(em('saved access token') + 'at' + MY_TWITTER_CREDS)

    oauth_token, oauth_secret = twitter.read_token_file(MY_TWITTER_CREDS)
    tw = twitter.Twitter(auth=twitter.OAuth(oauth_token, oauth_secret,
                                            CONSUMER_KEY, CONSUMER_SECRET))
    tw.statuses.update(status=tweet)
    print('Tweeted.')


if __name__ == '__main__':
    # Twitter Setting
    APP_NAME = 'website_update_notifier'
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    # Site Setting
    sites = [KuCs(), KuCommon(), KuCsKyuko()]

    # argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--twitter', dest='is_tweet',
                        action='store_true', default=False)
    parser.add_argument('-ck', '--consumer_key', default=CONSUMER_KEY)
    parser.add_argument('-cs', '--consumer_secret', default=CONSUMER_SECRET)
    parser.add_argument('-m', '--mail', dest='is_mail',
                        action='store_true', default=False)
    parser.add_argument('-u', '--user', default='')
    parser.add_argument('-p', '--password', default='')
    args = parser.parse_args()

    if(args.is_tweet and (args.consumer_key == '' or args.consumer_secret == '')):
        print(
            em('Arg Error required consumer key and consumer secret when you use twitter'))
        exit(1)
    if(args.is_mail and (args.user == '' or args.password == '')):
        print(em('Arg Error required -u xxxx -p xxxx when you use -m option'))
        exit(1)

    # check
    flg = False
    mail_contents = ''
    twitter_contents = '[Auto] Updated Following sites\r\n'

    for site in sites:
        is_updated, new_contents = site.check_update()
        if is_updated:
            print(blue(under_line('New data found')) + ' at ' + site.name)
            print(new_contents)
            mail_contents += new_contents
            twitter_contents += "%s\r\n%s\r\n" % (site.name, site.url)
            flg = True
        else:
            print(under_line('Not Updated') + ' at ' + site.name)

    if flg:
        if args.is_mail:
            print(mail_contents)
            # send_ku_mail(args.user,args.password,'サイト更新情報',mail_contents)
        if args.is_tweet:
            print(twitter_contents)
            # send_twitter(APP_NAME,args.consumer_key,args.consumer_secret,twitter_contents)
