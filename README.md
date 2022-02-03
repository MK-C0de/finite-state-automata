# Programming Languages P4

We will extend the functionality of fsa.py to generate a Lisp program that can process the FSA represented in the file.

Project specifications:

Your objective is to develop a Lisp program (Part 1) and a Python program (Part 2 of this project) as follows:

    Part 1: Design, program and test a Lisp program that can evaluate the FSA pictured below. Name the file part1.lsp. From this program, you will be able to recognize the format of a Lisp program that solves FSA problems. Knowing this overall format will guide part 2.

    Part 2: Use the program in Python from project 3 that can load and represent an FSA as the starting point. Extend that program to generate a Lisp program in the format of the Lisp program you created in Part 1. The generated Lisp program should be named part2.lsp. Again, your solution should be general - not hard-coded for the particular FSA presented here.

Running the programs:

Part 1. Provide p1.bat It only needs one line:

xlwin32 part1.lsp

Part 2.

Include a batch file named p2.bat with the following
python lisp-fsa-gen.py fsa.txt   // generates the Lisp program part2.lsp
timeout /t 2                     // wait for first program to finish
xlwin32 part2.lsp                // invoke xlwin32.exe with generated fsa processor
