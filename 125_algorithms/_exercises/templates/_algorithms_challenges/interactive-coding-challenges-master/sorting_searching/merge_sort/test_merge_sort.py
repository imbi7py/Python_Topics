from nose.tools ______ assert_equal, assert_raises


class TestMergeSort(object

    ___ test_merge_sort(self
        merge_sort = MergeSort()

        print('None input')
        assert_raises(TypeError, merge_sort.sort, None)

        print('Empty input')
        assert_equal(merge_sort.sort([]), [])

        print('One element')
        assert_equal(merge_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        assert_equal(merge_sort.sort(data), sorted(data))

        print('Success: test_merge_sort')


___ main(
    test = TestMergeSort()
    test.test_merge_sort()


__ __name__ __ '__main__':
    main()