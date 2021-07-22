import sys

if sys.version_info[0] == 2:
    from piksi_multi import PiksiMulti
    from geodetic_survey import GeodeticSurvey
else:
    from .piksi_multi import PiksiMulti
    from .geodetic_survey import GeodeticSurvey
