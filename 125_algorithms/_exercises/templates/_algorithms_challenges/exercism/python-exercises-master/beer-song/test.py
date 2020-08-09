______ unittest

from beer_song ______ song, verse


class BeerTest(unittest.TestCase
    ___ test_a_verse(self
        self.assertEqual(
            verse(8),
            "8 bottles of beer on the wall, 8 bottles of beer.\n"
            "Take one down and pass it around, "
            "7 bottles of beer on the wall.\n"
        )

    ___ test_verse_1(self
        self.assertEqual(
            verse(1),
            "1 bottle of beer on the wall, 1 bottle of beer.\n"
            "Take it down and pass it around, "
            "no more bottles of beer on the wall.\n"
        )

    ___ test_verse_2(self
        self.assertEqual(
            verse(2),
            "2 bottles of beer on the wall, 2 bottles of beer.\n"
            "Take one down and pass it around, 1 bottle of beer on the wall.\n"
        )

    ___ test_verse_0(self
        self.assertEqual(
            verse(0),
            "No more bottles of beer on the wall, no more bottles of beer.\n"
            "Go to the store and buy some more, "
            "99 bottles of beer on the wall.\n"
        )

    ___ test_songing_several_verses(self
        self.assertEqual(
            song(8, 6),
            "8 bottles of beer on the wall, 8 bottles of beer.\n"
            "Take one down and pass it around, "
            "7 bottles of beer on the wall.\n\n"
            "7 bottles of beer on the wall, 7 bottles of beer.\n"
            "Take one down and pass it around, "
            "6 bottles of beer on the wall.\n\n"
            "6 bottles of beer on the wall, 6 bottles of beer.\n"
            "Take one down and pass it around, "
            "5 bottles of beer on the wall.\n\n"
        )

    ___ test_song_all_the_rest_of_the_verses(self
        self.assertEqual(
            song(3),
            "3 bottles of beer on the wall, 3 bottles of beer.\n"
            "Take one down and pass it around, "
            "2 bottles of beer on the wall.\n\n"
            "2 bottles of beer on the wall, 2 bottles of beer.\n"
            "Take one down and pass it around, "
            "1 bottle of beer on the wall.\n\n"
            "1 bottle of beer on the wall, 1 bottle of beer.\n"
            "Take it down and pass it around, "
            "no more bottles of beer on the wall.\n\n"
            "No more bottles of beer on the wall, no more bottles of beer.\n"
            "Go to the store and buy some more, "
            "99 bottles of beer on the wall.\n\n"
        )


__ __name__ __ '__main__':
    unittest.main()
