# way-1 to import a module
import one
one.multiplication_table(5)

# way-2 to import a module
from one import multiplication_table
multiplication_table(5)

# way-3 to import a module
from one import *
multiplication_table(5)

# way-4 to import a module
import one as o
o.multiplication_table(5)
