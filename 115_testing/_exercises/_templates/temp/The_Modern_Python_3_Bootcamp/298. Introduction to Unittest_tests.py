______ unittest
____ activities ______ eat, nap, is_funny, laugh


c_ ActivityTests(unittest.TestCase):
    ___ test_eat_healthy
        """eat should have a positive message for healthy eating"""
        assertEqual(
            eat("broccoli", is_healthy_True),
            "I'm eating broccoli, because my body is a temple"
        )

    ___ test_eat_unhealthy
        """eat should indicate you've given up for eating unhealthy"""
        assertEqual(
            eat("pizza", is_healthy_False),
            "I'm eating pizza, because YOLO!"
        )

    ___ test_eat_healthy_boolean
        """is_healthy must be a bool"""
        with assertRaises(ValueError):
            eat("pizza", is_healthy_"who cares?")

    ___ test_short_nap
        """short naps should be refreshing"""
        assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap"
        )

    ___ test_long_nap
        """long naps should be discouraging"""
        assertEqual(
            nap(3), "Ugh I overslept.  I didn't mean to nap for 3 hours!"
        )

    ___ test_is_funny_tim
        assertEqual(is_funny("tim"), False)

    # self.assertFalse(is_funny("tim"), "tim should not be funny")

    ___ test_is_funny_anyone_else
        """anyone else but tim should be funny"""
        assertTrue(is_funny("blue"), "blue should be funny")
        assertTrue(is_funny("tammy"), "tammy should be funny")
        assertTrue(is_funny("sven"), "sven should be funny")

    ___ test_laugh
        """laugh returns a laughing string"""
        assertIn(laugh(), ('lol', 'haha', 'tehehe'))


if __name__ == "__main__":
    unittest.main()