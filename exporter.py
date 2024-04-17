import datetime as dt
import os
import shutil
# from notification import show_notification as notify
import subprocess
import os
import sys
base_path = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
current_user = os.getlogin()
current_date = dt.date.today()
current_time = dt.datetime.now().time()
hour=current_time.hour
minute=current_time.minute
current_time=(f'{hour}:{minute}')
current_day=current_date.weekday()
days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
current_day=days[current_day]
source_path = f'Data/Attandance_list/Present_list_{current_date}.xlsx'
destination_path = f'C:/Users/{current_user}/Downloads/Face detection attandance system/Present_list_{current_date}.xlsx'
def export():
    os.makedirs(f'C:/Users/{current_user}/Downloads/Face detection attandance system',exist_ok=True)
    shutil.copy(source_path, destination_path)
directory_path = f"C:/Users/{current_user}/Downloads/Face detection attandance system"
def opene():
    # Check if the directory exists
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        # Use the appropriate command to open the directory based on your operating system
        if os.name == 'posix':  # Linux or macOS
            subprocess.Popen(["xdg-open", directory_path])
        elif os.name == 'nt':  # tpls
            # subprocess.Popen(["explorer", directory_path])
            os.startfile(directory_path,)
        elif os.name == 'os2':
            subprocess.Popen(["open", directory_path])  # OS/2
        # For other operating systems, you may need to implement the appropriate command
    else:
        print("Directory does not exist.")

if __name__=='__main__':
    export()
    opene()