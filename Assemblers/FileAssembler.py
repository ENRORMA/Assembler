#python 3.11.1

import sys

#initialize variables
WordInput = ""
NumInput = ""
BitString = ""
InstructionString = ""
InstructionInput = ""
InstructionLetter = ""
File = ""
FileName = ""
Argument = ""
UnknownInstructions = 0
Executed = False

Argument = sys.argv[1:]
FileName =  "".join(Argument)

with open(FileName , "r") as file:
	File = file.read()
print (File)

File = File.lower()

InstructionLetter = File[0:1]

#print with colors
class color:
	red = "\033[1;31;40m"
	green = "\033[1;32;40m"
	white = "\033[1;37;0m"

print (color.white + "type " + color.green + "\"help\"" + color.white + " for help")

while True:
	if Executed == True:
		File = File[1:1000000000000000]
		InstructionLetter = File[0:1]
	while InstructionLetter != " " and InstructionLetter != "" and InstructionLetter != "\n":
		InstructionInput = InstructionInput + InstructionLetter
		File = File[1:1000000000000000]
		InstructionLetter = File[0:1]
		Executed = True
	WordInput = InstructionInput
	InstructionInput = ""
	match WordInput:
		case "done":
			print (color.green + "Done" + color.white)
			print ("")
			if UnknownInstructions > 0:
				print (color.red + "Errors: " , UnknownInstructions , color.white)
				print (color.red + "the amount of errors might not be the amount of mistakes in your code Example:" + color.white)
				print (color.red + "if you type \"hmp\" instead of \"jmp\" the instruction will not be recognized and you will get an error but you will also get an error for the number after the jump instruction" + color.white)
			print (InstructionString)
			break
		case "help":
			print (color.white + "Type " + color.green + "\"done\"" + color.white + " to exit and print the Assembled code")
			print (color.white + "Type " + color.green + "\"help\"" + color.white + " to display this message")
			print (color.white + "Type " + color.green + "\"view\"" + color.white + " to print the assembled code")
			print (color.white + "Type " + color.green + "\";\"" + color.white + " to write a new line")
			print (color.white + "Type " + color.green + "\"inlude\"" + color.white + " to load an unsigned integer integer")
			print (color.white + "Type " + color.green + "\"inc\"" + color.white + " to increment a number (carry in)")
			print (color.white + "Type " + color.green + "\"inv\"" + color.white + " to invert A")
			print (color.white + "Type " + color.green + "\"set\"" + color.white + " to write a number to the selected register")
			print (color.white + "Type " + color.green + "\"uin\"" + color.white + " to enable the user input and turn on the input light")
			print (color.white + "Type " + color.green + "\"out\"" + color.white + " to output a integer")
			print (color.white + "Type " + color.green + "\"stop\"" + color.white + " to stop the program counter and stay on the current line")
			print (color.white + "Type " + color.green + "\"jmp\"" + color.white + " to unconditionally jump to the selected line")
			print (color.white + "Type " + color.green + "\"cmp\"" + color.white + " to compare A and B")
			print (color.white + "Type " + color.green + "\"call\"" + color.white + " to jump to the selected location and save a return address")
			print (color.white + "Type " + color.green + "\"return\"" + color.white + " to return to the line after the " + color.green + "\"call\"" + color.white + " instruction")
			print (color.white + "Type " + color.green + "\"ldr\"" + color.white + " to read the result of the current or last calculation")
			print (color.white + "Type " + color.green + "\"lda\"" + color.white + " to read the selected register as A")
			print (color.white + "Type " + color.green + "\"ldb\"" + color.white + " to read the selected register as B")
			print (color.white + "Type " + color.green + "\"#\"" + color.white + " to make a comment, end the comment with \"#\"")
		case "view":
			print (InstructionString)
		case ";":
			print ("New Line")
			InstructionString = InstructionString + "\n"
		case "include":
			print ("Load")
			if Executed == True:
				File = File[1:1000000000000000]
				InstructionLetter = File[0:1]
			while InstructionLetter != " " and InstructionLetter != "":
				InstructionInput = InstructionInput + InstructionLetter
				File = File[1:1000000000000000]
				InstructionLetter = File[0:1]
			NumInput = InstructionInput
			InstructionInput = ""
			Num = int(NumInput)
			if Num <= 255:
				if Num >= 128:
					Num = Num - 128
					BitString = BitString + "1"
					InstructionString = InstructionString + "L8 "
				else:
					BitString = BitString + "0"
				if Num >= 64:
					Num = Num - 64
					BitString = BitString + "1"
					InstructionString = InstructionString + "L7 "
				else:
					BitString = BitString + "0"
				if Num >= 32:
					Num = Num - 32
					BitString = BitString + "1"
					InstructionString = InstructionString + "L6 "
				else:
					BitString = BitString + "0"
				if Num >= 16:
					Num = Num - 16
					BitString = BitString + "1"
					InstructionString = InstructionString + "L5 "
				else:
					BitString = BitString + "0"
				if Num >= 8:
					Num = Num - 8
					BitString = BitString + "1"
					InstructionString = InstructionString + "L4 "
				else:
					BitString = BitString + "0"
				if Num >= 4:
					Num = Num - 4
					BitString = BitString + "1"
					InstructionString = InstructionString + "L3 "
				else:
					BitString = BitString + "0"
				if Num >= 2:
					Num = Num - 2
					BitString = BitString + "1"
					InstructionString = InstructionString + "L2 "
				else:
					BitString = BitString + "0"
				if Num >= 1:
					Num = Num - 1
					BitString = BitString + "1"
					InstructionString = InstructionString + "L1 "
				else:
					BitString = BitString + "0"
				print (BitString)
			else:
				print (color.red + "Number Is Too Big, Exiting include" + color.white)
			BitString = ""
		case "inc":
			print ("Increment")
			InstructionString = InstructionString + "L9 "
		case "inv":
			print ("Invert A")
			InstructionString = InstructionString + "L10 "
		case "set":
			print ("Write")
			if Executed == True:
				File = File[1:1000000000000000]
				InstructionLetter = File[0:1]
			while InstructionLetter != " " and InstructionLetter != "":
				InstructionInput = InstructionInput + InstructionLetter
				File = File[1:1000000000000000]
				InstructionLetter = File[0:1]
			NumInput = InstructionInput
			InstructionInput = ""
			Num = int(NumInput)
			if Num <= 7:
				if Num >= 4:
					Num = Num - 4
					BitString = BitString + "1"
					InstructionString = InstructionString + "L13 "
				else:
					BitString = BitString + "0"
				if Num >= 2:
					Num = Num - 2
					BitString = BitString + "1"
					InstructionString = InstructionString + "L12 "
				else:
					BitString = BitString + "0"
				if Num >= 1:
					Num = Num - 1
					BitString = BitString + "1"
					InstructionString = InstructionString + "L11 "
				else:
					BitString = BitString + "0"
				print (BitString)
			else:
				print (color.red + "Number Is Too Big, Exiting set" + color.white)
			BitString = ""
		case "uin":
			print ("User Input")
			InstructionString = InstructionString + "L14 "
		case "out":
			print ("Output")
			InstructionString = InstructionString + "L15 "
		case "stop":
			print ("stop the program counter")
			InstructionString = InstructionString + "L16 "
		case "jmp":
			print ("Jump")
			if Executed == True:
				File = File[1:1000000000000000]
				InstructionLetter = File[0:1]
			while InstructionLetter != " " and InstructionLetter != "":
				InstructionInput = InstructionInput + InstructionLetter
				File = File[1:1000000000000000]
				InstructionLetter = File[0:1]
			NumInput = InstructionInput
			InstructionInput = ""
			Num = int(NumInput)
			if Num <= 63:	#Number Of Lines
				if Num >= 32:
					Num = Num - 32
					BitString = BitString + "1"
					InstructionString = InstructionString + "R6 "
				else:
					BitString = BitString + "0"
				if Num >= 16:
					Num = Num - 16
					BitString = BitString + "1"
					InstructionString = InstructionString + "R5 "
				else:
					BitString = BitString + "0"
				if Num >= 8:
					Num = Num - 8
					BitString = BitString + "1"
					InstructionString = InstructionString + "R4 "
				else:
					BitString = BitString + "0"
				if Num >= 4:
					Num = Num - 4
					BitString = BitString + "1"
					InstructionString = InstructionString + "R3 "
				else:
					BitString = BitString + "0"
				if Num >= 2:
					Num = Num - 2
					BitString = BitString + "1"
					InstructionString = InstructionString + "R2 "
				else:
					BitString = BitString + "0"
				if Num >= 1:
					Num = Num - 1
					BitString = BitString + "1"
					InstructionString = InstructionString + "R1 "
				else:
					BitString = BitString + "0"
			else:
				print (color.red + "Number Is Too Big, Exiting jmp" + color.white)
			print (BitString)
			BitString = ""
		case "cmp":
			print ("If A=B")
			InstructionString = InstructionString + "R7 "
		case "call":
			print ("jump and save a return address")
			InstructionString = InstructionString + "R8 "
		case "return":
			print ("Jump To Return Address")
			InstructionString = InstructionString + "R9 "
		case "ldr":
			print ("Load Adder Result")
			InstructionString = InstructionString + "R10 "
		case "lda":
			print ("Register A Read")
			if Executed == True:
				File = File[1:1000000000000000]
				InstructionLetter = File[0:1]
			while InstructionLetter != " " and InstructionLetter != "":
				InstructionInput = InstructionInput + InstructionLetter
				File = File[1:1000000000000000]
				InstructionLetter = File[0:1]
			NumInput = InstructionInput
			InstructionInput = ""
			Num = int(NumInput)
			if Num <= 7: #Number Of Registers
				if Num >= 4:
					Num = Num - 4
					BitString = BitString + "1"
					InstructionString = InstructionString + "R13 "
				else:
					BitString = BitString + "0"
				if Num >= 2:
					Num = Num - 2
					BitString = BitString + "1"
					InstructionString = InstructionString + "R12 "
				else:
					BitString = BitString + "0"
				if Num >= 1:
					Num = Num - 1
					BitString = BitString + "1"
					InstructionString = InstructionString + "R11 "
				else:
					BitString = BitString + "0"
				print (BitString)
				BitString = ""
			else:
				print (color.red + "Number Is Too Big, Exiting lda" + color.white)
		case "ldb":
			print ("Register B Read")
			if Executed == True:
				File = File[1:1000000000000000]
				InstructionLetter = File[0:1]
			while InstructionLetter != " " and InstructionLetter != "":
				InstructionInput = InstructionInput + InstructionLetter
				File = File[1:1000000000000000]
				InstructionLetter = File[0:1]
			NumInput = InstructionInput
			InstructionInput = ""
			Num = int(NumInput)
			if Num <= 7: #Number Of Registers
				if Num >= 4:
					Num = Num - 4
					BitString = BitString + "1"
					InstructionString = InstructionString + "R16 "
				else:
					BitString = BitString + "0"
				if Num >= 2:
					Num = Num - 2
					BitString = BitString + "1"
					InstructionString = InstructionString + "R15 "
				else:
					BitString = BitString + "0"
				if Num >= 1:
					Num = Num - 1
					BitString = BitString + "1"
					InstructionString = InstructionString + "R14 "
				else:
					BitString = BitString + "0"
				print (BitString)
				BitString = ""
			else:
				print (color.red + "Number Is Too Big, Exiting ldb" + color.white)
		case "#":
			File = File[1:1000000000000000]
			InstructionLetter = File[0:1]
			while InstructionLetter != "#":
				File = File[1:1000000000000000]
				InstructionLetter = File[0:1]
			File = File[1:1000000000000000]
			InstructionLetter = File[0:1]
		case _:
			print (color.red + "Unknown Instruction" + color.white)
			UnknownInstructions = UnknownInstructions + 1
			if UnknownInstructions >= 10000:
				print ("")
				print ("You have more than 10.000 Errors, the assembler is stopping")
				print ("Make sure your code has the word \"done\" at the end like in this example:")
				print ("")
				print ("include 1 set 1 ;")
				print ("lda 1 ldb 1 ldr out stop")
				print ("done")
				break
