import os
import getpass


def menu_interface():
    print("\n\t###############################################")
    print("""\t\t Press 1: Basic Functions
             \t Press 2: Advanced Functions
             \t Press 0: Exit""")
    print("\t################################################")


def adv_menu():
    print("\n\t###############################################")
    print("""\t\t Press 1: Configure the Web Server
             \t Press 2: Configuring yum and Install Docker
             \t Press 3: Login into other system
             \t Press 4: Run Docker Commands
             \t Press 5: Send File to the connected system
             \t Press 6: Setup Hadoop
             \t Press 7: Create LVM Partition
             \t Press 8: Increase size of existing LVM partition
             \t Press 9: Configure Yum/DNF
             \t Press 10: Back
             \t Press 0: Exit""")
    print("\t################################################")


def basic_menu():
    print("\n\t###############################################")
    print("""\t\t Press 1: Date
             \t Press 2: Calendar
             \t Press 3: Current Directory
             \t Press 4: List of directories
             \t Press 5: Create a new directory
             \t Press 6: Delete an existing directory
             \t Press 7: Create a file
             \t Press 8: Delete an existing file
             \t Press 9: Create a new User account
             \t Press 10: Back
             \t Press 0: Exit""")
    print("\t###############################################")


def hadoop_setup():
	print("""
	Setting Up Hadoop on local system """)
	print("""
		Select the option:
		Configure system as: 
		1: Namenode
		2: Datanode""")

	option = int(input("Enter your choice : "))
		
	if option == 1:
		IP = input("Enter the IP of your System: ")
		port_no = input("Port number for Hadoop: ")
		folder = input("Enter the the folder you want to create for namenode : ")
		os.system("sudo rpm -ivh /root/jdk-8u171-linux-x64.rpm")
		print(os.system("sudo rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force"))
		os.system("mkdir /etc/{}".format(folder))
		
		with open("/etc/hadoop/hdfs-site.xml", "w") as out_file:
			hdfs_line ="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>

<name>dfs.name.dir</name>
<value>{}</value>

</property>

</configuration>
""".format(folder)
			out_file.write(hdfs_line)
		with open("/etc/hadoop/core-site.xml", "w") as out_file:
					
			core_line ="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>

<name>fs.default.name</name>
<value>hdfs://{}:{}</value>

</property>

</configuration>
""".format(IP,port_no)
			out_file.write(core_line)
			
		os.system("sudo hadoop namenode -format {}".format(folder))
		os.system("sudo hadoop-daemon.sh start namenode")

	elif option == 2 :
		IP = input("Enter the IP of Namenode System : ")
		port_no = input("Enter the port no of Namenode : ")
		folder = input("Enter the the folder you want to create for datanode : ")
		os.system("sudo rpm -ivh /root/jdk-8u171-linux-x64.rpm")
		os.system("sudo rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force")
		os.system("mkdir /{}".format(folder))
			

		with open("/etc/hadoop/hdfs-site.xml", "w") as out_file:
					
			hdfs_line ="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>

<name>dfs.data.dir</name>
<value>{}</value>

</property>

</configuration>
""".format(folder)
			out_file.write(hdfs_line)
		with open("/etc/hadoop/core-site.xml", "w") as out_file:
					
			core_line ="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>

<name>fs.default.name</name>
<value>hdfs://{}:{}</value>

</property>

</configuration>
""".format(IP,port_no)
			out_file.write(core_line)
			
		
		os.system("sudo hadoop-daemon.sh start datanode")




os.system("clear")
os.system("tput setaf 1")
print("\t\t\tWelcome To The TUI Program")
os.system("tput setaf 7")
print("\t\t\t--------------------------")

#To set password
i=0
while i<2:
    passwd = getpass.getpass("Enter the Password : ")
    apass = "Pass@123"
    if passwd==apass:
        os.system("tput setaf 4")
        print("Logged in successfully")
        os.system("tput setaf 7")
        break
    else:
        os.system("tput setaf 1")
        print("Wrong Password. Please retry")
        os.system("tput setaf 7")
    i+=1
else:
    os.system("tput setaf 1")
    print("Authentication failed\nexiting........")
    os.system("tput setaf 7")
    os.system("sleep 1")
    exit()

while True:
    print("Select your Task location (local/remote): ",end=' ')
    location=input()

    if location=="local" or location=="remote":
        break
    else:
        print("Invalid Location!")
    i+=1
    
#Menu Interface for reference



if location=="remote":
    os.system("tput setaf 3")
    print("Enter the remote IP address : ")
    os.system("tput setaf 7")
    remoteip=input()

y=0

while True:
    if y==0:
        y=1
    else:
        os.system("tput setaf 1")
        print("\t\t\tWelcome To The TUI Program")
        os.system("tput setaf 7")
        print("\t\t\t--------------------------")

    menu_interface()
    os.system("tput setaf 3")
    print("\n\t\tEnter your Choice : ",end=" ")
    os.system("tput setaf 7")
    y=int(input())

    if y==1:
        os.system("clear")
        os.system("tput setaf 1")
        print("\t\t\tWelcome To The TUI Program")
        os.system("tput setaf 7")
        print("\t\t\t--------------------------")

        while True:

            basic_menu()
            os.system("tput setaf 3")
            print("\n\t\tEnter your Choice : ",end=" ")
            os.system("tput setaf 7")
            x=int(input())

    
            if location=="remote":

                if x==1:
                    os.system("tput setaf 4")
                    os.system("ssh %s date" %remoteip)
                    os.system("tput setaf 7")
    
                elif x==2:
                    os.system("tput setaf 4")
                    os.system("ssh %s cal" %remoteip)
                    os.system("tput setaf 7")
    
                elif x==3:
                    os.system("tput setaf 4")
                    os.system("ssh %s pwd" %remoteip)
                    os.system("tput setaf 7")
    
                elif x==4:
                    os.system("tput setaf 4")
                    os.system("ssh %s ls" %remoteip)
                    os.system("tput setaf 7")
    
                elif x==5:
                    os.system("tput setaf 4")
                    print("=>Enter the name of the directory to be created : ",end=' ')
                    os.system("tput setaf 7")
                    create_directory=input()
                    if os.system("ssh %s mkdir %s" %(remoteip, create_directory))==0:
                        os.system("tput setaf 2")
                        print("=>Directory created successfully")
                    os.system("tput setaf 7")

                elif x==6:
                    os.system("tput setaf 4")
                    print("=>Enter the name of the directory to be removed : ",end=' ')
                    rem_dir=input()
                    if os.system("ssh %s rm -r -f %s" %(remoteip, rem_dir))==0:
                        os.system("tput setaf 2")
                        print("=>Directory removed successfully")
                    else:
                        print("File does not exist")
                    os.system("tput setaf 7")

                elif x==7:
                    os.system("tput setaf 4")
                    print("=>Enter the name of the file to be created : ",end=' ')
                    name=input()
                    if os.system("ssh %s touch %s" %(remoteip, name))==0:
                        os.system("tput setaf 2")
                        print("=>File created successfully")
                    os.system("tput setaf 7")

                elif x==8:
                    os.system("tput setaf 4")
                    print("=>Enter the name of the file you want to delete : ",end=' ')
                    name=input()
                    if os.system("ssh %s rm %s" %(remoteip, name))==0:
                        os.system("tput setaf 2")
                        print("=>File deleted successfully")
                    else:
                        print("File does not exist")
                    os.system("tput setaf 7")

                elif x==9:
                    os.system("tput setaf 4")
                    print("=>Enter the Username you want to create : ",end=" ")
                    name=input()
                    if os.system("ssh %s useradd %s" %(remoteip, name))==0:
                        os.system("tput setaf 2")
                        print("User created successfully")
                    else:
                        print("Failed to create user")
                    os.system("tput setaf 7")
                
                elif x==10:
                    os.system("clear")
                    break

                elif x==0:
                    os.system("tput setaf 1")
                    print("=>Exiting.....")
                    os.system("tput setaf 7")
                    os.system("sleep 1")
                    os.system("clear")
                    exit()

                else:
                    os.system("tput setaf 1")
                    print("=>Option not supported!")
                    os.system("tput setaf 7")
    
                input("Press any key to continue")
                os.system("clear")
                os.system("tput setaf 1")
                print("\t\t\tWelcome To The TUI Program")
                os.system("tput setaf 7")
                print("\t\t\t--------------------------")
                


            elif location=="local":
        
                if x==1:
                    os.system("tput setaf 4")
                    os.system("date")
                    os.system("tput setaf 7")

                elif x==2:
                    os.system("tput setaf 4")
                    os.system("cal")
                    os.system("tput setaf 7")

                elif x==3:
                    os.system("tput setaf 4")
                    os.system("pwd")
                    os.system("tput setaf 7")

                elif x==4:
                    os.system("tput setaf 4")
                    os.system("ls")
                    os.system("tput setaf 7")

                elif x==5:
                    os.system("tput setaf 4")
                    print("=>Enter the name of the directory to be created : ",end=' ')
                    os.system("tput setaf 7")
                    create_directory=input()
                    if os.system("mkdir %s" %create_directory)==0:
                        os.system("tput setaf 2")
                        print("=>Directory created successfully")
                    os.system("tput setaf 7")

                elif x==6:
                    os.system("tput setaf 4")
                    print("=>Enter the name of the directory to be removed : ",end=' ')
                    rem_dir=input()
                    if os.system("rm -r-f %s" %rem_dir)==0:
                        os.system("tput setaf 2")
                        print("=>Directory removed successfully")
                    os.system("tput setaf 7")

                elif x==7:
                    os.system("tput setaf 4")
                    print("=>Enter the name of the file to be created : ",end=' ')
                    name=input()
                    if os.system("touch %s" %name)==0:
                        os.system("tput setaf 2")
                        print("=>File created successfully")
                    os.system("tput setaf 7")
    
                elif x==8:
                    os.system("tput setaf 4")
                    print("=>Enter the name of the file you want to delete : ",end=' ')
                    name=input()
                    if os.system("rm %s" %name)==0:
                        os.system("tput setaf 2")
                        print("=>File deleted successfully")
                    os.system("tput setaf 7")

                elif x==9:
                    os.system("tput setaf 4")
                    print("=>Enter the Username you want to create : ",end=" ")
                    name=input()
                    if os.system("useradd %s" %name)==0:
                        os.system("tput setaf 2")
                        print("User created successfully")
                    else:
                        print("Failed to create user")
                    os.system("tput setaf 7")

                elif x==10:
                    os.system("clear")
                    break

                elif x==0:
                    os.system("tput setaf 1")
                    print("=>Exiting.......")
                    os.system("tput setaf 7")
                    os.system("sleep 1")
                    os.system("clear")
                    exit()

                else:
                    os.system("tput setaf 1")
                    print("=>Option not supported!")
                    os.system("tput setaf 7")

                input("Press any key to continue")
                os.system("clear")
                os.system("tput setaf 1")
                print("\t\t\tWelcome To The TUI Program")
                os.system("tput setaf 7")
                print("\t\t\t--------------------------")
                
    
    elif y==2:
        os.system("clear")
        os.system("tput setaf 1")
        print("\t\t\tWelcome To The TUI Program")
        os.system("tput setaf 7")
        print("\t\t\t--------------------------")

        while True:
            adv_menu()
            os.system("tput setaf 3")
            print("\n\t\tEnter your Choice : ",end=" ")
            os.system("tput setaf 7")
            x=int(input())

            if location=="local":
                
                if x==1:
                    os.system("tput setaf 2")
                    print("Installing Daemon......")
                    os.system("sleep 1")
                    os.system("dnf install httpd  -y")
                    os.system("tput setaf 4")
                    print("Enter the location of the Web page : ")
                    page_name = input()
                    if os.system("cp %s /var/www/html/" %(page_name))==0:
                        os.system("systemctl stop firewalld")
                        os.system("systemctl start httpd")
                        os.system("systemctl enable httpd")
                        os.system("tput setaf 3")
                        print("Configuring the server.......")
                        os.system("sleep 1")
                        print("Web server has been configured")
                    else:
                        print("Unable to configure web server")
                    os.system("tput setaf 7")
                
                elif x==2:
                    with open("/etc/yum.repos.d/docker.repo", "w") as out_file:
					
                            docker_line ="""
[docker]
baseurl = https://download.docker.com/linux/centos/7/x86_64/stable/
gpgcheck = 0
name = My docker repo
"""
                            out_file.write(docker_line)
                    os.system("sudo yum install docker-ce --nobest")
                    os.system("sudo systemctl start docker")
                    os.system("sudo systemctl enable docker")
                
                elif x==3:
                    os.system("tput setaf 4")
                    print("Please Enter the IP address of the remote system you want to Log into : ")
                    os.system("tput setaf 7")
                    ip_addr = input()
                    os.system("tput setaf 4")
                    print("Please Enter the User Account name of the remote System : ")
                    os.system("tput setaf 7")
                    user_name = input()
                    os.system("ssh -l %s %s" %(user_name, ip_addr)) 
                
                elif x==4:
                    while True:
                        os.system("clear")
                        print("""
1: Running container
2: Available images 
3: Launch new container
4: Stop running conatiner
5: Start stopped container
6: Login to running cotainer
7: List of containers( stoped and running)
8: Kill all the running containers
9: Exit from docker menu""")
                        os.system("setenforce 0")
                        cmd = int(input("Enter your choice "))
                        if cmd == 1:
                            os.system("sudo docker ps")
                        elif cmd == 2:
                            os.system("sudo docker images ")	
                        elif cmd == 3:
                            name = input("Enter name you want to give to your os:")
                            print("Select image from following list : ")		
                            os.system("sudo docker images : ")
                            image = input("Enter image name : ")
                            version = input("Enter version : ")
                            os.system("sudo docker run -it --name {} {}:{}".format(name,image,version))
                        elif cmd == 4: 
                            name = input("Enter the name of os you want to stop")
                            print("sudo docker stop {}".format(name))
                        elif cmd == 5:
                            os.system("docker ps -a")
                            name = input("Select container name from below stopped containers : ")
                            os.system("sudo docker start {}".format(name)) 
                        elif cmd == 6:
                            os.system("docker ps -a")
                            name = input("Select container name from below containers : ")
                            os.system("sudo docker attach {}".format(name))
                        elif cmd == 7: 
                            os.system("sudo docker ps -a")
                        elif cmd == 8:
                            os.system("sudo docker kill `docker ps -a`")
                        elif cmd ==9:
                            os.system("clear")
                            break
                        else:
                            os.system("tput setaf 1")
                            print("=>Option not supported!")
                            os.system("tput setaf 7")
                
                elif x==5:
                    os.system("tput setaf 4")
                    print("Please Enter the IP address of the remote system : ")
                    os.system("tput setaf 7")
                    ip_addr = input()
                    os.system("tput setaf 4")
                    print("Please Enter the File Name : ")
                    os.system("tput setaf 7")
                    File_name = input()
                    os.system("tput setaf 4")
                    print("Please Enter Download Location in the Remote system : ")
                    os.system("tput setaf 7")
                    Down_Loc = input()
                    os.system("scp %s %s:%s" %(File_name, ip_addr, Down_Loc))
                    os.system("tput setaf 3")
                    print("File sent successfully")
                    os.system("tput setaf 7")    
                
                elif x==6:
                    hadoop_setup()
                
                elif x==7:
                    dev = []
                    b = ""
                    print("Creating LVM partition : ")
                    no_device = int(input("Enter no of devices you want to create a LVM : "))
                    for i in range(no_device):	
                        a = "/dev/{}".format(input("Device {}".format(i+1)))
                        b = b + a + " " 
                        dev.append(a)
                    for j in range(len(dev)):
                        os.system("sudo pvcreate {}".format(dev[j]))
                    vg_name = input("Enter your Volume Group Name : ")
                    os.system("sudo vgcreate {} {}".format(vg_name,b))
                    size = input("Enter the size of lvm partition you want : ")
                    lvm_name = input("Enter the name of LVM : ")
                    os.system("sudo lvcreate --size {} --name {} {}".format(size,lvm_name,vg_name))
                    folder=input("Enter the path of folder contributing to namenode")
                    os.system("sudo mkfs.ext4 /dev/{}/{}".format(vg_name,lvm_name))	
                    os.system("sudo mount /dev/{}/{} {}".format(vg_name,lvm_name,folder))
                
                elif x==8:
                    size = input("Enter amount of space you want to increase : ")
                    vg_name = input("Enter VG name of LVM")
                    lvm_name = input("Enter LVM name")
                    os.system("sudo lvextend --size +{} /dev/{}/{}".format(size,vg_name,lvm_name))
                    os.system("sudo resize2fs /dev/{}/{}".format(vg_name,lvm_name))
                
                elif x==9:
                    os.system("cd /etc/yum.repos.d/")
                    os.system("tput setaf 4")
                    print("Enter the name of the repository you want to install : ")
                    os.system("tput setaf 7")
                    repo_name = input()
                    os.system("touch %s.repo" %repo_name)
                    
                    if os.system("echo -e [dvd1]\\nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\\ngpgcheck=0\\n\\n[dvd2]\\nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\\ngpgcheck=0 | cat > %s.repo" %repo_name) == 0:
                        os.system("cd")
                        os.system("dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
                        os.system("tput setaf 2")
                        print("Yum/DNF has been configured")
                    os.system("tput setaf 7")
                
                elif x==10:
                    os.system("clear")
                    break

                elif x==0:
                    os.system("tput setaf 1")
                    print("Exiting....")
                    os.system("tput setaf 7")
                    os.system("sleep 1")
                    os.system("clear")
                    exit()
                
                else:
                    os.system("tput setaf 1")
                    print("=>Option not supported!")
                    os.system("tput setaf 7")
                    
                input("Press any key to continue")
                os.system("clear")
                os.system("tput setaf 1")
                print("\t\t\tWelcome To The TUI Program")
                os.system("tput setaf 7")
                print("\t\t\t--------------------------")

            if location=="remote":
            
                if x==1:
                    os.system("tput setaf 2")
                    print("Installing Daemon in the remote system......")
                    os.system("sleep 1")
                    if os.system("ssh %s 'dnf install httpd'" %remoteip)==0:
                        os.system("tput setaf 4")
                        print("Enter the location of the Web page : ")
                        page_name = input()
                        if os.system("ssh %s 'cp %s /var/www/html/web_page.html'" %(remoteip, page_name))==0:
                            os.system("ssh %s 'systemctl stop firewalld'" %remoteip)
                            os.system("ssh %s 'systemctl start httpd'")
                            os.system("tput setaf 3")
                            print("Configuring the server.......")
                            os.system("sleep 1")
                            print("Web server has been configured in [%s] host" %remoteip)
                        else:
                            print("Unable to configure web server")
                    os.system("tput setaf 7")
                
                elif x==2:
                    os.system("tput setaf 4")
                    print("Option Coming Soon ")
                
                elif x==3:
                    os.system("tput setaf 4")
                    print("Please Enter the User Account name of the remote System : ")
                    os.system("tput setaf 7")
                    user_name = input()
                    os.system("ssh -l %s %s" %(user_name, remoteip))
                elif x==4:
                    print("Option Coming soon")
                
                elif x==5:
                    os.system("tput setaf 4")
                    print("Please Enter the File Name : ")
                    os.system("tput setaf 7")
                    File_name = input()
                    os.system("tput setaf 4")
                    print("Please Enter Download Location in the Remote system : ")
                    os.system("tput setaf 7")
                    Down_Loc = input()
                    os.system("scp %s %s:%s" %(File_name, remoteip, Down_Loc))
                    os.system("tput setaf 3")
                    print("File sent successfully")
                    os.system("tput setaf 7")
                
                elif x==6:
                    print("Option Coming soon")
                
                elif x==7:
                    print("Option Coming soon")
                
                elif x==8:
                    print("Option Coming soon")
                
                elif x==9:
                    os.system("cd /etc/yum.repos.d/")
                    os.system("tput setaf 4")
                    print("Enter the name of the repository you want to install : ")
                    os.system("tput setaf 7")
                    repo_name = input()
                    os.system("ssh %s 'cd /etc/yum.repos.d/; touch %s.repo; echo -e [dvd1]\\nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\\ngpgcheck=0\\n\\n[dvd2]\\nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\\ngpgcheck=0 > %s.repo'" %(remoteip, repo_name, repo_name))
                    os.system("tput setaf 2")
                    print("Yum/DNF has been configured")
                    os.system("tput setaf 7")
                
                elif x==10:
                    os.system("clear")
                    break
                
                elif x==0:
                    os.system("tput setaf 1")
                    print("Exiting....")
                    os.system("tput setaf 7")
                    os.system("sleep 1")
                    os.system("clear")
                    exit()
                
                else:
                    os.system("tput setaf 1")
                    print("=>Option not supported!")
                    os.system("tput setaf 7")

                input("Press any key to continue")
                os.system("clear")
                os.system("tput setaf 1")
                print("\t\t\tWelcome To The TUI Program")
                os.system("tput setaf 7")
                print("\t\t\t--------------------------")


    elif y==0:
        os.system("tput setaf 1")
        print("=>Exiting.......")
        os.system("tput setaf 7")
        os.system("sleep 1")
        os.system("clear")
        exit()

    else:
        os.system("tput setaf 1")
        print("=> Option Not Supported!")
        os.system("tput setaf 7")
        input("Press any key to continue")
        os.system("clear")
        

