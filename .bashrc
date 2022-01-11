# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
# git is needed, and R is helpful for quick calculations when necessary, 
# as is Python
module load git
module load r
module load python

# Push a git commit
function push {
	git add --all
	git commit -m "$1"
	git push origin master
}

# Source bashrc
function sbash {
	source ~/.bashrc
}

# Vim edit bashrc
function vbash {
	vim ~/.bashrc
}

# Show bashrc
function cbash {
	cat ~/.bashrc
}

# Edit PBS script
function vpbs {
	vim ~/Sem3_2021_Project_light/execute.pbs
}

# Change into sem3 project repo dir
function cdsem3 {
	cd ~/Sem3_2021_Project_light/$1
}

# Update sem3 project repo
function sem3up {
	cdsem3
	git pull origin master
}

# Execute PBS script
function pbsex {
	cdsem3
	qsub execute.pbs
}

# List all subjobs running for current user
function pbsstat {
	qstat -t -u $USER
}

# Run contCompJobs on the ID of the job you want to monitor the progress of
function contCompJobs {
	comp1=$(pbsstat | grep X | grep "$1" | wc -l)
	alljobs=48
	ratio=$(R -e "$comp1/$alljobs*100" | grep "\[1\]" | sed 's/\[1\]\s//g')
	echo "Job $1 is $ratio% complete"
	while :
	do
		comp2=$(pbsstat | grep X | grep "$1" | wc -l)
		if [[ $comp2 > $comp1 ]]; then
			comp1=$comp2
			ratio=$(R -e "$comp2/$alljobs*100" | grep "\[1\]")
			ratio=$(echo $ratio | sed 's/\[1\]\s//g')
			echo "Job $1 is $ratio% complete"
		elif [[ $comp2 < $comp1 ]] && [[ $comp2 == "0" ]]; then
			echo "Job is complete!" && return
		fi
	done
}

function vct {
	cdsem3
	vim computeTrajectory.py
}

export PS1="\u@\h \W]\n\\$ "
export PS1="[ $(date "+%l:%M:%S%p, %A %d %B %Y")|$PS1"
