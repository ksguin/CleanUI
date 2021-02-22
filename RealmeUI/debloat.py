import subprocess

def adb_uninstall(pkg):
	subprocess.call("adb shell pm uninstall --user 0 {}".format(pkg),shell=True)
	return
	
def adb_disable(pkg):
    subprocess.call("adb shell pm disable-user --user 0 {}".format(pkg),shell=True)
    return

#Uninstall File Source
Uninstall_list = open('Uninstall_list.txt', 'r')
Lines = Uninstall_list.readlines()
print("     ___________________________________________________")
print("     |     ...Uninstalling the following apps...       |")
print("     ---------------------------------------------------")
for line in Lines:
    line = line.strip()
    if "".__ne__(line):
    	adb_uninstall(line)
    	print("Package: {}".format(line))
    	print("----------")
Uninstall_list.close()

#Disable File Source
Disable_list = open('Disable_list.txt', 'r')
Lines = Disable_list.readlines()
print("     ________________________________________________")
print("     |     ...Disabling the following apps...       |")
print("     ------------------------------------------------")
for line in Lines:
    line = line.strip()
    if "".__ne__(line):
    	adb_disable(line)
        #output already shows package name
    	print("----------")
Disable_list.close()

print("\n")
print("     ______________________________________")
print("     |     ...Enjoy the Clean UI...       |")
print("     --------------------------------------")
print("\n")
