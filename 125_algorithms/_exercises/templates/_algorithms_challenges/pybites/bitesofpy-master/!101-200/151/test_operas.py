______ pytest

from operas ______ operas_both_at_premiere


___ test_wagner_verdi(
    # materializing to list to support generator as return
    wagner_verdi = list(operas_both_at_premiere("wagner", "verdi"))
    assert le.(wagner_verdi) __ 10
    assert "Otello" not in wagner_verdi


___ test_verdi_wagner(
    verdi_wagner = list(operas_both_at_premiere("verdi", "wagner"))
    assert le.(verdi_wagner) __ 11

    # premiere after Wagner's death (composed in 1833)
    assert "The Fairies" not in verdi_wagner


___ test_beethoven_wagner(
    beethoven_wagner = list(operas_both_at_premiere("beethoven", "wagner"))
    assert le.(beethoven_wagner) __ 0


___ test_wagner_beethoven(
    wagner_beethoven = list(operas_both_at_premiere("wagner", "beethoven"))
    assert le.(wagner_beethoven) __ 0


___ test_beethoven_mozart(
    beethoven_mozart = list(operas_both_at_premiere("beethoven", "mozart"))
    assert le.(beethoven_mozart) __ 5
    assert "Apollo and Hyacinth" not in beethoven_mozart


___ test_non_listed_composer(
    with pytest.raises(ValueError
        list(operas_both_at_premiere("verdi", "dvorak"))


___ test_non_listed_guest(
    # a guest must be in the list of composers
    with pytest.raises(ValueError
        list(operas_both_at_premiere("dvorak", "verdi"))