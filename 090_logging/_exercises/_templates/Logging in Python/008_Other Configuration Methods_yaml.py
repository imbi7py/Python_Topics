______ l____.config
______ yaml

with open('config.yaml', 'r') __ f:
    config _ yaml.safe_load(f.read())
    l____.config.dictConfig(config)

logger _ l____.getLogger(__name__)

logger.debug('This is a debug message')
# 2018-07-13 14:05:03,766 - __main__ - DEBUG - This is a debug message