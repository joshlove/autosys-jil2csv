autosys-jil2csv
===============

Simple script(s) to take jil output (autorep -j * -q) and parse it into csv. Useful where you are not the autosys admin but require a deep knowledge of the range of jobs.

My goal is to write scripts in various langs (because why not). Input is expected to be a file populated with jil code. Output should be delimited. Shell script (bash) will come first, likely followed by ruby, python and then perl.

This CSV could easily be used to populate data. Unlike some of the other autosys tools on github, this does not assume you have access to the autosys database.
