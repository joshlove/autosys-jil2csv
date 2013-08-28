#!/usr/bin/env python
import sys, re, tempfile

in_file = open(sys.argv[1], "r")
out_file = open(sys.argv[2], "w")
#temp_file = open("tempjil.tmp", "w")
temp_file = tempfile.TemporaryFile()

#Preprocessing 
for line in in_file:
	line = line.replace('job_type:','\njob_type:')	#Moves job type to its own line
	line = line.replace("\r\n","\n")				#Converts to Unix line endings
	line = re.sub('^ |\t','',line)					#rips off only leading spaces/tabs (newlines are needed)
	temp_file.write(line)
in_file.close()
temp_file.write("\n") #ensures the last job is appended
temp_file.seek(0)

#default values, if I missed any or CA adds any, they can go anywhere in here
#Just remember to change the output string below
default_data = {'insert_job': '','job_type': '','box_name': '','command': '','machine': '','owner': '','permission': '','date_conditions': '','days_of_week': '','start_times': '','run_window': '','condition': '','description': '','n_retrys': '','term_run_time': '','box_terminator': '','job_terminator': '','std_out_file': '','std_err_file': '','min_run_alarm': '','max_run_alarm': '','alarm_if_fail': '','max_exit_status': '','chk_files': '','profile': '','job_load': '','priority': '','auto_delete': '','group': '','application': '', 'exclude_calendar': ''}
datasets = []
data = default_data.copy()
outputString=""

for line in temp_file:
	if line == "\n":
		if outputString:
			datasets.append(outputString)
			data = default_data.copy()
			outputString=""
			continue
	elif re.match(r'^/\*',line):
		continue
	else:
		parameter, value = line.split(':',1)
		data[parameter] = value.strip()
		outputString=data['insert_job']+"\t"+data['job_type']+"\t"+data['box_name']+"\t"+data['command']+"\t"+data['machine']+"\t"+data['owner']+"\t"+data['permission']+"\t"+data['date_conditions']+"\t"+data['days_of_week']+"\t"+data['start_times']+"\t"+data['run_window']+"\t"+data['condition']+"\t"+data['description']+"\t"+data['n_retrys']+"\t"+data['term_run_time']+"\t"+data['box_terminator']+"\t"+data['job_terminator']+"\t"+data['std_out_file']+"\t"+data['std_err_file']+"\t"+data['min_run_alarm']+"\t"+data['max_run_alarm']+"\t"+data['alarm_if_fail']+"\t"+data['max_exit_status']+"\t"+data['chk_files']+"\t"+data['profile']+"\t"+data['job_load']+"\t"+data['priority']+"\t"+data['auto_delete']+"\t"+data['group']+"\t"+data['application']+"\n"
		
		
for job in datasets:
	out_file.write(job)
			
#Close files
out_file.close()
temp_file.close()
