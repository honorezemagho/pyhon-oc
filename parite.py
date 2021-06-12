#! /usr/bin/env python3
# coding: utf-8

import argparse

import analysis.csv as c_an 
import analysis.xml as x_an
import logging as lg

def parse_arguments(): 
    parser = argparse.ArgumentParser() 
    parser.add_argument("-d","--datafile",help="""CSV file containing pieces of information about the members of parliament""")
    parser.add_argument("-e","--extension", help="""Type  of file to analyse. Is it a CSV or an XML?""")
    parser.add_argument("-p","--byparty", help="""Display a graph by each political party""")
    parser.add_argument("-i","--info", help="""Information about the file!""")
    return parser.parse_args() 

def main():
    args = parse_arguments()
    try:
        datafile = args.datafile
        if datafile == None:
            raise Warning('You must indicate a datafile!')
        
        extension = args.extension 
        if extension == None:
            raise Warning('You must indicate an extension either csv or xml!')
        
        
        if args.extension == 'xml':
            x_an.launch_analysis(datafile)
        elif args.extension == 'csv':
            c_an.launch_analysis(datafile, args.byparty, args.info)
    except Warning as e:
        lg.warning(e)
        
    finally:
        lg.info('#################### Analysis is over ######################')

if __name__ == "__main__":
    main()