from password ______ validate_password, used_passwords


___ test_password_len(
    assert not validate_password('short')
    assert not validate_password('waytoolongpassword')


___ test_password_missing_chars(
    assert not validate_password('UPPERCASE')
    assert not validate_password('lowercase')
    assert not validate_password('PW_no_digits')
    assert not validate_password('Pw9NoPunc')
    assert not validate_password('_password_')
    assert not validate_password('@#$$)==1')


___ test_password_only_one_letter(
    assert not validate_password('@#$$)==1a')


___ test_validate_password_good_pws(
    assert validate_password('passWord9_')
    assert validate_password('another>4Y')
    assert validate_password('PyBites@1912')
    assert validate_password('We<3Python')


___ test_password_not_used_before(
    assert not validate_password('PassWord@1')
    assert not validate_password('PyBit$s9')


___ test_password_cache_cannot_reuse(
    num_passwords_use = le.(used_passwords)
    assert validate_password('go1@PW')
    assert le.(used_passwords) __ num_passwords_use + 1
    assert not validate_password('go1@PW')