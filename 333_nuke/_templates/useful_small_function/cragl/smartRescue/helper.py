"""Helper functionality."""

# Import built-in modules
______ ast
______ d_t_
______ j___
______ __
______ re
______ shutil
______ subprocess
______ ___

# Import local modules
____ smartRescue.constants ______ CRAGL_SMARTRESCUE_CONFIG_PATH
____ smartRescue.constants ______ CRAGL_SMARTRESCUE_PROCESS_PATH
____ smartRescue.constants ______ DOCSTRING_EXTRACTION_PATTERN
____ smartRescue.constants ______ NAME


___ get_nuke_scripts(path, ignore_prefix):
    """Get all .nk files from the given path ignoring rescue and prefix files.

    Args:
        path (str): Absolute path of folder to collect .nk files from.
        ignore_prefix (str): Ignore all .nk files that start with this prefix.

    Returns:
        list: Absolute path of files to include in collection.

    """
    __ __.path.isfile(path):
        r_ [path]

    rescue_file_pattern _ r"rescue_\d+-\d+"
    r_ [__.path.join(path, file_)
            ___ file_ __ __.listdir(path)
            __ file_.endswith(".nk")
            and no. file_.startswith(ignore_prefix)
            and no. re.search(rescue_file_pattern, file_)]


___ create_working_file_copies(files):
    """Create working file copies to use instead of the original files.

    Args:
        files (list): Absolute paths of working files to create copy for.

    Returns:
        list: Absolute file paths of copy working files.

    """
    copy_files _ []
    date _ date_now()
    ___ file_ __ files:
        parent_dir, filename _ __.path.split(file_)
        basename _ __.path.splitext(filename)[0]
        copy_filename _ "{}_rescue_{}.nk".f..(basename, date)
        dest _ __.path.join(parent_dir, copy_filename)
        shutil.copy(file_, dest)
        copy_files.ap..(dest)

    r_ copy_files


___ date_now():
    """Return the date and time of now.

    Returns:
        str: Date and time of now in the format:
            YYYYMMDD-HH-SS.

    """
    r_ "{:%Y%m%d-%H%M%S}".f..(d_t_.d_t_.now())


___ get_process_folder():
    """Get absolute path of folder to process.

    If the environment variable 'SMART_RESCUE_PROCESS_PATH', that points to the
    folder that contains the Nuke working files, is set, we will prefer this
    path. If this environment variable is not set, we use the package internal
    'process' folder.

    Returns:
        str: Absolute path of folder to process.

    """
    environment_process_folder _ __.environ.get(CRAGL_SMARTRESCUE_PROCESS_PATH)
    __ environment_process_folder:
        r_ environment_process_folder

    this_dir _ __.path.dirname( -f)
    path _ __.path.join(this_dir, "..", "process")
    r_ __.path.n_p_(path)


___ get_config():
    """Get configuration from environment path of from package path.

    We prefer the path that is set via the SMART_RESCUE_CONFIG_PATH
    environment variable. If it is not set we use the configuration file
    path from this package.

    Returns:
        str, dict: Absolute path of configuration file that we loaded and the
            configuration values to use for smartRescue.

    """
    environment_path _ __.environ.get(CRAGL_SMARTRESCUE_CONFIG_PATH)
    __ environment_path:
        path _ environment_path
    ____
        path _ copy_config_file()

    w__ o..(path, "r") __ file_:
        r_ path, j___.load(file_)


___ load_icons():
    """Load all icons from the icons folder.

    This scans the icons directory and creates an icon dictionary using the
    file names without extension as keys.

    Returns:
        dict: Dictionary of icons in the format:
            {
                "icon1": "path1",
                "icon2": "path2",
                "icon3": "path3",
                ...
            }

    """
    this_dir _ __.path.dirname( -f)
    dir_icon _ __.path.join(this_dir, "icons")
    dir_icon _ __.path.n_p_(dir_icon)

    icons _ {}
    ___ file_ __ __.listdir(dir_icon):
        name _ __.path.splitext(file_)[0]
        path _ __.path.join(dir_icon, file_)
        icons[name] _ path

    r_ icons


___ get_docstring(path):
    """Get the module docstring from the module with the given path.

    Args:
        path (str): Absolute path of module to extract module docstring from.

    Returns:
        str: The module doc string of the given file.

    """
    w__ o..(path, "r") __ file_:
        tree _ ast.parse(file_.read())
    r_ ast.get_docstring(tree)


___ get_docstring_elements(path):
    """Get the one line header, body, standard- and advanced examples.

    Args:
        path (str): Absolute path of module to extract module docstring from.

    Returns:
        str, str, str, str: The module doc string's one liner description,
            body, standard examples and advanced examples

    """
    docstring _ get_docstring(path)
    regex _ re.search(DOCSTRING_EXTRACTION_PATTERN, docstring, re.DOTALL)
    __ regex:
        description _ regex.groupdict()["description"].split("\n")
        header _ description[0]
        body _ "\n".join(description[1:])
        standard _ regex.groupdict()["example_standard"]
        advanced _ regex.groupdict()["example_advanced"]

        r_ header, body, standard, advanced

    r_ docstring, "", "", ""


___ ensure_file_extension(path, ext):
    """Ensure the given file extension on the given path.

    Args:
        path (str): Path to ensure the given extension on.
        ext (str): Extension to ensure.

    Returns:
        str: The given path including the given file extension.

    """
    base, extension _ __.path.splitext(path)
    ext _ ext.replace(".", "")
    __ extension __ ext:
        r_ path
    r_ "{}.{}".f..(base, ext)


___ get_tool_root(which):
    """Get public/private root directory path based on 'which'.

    Create directory if it does not exist.

    Args:
        which (str): Which tool root to get. ("private", "public")

    Returns:
        str: Absolute path of public/private tool root.

    Raises:
        OSError: When the directory could not be created.

    """
    cragl_dir _ ".cragl" __ which __ "private" ____ "cragl"
    root _ __.path.join(__.path.expanduser("~"), cragl_dir, NAME)

    __ no. __.path.isdir(root):
        ___
            __.makedirs(root)
        except OSError __ error:
            raise OSError("Error creating directory: ", error.m..)

    r_ root


___ get_local_config_file():
    """Get absolute path of config file.

    Returns:
        str: Absolute path of config file.

    """
    r_ __.path.join(get_tool_root("private"), "config.json")


___ copy_config_file():
    """Copy over config file if not existing.

    Here we copy over the template configuration file of this package to the
    the private cragl folder in ~/.cragl/smartRescue/config.json.

    Returns:
        str: Absolute path of generated config file.

    """
    dest _ get_local_config_file()
    __ no. __.path.isfile(dest):
        this_dir _ __.path.dirname( -f)
        src _ __.path.join(this_dir, "data", "config.json")
        src _ __.path.abspath(src)
        shutil.copy(src, dest)
    r_ dest


___ open_website(url):
    """Open browser locating to given url.

    Args:
        url (str): Url to open in the web browser.

    Raises:
        OSError: When we can't open the url in the web browser using linux.

    """
    __ ___.pl.. __ 'win32':
        # This is only available in windows.
        __.startfile(url)  # pylint: disable=no-member
    ____ ___.pl.. __ 'darwin':
        subprocess.P..(['open', url])
    ____
        ___
            subprocess.P..(['xdg-open', url])
        except OSError:
            msg _ ("Cannot open browser. Please open it manually and "
                   "navigate to:\n\n{}".f..(url))
            raise OSError(msg)
