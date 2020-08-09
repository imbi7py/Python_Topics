from merge ______ get_person_age, NOT_FOUND


___ test_regular_name(
    assert get_person_age('tim') __ 30
    assert get_person_age('helen') __ 26
    assert get_person_age('otto') __ 44


___ test_case_insensitive_lookup(
    assert get_person_age('Tim') __ 30
    assert get_person_age('BOB') __ 17
    assert get_person_age('BrEnDa') __ 17


___ test_name_not_found(
    assert get_person_age('timothy') __ NOT_FOUND
    assert get_person_age(None) __ NOT_FOUND
    assert get_person_age(False) __ NOT_FOUND
    assert get_person_age(-1) __ NOT_FOUND


___ test_duplicate_name(
    assert get_person_age('thomas') __ 46
    assert get_person_age('ana') __ 26