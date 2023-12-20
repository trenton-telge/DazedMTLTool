from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
import traceback
from colorama import Fore
import os
from tqdm import tqdm

from modules.rpgmakermvmz import handleMVMZ
from modules.rpgmakerace import handleACE
from modules.csv import handleCSV
from modules.txt import handleTXT
from modules.tyrano import handleTyrano
from modules.json import handleJSON
from modules.kansen import handleKansen
from modules.lune2 import handleLuneTxt
from modules.atelier import handleAtelier
from modules.anim import handleAnim

# For GPT4 rate limit will be hit if you have more than 1 thread.
# 1 Thread for each file. Controls how many files are worked on at once.
THREADS = int(os.getenv('fileThreads'))

# Info Message
tqdm.write(Fore.LIGHTYELLOW_EX + "WARNING: Once a translation starts do not close it unless you want to lose your\
translated data. If a file fails or gets stuck, translated lines will remain translated so you don't have \
to worry about being charged twice. You can simply copy the file generated in /translations back over to \
/files and start the script again. It will skip over any translated text." + Fore.RESET, end='\n\n')

def main():
    estimate = ''
    while estimate == '':
        estimate = input('Select Translation or Cost Estimation:\n\n1. Translate\n2. Estimate\n')
        match estimate:
            case '1':
                estimate = False
            case '2':
                estimate = True
            case _:
                estimate = ''

    totalCost = 0
    version = ''
    while version == '':
        version = input('Select the RPGMaker Version:\n\n\
1. MV/MZ\n\
2. ACE\n\
3. CSV (From Translator++)\n\
4. Text (Custom)\n\
5. Tyrano\n\
6. JSON\n\
7. Kansen\n\
8. Lune\n\
9. Atelier\n\
10. Anim\n'
        )
        match version:
            case '1':
                # Open File (Threads)
                with ThreadPoolExecutor(max_workers=THREADS) as executor:
                    futures = [executor.submit(handleMVMZ, filename, estimate) \
                                for filename in os.listdir("files") if filename.endswith('json')]
                    
                    for future in as_completed(futures):
                        try:
                            totalCost = future.result()
                        except Exception as e:
                            tracebackLineNo = str(traceback.extract_tb(sys.exc_info()[2])[-1].lineno)
                            tqdm.write(Fore.RED + str(e) + '|' + tracebackLineNo + Fore.RESET)

            case '2':
                # Open File (Threads)
                with ThreadPoolExecutor(max_workers=THREADS) as executor:
                    futures = [executor.submit(handleACE, filename, estimate) \
                                for filename in os.listdir("files") if filename.endswith('yaml')]
                    
                    for future in as_completed(futures):
                        try:
                            totalCost = future.result()
                        except Exception as e:
                            tracebackLineNo = str(traceback.extract_tb(sys.exc_info()[2])[-1].lineno)
                            tqdm.write(Fore.RED + str(e) + '|' + tracebackLineNo + Fore.RESET)

            case '3':
                # Open File (Threads)
                with ThreadPoolExecutor(max_workers=THREADS) as executor:
                    futures = [executor.submit(handleCSV, filename, estimate) \
                                for filename in os.listdir("files") if filename.endswith('csv')]
                    
                    for future in as_completed(futures):
                        try:
                            totalCost = future.result()
                            
                        except Exception as e:
                            tracebackLineNo = str(traceback.extract_tb(sys.exc_info()[2])[-1].lineno)
                            tqdm.write(Fore.RED + str(e) + '|' + tracebackLineNo + Fore.RESET)

            case '4':
                # Open File (Threads)
                with ThreadPoolExecutor(max_workers=THREADS) as executor:
                    futures = [executor.submit(handleTXT, filename, estimate) \
                                for filename in os.listdir("files") if filename.endswith('txt')]
                    
                    for future in as_completed(futures):
                        try:
                            totalCost = future.result()
                            
                        except Exception as e:
                            tracebackLineNo = str(traceback.extract_tb(sys.exc_info()[2])[-1].lineno)
                            tqdm.write(Fore.RED + str(e) + '|' + tracebackLineNo + Fore.RESET)

            case '5':
                # Open File (Threads)
                with ThreadPoolExecutor(max_workers=THREADS) as executor:
                    futures = [executor.submit(handleTyrano, filename, estimate) \
                                for filename in os.listdir("files") if filename.endswith('ks')]
                    
                    for future in as_completed(futures):
                        try:
                            totalCost = future.result()
                            
                        except Exception as e:
                            tracebackLineNo = str(traceback.extract_tb(sys.exc_info()[2])[-1].lineno)
                            tqdm.write(Fore.RED + str(e) + '|' + tracebackLineNo + Fore.RESET)

            case '6':
                # Open File (Threads)
                with ThreadPoolExecutor(max_workers=THREADS) as executor:
                    futures = [executor.submit(handleJSON, filename, estimate) \
                                for filename in os.listdir("files") if filename.endswith('json')]
                    
                    for future in as_completed(futures):
                        try:
                            totalCost = future.result()
                            
                        except Exception as e:
                            tracebackLineNo = str(traceback.extract_tb(sys.exc_info()[2])[-1].lineno)
                            tqdm.write(Fore.RED + str(e) + '|' + tracebackLineNo + Fore.RESET)

            case '7':
                # Open File (Threads)
                with ThreadPoolExecutor(max_workers=THREADS) as executor:
                    futures = [executor.submit(handleKansen, filename, estimate) \
                                for filename in os.listdir("files") if filename.endswith('ks')]
                    
                    for future in as_completed(futures):
                        try:
                            totalCost = future.result()
                            
                        except Exception as e:
                            tracebackLineNo = str(traceback.extract_tb(sys.exc_info()[2])[-1].lineno)
                            tqdm.write(Fore.RED + str(e) + '|' + tracebackLineNo + Fore.RESET)

            case '8':
                # Open File (Threads)
                with ThreadPoolExecutor(max_workers=THREADS) as executor:
                    futures = [executor.submit(handleLuneTxt, filename, estimate) \
                                for filename in os.listdir("files") if filename.endswith('txt')]
                    
                    for future in as_completed(futures):
                        try:
                            totalCost = future.result()
                            
                        except Exception as e:
                            tracebackLineNo = str(traceback.extract_tb(sys.exc_info()[2])[-1].lineno)
                            tqdm.write(Fore.RED + str(e) + '|' + tracebackLineNo + Fore.RESET)

            case '9':
                # Open File (Threads)
                with ThreadPoolExecutor(max_workers=THREADS) as executor:
                    futures = [executor.submit(handleAtelier, filename, estimate) \
                                for filename in os.listdir("files") if filename.endswith('txt')]

                    for future in as_completed(futures):
                        try:
                            totalCost = future.result()

                        except Exception as e:
                            tracebackLineNo = str(traceback.extract_tb(sys.exc_info()[2])[-1].lineno)
                            tqdm.write(Fore.RED + str(e) + '|' + tracebackLineNo + Fore.RESET)

            case '10':
                # Open File (Threads)
                with ThreadPoolExecutor(max_workers=THREADS) as executor:
                    futures = [executor.submit(handleAnim, filename, estimate) \
                                for filename in os.listdir("files") if filename.endswith('json')]

                    for future in as_completed(futures):
                        try:
                            totalCost = future.result()

                        except Exception as e:
                            tracebackLineNo = str(traceback.extract_tb(sys.exc_info()[2])[-1].lineno)
                            tqdm.write(Fore.RED + str(e) + '|' + tracebackLineNo + Fore.RESET)

            case _:
                version = ''
        
    if totalCost != 'Fail':
        if estimate is False:
            # This is to encourage people to grab what's in /translated instead
            deleteFolderFiles('files')

        # Prevent immediately closing of CLI
        # tqdm.write(totalCost)
        # input('Done! Press Enter to close.')

def deleteFolderFiles(folderPath):
    for filename in os.listdir(folderPath):
        file_path = os.path.join(folderPath, filename)
        if file_path.endswith(('.json', '.yaml', '.ks')):
            os.remove(file_path)   
