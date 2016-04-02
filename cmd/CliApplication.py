# -*- coding: utf-8 -*-

import sys
import getopt
from pyATK.utils.misc import if_else


class Option:
	def __init__(self, shortForm, longForm=None, description=None, valueRequired=None):
		self.shortForm = shortForm
		self.longForm = longForm
		self.description = description
		self.valueRequired = valueRequired
		self.value = None

	def __str__(self):
		return self.shortForm + if_else(self.longForm is not None, ", --" + self.longForm, "") + \
				if_else(self.description is not None, "\t\t" + self.description, "")


class Argument:
	def __init__(self, argumentName, description, valueRequired):
		self.name = argumentName
		self.description = description
		self.valueRequired = valueRequired
		self.value = None

	def __str__(self):
			return "<" + self.name + ">"


class CliApplication:

	VALUE_REQUIRED = 0x0
	VALUE_OPTIONAL = 0x1
	VALUE_NONE = 0x2

	STATUS_SUCCESS = 0x0
	STATUS_FAILURE = 0x1

	def __init__(self):
		self.options = []
		self.arguments = []
		self.setOptions = 0
		self.setArguments = 0
		self.name = None
		self.version = None
		self.expectingOptions = False
		self.expectingArguments = False

		self.addOption("h", "help", "Displays this help message", CliApplication.VALUE_NONE)


	def addOption(self, shortForm, longForm=None, description=None, valueRequired=VALUE_NONE):
		self.assertValidValue(valueRequired)

		opt = Option(shortForm, longForm, description, valueRequired)
		self.options.append(opt)
		if self.expectingOptions is False:
			self.expectingOptions = True
		return self

	def addArgument(self, argumentName, description, valueRequired):
		self.assertValidValue(valueRequired)
		
		arg = Argument(argumentName, description, valueRequired)
		self.arguments.append(arg)
		if self.expectingArguments is False:
			self.expectingArguments = True
		return self

	def getValueForOption(self, option):
		for opt in self.options:
			if option in [opt.shortForm, opt.longForm]:
				return opt.value
		return None

	def printUsage(self):
		if self.name is not None:
			print("\n" + self.name + if_else(self.version is not None, str(self.version), "") + " [OPTIONS] <ARGUMENTS>")

		print("\n\nUsage:")
		for option in self.options:
			print(option)
		print("")

	def run(self):
		try:
			opts, args = getopt.getopt(sys.argv[1:], self.getShortFormString(), self.getLongFormList())
		except getopt.GetoptError as err:
			print(err)
			sys.exit(1)

		for opt, arg in opts:
			if self.expectingOptions is False:
				print("Extra option(s) provided. Don't know what to do with that")
				self.printUsage()
				return CliApplication.STATUS_FAILURE
			if "-h" == opt or "--help" == opt:
				self.printUsage()
				return CliApplication.STATUS_SUCCESS
			for couple in self.getOptionCouples():
				if opt in couple:
					self.options[self.getOptionByName(opt)].value = arg
					self.setOptions += 1
					break

		index = 0
		for arg in args:
			if self.expectingArguments is False:
				print("Extra argument(s) provided. Don't know what to do with that.")
				self.printUsage()
				return CliApplication.STATUS_FAILURE
			else:
				print(arg)
				self.arguments[index].value = arg
				self.setArguments += 1
				index += 1

		return self.doRun()

	def doRun(self):
		raise NotImplementedError("This method is not implemented!")

	#
	# Input methods
	#
	def confirm(self, question):
		print(question + " [Y/n]")
		response = input()
		if response.startswith("Y"):
			return True
		return False

	# @TODO : Add retry flag
	def choice(self, question, choices={}, message=None):
		keys = []
		if message is None:
			message = "Please select your choice"
		for key, choice in choices:
			print("[" + str(key) + "] " + str(choice))
			keys.append(str(key))
		print(message)
		response = input()
		if response in keys:
			return response
		return None

	#
	# Utility methods
	#
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


	def assertValidValue(self, valueRequired):
		if valueRequired not in [CliApplication.VALUE_NONE, CliApplication.VALUE_OPTIONAL, CliApplication.VALUE_REQUIRED]:
			raise ValueError("Wrong value provided. Should be one of VALUE_REQUIRED, VALUE_OPTIONAL, VALUE_NONE")



