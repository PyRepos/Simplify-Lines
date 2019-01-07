### Embedded version for Line Simplification

import arcpy
import os

FILE_CONFIG={
    'GEODATABASE' : 'REPORTS.mdb',
    'SMLINES' : 'Sm_Lines'
    }

GEODATABASE_GEODATABASE_CONFIG = {
    'StartEN' : '\StartEN',
    'EndEN' : '\EndEN',
    'StartEnd' : '\OSR_POINTS',
    'SsReport' : '\SMARTscan_report',
    'smPointLyName' : 'Sm_PointsXY',
    'smLineLyName' : '\smLineLyName',
    'SMLINES_COPY' : 'Test',
    'SMLINES' : '\Sm_Lines',
    'Copy':'\Test'
    }

arcpy.env.workspace = "C:\\1-CarnellDeployment\GeneralTest"
gdbDatabasePath = os.path.join(arcpy.env.workspace, FILE_CONFIG['GEODATABASE'])

#Set local parameters
inFeatureClass = os.path.join(gdbDatabasePath + GEODATABASE_GEODATABASE_CONFIG['SMLINES']).replace('\\','/')
copFeatureClass = os.path.join(gdbDatabasePath + GEODATABASE_GEODATABASE_CONFIG['Copy']).replace('\\','/')
gTolerance = "2 Feet"

#Since Generalize permanently updates the input, first make a copy of the original FC
arcpy.CopyFeatures_management (inFeatureClass, copFeatureClass)

#Use the Generalize tool to simplify the Buffer input to shorten Buffer processing time
arcpy.Generalize_edit(copFeatureClass, gTolerance)

