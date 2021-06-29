import pandas as pd
import csv

c1 = pd.read_csv("C130FinalCSV.csv")
print(c1.shape)

del c1["hyperlink"]
del c1["temp_planet_date"]
del c1["temp_planet_mass"]
del c1["pl_letter"]
del c1["pl_name"]
del c1["pl_controvflag"]
del c1["pl_pnum"]
del c1["pl_orbper"]
del c1["pl_orbpererr1"]
del c1["pl_orbpererr2"]
del c1["pl_orbperlim"]
del c1["pl_orbsmax"]
del c1["pl_orbsmaxerr1"]
del c1["pl_orbsmaxerr2"]
del c1["pl_orbsmaxlim"]
del c1["pl_orbeccen"]
del c1["pl_orbeccenerr1"]
del c1["pl_orbeccenerr2"]
del c1["pl_orbeccenlim"]
del c1["pl_orbinclerr1"]
del c1["pl_orbinclerr2"]
del c1["pl_orbincllim"]
del c1["pl_bmassj"]
del c1["pl_bmassjerr1"]
del c1["pl_bmassjerr2"]
del c1["pl_bmassjlim"]
del c1["pl_bmassprov"]
del c1["pl_radj"]
del c1["pl_radjerr1"]
del c1["pl_radjerr2"]
del c1["pl_radjlim"]
del c1["pl_denserr1"]
del c1["pl_denserr2"]
del c1["pl_denslim"]
del c1["pl_ttvflag"]
del c1["pl_kepflag"]
del c1["pl_k2flag"]
del c1["pl_nnotes"]
del c1["ra"]
del c1["dec"]
del c1["st_dist"]
del c1["st_disterr1"]
del c1["st_disterr2"]
del c1["st_distlim"]
del c1["gaia_dist"]
del c1["gaia_disterr1"]
del c1["gaia_disterr2"]
del c1["gaia_distlim"]
del c1["st_optmag"]
del c1["st_optmagerr"]
del c1["st_optmaglim"]
del c1["st_optband"]
del c1["gaia_gmag"]
del c1["gaia_gmagerr"]
del c1["gaia_gmaglim"]
del c1["st_tefferr1"]
del c1["st_tefferr2"]
del c1["st_tefflim"]
del c1["st_masserr1"]
del c1["st_masserr2"]
del c1["st_masslim"]
del c1["st_raderr1"]
del c1["st_raderr2"]
del c1["st_radlim"]
del c1["rowupdate"]
del c1["pl_facility"]

print(c1.shape)

c1 = c1.rename({
    'pl_hostname': "solar_system_name",
    'pl_discmethod':"planet_discovery_method",
    'pl_orbincl': "planet_orbital_inclination",
    'pl_dens': "planet_density",
    'ra_str': "right_ascension",
    'dec_str': "declination",
    'st_teff': "host_temperature",
    'st_mass': "host_mass",
    'st_rad': "host_radius"
},axis = 'columns')

c1.to_csv('main.csv')