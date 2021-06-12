#! /usr/bin/env python3
# coding: utf-8

import os
import logging as lg

lg.basicConfig(level=lg.DEBUG)


def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "data", data_file)

    try:
        with open(path_to_file, "r") as file:
            preview = file.readline()  # read first line
            lg.info(
                "Yeah! We managed to read the file. Here is a preview: {}".format(
                    preview
                )
            )
    except FileNotFoundError as nfe:
        lg.critical("Ow :( The file was not found. Here is the message %s", nfe)

