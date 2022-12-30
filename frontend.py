import PySimpleGUI as psg
from zip_creator_backend import make_archive

label1 = psg.Text("Select files to compress:")
input1 = psg.Input()
choose_button1 = psg.FilesBrowse("Choose", key="files")

label2 = psg.Text("Select destination folder:")
input2 = psg.Input()
choose_button2 = psg.FolderBrowse("Choose", key="folder")

compress_button = psg.Button("Compress", key="Compress")
output_label = psg.Text(key="output", text_color="light green")

window = psg.Window("File Compressor",
                    layout=[[label1, input1, choose_button1],
                    [label2, input2, choose_button2],
                    [compress_button, output_label]])

while True:
    
    event, values = window.read()
    match event:
        case "Compress":
            filepaths = values["files"].split(";") # creates a list of filepaths from the selected files that are returned from the event handler
            folder = values["folder"]
            make_archive(filepaths, folder)
            window["output"].update(value="Compression successfully completed !")
        case psg.WIN_CLOSED:
            break

window.close()