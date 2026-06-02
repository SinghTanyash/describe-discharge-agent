from extractors.hospital_course_extractor import (
    HospitalCourseExtractor
)

with open(
    "outputs/patient2_ocr.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()

course = (
    HospitalCourseExtractor().extract(text)
)

print("\nHOSPITAL COURSE\n")
print(course)