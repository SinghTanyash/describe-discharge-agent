from tools.ocr_corrector import OCRCorrector

sample = """
Urine routine done showed ketone bodies(+),
10- I2/hpf of pus cells,
presence of bactreia.

Patient was adviced to stay back.

TAB. ENTR¢ 10 -] 3 DAYS
"""

result = OCRCorrector().correct(
    sample
)

print(result)