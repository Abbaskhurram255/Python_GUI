@echo off
copy *.py "C:\Users\Adi\Documents\GitHub\hindCPlusPlus" && copy "requirements.txt" "C:\Users\Adi\Documents\GitHub\hindCPlusPlus" && xcopy "build" "C:\Users\Adi\Documents\GitHub\hindCPlusPlus\build" /s /e /i /h /c /y
if exist hindGui (
    xcopy "hindGui" "C:\Users\Adi\Documents\GitHub\hindCPlusPlus\hindGui" /s /e /i /h /c /y
)
echo Uploading...
cd C:\Users\Adi\Documents\GitHub\hindCPlusPlus && git add . && git commit -m "Update KL_Py.py" && git push
cd C:\Users\Adi\Downloads\Python_GUI && git add . && git commit -m "Update ." && git push && cd ..\