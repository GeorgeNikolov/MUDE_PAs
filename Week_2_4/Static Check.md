# Static Check

_Note: the results of the static check are not indicative of your grade. This is here to help you fulfill the basic requirements of the assignment._

This static check was generated on: 7 December 2023 (12:08)

Make sure you're passing the static check, otherwise you may experience deductions in your grade. 
The requirements this assignment were the following:
- The notebook `PA12B_axis_of_awesome.ipynb` exists and runs without errors.
- You have a `license.lic` file committed and it confirms the proper license.

Status: errors present

- Notebook ```PA12B_axis_of_awesome.ipynb``` has an error:
```An error occurred while executing the following cell:
------------------
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(coins.reshape(-1));
------------------


---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[9], line 2
      1 from statsmodels.graphics.tsaplots import plot_acf
----> 2 plot_acf(coins.reshape(-1));

AttributeError: 'list' object has no attribute 'reshape'
```
- No `lincense.lic` file was found. Have you run notebook A?

