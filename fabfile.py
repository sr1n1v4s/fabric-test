from fabric.api import local

def test1():
	local("cd /home/devops/python_tutorial/fabricscripts/fabric-test && touch file1 file2 file3")
	local("cd /home/devops/python_tutorial/fabricscripts/fabric-test && git add . && git commit -m test1")
	local("cd /home/devops/python_tutorial/fabricscripts/fabric-test && git push origin master")
