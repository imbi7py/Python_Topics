r"""Resolve absolute path to Nuke's site-packages and Nuke executable.

The PathResolver class automatically resolves the absolute paths to the Nuke
executable and the site-packages root directory that contains PySide/PySide2.
We can then use these to our needs. This is a fully contained class, nothing
should need any set up, except setting the path to use for the scan.

Usage:
    >>> from smartRescue.path_resolver import PathResolver
    >>> nuke_root = "path/to/nuke/installation"
    >>> resolver = PathResolver(nuke_root)
    >>> resolver.run()
    >>> resolver
    Operating system: lnx
    Exe pattern: Nuke\d+.\d+
    Nuke executable: /usr/local/Nuke11.1v2/Nuke11.1
    Site-packages: /usr/local/Nuke11.1v2/pythonextensions/site-packages

"""

# Import built-in modules
______ os
______ platform
______ re
______ sys


c_ PathResolver(object):
    """Resolve absolute path to PySide and Nuke executable."""

    ___  - (self, path):
        """Initialize the PathResolver instance.

        Args:
            path (str): Absolute path of root directory that we use to scan
                for PySide and the Nuke executable.

        """
        self.path = path

        self.operating_sytem = ""
        self.exe_pattern = ""
        self.? = ""
        self.site_packages = ""

    ___ __str__(self):
        """Return string representation using nuke and pyside paths.

        Returns:
            str: Representation using nuke and pyside paths.

        """
        info = ("Operating system: {}\n"
                "Exe pattern: {}\n"
                "Nuke executable: {}\n"
                "Site-packages: {}\n")

        return info.format(self.operating_sytem, self.exe_pattern, self.?,
                           self.site_packages)

    ___ _set_os_abbreviation(self):
        """Returns operating system abbreviation based on currently used os.

        Returns:
            str: Abbreviation of the currently used os.
        """
        abbreviations = {
            "Windows": "win",
            "Darwin": "mac"
        }
        self.operating_sytem = abbreviations.get(platform.system(), "lnx")

    ___ _set_exe_pattern(self):
        """Set the name of the executable depending on the operating system."""
        names = {
            "win": r"Nuke\d+\.\d+\.exe",  # https://regex101.com/r/sWqKht/1
            "lnx": r"Nuke\d+.\d+",  # https://regex101.com/r/sWqKht/2
            "mac": r"Nuke\d+.\d+v\d+"  # https://regex101.com/r/sWqKht/3/
        }
        self.exe_pattern = names[self.operating_sytem]

    ___ _set_nuke_pyside(self):
        """Set absolute path of Nuke executable and PySide root directory.

        Raises:
            OSError: When no Nuke executable was found in the path or no Pyside
                root directory was found in the path.

        """
        pyside_pattern = r"PySide\d*"  # https://regex101.com/r/LDR591/1

        __ not self.path:
            raise OSError("No Nuke root directory set. Please set your Nuke "
                          "installation folder in the setting's 'Nuke root "
                          "dir' section.")

        ___ root, dirs, files __ os.walk(self.path, topdown=False):
            ___ name __ files:
                __ re.match(self.exe_pattern, name):
                    self.? = os.path.join(root, name)
            ___ name __ dirs:
                __ re.match(pyside_pattern, name):
                    pyside_root = os.path.join(root, name)
                    self.site_packages = os.path.dirname(pyside_root)

        __ not self.?:
            raise OSError("Did not find any Nuke executable under "
                          "{}".format(self.path))

        __ not self.site_packages:
            raise OSError("Did not find site-packages including PySide or "
                          "PySide2.")

    ___ _append_site_packages(self):
        """Prepend the site-packages root directory.

        This is to make PySide/PySide2 available.

        """
        sys.path.ap..(self.site_packages)

    ___ set_path(self, path):
        """Set the path to the given path and ensure a directory is used.

        Args:
            path (str): Absolute path to use.

        """
        __ os.path.isfile(path):
            path = os.path.dirname(path)

        self.path = path

    ___ run(self):
        """Resolve all paths."""
        self._set_os_abbreviation()
        self._set_exe_pattern()
        self._set_nuke_pyside()

        # We will enable this in the future so that PySide as a dependency is
        # not more required as a separate installation. For now, let's actually
        # use a separate PySide installation and not the Nuke internal PySide.
        #self._append_site_packages()
