
INSTRUCTIONS:

To launch the program, you can use the "execute.bat" file found in the main directory "Decision Tree."
If you prefer, you can directly use the "DecisionTree.jar" file in the dist folder.

Once the program opens, you can select import to load an ARFF file into python. I have provided the entire nominal WEKA library
in the "Arff files" of the main directory. This is just for ease of use as the program has been made to automatically
open to the main directory. Once you've imported it, the label will change to the selected program, and you can press generate
to draw the tree. If nothing happens, it probably means that weka couldn't successfully convert the data (it wasn't nominal).





NOTES:

I haven't tested CSV files, and some of the new GUI additions may have comprimised the programs capability 
to handle them (it can draw them fine, but it might cause errors when preparing the data). I haven't tested it so I 
can't be sure, but I'd guess it doesn't.

Numeric attribute entropies haven't been introduced, only their original entropies are given on purpose - I turned off 
everything after that - when numeric attributes are detected. They could be added once I understand how to do it, just need
to replace pass with code in a single if statement... On that note - Good luck reading the code, I have yet to put it through 
optimization (which is when I make it readable for others) because my lack of time. I focused on putting out something that 
worked, not code meant to be understood by others. This project probably took a good 10-15 hours to complete, done in 2-3 hour
bursts over time.

Let me know if you have any issues running it, seemed to work fine on the computers at campus last I tried.



