# LinuxServer/FreeCad – freecadcmd not working in cli

## steps previous debugged ending with issue
  All Code is available 

1) Add Dockerfile:
   
![image](https://github.com/ThaL3g3nd27/issue-FreeCad-freecadcmd/assets/163481580/d028a269-97c4-4b47-89b5-991e4c7dd9f8)

2) Add the docker-compose.yaml
   
![image](https://github.com/ThaL3g3nd27/issue-FreeCad-freecadcmd/assets/163481580/bd6730a3-759a-4812-8337-74c9123893a5)


3) Build the Docker Image

	`docker-compose build`

4) Run the image using docker-compose

	`docker-compose up -d`

5) Open Browser to localhost:3000

![image](https://github.com/ThaL3g3nd27/issue-FreeCad-freecadcmd/assets/163481580/60a2c2d8-fc5f-471e-87f8-bbdc4b8c4c11)

&emsp; App works great

6) Open the boxtest.py within the FreeCad Gui

	File>Open>/app/py_scripts>boxtest.py (Defined in docker compose)

 ![image](https://github.com/ThaL3g3nd27/issue-FreeCad-freecadcmd/assets/163481580/c68adbdb-cf10-45a8-8892-c477cf49abca)

7) Run the Code in the FreeCad Gui

![image](https://github.com/ThaL3g3nd27/issue-FreeCad-freecadcmd/assets/163481580/c8a920d4-10c5-4a98-9f50-26b97638fa5a)


8) Box object is made

![image](https://github.com/ThaL3g3nd27/issue-FreeCad-freecadcmd/assets/163481580/4698fc00-d552-4254-83fc-7f5bf89b95de)

&emsp; And auto exported/downloaded as a box.step file in /py_scripts

![image](https://github.com/ThaL3g3nd27/issue-FreeCad-freecadcmd/assets/163481580/6f26b17b-0e89-45a9-8274-2bcc2bafdbf1)

&emsp; Python works Great!

&emsp; (If Needed) shutdown container - `docker compose down`




# ISSUE THE CLI doesn't WORK

9) Delete the box.step file so we know if the python script was ran again.

![image](https://github.com/ThaL3g3nd27/issue-FreeCad-freecadcmd/assets/163481580/9e4cebf1-791f-43bf-ac79-04d211851710)


10) Docker Exec into the running container

  `docker exec -it freecad bash`

![image](https://github.com/ThaL3g3nd27/issue-FreeCad-freecadcmd/assets/163481580/095e6b5a-5bf3-40f6-b9ca-a5832bc4579f)

11) cd into the py_scripts directory

![image](https://github.com/ThaL3g3nd27/issue-FreeCad-freecadcmd/assets/163481580/ab1396c2-8dfa-44d4-bf0d-34626b8960c8)


12) Open the freecadcmd cli to make sure it works

![image](https://github.com/ThaL3g3nd27/issue-FreeCad-freecadcmd/assets/163481580/f481dbea-35c8-4466-a695-984347bcdd45)

&emsp; This is due to Python environment variables… 

# Correct Example Usage:

https://youtu.be/RQW723n3DkU?si=dIt7jef6VmLHqkaF&t=596
![image](https://github.com/ThaL3g3nd27/issue-FreeCad-freecadcmd/assets/163481580/b43c0d03-22e4-437f-a9ec-e2fc14a49fb6)

# Purpose of the issue:

The Purpose of doing it from the command line is to automate the creation of the object defined by parameters/database so a backend can parametrically make parts.
The gui will only be used for testing. 

# Link to linuxServer/FreeCad:
https://github.com/linuxserver/docker-freecad.git
![image](https://github.com/ThaL3g3nd27/issue-FreeCad-freecadcmd/assets/163481580/e09b7588-403e-445c-9daf-19d911a01db7)

