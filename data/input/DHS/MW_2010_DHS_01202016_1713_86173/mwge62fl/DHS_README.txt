DHSID = DHSCC&DHSYEAR&DHSCLUST (with 8 digits) from survey documentation

DHSCC = 2 letter DHS country code (http://www.measuredhs.com/accesssurveys/distribution_files.cfm)

DHSYEAR = 4 digit year of data collection from the survey documentation from survey documentation

DHSCLUST = integer cluster identification number

CCFIPS = Federal Information Processing Standards (FIPS) 2 letter country code (http://www.itl.nist.gov/fipspubs/fip10-4.htm)

ADM1FIPS = Federal Information Processing Standards (FIPS) 2  letter country code plus 2 letter/digit region code (http://www.itl.nist.gov/fipspubs/fip10-4.htm)

ADM1FIPSNA = Federal Information Processing Standards (FIPS) first sub-national administrative division name (http://www.itl.nist.gov/fipspubs/fip10-4.htm)

ADM1SALBCO = Second Administrative Level Boundaries (SALB) first sub-national administrative division code (http://www.unsalb.org) 
*NOTE: website requires free registration for downloads

ADM1SALBNA = Second Administrative Level Boundaries (SALB) first sub-national administrative division name (http://www.unsalb.org) 
*NOTE: website requires free registration for downloads

ADM1DHS = First sub-national administrative division code when sampling is representative at the Admin 1 level.  This variable will match hv024 of the recode file.
*NOTE: If survey is not representative at the ADMIN1 level, this field will be left blank 

ADM1NAME = First sub-national administrative division name when sampling is representative at the Admin 1 level. This variable will match hv024 of the recode file.
*NOTE: If survey is not representative at the ADMIN1 level, this field will be left blank 

DHSREGCO = integer region code associated with the DHS region created for sampling.  This variable will match either the shdist variable of the recode file.
*NOTE:  In older templates, REPAIR1DHS was used.   Thise field has been replaced by DHSREGCO and is no longer used. 

DHSREGNA = name associated with the DHS region created for sampling.  This variable will match either the shdist variable of the recode file.
*NOTE:  In older templates, REPAIR1NAME was used.   Thise field has been replaced by DHSREGNA and is no longer used. 

SOURCE = source of data used to determine the latitude and longitude values
“GPS” for data collected by the survey team
"CEN" for preexisting data provided by the census agency/ministry
“GAZ” for data extracted from a gazetteer of village/place names
“MAP” for data extracted from a paper map
"MIS" for clusters in which data could not be fully verified

URBAN_RURA = Urban (U) and Rural (R) sample classification

LATNUM = cluster's latitude coordinate in decimal degrees

LONGNUM = cluster's longitude coordinate in decimal degrees

ALT_GPS = elevation/altitude (in meters) recorded from the GPS reciever

ALT_DEM = elevation/altitude (in meters) from the SRTM (Shuttle Radar Topography Mission) DEM (Digital Elevation Model) for the specified coordinate location
*NOTE: If the cluster is missing coordinates (MIS) the ALT_DEM will be set to 9999
*NOTE: Elevations in GTOPO30 are regularly spaced at 30-arc seconds or approximately 1 kilometer (http://dds.cr.usgs.gov/srtm/version1/SRTM30)

DATUM = always "WGS84" for the geographic coordinate system World Geodetic System (WGS) 1984
