# TwoDim_Contour
Plots a series of 2-dimensional data in the form of a contour map. Contours are based on 'spatial'-density of datapoints in the domain of the ternary plot. Multiple 'sets' of series of 2D data can be plotted on the same figure, each with different colours of their contour maps.

<!-- Options -->
## Options
 User can specify the following parameters when calling the function:
 - choose the colours of the contour colours, according to cmap available options (https://matplotlib.org/stable/tutorials/colors/colormaps.html).
 - choose the number of contours.
 - to plot contour lines.
 - to display values of the contour level values within the contour lines.
 - to plot the individual datapoints of each dataset.
 - to plot multiple datasets.
 - the x- and y-axis limits of the plot.
 - the x- and y-axis labels.
 
User can also easily adjust plotting preferences (such as text size and datapoint size) by adjusting the variables defined within the first lines of the function, if so wishes.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Example output -->
## Example output

It should be noted that all data must be in the form of a list (of the different groups of data with different contour colours) of lists (of multiple datapoints for each contour):

<br />
<div align="center">
 
 [[A11, A12, .. A1n], ... [Am1, Am2, ... Amn]]
 
 </div>

- where n is the numer of datapoints in a given dataset (a particular colour of contours) and m is the number of datasets to plot individually (the number of individual contour plots of differing colours). Even if m = 1, data must be in the form of [[A11, A12, ... A1n]], where xData[0] = [[A11, A12, ... A1n]] and not = A11.

<br />
<div align="center">

[![Product Name Screen Shot][product-screenshot]](https://example.com)
 
 </div>
 
 This figures above were generated from the following user-specified options:
 - xData = [[A11, A12, .. A1n], [[A21, A22, ... A2n]], where A = Mg# = Mg / Mg + Fe
 - yData = [[B11, B12, .. B1n], [[B21, B22, ... B2n]], where B = SiRatio = Si + Al / Si + Al + Mg + Fe
     - red: data_1 (such as A11), blue: data_2 (such as A21)
 - NumLevels = 10
 - Colour = ['Blues', 'Reds']
 - type = 'silicate'
 - xMax = 0.85
 - xMin = 0.5
 - yMax = 0.55
 - yMin = 0.375
 - yLabel = 'Mg#'
 - xLabel = 'SiRatio'
 - and differing data options for each sub-figure:
     - A) ContLines = 'n',  ContourValues = 'n',  ContColourFill = 'y',  DataPointDisp = 'y'
     - B) ContLines = 'y',  ContourValues = 'y',  ContColourFill = 'y',  DataPointDisp = 'n'
     - C) ContLines = 'n',  ContourValues = 'n',  ContColourFill = 'y',  DataPointDisp = 'n'
 
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community what it is. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Dan Hallatt - daniel.hallatt@univ-lille.fr

Project Link: [https://github.com/DanHallatt/TwoDim_Contour](https://github.com/DanHallatt/TwoDim_Contour)

Associated Institute Link: https://umet.univ-lille.fr/MTP/index.php?lang=fr

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Related repositories -->
## Related repositories
- plotting static contours of entire datasets in a ternary diagram: https://github.com/DanHallatt/Ternary_Contour
- making a video of dynamic contours compositions/metrics in 2D, as a window slides through the series of data: https://github.com/DanHallatt/TwoDim_Contour_Vid
- making a video of dynamic ternary contours, as a window slides through the series of data: https://github.com/DanHallatt/Ternary_Contour_Vid

<p align="right">(<a href="#top">back to top</a>)</p>


[product-screenshot]: Images/ExampleFigureOptions.png
