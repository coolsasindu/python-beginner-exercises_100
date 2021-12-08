has_high_income = True
has_good_credit = False
has_Criminal_record = False

# and is both NEED TRUE
if has_high_income and has_good_credit:
    print("Eligible for lone")
else:
    print('Don\'t')

# or at least one
if has_high_income or has_good_credit:
    print("Eligible for lone")
else:
    print('Don\'t')


# and not
if has_high_income and not has_Criminal_record:
    print("Eligible for lone")
else:
    print('Don\'t')
