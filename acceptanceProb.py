def P(e,eprime,T):
	if e < eprime:
		return 1
	else:
		exp = (-(eprime - e)/T)
		return exp