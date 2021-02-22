import subprocess

def adb_reinstall(pkg):
	subprocess.call("adb shell cmd package install-existing {}".format(pkg),shell=True)
	return


#Uninstall File Source
Uninstall_list = open('Uninstall_list.txt', 'r')
Lines = Uninstall_list.readlines()
print("     ______________________________________________________")
print("     |     ...Re-installing the Uninstalled apps...       |")
print("     ------------------------------------------------------")
for line in Lines:
    line = line.strip()
    if "".__ne__(line):
    	adb_reinstall(line)
    	print("Package: {}".format(line))
    	print("----------")
Uninstall_list.close()

#Disable File Source
Disable_list = open('Disable_list.txt', 'r')
Lines = Disable_list.readlines()
print("     ___________________________________________________")
print("     |     ...Re-installing the Disabled apps...       |")
print("     ---------------------------------------------------")
for line in Lines:
    line = line.strip()
    if "".__ne__(line):
    	adb_reinstall(line)
        #output already shows package name
    	print("----------")
Disable_list.close()
