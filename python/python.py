#!/usr/bin/python

import sys, getopt

def check_help(argv):
   try:
      opts, args = getopt.getopt(argv,"i:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      b = ' -i <inputfile> -o <outputfile>'
      mensaje_help = 'Usar la siguiente sintaxis ' + sys.argv[0] + b + ' ...'
      print mensaje_help
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg


if __name__ == "__main__":
   check_help(sys.argv[1:])

   print inputfile