#!/usr/bin/env python

import os
import sys
import urllib2
import string

from common.global_vars import *


def get_filename(cd_header, breed_id):
    global offa_save_path
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)

    if cd_header is None:
        return
    try:
        fname = str(cd_header).split('; ')[1].split('=')[1]
    except IndexError:
        return

    cdisp = ''.join(c for c in fname if c in valid_chars)
    if len(cdisp) == 0:
        return

    if breed_id is None:
        return offa_save_path + '/' + cdisp

    return offa_save_path + '/' + breed_id + '/' + cdisp


def get_offa_data(qf, brid):
    global breeds
    global offa_save_path

    offa_url = 'http://www.ofa.org'
    reports_url = offa_url + '/reports.html'
    downloads_url = offa_url + '/reports.php'

    try:
        response = urllib2.urlopen(reports_url +
                                   '?quarter=' + qf +
                                   '&breed=' + brid +
                                   '&btnSelect=Select')
    except urllib2.HTTPError, e:
        print >>sys.stderr, 'HTTPError: ' + str(e)
        return
    except urllib2.URLError, e:
        print >>sys.stderr, 'URLError: ' + str(e.reason)
        return
    except:
        print >>sys.stderr, 'Exception: ' + str(sys.exc_info()[0])
        return

    # details = response.read()  # TODO parse the field names in html table
    cookie = response.info().getheader('Set-Cookie')
    if cookie is None:
        print >>sys.stderr, 'Missing cookie header: skip report ' + qf + ' for breed ' + breeds[brid]
        return

    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', cookie))
    opener.addheaders.append(('Referer', offa_url))
    dresponse = opener.open(downloads_url + '?btnDownload=Download')

    fpath = get_filename(dresponse.info().getheader('Content-disposition'), brid)
    if fpath is None:
        print >>sys.stderr, 'Missing filename header: skip report ' + qf + ' for breed ' + breeds[brid]
        return

    if not os.path.exists(offa_save_path) or not os.path.isdir(offa_save_path):
        print >>sys.stderr, 'Directory ' + offa_save_path + ' does not exist'
        return

    if not os.path.exists(offa_save_path + '/' + brid):
        try:
            os.makedirs(offa_save_path + '/' + brid)
        except:
            print >>sys.stderr, 'Error creating save directory for breed ' + breeds[brid]
            return

    if os.path.isfile(fpath):
        print >>sys.stderr, 'File ' + fpath + ' exists'
        print >>sys.stderr, 'Write report ' + qf + ' for breed ' + breeds[brid] + ' to file ' + fpath + ': skip'
        return

    try:
        target = open(fpath, 'w')
    except IOError, e:
        print >>sys.stderr, e
        print >>sys.stderr, 'Write report ' + qf + ' for breed ' + breeds[brid] + ' to file ' + fpath + ': skip'
        return

    content = dresponse.read()
    target.write(content)
    target.close()
    print >>sys.stderr, str('Write report ' + qf +
                            ' for breed ' + breeds[brid] +
                            ' to file ' + fpath + ': OK')
    return fpath


def main():
    global breeds, quarters, offa_save_path

    print "Starting download to " + offa_save_path

    for quarter in quarters:
        get_offa_data(quarters[quarter], "PO")
    '''
    for breed_id in breeds:
        for quarter in quarters:
            get_offa_data(quarters[quarter], breed_id)
    '''


if __name__ == "__main__":
    main()
