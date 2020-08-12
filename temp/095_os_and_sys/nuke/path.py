# path.py

#acl All:read
#format PYTHON

# -*- coding: iso-8859-1 -*-
""" path.py - An object representing a path to a file or directory.

Example:

from path import path
d = path('/home/guido/bin')
for f in d.files('*.py'):
    f.chmod(0755)

This module requires Python 2.2 or later.


URL:     http://www.jorendorff.com/articles/python/path
Author:  Jason Orendorff <jason@jorendorff.com> (and others - see the url!)
Date:    7 Mar 2004

Adapted for stdlib by: Reinhold Birkenfeld, July 2005
Modified by Bjorn Lindqvist <bjourne@gmail.com>, January 2006
"""

# TODO
#   - Better error m.. in listdir() when self isn't a
#     directory. (On Windows, the error m.. really sucks.)
#   - Make sure everything has a good docstring.
#   - Add methods for regex find and replace.
#   - Perhaps support arguments to touch().
#   - Could add split() and join() methods that generate warnings.
#   - Note:  __add__() technically has a bug, I think, where
#     it doesn't play nice with other types that implement
#     __radd__().  Test this.

____ snitcher ______ snitch
snitch()

______ fnmatch
______ glob
______ __
______ shutil
______ sys

__all__ _ ['path']
__version__ _ '2.0.4'

# Universal newline support
_textmode _ 'r'
__ hasattr(file, 'newlines'):
    _textmode _ 'U'

# Use unicode strings __ possible
_base _ str
__ __.path.supports_unicode_filenames:
    _base _ unicode


c_ path(_base):
    """ Represents a filesystem path.

    For documentation on individual methods, consult their
    counterparts in os.path.
    """

    # --- Special Python methods.
    ___ __new__(typ, *args):
        """
        Creates a new path object concatenating the *args.  *args
        may only contain Path objects or strings.  If *args is
        empty, Path(os.curdir) is created.
        """
        __ no. args:
            r_ typ(__.curdir)
        for arg __ args:
            __ no. isinstance(arg, basestring):
                r_ ValueError("%s() arguments must be Path, str or "
                                 "unicode" % typ. -n)
        __ len(args) __ 1:
            r_ _base.__new__(typ, *args)
        r_ typ(__.path.j..(*args))

    ___ __repr__
        r_ '%s(%r)' % (__class__. -n, _base(self))

    # Adding a path and a string yields a path.
    ___ __add__(self, more):
        r_ __class__(_base(self) + more)

    ___ __radd__(self, other):
        r_ __class__(other + _base(self))

    @classmethod
    ___ cwd(cls):
        """ Return the current working directory as a path object. """
        r_ path(__.getcwd())

    # --- Operations on path strings.

    ___ abspath
        r_ __class__(__.path.abspath(self))

    ___ normcase
        r_ __class__(__.path.normcase(self))

    ___ normpath
        r_ __class__(__.path.normpath(self))

    ___ realpath
        r_ __class__(__.path.realpath(self))

    ___ expanduser
        r_ __class__(__.path.expanduser(self))

    ___ expandvars
        r_ __class__(__.path.expandvars(self))

    ___ expand
        """ Clean up a filename by calling expandvars(),
        expanduser(), and normpath() on it.

        This is commonly everything needed to clean up a filename
        read from a configuration file, for example.
        """
        r_ expandvars().expanduser().normpath()

    ___ _get_namebase
        base, ext _ __.path.splitext(name)
        r_ base

    ___ _get_ext
        f, ext _ __.path.splitext(_base(self))
        r_ ext

    ___ _get_drive
        drive, r _ __.path.splitdrive(self)
        r_ __class__(drive)

    ___ _get_dirname
        r_ __class__(__.path.dirname(self))

    parent _ property(
        _get_dirname, None, None,
        """ This path's parent directory, as a new path object.

        For example, path('/usr/local/lib/libpython.so').parent == path('/usr/local/lib')
        """)

    name _ property(
        __.path.basename, None, None,
        """ The name of this file or directory without the full path.

        For example, path('/usr/local/lib/libpython.so').name == 'libpython.so'
        """)

    namebase _ property(
        _get_namebase, None, None,
        """ The same as path.name, but with one file extension stripped off.

        For example, path('/home/guido/python.tar.gz').name     == 'python.tar.gz',
        but          path('/home/guido/python.tar.gz').namebase == 'python.tar'
        """)

    ext _ property(
        _get_ext, None, None,
        """ The file extension, for example '.py'. """)

    drive _ property(
        _get_drive, None, None,
        """ The drive specifier, for example 'C:'.
        This is always empty on systems that don't use drive specifiers.
        """)


    ___ splitpath
        """ p.splitpath() -> Return (p.parent, p.name). """
        parent, child _ __.path.split(self)
        r_ __class__(parent), child

    ___ stripext
        """ p.stripext() -> Remove one file extension from the path.

        For example, path('/home/guido/python.tar.gz').stripext()
        returns path('/home/guido/python.tar').
        """
        r_ path(__.path.splitext(self)[0])

    __ hasattr(__.path, 'splitunc'):
        ___ splitunc
            unc, rest _ __.path.splitunc(self)
            r_ __class__(unc), rest

        ___ _get_uncshare
            unc, r _ __.path.splitunc(self)
            r_ __class__(unc)

        uncshare _ property(
            _get_uncshare, None, None,
            """ The UNC mount point for this path.
            This is empty for paths on local drives. """)

    ___ splitall
        """ Return a list of the path components in this path.

        The first item in the list will be a path.  Its value will be
        either os.curdir, os.pardir, empty, or the root directory of
        this path (for example, '/' or 'C:\\').  The other items in
        the list will be strings.

        path.path(*result) will yield the original path.
        """
        parts _ []
        loc _ self
        while loc !_ __.curdir and loc !_ __.pardir:
            prev _ loc
            loc, child _ prev.splitpath()
            loc _ __class__(loc)
            __ loc __ prev:
                break
            parts.append(child)
        parts.append(loc)
        parts.reverse()
        r_ parts

    ___ relpath
        """ Return this path as a relative path,
        based from the current working directory.
        """
        r_ __class__.cwd().relpathto(self)


    ___ relpathto(self, dest):
        """ Return a relative path from self to dest.

        If there is no relative path from self to dest, for example __
        they reside on different drives in Windows, then this returns
        dest.abspath().
        """
        origin _ abspath()
        dest _ __class__(dest).abspath()

        orig_list _ origin.normcase().splitall()
        # Don't normcase dest!  We want to preserve the case.
        dest_list _ dest.splitall()

        __ orig_list[0] !_ __.path.normcase(dest_list[0]):
            # Can't get here from there.
            r_ dest

        # Find the location where the two paths start to differ.
        i _ 0
        for start_seg, dest_seg __ zip(orig_list, dest_list):
            __ start_seg !_ __.path.normcase(dest_seg):
                break
            i +_ 1

        # Now i is the point where the two paths diverge.
        # Need a certain number of "os.pardir"s to work up
        # from the origin to the point of divergence.
        segments _ [__.pardir] * (len(orig_list) - i)
        # Need to add the diverging part of dest_list.
        segments +_ dest_list[i:]
        __ len(segments) __ 0:
            # If they happen to be identical, use os.curdir.
            r_ __class__(__.curdir)
        else:
            r_ __class__(__.path.j..(*segments))


    # --- Listing, searching, walking, and matching

    ___ listdir(self, pattern_None):
        """ D.listdir() -> List of items in this directory.

        Use D.files() or D.dirs() instead __ you want a listing
        of just files or just subdirectories.

        The elements of the list are path objects.

        With the optional 'pattern' argument, this only lists
        items whose names match the given pattern.
        """
        names _ __.listdir(self)
        __ pattern is no. None:
            names _ fnmatch.filter(names, pattern)
        r_ [path(self, child) for child __ names]

    ___ dirs(self, pattern_None):
        """ D.dirs() -> List of this directory's subdirectories.

        The elements of the list are path objects.
        This does not walk recursively into subdirectories
        (but see path.walkdirs).

        With the optional 'pattern' argument, this only lists
        directories whose names match the given pattern.  For
        example, d.dirs('build-*').
        """
        r_ [p for p __ listdir(pattern) __ p.isdir()]

    ___ files(self, pattern_None):
        """ D.files() -> List of the files in this directory.

        The elements of the list are path objects.
        This does not walk into subdirectories (see path.walkfiles).

        With the optional 'pattern' argument, this only lists files
        whose names match the given pattern.  For example,
        d.files('*.pyc').
        """

        r_ [p for p __ listdir(pattern) __ p.isfile()]

    ___ walk(self, pattern_None):
        """ D.walk() -> iterator over files and subdirs, recursively.

        The iterator yields path objects naming each child item of
        this directory and its descendants.  This requires that
        D.isdir().

        This performs a depth-first traversal of the directory tree.
        Each directory is returned just before all its children.
        """
        for child __ listdir():
            __ pattern is None or child.match(pattern):
                yield child
            __ child.isdir():
                for item __ child.walk(pattern):
                    yield item

    ___ walkdirs(self, pattern_None):
        """ D.walkdirs() -> iterator over subdirs, recursively.

        With the optional 'pattern' argument, this yields only
        directories whose names match the given pattern.  For
        example, mydir.walkdirs('*test') yields only directories
        with names ending in 'test'.
        """
        for child __ dirs():
            __ pattern is None or child.match(pattern):
                yield child
            for subsubdir __ child.walkdirs(pattern):
                yield subsubdir


    ___ walkfiles(self, pattern_None):
        """ D.walkfiles() -> iterator over files in D, recursively.

        The optional argument, pattern, limits the results to files
        with names that match the pattern.  For example,
        mydir.walkfiles('*.tmp') yields only files with the .tmp
        extension.
        """
        for child __ listdir():
            __ child.isfile():
                __ pattern is None or child.match(pattern):
                    yield child
            elif child.isdir():
                for f __ child.walkfiles(pattern):
                    yield f

    ___ match(self, pattern):
        """ Return True __ self.name matches the given pattern.

        pattern - A filename pattern with wildcards,
            for example '*.py'.
        """
        r_ fnmatch.fnmatch(name, pattern)

    ___ matchcase(self, pattern):
        """ Test whether the path matches pattern, returning true or
        false; the comparison is always case-sensitive.
        """
        r_ fnmatch.fnmatchcase(name, pattern)

    ___ glob(self, pattern):
        """ Return a list of path objects that match the pattern.

        pattern - a path relative to this directory, with wildcards.

        For example, path('/users').glob('*/bin/*') returns a list
        of all the files users have in their bin directories.
        """
        r_ map(path, glob.glob(_base(path(self, pattern))))

    # --- Methods for querying the filesystem.

    exists _ __.path.exists
    isabs _ __.path.isabs
    isdir _ __.path.isdir
    isfile _ __.path.isfile
    islink _ __.path.islink
    ismount _ __.path.ismount

    __ hasattr(__.path, 'samefile'):
        samefile _ __.path.samefile

    ___ atime
        """Last access time of the file."""
        r_ __.path.getatime(self)


    ___ mtime
        """Last-modified time of the file."""
        r_ __.path.getmtime(self)

    ___ ctime
        """
        Return the system's ctime which, on some systems (like Unix)
        is the time of the last change, and, on others (like Windows),
        is the creation time for path.

        The return value is a number giving the number of seconds
        since the epoch (see the time module). Raise os.error __ the
        file does not exist or is inaccessible.
        """
        r_ __.path.getctime(self)

    ___ size
        """Size of the file, in bytes."""
        r_ __.path.getsize(self)

    __ hasattr(__, 'access'):
        ___ access(self, mode):
            """ Return true __ current user has access to this path.

            mode - One of the constants os.F_OK, os.R_OK, os.W_OK, os.X_OK
            """
            r_ __.access(self, mode)

    ___ stat
        """ Perform a stat() system call on this path. """
        r_ __.stat(self)

    ___ lstat
        """ Like path.stat(), but do not follow symbolic links. """
        r_ __.lstat(self)

    __ hasattr(__, 'statvfs'):
        ___ statvfs
            """ Perform a statvfs() system call on this path. """
            r_ __.statvfs(self)

    __ hasattr(__, 'pathconf'):
        ___ pathconf(self, name):
            r_ __.pathconf(self, name)


    # --- Modifying operations on files and directories

    ___ utime(self, times):
        """ Set the access and modified times of this file. """
        __.utime(self, times)

    ___ chmod(self, mode):
        __.chmod(self, mode)

    __ hasattr(__, 'chown'):
        ___ chown(self, uid, gid):
            __.chown(self, uid, gid)


    ___ rename(self, new):
        __.rename(self, new)

    ___ renames(self, new):
        __.renames(self, new)


    # --- Create/delete operations on directories

    ___ mkdir(self, mode_0777):
        __.mkdir(self, mode)

    ___ makedirs(self, mode_0777):
        __.makedirs(self, mode)

    ___ rmdir
        __.rmdir(self)

    ___ removedirs
        __.removedirs(self)


    # --- Modifying operations on files

    ___ touch
        """ Set the access/modified times of this file to the current time.
        Create the file __ it does not exist.
        """
        fd _ __.open(self, __.O_WRONLY | __.O_CREAT, 0666)
        __.close(fd)
        __.utime(self, None)

    ___ remove
        __.remove(self)

    ___ unlink
        __.unlink(self)


    # --- Links

    __ hasattr(__, 'link'):
        ___ link(self, newpath):
            """ Create a hard link at 'newpath', pointing to this file. """
            __.link(self, newpath)

    __ hasattr(__, 'symlink'):
        ___ symlink(self, newlink):
            """ Create a symbolic link at 'newlink', pointing here. """
            __.symlink(self, newlink)


    __ hasattr(__, 'readlink'):
        ___ readlink
            """ Return the path to which this symbolic link points.

            The result may be an absolute or a relative path.
            """
            r_ __class__(__.readlink(self))

        ___ readlinkabs
            """ Return the path to which this symbolic link points.

            The result is always an absolute path.
            """
            p _ readlink()
            __ p.isabs():
                r_ p
            else:
                r_ __class__(parent, p).abspath()


    # --- High-level functions from shutil

    copyfile _ shutil.copyfile
    copymode _ shutil.copymode
    copystat _ shutil.copystat
    copy _ shutil.copy
    copy2 _ shutil.copy2
    copytree _ shutil.copytree
    __ hasattr(shutil, 'move'):
        move _ shutil.move
    rmtree _ shutil.rmtree


    # --- Special stuff from os

    __ hasattr(__, 'chroot'):
        ___ chroot
            __.chroot(self)
