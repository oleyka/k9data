#!/usr/bin/env python

import os
import sys
import urllib2
import HTMLParser
import string

from global_vars import quarters, breeds, save_path


def get_data(qf, brid):
    try:
        response = urllib2.urlopen('http://www.ofa.org/reports.html?quarter=' +
                                   qf + '&breed=' + brid + '&btnSelect=Select'
                                  )
    except urllib2.HTTPError, e:
        print >>sys.stderr, 'HTTPError: ' + str(e)
        return
    except urllib2.URLError, e:
        print >>sys.stderr, 'URLError: ' + str(e.reason)
        return
    except:
        print >>sys.stderr, 'Exception: ' + str(sys.exc_info()[0])
        return

    details = response.read()
    cookie = response.info().getheader('Set-Cookie')

    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', cookie))
    opener.addheaders.append(('Referer', 'http://www.ofa.org'))
    response2 = opener.open("http://www.ofa.org/reports.php?btnDownload=Download")
    cdisp = response2.info().getheader('Content-disposition')
    if cdisp == None:
        print >>sys.stderr, 'Missing filename header: skip report ' + qf + ' for breed ' + breeds[brid]
    else:
        fname = get_filename(cdisp)
        if (len(fname) > 0):
            fpath = save_path + fname
            if os.path.isfile(fpath):
                print >>sys.stderr, 'File ' + fpath + ' exists'
                print >>sys.stderr, 'Write report ' + qf + ' for breed ' + breeds[brid] + ' to file ' + fpath + ': skip'
                return

            content = response2.read()
            try:
                target = open(fpath, 'w')
                target.write(content)
                target.close()
                print >>sys.stderr, 'Write report ' + qf + ' for breed ' + breeds[brid] + ' to file ' + fpath + ': OK'
            except IOError, e:
                print >>sys.stderr, e
                print >>sys.stderr, 'Write report ' + qf + ' for breed ' + breeds[brid] + ' to file ' + fpath + ': skip'
        else:
            print >>sys.stderr, 'Write report ' + qf + ' for breed ' + breeds[brid] + ' to file ' + fpath + ': skip'
            

def get_filename(cd):
    try:
        fname = cd.split('; ')[1].split('=')[1]
    except IndexError:
        print >>sys.stderr, 'Malformed filename header'
        return ''
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    return ''.join(c for c in fname if c in valid_chars)

def main():
    # print get_filename('attachment; filename=///PO30///$ -jun-16.csv')
    get_data("web30-jun-16up.zip", "PO")
    '''
    for quarter_file in quarters:
        for breed_id in keys(breeds):
            get_data(quarter_file, breed_id)
    '''


if __name__ == "__main__":
    main()
