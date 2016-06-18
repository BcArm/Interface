UI_Path=UI

echo "Generating UIs...\n"
echo "Generating MainUI"
pyuic4 -o $UI_Path/MainUI/MainUI.py $UI_Path/MainUI/MainUI.ui

echo "Generating GridUI"
pyuic4 -o $UI_Path/GridUI/GridUI.py $UI_Path/GridUI/GridUI.ui

echo "\nStarting Interface\n"
python GUI.py
