""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""---------------------------------------------------||||Contents:||||----------------------------------------------------"""""""""


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
1. Main menu body                    	1. print_main_menu ()
					2. to_process_answer_in_main_menu (answer)
					3. main_menu ()
	
2. Processing menu body			1. print_processing_menu ()
					2. to_process_answer_in_processing_menu (answer)
					3. processing_menu ()

3. Temporary files menu body		1. print_temporary_files_menu ()
					2. to_process_answer_in_temporary_files_menu (answer)
					3. temporary_files_menu ()

4. Interface tools			1. die ()
					2. quit ()
					3. open_FAQ ()
					4. open_manual ()
					5. progressbar ()
					6. mess_destroyer (answer)
					7. checker_before_start (mode, mode)

5. Parsing tools			1. parser (mode, file_or_directory(s))
					2. start_processing (file_with_the_list_of_files)
					3. day_parser (directory)
					4. BSM_parser (directory)

6. Processing tools			1. raw_file_to_txt (file_to_process)
					2. txt_head_cleaner (file_to_process)
					3. txt_head_parser (head_to_process)
					4. txt_to_amplitudes (file_to_process)
					5. get_quick_pedestals (file_to_process)
					6. get_cleaned_quick_pedestal (file_to_process)
					7. get_precise_pedestals (file_to_process)
					8. amplitudes_minus_pedestals (file_to_process, file_of_pedestals)
					9. amplitudes_to_photoelectrons (file_to_process, file_with_pe_codes_and_rel_sensitives)
					10. 

7. Analyze tools			1. 
					2. 
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#from scipy import stats
#from matplotlib import pyplot as plt
#import matplotlib as mpl
import numpy as np
import shutil
import sys
#import time
import subprocess
#import processing_functions as prf
import pandas as pd
import re
import os

#script_dir = "/home/yaroslav/Documents/TAIGA_PYTHON"
script_dir = os.getcwd()
data_dir = "/DATA"


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""---------------------------------------------||||Main menu body:||||----------------------------------------------"""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Main menu body 1"""

def print_main_menu ():
	print ("""\n\n
	Hello! Here you can process the TAIGA IACT raw data files.\n
	Along the way you can choose the processing parameters that you consider convenient for you\n\n
	If:\n
	- program works incorrect,\n
	- you have questions about program functioning,\n
	- you have wishes or proposal regarding program functioning in the future versions,\n\n
	Please contact me by e-mail: yaroslav_sagan@mail.ru\n\n
	
	Have a nice day and a clear sky!\n
	#################################################################################\n\n\n
	
	
	--------------------------------------------------||||Main menu:||||------------------------------------------------\n\n
	
	-------------------------------------------------Choose a command:-----------------------------------------------\n\n
	1  | Briefly about the algorithms.\n
	2  | FAQ.\n
	3  | Start work.\n
	4  | Download some data from MSU grid.\n
	0  | Quit.\n
	------------------------------------------------------------------------------------------------------------------------------\n
	:->  
	""")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Main menu body 2"""

def to_process_answer_in_main_menu (answer):
	if (answer != "1" and answer != "2" and answer != "3" and answer != "4" and answer != "0"):
		print("It seems that you've made the mistake. Please, try again:")
		to_process_answer_in_main_menu (answer)
	elif answer == "1": open_manual ()
	elif answer == "2": open_FAQ ()
	elif answer == "3": processing_menu ()
	elif answer == "4":
		subprocess.call ("./msu_grid_ssh_access", shell=True)
		main_menu ()	
	elif answer == "0": quit ()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Main menu body 3"""

def main_menu ():
	subprocess.call ("clear")
	print_main_menu ()
	ans_1 = input ()
	to_process_answer_in_main_menu (ans_1)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""------------------------------------------||||Processing menu body:||||----------------------------------------"""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Processing menu body 1"""

def print_processing_menu ():
	print ("""
	---------------------------------------------------What to process?:-------------------------------------------------\n\n
	1 | To process a couple of days.\n
	2 | To process a day.\n
	3 | To process one BSM from one day.\n
	4 | To process one file.\n
	5 | To process a couple of files.\n
	6 | Return to the main menu.\n
	7 | Delete old temporary files (anyway will be automatically rewrote after processing).\n 
	0 | Quit.\n
	-------------------------------------------------------------------------------------------------------------------------------\n
	:->  
	""")


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Processing menu body 2"""

def to_process_answer_in_processing_menu (answer):

	if (answer != "1" and answer != "2" and answer != "3" and answer != "4" and answer != "5" and answer != "6" and answer != "7" and answer != "0"):
		print("It seems that you've made the mistake. Please, try again:")
		to_process_answer_in_processing_menu (answer)
#	elif answer == "1": pass #couple_days
#	elif answer == "2": pass #one_day
#	elif answer == "3": pass #one_BSM from one day
#	elif answer == "4": pass #one_file
#	elif answer == "5": pass #couple_of_files
	elif answer == "6": main_menu ()
	elif answer == "7": mess_destroyer (2)
	elif answer == "0": quit ()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Processing menu body 3"""

def processing_menu ():
	subprocess.call ("clear")
	print_processing_menu ()
	ans_2 = input ()
	to_process_answer_in_processing_menu (ans_2)
	return ans_2


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""---------------------------------------||||Temporary files menu body:||||-------------------------------------"""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Temporary files menu body 1"""

def print_temporary_files_menu ():
	print ("""
	------------------------------------------What to do with temporary files:--------------------------------------\n\n
	1 | To leave all the temporary files after processing finish.\n
	2 | To delete all the temporary files after processing finish.\n
	3 | To create ONLY the list of files to process and not to process them.\n
	4 | To create the list of  files to process and not to process it. + To create the gypothetical list of temporary files.\n 
	5 | Return to the processing menu.\n
	0 | Quit.\n
	---------------------------------------------------------------------------------------------------------------------------------\n
	:->  
	""")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Temporary files menu body 2"""

def to_process_answer_in_temporary_files_menu (answer):

	if (answer != "1" and answer != "2" and answer != "3" and answer != "0" and answer != "4" and answer != "5"):
		print("It seems that you've made the mistake. Please, try again:")
		to_process_answer_in_temporary_files_menu (answer)
#	elif answer == "1": pass
#	elif answer == "2": pass
#	elif answer == "3": pass
	elif answer == "4": pass
	elif answer == "5": processing_menu ()
	elif answer == "0": quit ()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Temporary files menu body 3"""

def temporary_files_menu ():
	subprocess.call ("clear")
	print_temporary_files_menu ()
	ans_3 = input ()
	to_process_answer_in_temporary_files_menu (ans_3)
	return ans_3


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""----------------------------------------------||||Interface Tools:||||------------------------------------------------"""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Interface Tools 1"""

def die ():
	print ("Incorrect value! I've been crushed!.........X_X\n")
	sys.exit ()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Interface Tools 2"""

def quit ():
	print ("Are you sure? y/n:\n")
	w = input ()
	if w == "y": sys.exit ()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Interface Tools 3"""

def open_FAQ ():
	print ("Open FAQ")
	subprocess.call ("nano " + script_dir + "/FAQ.txt", shell=True)
	main_menu ()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Interface Tools 4"""

def open_manual ():
	print ("Open manual")
	subprocess.call ("nano " + script_dir + "/MANUAL.txt", shell=True)
	main_menu ()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Interface Tools 5"""

def progressbar (i, n):

	c, r = shutil.get_terminal_size (fallback = (80, 24))    
	for i in range (n):
#	    time.sleep (0.01)
	    sys.stdout.write ("\r %d%% [%-80s]" % ((int(100*i/n)), u'\u2589'*(int(c*i/n) + 1)))
	    sys.stdout.flush ()
	print ("Done\n")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Interface Tools 6"""

def mess_destroyer (answer):
	
	if answer == 2:
		mess_file = open (script_dir + "/.mess.txt", "r")
		try:
			for line in mess_file: os.remove ("line[22:]")
		except: print("Unknown error while temporary files deleting! Please, delete your manually!")
		mess_file.close ()
		os.remove (script_dir + "/.mess.txt")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Interface Tools 7"""

def checker (mode_2, mode_3):

	if mode_2 == "1": set_1 = "Couple of days"
	elif mode_2 == "2": set_1 = "One day"
	elif mode_2 == "3": set_1 = "One BSM from one day"
	elif mode_2 == "4": set_1 = "One file"
	elif mode_2 == "5": set_1 = "Couple of files"
	if mode_3 == "1": set_2 = "Leave"
	elif mode_3 == "2": set_2 = "Delete"
	elif mode_3 == "3": set_2 = "Only create the list of files to process"
	elif mode_3 == "4": set_2 = "Only create the list of files to process and the list of temporary files"
	
	print("You've chosen next modes:\n\nProcessing mode: %s.\n\nTemporary files after processing:\n\n%s.\n\n" % (set_1, set_2))
	print("Press 1 to go on or 0 to return to the main menu:\n")
	n = input()
	if n == "0": main_menu()
	elif n == "1": parser (int(mode_2), int(mode_3))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""-----------------------------------------------||||Parsing Tools:||||--------------------------------------------------"""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Parsing Tools 1"""

def parser (answer2, answer3):

	files_list = open (script_dir + "/.files_list.txt", "tw", encoding="utf-8")
	mess_file = open (script_dir + "/.mess.txt", "tw", encoding="utf-8")
	mess_file.write ("Made temporary file:  " + script_dir + "/.files_list.txt\n")
	mess_file.close ()

	dir_pattern = re.compile("^BSM\d{2}$")
	file_pattern = re.compile("^\d{8}\.\d{3}")

	if answer2 == 4: #OK

		print("Enter the relative path to the file in format: /ddmmyy/BSMnn/ddddy00x.00x (for example: /060118/BSM01/06018001.001)\n")
		file_to_process = input()

		print ("The list of files to process are compiling...\n")

		abs_file_path = script_dir + data_dir + file_to_process
		files_list.write(abs_file_path)
		
		print ("The list of files to process was made. It's in the script directory under the name  .files_list.txt\n")

	elif answer2 == 5: #OK
		print (
			"""Enter the list of the files through the space in format:\n
			/ddmmyy/BSMnn/ddddy00a.00a /ddmmyy/BSMnn/ddddy00b.00b /ddmmyy/BSMnn/ddddy00c.00c etc.\n
			(for example: /060118/BSM01/06018001.001 /281017/BSM01/28107001.001 etc.)\n
			Notice, that execution time is proportional to the number of files.\n
			""")

		file_list = list(input().split())

		print ("The list of files to process are compiling...\n")

		for abs_file in file_list:
			abs_file_path = script_dir + data_dir + abs_file
			files_list.write (abs_file_path + "\n")

		print ("The list of files to process was made. It's in the script directory under the name  .files_list.txt\n")

	elif answer2 == 2: #OK
		
		print (
			"""Enter the relative path to the day folder in format:  /ddmmyy\n
			(for example: /281017 etc.)\n
			Notice, that execution time is proportional to the number of files.\n""")

		dir_name = input ()

		print ("The list of files to process are compiling...\n")

		abs_dir_path = script_dir + data_dir + dir_name
		list_of_BSM = day_parser (abs_dir_path)
		for BSM in list_of_BSM.split ():
			BSM_name = abs_dir_path + "/" + BSM
			list_of_files = BSM_parser (BSM_name)
			files_list.write ('\n'.join ([(BSM_name + "/" + x) for x in list_of_files.split()]))
			files_list.write('\n')

		print ("The list of files to process was made. It's in the script directory under the name  .files_list.txt\n")
			
	elif answer2 == 3: #OK

		print (
			"""Enter the relative path to the BSM folder in format:  /ddmmyy/BSMnn\n
			(for example: /281017/BSM05 etc.)\n
			Notice, that execution time is proportional to the number of files.\n""")

		BSM_name = input ()

		print ("The list of files to process are compiling...\n")

		abs_BSM_path = script_dir + data_dir + BSM_name
		list_of_files = BSM_parser (abs_BSM_path)
		files_list.write ('\n'.join ([(abs_BSM_path + "/" + x) for x in list_of_files.split()]))

		print ("The list of files to process was made. It's in the script directory under the name  .files_list.txt\n")

	elif answer2 == 1: #NOT CHECKED!!!
		print (
			"""Enter the list of the days through the space in format:\n
			/ddmmyy /ddmmyy /ddmmyy etc.\n
			(for example: /060118/BSM01/06018001.001 /281017/BSM01/28107001.001 etc.)\n
			Notice, that execution time is proportional to the number of files.\n
			""")

		list_of_days = list(input().split())

		print ("The list of files to process are compiling...\n")

		for day in list_of_days:
			abs_dir_path = script_dir + data_dir + day
			list_of_BSM = day_parser (abs_dir_path)
			for BSM in list_of_BSM.split ():
				BSM_name = abs_dir_path + "/" + BSM
				list_of_files = BSM_parser (BSM_name)
				files_list.write ('\n'.join ([(BSM_name + "/" + x) for x in list_of_files.split()]))
				files_list.write('\n')

		print ("The list of files to process was made. It's in the script directory under the name  .files_list.txt\n")

	else:
		print("It seems that you've made the mistake. Please, try again:\n")
		files_list.close()
		parser (answer2)

	files_list.close()

	if answer3 == 3:
		print ("The list of files to process was made. It's in the script directory under the name  .files_list.txt\n")
		main_menu ()

	if answer3 == 4:
		print ("The list of temporary files are compiling...\n")
		mess_file = open (script_dir + "/.mess.txt", "tw", encoding="utf-8")
		files_list = open (script_dir + "/.files_list.txt", "r")
		for line in files_list:
			mess_file.write ("Made temporary file:  " + line + ".txt\n")
			mess_file.write ("Made temporary file:  " + line + ".whd\n")
			mess_file.write ("Made temporary file:  " + line + ".amp\n")
#			mess_file.write ("Made temporary file:  " + line + ".pes\n")
#			mess_file.write ("Made temporary file:  " + line + ".qpd\n")
#			mess_file.write ("Made temporary file:  " + line + ".fpd\n")
#			mess_file.write ("Made temporary file:  " + line + ".dpd\n")
			"""???????????????? MORE ????????"""
		"""пока что файлы с амплитудами, ПОЧИЩЕННЫМИ ОТ ПЬЕДЕСТАЛОВ, не производятся!!!"""
		
		print ("The list of temporary files was made. It's in the script directory under the name  .mess.txt\n")
		mess_file.close ()
		files_list.close ()		

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Parsing Tools 2"""

def start_processing ():

	files_list = open (".files_list.txt", "r")
	i = 0
	files = files_list.read()
	for file_to_process in files:
		i += 1
		print ("All time:")
		syprogressbar (i, len(files))
		process_single_file(file_to_process)

	print ("All the processing operations are finished.")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Parsing Tools 2"""

def day_parser (directory): #OK
	
	dir_pattern = re.compile ("^BSM\d{2}$")
	an_dir_pattern = re.compile ("BSM\d{2}")
	bsm_dir_list_1 = [re.findall (dir_pattern, f) for f in os.listdir (directory)]
	bsm_dir_list_2 = ' '.join ([str (k) for k in bsm_dir_list_1])
	bsm_dir_list_3 = sorted(re.findall (an_dir_pattern, bsm_dir_list_2))
	bsm_dir_list = ' '.join ([g for g in bsm_dir_list_3])

	return bsm_dir_list

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Parsing Tools 3"""

def BSM_parser (directory): #OK

	raw_file_pattern = re.compile ("^\d{8}\.\d{3}$")
	an_raw_file_pattern = re.compile ("\d{8}\.\d{3}")
	list_files_1 = [re.findall (raw_file_pattern, k) for k in os.listdir (directory)]
	list_files_2 = ' '.join ([str (k) for k in list_files_1])
	list_files_3 = sorted(re.findall (an_raw_file_pattern, list_files_2))
	list_files = ' '.join ([g for g in list_files_3])

	return list_files

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""----------------------------------------------||||Processing tools:||||----------------------------------------------"""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Processing menu body 1"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def process_single_file(file_to_process):

	mess_file = open(".mess.txt","tw")


#Converting the raw file to .txt ( --> .txt)
	from_raw_to_txt(file_to_process)
	mess_file.write("Made temporary file:  " + make_BSM_file_temp(file_to_process)[:-4] + ".txt\n")
	print("Made temporary file:  " + make_BSM_file_temp(file_to_process)[:-4] + ".txt\n")
#Cleaning the .txt file of head and flags (.txt --> .whd)
	head_cleaner(make_BSM_file_temp(file_to_process)[:-4] + ".txt")
	mess_file.write("Made temporary file:  " + make_BSM_file_temp(file_to_process)[:-4] + ".whd\n")
	print("Made temporary file:  " + make_BSM_file_temp(file_to_process)[:-4] + ".whd\n")
#Converting the .wh file to amplitudes (.whd --> .amp)
	data_to_ampl(make_BSM_file_temp(file_to_process)[:-4] + ".whd")
	mess_file.write("Made temporary file:  " + make_BSM_file_temp(file_to_process)[:-4] + ".amp\n")
	print("Made temporary file:  " + make_BSM_file_temp(file_to_process)[:-4] + ".amp\n")
#Collecting quick pedestals ( --> .qpd)
#	get_quick_pedestals(make_BSM_file_temp(file_to_process)[:-4] + ".whd")
#	mess_file.write("Made temporary file:  " + make_BSM_file_temp(file_to_process)[:-4] + ".qpd\n")
#Converting the .amp file to photoelectrons (.amp --> .pes)
#subprocess.call("ipython Y_ampl_to_pe.py " + Y_syiactfunc.make_BSM_file_temp(file_to_process)[:-4] + ".amp", shell=True)


#subprocess.call("ipython Y_data_txt_head_cleaner.py " + file_to_process[:-12] + "." + file_to_process[-12:-4] + ".wh", shell=True)
#subprocess.call("ipython Y_data_txt_head_cleaner.py " + file_to_process[:-12] + "." + file_to_process[-12:-4] + ".ap", shell=True)
#subprocess.call("ipython Y_data_txt_head_cleaner.py " + file_to_process[:-12] + "." + file_to_process[-12:-4] + "asd", shell=True)


	mess_file.close()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def from_raw_to_txt (file_to_process):

#script_dir = "/home/yaroslav/Documents/TAIGA_PYTHON"
#data_dir = "/DATA"

#fin = open(file_to_process, 'rb')
#data = np.loadtxt(fin, dtype=np.uint16)
#np.savetxt(file_to_process[:-4] +".txt", data, fmt="%d")

#fout = open(Y_syiactfunc.make_BSM_file_temp(file_to_process)[:-4] + ".txt", 'tw', encoding='utf-8')




	fin = open(file_to_process, 'rb').read()
	fout = open(make_BSM_file_temp(file_to_process)[:-4] + ".txt", 'tw', encoding='utf-8')

	#main_array = np.zeros((len(fin), 4))

	for i in range (0, len(fin), 4):
		print("Raw data reading:")
		syprogressbar(i, len(fin))
	#	main_array[i][0], main_array[i][1], main_array[i][2], main_array[i][3] = fin[i], fin[i+1], fin[i+2], fin[i+3]

	#np.savetxt(fout, main_array, fmt="%d")
		fout.write(str(fin[i]) + "\t" + str(fin[i+1]) + "\t" + str(fin[i+2]) + "\t" + str(fin[i+3]) + '\n')

#	fin.close()
	fout.close()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def syprogressbar (x, y):

	print("Progress of operation:" + str(int(x/y*100)) + "%")
	print("["+ (int(x/y*100))*"#" + int((y-x)/y*100)*"_" + "]")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def make_BSM_file_temp (s):

	return s[:-12] + "." + s[-12:]
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def head_cleaner(file_to_process):

	fin = open(file_to_process, 'r')	
	data = np.loadtxt(fin)[6:]
	print("Data cleaning")
	data = data[np.all(data != 255, axis=1)]
	np.savetxt(file_to_process[:-4] +".whd", data, fmt="%d")
	fin.close()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def data_to_ampl(file_to_process):

	fin = open(file_to_process, 'r')
	data = np.loadtxt(fin)
	ampl = np.zeros((len(data), 2))
	print("Converting to amplitudes")
	ampl[:,0] = data[:,0] + 256*data[:,1]
	ampl[:,1] = data[:,2] + 256*data[:,3]
	np.savetxt(file_to_process[:-4] +".amp", ampl, fmt="%d")
	fin.close()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
