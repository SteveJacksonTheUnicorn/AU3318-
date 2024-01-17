# AU3318-Tapping-signal-analysis-and-processing

This is a rough product of the project in AU3318 course. 
The project asks you to separate a series of tapping signals and analysis in both time domain and grequency domain, the specific mission is in the following. 

Given different tightness of signals.
1. [Separate](separate.py) the signal of each tap in the time domain (Select an appropriate and identical time domain signal length).
2. Transform the selected signal into **[frequency](frequency_ana.py) domain**.
3. Compare and analyse the characteristics of different tightness signals.[code](joint.m)
4. Extract features and classify them using two different methods. I used a [self-designed](no_ML.m) method and [svm](svm.py) to classify them.
5. Obtain the relationship between tightness (pressure value) and frequency.[code](fitness.py)

The general [config](config.py) file.
