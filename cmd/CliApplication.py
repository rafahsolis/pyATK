import sys
import getopt


class Option:
	def __init__(self, shortForm, longForm, description, valueRequired):
		self.shortForm = shortForm
		self.longForm = longForm
		self.description = description
		self.valueRequired = valueRequired
		self.value = None

	def prettyPrint(self):
		pass

class CliApplication:

	VALUE_REQUIRED = 0x0
	VALUE_OPTIONAL = 0x1
	VALUE_NONE     = 0x2

	STATUS_SUCESS  = 0x4
	STATUS_FAILURE = 0x8

	def __init__(self):
		self.options = []
		self.callback = None


	def addOption(self, shortForm, longForm, description, valueRequired):
		opt = Option(shortForm, longForm, description, valueRequired)
		self.options.append(opt)
		return self

	def getValueForOption(self, option):
		for opt in self.options:
			if option in [opt.shortForm, opt.longForm]:
				return opt.value
		return None

	def printUsage(self):
		for option in self.options:
			print("-" + option.shortForm + ", --" + option.longForm + ":\t\t" + option.description)
			print("")

	def getShortFormString(self):
		result = ""
		for opt in self.options:
			if opt.valueRequired is CliApplication.VALUE_NONE:
				result = result + opt.shortForm
			else:
				result = result + opt.shortForm + ":"

		return result

	def getLongFormList(self):
		result = []
		for opt in self.options:
			if opt.valueRequired is CliApplication.VALUE_NONE:
				result.append(opt.longForm)
			else:
				result.append(opt.longForm + "=")
		return result

	def getOptionCouples(self):
		result = []
		for opt in self.options:
			result.append(["-" + opt.shortForm, "--" + opt.longForm])
		return result

	def getOptionByName(self, name):
		for option in self.options:
			if name in ["-" + option.shortForm, "--" + option.longForm]:
				return self.options.index(option)
		raise Exception("Option " + name + " was not found")

	def setCallback(self, callback):
		self.callback = callback

	def run(self):
		try:
			opts, args = getopt.getopt(sys.argv[1:], self.getShortFormString(), self.getLongFormList())
		except getopt.GetoptError as err:
			print(err)
			sys.exit(1)

		for opt, arg in opts:
			for couple in self.getOptionCouples():
				if opt in couple:
					self.options[self.getOptionByName(opt)].value = arg
					break;

		self.doRun()

	def doRun(self):
		if self.callback is not None:
			if callable(self.callable) is True:
				self.callback()
				return
			else:
				raise TypeError(self.callback.__name__ + " is not callable")

		for option in self.options:
			if option.value is None:
				print(option.longForm + " --> None")
			else:
				print(option.longForm + " --> " + option.value)






