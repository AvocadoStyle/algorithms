def upper_condition(st: str, ending_st: str):
    li_st = st.split()
    print(list(map(lambda x: x.capitalize() if x.endswith(ending_st) else x, li_st)))

st = "papaya\ngdola\nplaying soccer activated loving"
ending_st = "ing"
upper_condition(st, ending_st)