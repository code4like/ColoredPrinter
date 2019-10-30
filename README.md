# ColoredPrinter Guideline
ColoredPrinter is an easy-use tool, which has packaged verious color constants and font styles to make the output more colorful in your python program.

 + Enivorment  
    ~ python 3.7.5
 
 + How to get it？
    Just run the command  ```pip install coloredprinter ```
 
 + UseAge
   
   - import the module  
      ``` from printer.ColoredPrinter import Printer ```  
      ``` from color.ColorConstant import FrontColor, BackgroundColor```  
      ``` from style.FontStyleConstant import FontStyle ```  
   - init the Printer  
     ``` printer = Printer() ```  
   - set the fontstyle  
     ``` printer.setFontStyle(FontStyle.UNDERLINE) ```  
   - set the front-color  
     ``` printer.setFrontColor(FrontColor.CYAN) ```
   - set the background-color  
     ``` printer.setBackGroundColor(BackgroundColor.YELLOW) ```  
   - invoke the println function  
     ``` printer.println('Now,you can see the cyan output with underline and yellow background!') ```         
 
+ Color Constant  

     |              ColorName                  | 
     | ----------------------------------------|
     | <font color=#000000> BLACK </font>        |    
     | <font color=#FF0000>RED</font>          |
     | <font color=#008000>GREEN</font>        |
     | <font color=#FFFF00>YELLOW</font>       |
     | <font color=#0000FF>BLUE</font>         |
     | <font color=	#9932CC>DARKORCHILD</font>|
     | <font color=#00FFFF>CYAN</font>         |
     | <font color=#FFFFFF>WHITE</font>        |  

+  Font Styles  

     |       StyleName     |  
     | --------------------|
     |   HIGHLIGHT         |    
     |    NO_BOLD          |
     |   UNDERLINE         |
     |   NO_UNDERLINE      |
     |    SPARKLE          |
     |   NO_SPARKLE        |
     |  REVERSE_DISPLAY    |
     | NO_REVERSE_DISPLAY  |            
