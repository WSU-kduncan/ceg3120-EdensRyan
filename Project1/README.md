Setup: 

Linux instance cheat sheet: 

bob = local machine 

ubuntu = AWS instance 

git = alternate user on the AWS instance 

The first step was accessing my AWS account via the command ($ ssh -i CEG3120FTW.pem ubuntu@3.232.159.130) 

From the home directory of that account I created the git repository with ($ git init --bare theArchive.git) Special attention was paid to the --bare portion of the command since missing it would create a separate workstation instead of a repository. This “init” command initializes the repo that I will be accessing through other users.  

I then opened another instance of linux with my home machine “bob”. And used the command ($git clone ubuntu@3.232.159.130:theArchive.git --config core.sshCommand="ssh -i ~/infoTech.pem"). This generated a workstation version of the ubuntu repo in bob.   

A new user was then added to the AWS system by inputting ($ sudo adduser git). The program then asked for a password and other profile based information for the newly created user “git”. I chose to give git the same private key that bob has for ease of access. But I could have also generated a new keypair saved the private key in the git user home and added the public key to the list of authorized keys in the repo host file.  

 

It should be noted any new folder containing a private key must have its permissions modified before the ssh command will allow it to be used. The permissions can be changed with ($ chmod 700 filename). This gives the user full permissions to read, write, and execute while denying all permissions to the group and others.  

 

Usage: 

I now returned to bob and accessed my clone of theArchive. I generated a new folder called Stormlight with ($mkdir Stormlight) entered the folder with a cd command and created a file with ($ touch Dalinar). I then used ($ git add Stormlight) to place my changes in the staging area. ($git commit) which after demanding I provide it a username prepared my staging area to be sent back to the master copy in ubuntu along with a comment describing my changes. Then I used ($git push) to send my changes back to the master copy in ubuntu.  

The final thing I did was duplicate my command to clone the repo ($git clone ubuntu@3.232.159.130:theArchive.git --config core.sshCommand="ssh -i ~/infoTech.pem") with my new user git. This allowed me to check and see that my changes had successfully been transferred.   

 

Proof: 

I had some difficulty adding my screenshots into vim and found that I couldn't simply place them in the comments section of dropbox either. I have included them in a pdf that I attached directly to the file through github. I hope that is sufficent and apologize for any inconveniance. 
 

 
