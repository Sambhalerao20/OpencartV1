@echo on

echo =====================================
echo MOVING TO PROJECT DIRECTORY
echo =====================================

cd /d C:\Users\sambhaji.bhalerao\PycharmProjects\OpencartV1

echo.
echo =====================================
echo ACTIVATING VIRTUAL ENVIRONMENT
echo =====================================

call .venv\Scripts\activate.bat

echo.
echo =====================================
echo UPGRADING PIP
echo =====================================

python -m pip install --upgrade pip

echo.
echo =====================================
echo INSTALLING REQUIRED PACKAGES
echo =====================================

pip install pytest

pip install selenium

pip install webdriver-manager

pip install pytest-html

pip install pytest-xdist

pip install pytest-ordering

pip install openpyxl

pip install allure-pytest

echo.
echo =====================================
echo ALL PACKAGES INSTALLED SUCCESSFULLY
echo =====================================

pip list

pause