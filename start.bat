@echo off
echo İndiriliyor...
pip install -r requirements.txt
echo İndirme tamamlandı.
timeout /nobreak /t 1 > nul
cls
python main.py