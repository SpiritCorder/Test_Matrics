# -*- coding: utf-8 -*-
"""
@author: sahan
"""

from ProjectsRatings import ProjectsRatings
from surprise import KNNBasic
from surprise.model_selection import train_test_split
from RecommenderMetrics import RecommenderMetrics

pr = ProjectsRatings()

print("Loading project ratings...")
data = pr.loadProjectsRatingsData();


print("\nBuilding recommendation model...")
trainSet, testSet = train_test_split(data, test_size=.25, random_state=1)

algo = KNNBasic()
algo.fit(trainSet)

print("\nComputing recommendations...")
predictions = algo.test(testSet)

print("\nEvaluating accuracy of model...")
print("RMSE: ", RecommenderMetrics.RMSE(predictions))
print("MAE: ", RecommenderMetrics.MAE(predictions))