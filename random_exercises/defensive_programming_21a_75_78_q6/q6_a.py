def upper_condition(st: str, ending_st: str):
    li_st = st.split()
    return list(map(lambda x: x.capitalize() if x.endswith(ending_st) else x, li_st))

st = "papaya\ngdola\nplaying soccer activated loving"
ending_st = "ing"
print(upper_condition(st, ending_st))