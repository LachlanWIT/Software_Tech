# This python file is made for the purpose of opening the dataset

import urllib

def startFile():
	    try:
                dataSetFile = "https://www.kaggle.com/llihan/australia-nsw-traffic-penalty-data-20112017"
                urllib.request.urlretrieve(dataSetFile, "dataset.xls")
               if fail:
                try: 
                    print("Online copy not acquired please enter filepathway for local copy.")
                    dataSetFile = open(input("please enter file pathway: " ))
                    dataSetFile = dataSetFile.read()
                else: 
                    quit("No dataset found. Program will quit.")


#
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")
