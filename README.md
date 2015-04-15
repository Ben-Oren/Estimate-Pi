# README
A quick little demonstration of a method for calculating pi: estimating the area of a quarter circle with randomly-plotted points, multiplying that area by 4 (to get a full circle's area) and dividing the result by r**2 to get pi

The user gives a number of points; this number of points is randomly plotted inside a unit square

The number of points plotted within a quarter-circle inscribed within the square are divided by the total number of points plotted

This gives the ratio between an estimated area of the quarter-circle and the estimated area of the unit square

Since the area of the unit square is known and equal to 1, the estimated area of the quarter circle can be calulated (and is, simply, the ratio itself)

(Note that there are two ways in which estimation error creeps into this calculation: through the estimation of the quarter-circle AND the estimation of the area of the unit square)

The estimated area of the quarter circle is multiplied by 4 to get the estimated area of the total circle

Since the radius is 1, the area of the full circle is equal to pi*r**2 = pi*1 = pi

Thus, the estimated area of the total circle acts as an estimate for the value of pi
