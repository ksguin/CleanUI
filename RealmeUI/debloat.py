import subprocess
import re

#File Source
Uninstall_list = open('Package_list_description.txt', 'r')
Lines = Uninstall_list.readlines()
Uninstall_list.close()

def adb_uninstall(pkg):
	print("Package: {}".format(pkg))
	subprocess.call("adb shell pm uninstall --user 0 {}".format(pkg),shell=True)
	print("----------")
	return
	
def adb_disable(pkg):
	subprocess.call("adb shell pm disable-user --user 0 {}".format(pkg),shell=True)
	print("----------")
	return

def parse_yield_list(line):
    #Package name of form com.package.name
    return re.findall('[a-zA-Z0-9.]+', line)[0]
    
def clean_usable_input(Lines):
	parsed_list=[]
	for line in Lines:
		# Strip & replace multiple spaces to one
		line= re.sub('\s+',' ',line.strip())
		if not line.startswith('|') and not line.startswith('%'):
			continue
		parsed_list.append(parse_yield_list(line))
	return parsed_list
    
def uninstall_disable_fn(parsed_list):
	disable= False
	for x in parsed_list:
		if x.__eq__('Uninstall'):
			print("\t___________________________________________________")
			print("\t%     ...Uninstalling the following apps...       %")
			print("\t---------------------------------------------------")
			continue
		elif x.__eq__('Disable'):
			disable= True
			print("\t________________________________________________")
			print("\t%     ...Disabling the following apps...       %")
			print("\t------------------------------------------------")
			continue
		else:
			if disable == False:
				adb_uninstall(x)
			else:
				adb_disable(x)
	return

#Driver Program
parsed_list = clean_usable_input(Lines)
uninstall_disable_fn(parsed_list)

print("\n\t______________________________________")
print("\t%     ...Enjoy the Clean UI...       %")
print("\t--------------------------------------\n")
