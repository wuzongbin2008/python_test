#!/usr/bin/env python2.6
# coding: utf-8
"""
Date:
@author
"""
__author__ = 'Slasher'
__version__ = '0.1.0'

import os
import sys
import time
import logging

import conf
import pool
import sinastorageservice as s3


pdir = os.path.dirname( os.path.abspath( sys.argv[0] ) )
tempdir = os.path.join( pdir, 'tempfile' )

logfile = os.path.join( pdir, 'access.log' )
logging.basicConfig( filename = logfile, \
                     level = logging.DEBUG, \
                     format = '[%(asctime)s %(filename)s:%(lineno)d %(levelname)s] %(message)s' )

def _set( h ):

    h.set_need_auth( True )

    return

    h.set_domain( 'sinastorage.com' )
    h.set_port( 80 )
    h.set_timeout( 60 )

    h.set_expires( str( int( time.time() + 20 * 60 ) ) )
    h.set_expires_delta( 20 * 60 )

    h.set_extra( '?' )

    h.set_vhost( False )

    h.set_query_string( {   'ip' : str( time.time().__int__() + 24 * 3600 ) + ',7.7.7.7',
                            'foo' : 'bar',
                            } )

    h.set_request_header( {  'Content-Length' : '2013',
                             'Content-Type' : 'text/plain',
                             'Content-Disposition' : 'attachment; filename="ramanujan.txt"',
                            } )

    h.set_query_specific( { 'formatter' : 'json',
                            'fn' : 'rename.txt',
                            'rd' : '404.html',
                            } )

    h.set_https(  ssl = True,
                  port = 4443,
                  timeout = 180,
                  key_file = 'somewhere',
                  cert_file = 'somewhere', )

    h.reset()


def test_uplaod_file( h ,key,file):

    # key = 'DONOT_README'
    # fn = os.path.join( tempdir, 'DONOT_README' )

    try:
        out = h.upload_file( key, file )
        print repr(out)
        logging.info( "uplaod_file key='{key}' ok out='{out}'".format( key = key, out = out ) )
    except Exception, e:
        print e
        logging.error( "uplaod_file key='{key}' error out='{out}'".format( key = key, out = repr( e ) ) )


def test_post_file( h ):

    key = 'test/POST_FILE'
    fn = os.path.join( tempdir, 'DONOT_README' )

    print h.post_file( key, fn )


def test_upload_file_relax( h ):

    key = 'relax_upload'
    fsha1 = '9dfc376a81919c0a6cd71915c97f06600f9f2737'
    flen = 8063397

    print h.upload_file_relax( key, fsha1, flen )


def test_copy_file( h ):

    key = 'copy_upload'
    src = 'relax_upload'
    project = 'sandbox'

    print h.copy_file( key, src, project )


def test_get_file( h,key):

    #key = 'DONOT_README'

    print h.get_file( key )


def test_get_file_url( h ):

    key = 'DONOT_README'

    print h.get_file_url( key )


def test_get_file_meta( h ):

    key = 'relax_upload'

    print h.get_file_meta( key )


def test_get_project_list( h ):

    print h.get_project_list()


def test_get_files_list( h ):

    prefix = 'rela'
    marker = 'relax'
    maxkeys = 5
    delimiter = '/'

    print h.get_files_list( prefix, marker, maxkeys, delimiter )


def test_update_file_meta( h ):

    key = 'relax_upload'
    meta = { 'Content-Disposition' : 'attachment; filename="painting.jpg"' }

    print h.update_file_meta( key, meta.copy() )


def test_delete_file( h ):

    key = 'DONOT_README_1'

    print h.delete_file( key )


def _upload( key, fn ):

    handle = s3.S3( conf.accesskey, conf.secretkey, conf.project )
    handle.set_need_auth()

    try:
        out = handle.upload_file( key, fn )
        logging.info( "key='{key}' ok out='{out}'".format( key = key, out = out ) )
    except Exception, e:
        logging.error( "key='{key}' error out='{out}'".format( key = key, out = repr( e ) ) )

def test_upload_dirall( dir ):

    import pool

    threadpool = pool.WorkerPool( 10 )
    upload = threadpool.runwithpool( _upload )

    files = [ os.path.join( dirpath, name ) \
                    for dirpath, dirnames, filenames in os.walk( dir ) \
                        for name in filenames ]
    keys = [ key[ len( dir ) + 1: ] for key in files ]

    for key, fn in zip( keys, files ):
        upload( key, fn )

    threadpool.join()


def test_uplaod_bigfile():

    import large_upload

    key = 'big_file_upload'

    large_upload.upload_large( key )



if __name__ == "__main__":

    #test_upload_dirall( os.path.join( tempdir, 'updir' ) )
    #test_uplaod_bigfile()

    handle = s3.S3( conf.accesskey, conf.secretkey, conf.project )
    #_set( handle )

    #test_post_file( handle )
    #ex - ERROR - save_portrait_to_s3 key=''1378181244/portraits/1378181244.01.50'' filename=''/opt/portraits/001/009/1378181244.01.50'' exception out='OSError(2, 'No such file or directory')'
    key = "1378181244/portraits/1378181244.01.50"
    file = "/opt/portraits/001/009/1378181244.01.50"
    test_uplaod_file( handle,key,file)
    #test_upload_file_relax( handle )
    #test_copy_file( handle )

    #test_get_file( handle,key )
    #test_get_file_url( handle )
    #test_get_file_meta( handle )

    #test_get_project_list( handle )
    #test_get_files_list( handle )

    #test_update_file_meta( handle )

    #test_delete_file( handle )

    sys.exit( 0 )

