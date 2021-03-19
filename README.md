# CtmConverter
 Script to convert optifine compact connected textures to full connected textures.  
   
 Input of 5 ctm compact tiles (as seperate files):  
 <img src="https://raw.githubusercontent.com/sp614x/optifine/master/OptiFineDoc/doc/images/ctm_compact_template.png" alt="" data-canonical width="480" height="96" />  
 Returns 47 full ctm tiles (as seperate files):  
 <img src="https://raw.githubusercontent.com/sp614x/optifine/master/OptiFineDoc/doc/images/ctm_template.png" alt="" data-canonical width="480" height="160" />

## Usage (Windows only)
  1. Download button > Download zip
  2. Unzip
  3. Put ctm compact tiles in the "in" folder
  4. Run convert.bat
  5. Check results in "out" folder

## Limitations
  * Input tiles must all have the same resolution and be square
  * Only for PNG, other types not tested
  * Windows only, Mac can run .py through terminal
  * Slower for larger images (takes 60 milliseconds for 128x images)
  * Files don't have valid digital signatures
