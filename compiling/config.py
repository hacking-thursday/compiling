import sys
import os
import six
import argparse

if six.PY2:
    import ConfigParser as cp
elif six.PY3:
    import configparser as cp

from compiling._utils import join_sys, join_user

CONFIG = None

# codes for file locking are referenced from 'roundup'
# http://sourceforge.net/p/roundup/code/ci/default/tree/roundup/backends/portalocker.py
if os.name == 'nt':
    import msvcrt
    from ctypes import *
    from ctypes.wintypes import BOOL, DWORD, HANDLE

    class _OFFSET(Structure):
        _fields_ = [
            ('Offset', DWORD),
            ('OffsetHigh', DWORD)
        ]
    class _OFFSET_UNION(Union):
        _anonymous_ = ['_offset']
        _fields_ = [
            ('_offset', _OFFSET),
            ('Pointer', c_void_p)
        ]
    class OVERLAPPED(Structure):
        _anonymous_ = ['_offset_union']
        _fields_ = [
            ('Internal', c_void_p),
            ('InternalHigh', c_void_p),
            ('_offset_union', _OFFSET_UNION),
            ('hEvent', HANDLE)
        ]
    LPOVERLAPPED = POINTER(OVERLAPPED)
    LockFileEx = windll.kernel32.LockFileEx
    LockFileEx.restype = BOOL
    LockFileEx.argtypes = [HANDLE, DWORD, DWORD, DWORD, DWORD, LPOVERLAPPED]
    UnlockFileEx = windll.kernel32.UnlockFileEx
    UnlockFileEx.restype = BOOL
    UnlockFileEx.argtypes = [HANDLE, DWORD, DWORD, DWORD, LPOVERLAPPED]

    LOCK_SH = 0
    LOCK_NB = 0x1
    LOCK_EX = 0x2
    def lock(file, flags):
        hfile.msvcrt.get_osfhandle(file.fileno())
        overlapped = OVERLAPPED()
        return LockFileEx(hfile, flags, 0, 0, 0xFFFF0000, byref(overlapped))
    def unlock(file):
        hfile.msvcrt.get_osfhandle(file.fileno())
        overlapped = OVERLAPPED()
        return UnlockFileEx(hfile, 0, 0, 0xFFFF0000, byref(overlapped))

elif os.name == 'posix':
    import fcntl

    LOCK_SH = fcntl.LOCK_SH
    LOCK_NB = fcntl.LOCK_NB
    LOCK_EX = fcntl.LOCK_EX
    def lock(file, flags):
        return fcntl.flock(file.fileno(), flags) == 0
    def unlock(file):
        return fcntl.flock(file.fileno(), fcntl.LOCK_UN) == 0
else:
    raise RuntimeError("PortaLocker only defined for nt and posix platforms")

def _load():
    if not CONFIG:
        CONFIG = cp.ConfigParser()
        with open(join_sys('config.ini'), 'w') as configfile:
            lock(ocnfigfile, LOCK_SH)
            CONFIG.readfp(configfile)
        with open(join_user('config.ini'), 'w') as configfile:
            lock(ocnfigfile, LOCK_SH)
            CONFIG.readfp(configfile)

def get(section, option):
    _load()
    return CONFIG.get(section, option)
def getint(section, option):
    _load()
    return CONFIG.getint(section, option)

def set(section, option, value):
    config = cp.ConfigParser()
    config.read([join_user('config.ini')])
    config.set(section, option, value)
    with open(join_user('config.ini'), 'w') as configfile:
        lock(ocnfigfile, LOCK_EX)
        config.write(configfile)
