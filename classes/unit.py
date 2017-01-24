from enum import Enum

class Unit(Enum):
    NONE    = 0       # No Units
    TSP     = 1       # Teaspoon
    TBSP    = 2       # Tablespoon
    FLOZ    = 3       # Fluid Ounce
    CUP     = 4       # Cup
    PINT    = 5       # Pint
    QUART   = 6       # Quart
    GAL     = 7       # Gallon
    ML      = 8       # Milliliter
    L       = 9       # Liter
    DL      = 10      # Deciliter
    IB      = 11      # Pound
    OZ      = 12      # Ounce
    MG      = 13      # Milligram
    G       = 14      # Gram
    KG      = 15      # Kilogram

    @classmethod
    def get_unit(cls, str):
        str = str.lower()
        vals = {
            'tsp':          1,
            'tsp.':         1,
            'teaspoon':     1,
            'teaspoons':    1,
            'tbsp':         2,
            'tbsp.':        2,
            'tablespoon':   2,
            'tablespoons':  2,
            'fl. oz.':      3,
            'fl oz':        3,
            'floz':         3,
            'fluid ounce':  3,
            'fluid ounces': 3,
            'c':            4,
            'c.':           4,
            'cup':          4,
            'cups':         4,
            'pt':           5,
            'pt.':          5,
            'pint':         5,
            'pints':        5,
            'qt':           6,
            'qt.':          6,
            'quart':        6,
            'quarts':       6,
            'gal':          7,
            'gal.':         7,
            'gallon':       7,
            'gallons':      7,
            'ml':           8,
            'ml.':          8,
            'milliliter':   8,
            'milliliters':  8,
            'l':            9,
            'l.':           9,
            'liter':        9,
            'liters':       9,
            'dl':           10,
            'dl.':          10,
            'deciliter':    10,
            'deciliters':   10,
            'lb':           11,
            'lb.':          11,
            'pound':        11,
            'pounds':       11,
            'oz':           12,
            'oz.':          12,
            'ounce':        12,
            'ounces':       12,
            'mg':           13,
            'mg.':          13,
            'milligram':    13,
            'milligrams':   13,
            'g':            14,
            'g.':           14,
            'gram':         14,
            'grams':        14,
            'kg':           15,
            'kg.':          15,
            'kilogram':     15,
            'kilograms':    15,
        }
        if vals.get(str) != None:
            value = vals[str]
        else:
            value = 0
        return Unit(value)
