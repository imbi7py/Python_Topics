______ ?
______ ?.config
______ submodule


?.config.fileConfig("logging.ini", disable_existing_loggers_False)
logger _ ?.gL..( -n)


___ bar():
    logger.warning("Calling bar")


___ exc_logging():
    a, b _ 5, 0

    ___
        c _ a / b
    except ZeroDivisionError:
        logger.critical("Exception occurred", exc_info_True)


__  -n == '__main__':
    bar()
    submodule.foo()
    exc_logging()
