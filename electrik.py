import regex
import sys
import os.path
import os
CONFIG_ADAPTER_DIR = "adapter/"

adapter_loc = os.path.join(CONFIG_ADAPTER_DIR, sys.argv[1])
print(f'Loading adapter at {adapter_loc}')
file = sys.argv[2]
out = sys.argv[3]
print(f'Adapting {file} to {out} using adapter {adapter_loc}')
adapter = open(adapter_loc)
lines = adapter.readlines()
if lines[0].startswith('O!'):
  print('Adapter takes output argument')
else:
  print(f'[WARN] Adapter does not take output argument')
for i in lines[1:]:
  if i.startswith('Sys.Run('):
    command = i[8:].strip('(').strip(')').format(file=file)
    print(f'Running Command: {command}')
    os.system(command)
  elif i == '?':
    print('Adapter ended.')
    exit()
  else:
  raise Exception(f'Command {i} is invalid')
  
  
