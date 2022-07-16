# TwoDim_Contour
Plots a series of 2-dimensional data in the form of a contour map. Contours are based on 'spatial'-density of datapoints in the domain of the ternary plot. Multiple 'sets' of series of 2D data can be plotted on the same figure, each with different colours of their contour maps.

<!-- Options -->
## Options
 User can specify the following parameters when calling the function:
 - colour of the colour gradient, according to cmap available options (https://matplotlib.org/stable/tutorials/colors/colormaps.html).
 - the number of contours.
 - to plot contour lines.
 - to plot contour level values within the contour levels.
 - the x- and y-axis limits of the plot.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Example output -->
## Example output

<br />
<div align="center">

[![Product Name Screen Shot][product-screenshot]](https://example.com)
 
 </div>

This figure was generated from the following user-specified options:
 - xData = [x1, x2, ... xn] where x = Si + Al / (Si + Al + Mg + Fe) in at.%.
 - yData = [y1, y2, ... yn] where x = Mg# = Mg / (Mg + Fe) in at.%.
 - xMax = 0.6
 - xMin = 0.1
 - yMax = 1.0
 - yMin = 0.6
 - yLabel = 'Mg / (Mg + Fe) [at.%]
 - xLabel = '(Si + Al) / (Si + Al + Mg + Fe) [at.%]
- ContLines = 'y'
 - NumLevels = 7
 - Colour = 'Blues'
 
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


[product-screenshot]: Images/ExampleFigures.png
