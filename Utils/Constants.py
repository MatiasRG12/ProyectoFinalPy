class Constants:

    SIZES = [2, 4, 8, 16, 32, 64, 128, 256]
    
    ALGORITHMS = [
        "StrassenNaiv",
        "StrassenWinograd",
        "WinogradOriginal",
        "WinogradScaled",
        "NaivLoopUnrollingFour",
        "NaivLoopUnrollingTwo",
        "NaivOnArrays",
        "V3SequentialBlock",
        "V4ParallelBlock",
        "IV3SequentialBlock"
    ]
