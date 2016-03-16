from time import strptime


class Time:
	def __init__(self, hours=0, minutes=0, seconds=0):
		self.seconds = seconds + 60 * minutes + 3600 * hours

	def humanFormat(self):
		(y, m, d, h, mn, s) = self.timeTuple()
		x = []
		if y:
			x.append(str(y) + "yr")
		if m:
			x.append(str(m) + "mth")
		if d:
			x.append(str(d) + "d")
		if h:
			x.append(str(h) + "h")
		if mn:
			x.append(str(mn) + "m")
		if s:
			x.append(str(s) + "s")
		if not x:
			x = [str(s) + "s"]
		return ''.join(x)

	def timeTuple(self):
		y, s = divmod(self.seconds, 31536000)
		m, s = divmod(s, 2592000)
		d, s = divmod(s, 86000)
		h, s = divmod(s, 3600)
		mn, s = divmod(s, 60)
		return (y, m, d, h, mn, s)

	@classmethod
	def fromString(cls, s, fmt="%H:%M:%S"):
		t = strptime(s, fmt)
		return cls(t.tm_hour, t.tm_min, t.tm_sec)

	def __add__(self, other):
		seconds = self.seconds + other.seconds
		return Time(seconds=seconds)

	def __sub__(self, other):
		seconds = self.seconds - other.seconds
		return Time(seconds=seconds)


if __name__ == "__main__":
	time = Time.fromString("20:20:20")
	time2 = Time.fromString("23:59:59");
	time2 = time2 - time
	print(time2.humanFormat())

