# DoctorPatientProject

ID generation: the generation of id are based on the amount of people or admissions before them, to make a better generation one would use a randomized one, for a large enough interval, then if that is taken, one would then expand the search both ways untill finding one thats available, which should be linear time of the size of the interval.
DICTS: i use dicts here instead of arrays/list for the purpose of having no duplicates, one could use a Database as well( is better for scaling), but in the limited time i didnt priotize that.

use of id instead of SSN, as written in the code i use patientID instead of a SSN, for the sake of more privacy, since each patient only have one SSN and one ID, then i assume this is a better solution.

not tested but should work with mutiple admissions and doctors for singular patient.
