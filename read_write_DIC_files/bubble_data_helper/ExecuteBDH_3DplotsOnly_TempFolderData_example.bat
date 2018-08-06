REM Here is an example batch script that compresses all DIC data & outputs all plots.
REM Note the use of "chcp1252" in order to interpret the "é" character in my user name. 
REM This chcp code may differ on different operating systems or different versions of Windows.

REM To run a batch script like this, remeber to use the "cd" command to change the working directory to this file's location.
REM E.g., if the .bat file is saved on the desktop, enter "cd desktop", then enter "ExecuteBDH_TempFolderData_example.bat";
REM or, if the .bat file is saved in the temp folder, enter "cd C:\temp", then enter "ExecuteBDH_TempFolderData_example.bat".

chcp 1252

cd C:\Users\Andrés\inverse_bubble_inflation\read_write_DIC_files\bubble_data_helper\

python BubbleDataHelper_3DplotsOnly.py --dataFolder C:\\temp\Blue_PVC_Valmex_BubbleTest00 --removeZeroZ True --outputPlot True --surfaceGrid True
python BubbleDataHelper_3DplotsOnly.py --dataFolder C:\\temp\Blue_PVC_Valmex_BubbleTest01 --removeZeroZ True --outputPlot True --surfaceGrid True
python BubbleDataHelper_3DplotsOnly.py --dataFolder C:\\temp\Blue_PVC_Valmex_BubbleTest02 --removeZeroZ True --outputPlot True --surfaceGrid True
python BubbleDataHelper_3DplotsOnly.py --dataFolder C:\\temp\Blue_PVC_Valmex_BubbleTest03 --removeZeroZ True --outputPlot True --surfaceGrid True
python BubbleDataHelper_3DplotsOnly.py --dataFolder C:\\temp\Black_PVC_Cape_Coaters_BubbleTest01\ --removeZeroZ True --outputPlot True --surfaceGrid True
python BubbleDataHelper_3DplotsOnly.py --dataFolder C:\\temp\Black_PVC_Cape_Coaters_BubbleTest02\ --removeZeroZ True --outputPlot True --surfaceGrid True
REM python BubbleDataHelper_3DplotsOnly.py --dataFolder C:\\temp\Black_PVC_Cape_Coaters_BubbleTest03\ --removeZeroZ True --outputPlot True --surfaceGrid True
REM python BubbleDataHelper_3DplotsOnly.py --dataFolder C:\\temp\Black_PVC_Cape_Coaters_BubbleTest04\ --removeZeroZ True --outputPlot True --surfaceGrid True