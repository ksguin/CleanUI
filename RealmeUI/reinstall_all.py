import subprocess
import re

#File Source
Reinstall_list = open('Package_list_description.txt', 'r')
Lines = Reinstall_list.readlines()
Reinstall_list.close()

def adb_reinstall(pkg):
	print("Package: {}".format(pkg))
	subprocess.call("adb shell cmd package install-existing {}".format(pkg),shell=True)
	print("----------")
	return
	
def adb_enable(pkg):
	subprocess.call("adb shell pm enable --user 0 {}".format(pkg),shell=True)
	print("----------")
	return

def parse_yield_list(line):
    #Package name of form com.package.name
    return re.findall('[a-zA-Z.]+', line)[0]
    
def clean_usable_input(Lines):
	parsed_list=[]
	for line in Lines:
		# Strip & replace multiple spaces to one
		line= re.sub('\s+',' ',line.strip())
		if not line.startswith('|') and not line.startswith('%'):
			continue
		parsed_list.append(parse_yield_list(line))
	return parsed_list
    
def reinstall_fn(parsed_list):
	disable= False
	for x in parsed_list:
		if x.__eq__('Uninstall'):
			print("\t___________________________________________________")
			print("\t%     ...Reinstalling the following apps...       %")
			print("\t---------------------------------------------------")
			continue
		elif x.__eq__('Disable'):
			disable= True
			print("\t________________________________________________")
			print("\t%     ...Enabling the following apps...       %")
			print("\t------------------------------------------------")
			continue
		else:
			if disable == False:
				adb_reinstall(x)
			else:
				adb_enable(x)
	return

#Driver Program
parsed_list = clean_usable_input(Lines)
reinstall_fn(parsed_list)

print("\n\t______________________________________")
print("\t%     ...Enjoy the Unclean UI...     %")
print("\t--------------------------------------\n")
