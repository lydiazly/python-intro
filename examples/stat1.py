#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

statname = 'state.pvsm'
filename = 'xxx' + '..pvtu'
extractTimeSteps_name = 'ExtractTimeSteps'
#------------------------------------------------------
# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize.GetData()

# destroy renderView1
Delete(renderView1)
del renderView1
#------------------------------------------------------
# load state
LoadState(statname)

# find source
files = FindSource(filename)
ExtendFileSeries(files)

extractTimeSteps = FindSource(extractTimeSteps_name)

try:
    extractTimeSteps.Mode = 'Select Time Range'
except:
    extractTimeSteps.SelectionMode = 'Select Time Range'

itmin, itmax = (int(files.TimestepValues[0]), int(files.TimestepValues[-1]))
extractTimeSteps.TimeStepRange = [itmin, itmax]
SetActiveSource(extractTimeSteps)
#------------------------------------------------------
#### uncomment the following to render all views
RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
