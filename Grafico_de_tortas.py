from xml.etree.ElementPath import prepare_predicate
import pylab as pl
import numpy as np

n = 10
Z = np.ones(n)
Z[-1] *= 2

pl.axes([0.025, 0.025, 0.95, 0.95])

pl.pie(Z, explode=Z * 0.05, colors=["%f" % (i / float(n)) for i in range(n)])
pl.axis("equal")
pl.xticks(())
pl.yticks()
pl.show()

prepare_predicate