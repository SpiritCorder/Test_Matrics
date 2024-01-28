# -*- coding: utf-8 -*-
"""
@author: sahan
"""

import os
import csv
import sys

from surprise import Dataset
from surprise import Reader


class ProjectsRatings:

    projectID_to_name = {}
    name_to_projectID = {}
    ratingsPath = './ratings.csv'
    projectsPath = './projects.csv'
    
    def loadProjectsRatingsData(self):

        # Look for files relative to the directory we are running from
        os.chdir(os.path.dirname(sys.argv[0]))

        ratingsDataset = 0
        self.projectID_to_name = {}
        self.name_to_projectID = {}

        reader = Reader(line_format='user rating item', sep=',', skip_lines=1)

        ratingsDataset = Dataset.load_from_file(self.ratingsPath, reader=reader)

        with open(self.projectsPath, newline='', encoding='ISO-8859-1') as csvfile:
                projectReader = csv.reader(csvfile)
                next(projectReader)  #Skip header line
                for row in projectReader:
                    projectID = int(row[0])
                    projectName = row[1]
                    self.projectID_to_name[projectID] = projectName
                    self.name_to_projectID[projectName] = projectID

        return ratingsDataset
    
    
