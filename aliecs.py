#!/usr/bin/env python3

import argparse, json

class AliecsEnv:
  def __init__(self, input) -> None:
    if(type(input) is str):
      self.vars = self.ResolveVars(input)
    elif(type(input) is dict):
      self.vars = input
  def PrintQCworkflow(self):
    tableContents = {}
    colName = ['DPL', 'QC']
    colSuffix = ['_dpl_workflow', '_qc_remote_workflow']
    for k, v in self.vars.items():
      for i,name in enumerate(colName):
        if(k.find(colSuffix[i]) > -1):
          det = k.replace(colSuffix[i],'').upper()
          if(tableContents.get(det) is None): tableContents[det] = {}
          tableContents[det][name] = v
    # Print as Markdwon table
    print('|Detector|DPL workflow|QC workflow|Comment|')
    print('|---|:---| ---|:---|')
    for det in sorted(tableContents.keys()):
      print(f'|{det}|{tableContents[det]["DPL"]}|{tableContents[det]["QC"]}||')
    return None
  def ResolveVars(self, strVars : str ) -> dict:
    return vars

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Process ali-ecs env. configuration')
  parser.add_argument('input',type=str,help='Copy <Vars> from ali-ecs')
  args = parser.parse_args()
  newEnv = AliecsEnv(args.input)
  newEnv.PrintQCworkflow()