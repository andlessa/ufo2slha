#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 11:32:10 2019

@author: gonzalez
         Andre Lessa
"""

import numpy as np
import logging as logger


class ParameterSpace(object):
    """
    Holds information about the parameter space (variables and ranges)
    and the methods for generating samples of points in the parameter space.
    """
    
    def __init__(self,parametersDict,n_pieces,maxPoints=None):
        """
        :param parametersDict: A dictionary with the label for the parameters as keys and a list with the parameter lower and
                               upper limits as values.
        :param n_pieces: Number of pieces to split each parameter axis. It can be a single integer (all parameters are split
                         with the same number) or a dictionary with the parameter labels as keys and the number of
                         partitions as values.
        :param maxPoints: Maximum allowed number of total points to be generated. If it is not consistent with n_pieces,
                          the number of partitions will be evenly redefined for each dimension, so the total number of points
                          matches maxPoints.
        """
        
        self.parameters = np.array(sorted(list(parametersDict.keys())))
        self.minParameters = dict([[par,min(parametersDict[par])] for par in self.parameters])
        self.maxParameters = dict([[par,max(parametersDict[par])] for par in self.parameters])
        self.dim = self.parameters.size
        if isinstance(n_pieces,(int,float)):
            self.n_pieces = dict([key,int(n_pieces)] for key in self.parameters)
        elif isinstance(n_pieces,dict):
            self.n_pieces = n_pieces
        else:
            logger.error("n_pieces has to be a single integer or a dictionary")
            raise AttributeError()
        
        if maxPoints and np.prod(np.array(list(self.n_pieces.values()))) > maxPoints:
            n = int(np.ceil(float(maxPoints)**(1./self.dim)))
            self.n_pieces = dict([[key,n] for key in self.parameters])
            logger.info("Limiting the number of partitions in each dimension to %i" %n)
            
        for par,val in self.n_pieces.items():
            self.n_pieces[par] = max(1,val) #Make sure all dimensions get at least one point
            
        #Store steps in each dimension:
        self.steps = dict([[par,(self.maxParameters[par]-self.minParameters[par])/self.n_pieces[par]] 
                           for par in self.parameters])

    def get_jittered_samplig(self,outFile=None):
        '''
        Perform jittered sampling
        '''
        
        values = {}
        for par in self.parameters:
            minVal,maxVal = self.minParameters[par],self.maxParameters[par]
            nvals = self.n_pieces[par]
            values[par] = np.linspace(minVal,maxVal,nvals,endpoint=False)

        pVals = [values[par] for par in self.parameters]
        grid = np.meshgrid(*pVals)
        #Now create all points with a uniform grid:
        points = list(zip(*(x.flat for x in grid)))
        #Jitter points inside each grid cell:
        for ipt,pt in enumerate(points):
            pt = list(pt)
            for ipar,par in enumerate(self.parameters):
                pt[ipar] += np.random.uniform(0.,self.steps[par])                
            points[ipt] = tuple(pt)
        
        #Create structured numpy array with all numbers as floats:
        pTypes = [(par,pVals[0][i].dtype) for i,par in enumerate(self.parameters)]
        points = np.array(points,dtype=pTypes)
        
        if outFile:
            np.savetxt(outFile,points,fmt='%.5e',delimiter=',',header = ','.join(points.dtype.names)) 
        
        return points
                
 
    def get_random_sampling(self,outFile=None):
        '''Perform random sampling'''
        
        Npoints = np.prod(np.array(list(self.n_pieces.values())))
        points = []
        minVals = np.array([self.minParameters[par] for par in self.parameters])
        maxVals = np.array([self.maxParameters[par] for par in self.parameters])
        while len(points) < Npoints:
            pt = minVals + np.random.rand(self.dim)*(maxVals-minVals)
            points.append(tuple(pt))        

        #Create structured numpy array with all numbers as floats:
        pTypes = [(par,points[0][i].dtype) for i,par in enumerate(self.parameters)]
        points = np.array(points,dtype=pTypes) 
        
        if outFile:
            np.savetxt(outFile,points,fmt='%.5e',delimiter=',',header = ','.join(points.dtype.names)) 
        
        
        return points