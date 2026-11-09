import status_check

# test status_check.mp_eligibility
#def test_mp_eligibility():
    #assert status_check.mp_eligibility(True, 20)
    #assert not status_check.mp_eligibility(False, 70)
    #assert not status_check.mp_eligibility(True, 17)
    #assert status_check.mp_eligibility(True, 18)
    #assert status_check.mp_eligibility(True, 1000)
    #assert not status_check.mp_eligibility(False, 17)

def test_mp_eligibility_both_conditions_easily_true():
    assert status_check.mp_eligibility(True, 20)

def test_mp_eligibility_not_a_citizen():
    assert not status_check.mp_eligibility(False, 70)

def test_mp_eligibility_too_young():
    assert not status_check.mp_eligibility(True, 17)

def test_mp_eligibility_just_barely_old_enough():
    assert status_check.mp_eligibility(True, 18)

def test_mp_eligibility_no_max_age():
    assert status_check.mp_eligibility(True, 1000)

def test_mp_eligibility_both_false():
    assert not status_check.mp_eligibility(False, 17)


# test status_check.senator_eligibility
def test_senator_eligibility():
    assert False