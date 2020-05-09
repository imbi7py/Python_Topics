"""
 https://github.com/lathama/python-testing-example
"""

____ testingdemo.howto ______ AnExample
______ unittest

c_ TestAnExample(unittest.TestCase):

    ___ setUp
        theclass _ AnExample()
        epochtime _ 123456789
        epochtimepriorday _ 123370389

    ___ test_make_something
        result _ theclass.make_something()
        assertTrue(result)

    ___ test_report_something
        theclass.rightnow _ epochtime
        theclass.yesterdaythistime _ epochtimepriorday
        result _ theclass.report_something()
        goal _ theclass.descriptiontext + str(epochtime)
        goal +_ " and " + str(epochtimepriorday)
        assertEqual(goal, result)

    ___ test_should_fail
        assertTrue(theclass.should_fail())
    
#badspacesandfileendlinemakestylecheckunhappy