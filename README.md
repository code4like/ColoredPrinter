# ColoredPrinter Guideline
ColoredPrinter is an easy-use tool, which has packaged verious color constants and font styles to make the output more colorful in your python program.

 - Enivorment
    ~ python 3.7.5
 
 - How to get it？
    Just run the command  ```pip install coloredprinter ```
 
 - UseAge
   
   1. import the module  
      ``` from printer.ColoredPrinter import Printer ```  
      ``` from color.ColorConstant import FrontColor, BackgroundColor```  
      ``` from style.FontStyleConstant import FontStyle ```  
   2. init the Printer  
     ``` printer = Printer() ```  
   3. set the fontstyle  
     ``` printer.setFontStyle(FontStyle.UNDERLINE) ```  
   4. set the front-color  
     ``` printer.setFrontColor(FrontColor.CYAN) ```
   5. set the background-color  
     ``` printer.setBackGroundColor(BackgroundColor.YELLOW) ```  
   6. invoke the println function  
     ``` printer.println('Now,you can see the cyan output with underline and yellow background!') ```        
   then,you will the output:  
   ![ss](https://github.com/code4like/ImageSources/blob/master/ColoredPrinter/cvan.jpg)
