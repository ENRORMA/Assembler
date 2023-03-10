# usage
  ./Assembler.sh your file to assemble the file
  
  ./Assembler.sh to launch the manual assembler
  
# requirements
  python 3.11.1 (might work on earlier versions but i tested it on 3.11.1)
  
# change instruction names and other things
  you can easily change the instruction name by doing the following
    
    1) locate the instruction name you want to change in the assemblers (example jmp on line 194 in the file assembler)
    
    2) change case "jmp": to case "your instruction name": (example case "goto":)
    
    3) do the same changes to the other assembler

  to change the output instruction do the following
    
    1) locate the instruction you want to change (example out)
    
    2)change InstructionString = InstructionString + "L15 " to InstructionString = InstructionString + "your output instruction " (example InstructionString = InstructionString + "R10 ")
     
    3) do the same changes to the other assembler
