# Miniful
Miniful is a very minimal fuzzy logic python library. This tool is not designed to be a comprehensive library, but just a simple Sugeno reasoner for single antecedent / single consequent fuzzy rule-based systems. 

## Usage

```
from miniful import *

# A simple fuzzy model describing how the heating power of a gas burner depends on the oxygen supply.

F = FuzzyReasoner()

LOW_POWER = 0
MEDIUM_POWER = 50
HIGH_POWER = 100

FS_1 = FuzzySet( points=[[0, 1.],  [1., 1.],  [1.5, 0]],          term="low_flow" )
FS_2 = FuzzySet( points=[[0.5, 0], [1.5, 1.], [2.5, 1], [3., 0]], term="medium_flow" )
FS_3 = FuzzySet( points=[[2., 0],  [2.5, 1.], [3., 1.]],          term="high_flow" )
OXI_MF = MembershipFunction( [FS_1, FS_2, FS_3], concept="OXI" )

R1 = FuzzyRule( IF(OXI_MF, "low_flow"),    THEN("POWER", LOW_POWER),    comment="Rule case low flow" )
R2 = FuzzyRule( IF(OXI_MF, "medium_flow"), THEN("POWER", MEDIUM_POWER), comment="Rule case medium flow" )
R3 = FuzzyRule( IF(OXI_MF, "high_flow"),   THEN("POWER", HIGH_POWER),   comment="Rule case high flow" )
F.add_rules( [R1, R2, R3] )

# set antecedents values, perform Sugeno inference and print output values
F.set_variable("OXI", 0.23)
print FR.evaluate_rules()
```

## Installation

`pip install miniful`

## Further info
Created by Marco S. Nobile (University of Milano-Bicocca, Italy). 

If you need further information, please drop a line at: nobile@disco.unimib.it. 
