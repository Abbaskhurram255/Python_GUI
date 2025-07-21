@echo off
if not exist "C:\Users\Adi\Documents\GitHub\hindCPlusPlus" (
    exit
)
copy "KL_Py.py" "C:\Users\Adi\Documents\GitHub\hindCPlusPlus"
echo Uploading...
cd C:\Users\Adi\Documents\GitHub\hindCPlusPlus && git add . && git commit -m "Update KL_Py.py" && git push
cd C:\Users\Adi\Downloads\Python_GUI && git add . && git commit -m "Update ." && git push && cd ..\