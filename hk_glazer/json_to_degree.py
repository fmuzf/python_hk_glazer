# Copyright 2012 and 2013 Lyman Gillispie
# This code is distributed under the MIT License
# Author: Lyman Gillispie

def dict_to_dat(config):
    '''Super ugly conversion method,
    Args: config - a dictionary containing all of the appropriate elements
    Returns: os, a valid input.dat for the Hock melt model
    '''

    ostr = []

    ostr.append('\n')
    ostr.append('***********************************************************\n')
    ostr.append('{daysscreenoutput}    %output to screen every X day.  daysscreenoutput.\n')
    ostr.append('{inpath}    %Path for Inputfiles.  inpath\n')
    ostr.append('{outpath}    %Path for Outputfiles.  outpath\n')
    ostr.append('{jdbeg}  {yearbeg}    %first julian day to be calculated.  jdbeg  yearbeg\n')
    ostr.append('{jdend}  {yearend}    %last julian day to be calculated.  jdend  yearend\n')
    ostr.append('{disyes}    %discharge to be calculated: 1=yes,0=no,2=yes, but no discharge data.  disyes\n')
    ostr.append('{calcgridyes}    %1=whole grid computed,  2=only grid cell of weather station.  calcgridyes\n')
    ostr.append('%********* 1.) MODEL OUTPUT PARAMETERS ****************************\n')
    ostr.append('{maxmeltstakes}    %number of stakes for melt output.  maxmeltstakes\n')
    ostr.append('{plusminus}    %cum massbal multiplied by this factor in melting.dat.  plusminus\n')
    ostr.append('{do_out}    %0=no output 1=every step, 2=daily, 3=whole period 4=2and3.  do_out\n')
    ostr.append('%shayes exkyes solyes diryes dir2yes difyes gloyes albyes  swbyes linyes loutyes\n')
    ostr.append('{shayes} {exkyes} {solyes} {diryes} {dir2yes} {difyes} {gloyes} {albyes} {swbyes} {linyes} {loutyes}\n')
    ostr.append('%netyes senyes latyes raiyes enbyes melyes  ablyes surftempyes  posyes ddfyes\n')
    ostr.append('{netyes} {senyes} {latyes} {raiyes} {enbyes} {melyes} {ablyes} {surftempyes} {posyes} {ddfyes}\n')
    ostr.append('{surfyes}    %surface conditions to grid file (2=for specified JDs).  surfyes\n')
    ostr.append('{snowyes}    %snow cover to grid file at midnight.  snowyes\n')
    ostr.append('{daysnow}    %snow or surface written to file if jd dividable by this value.  daysnow\n')
    ostr.append('{numbersnowdaysout}    %number of jd for output of surface type/snow cover.  numbersnowdaysout\n')
    ostr.append(" ".join(map(str, config['jdsurface'])) + "    %jd to be written to output for surface type and snow cover\n")

    ostr.append("%----------- 2.) MASS BALANCE -------------------\n")
    ostr.append('{winterbalyes}    %gridout winter mass balance yes=1, no=0.  winterbalyes\n')
    ostr.append('{winterjdbeg}  {winterjdend}    %julian day winter starts and ends.  winterjdbeg  winterjdend\n')
    ostr.append('{summerbalyes}    %gridout summer mass balance yes=1, no=0.  summerbalyes\n')
    ostr.append('{summerjdbeg}  {summerjdend}    %julian day summer starts and ends.  summerjdbeg  summerjdend\n')
    ostr.append('{datesfromfileyes}    %1=dates for MB meas read from file, 0=fixed dates.  datesfromfileyes\n')
    ostr.append('{namedatesmassbal}    %file containing the dates of massbal meas.  namedatesmassbal\n')
    ostr.append('{beltwidth}    % vertical extent of elevation bands (m) for mass balance profiles.  beltwidth\n')
    ostr.append('{snow2zeroeachyearyes}    %set snow cover to 0 at start of each massbal year.  snow2zeroeachyearyes\n')
    ostr.append('{snowfreeyes}   %times series file with number of pixels snowfree written to file.  snowfreeyes \n')
    ostr.append('-----------------------------------------\n')
    ostr.append('{cumulmeltyes}   %gridoutput of melt cumulated=1 or mean=0.  cumulmeltyes\n')
    ostr.append('{cm_or_m}    %if cumulated, output in cm=10 or m=1000.  cm_or_m\n')
    ostr.append('{do_out_area}    %time series of spatial mean to output (yes=1 no=0).  do_out_area\n')
    ostr.append('{outgridnumber}    %number of individual grid points for which model result output.  outgridnumber\n')
    ostr.append('%***====read if number > 0============================***\n')
    ostr.append('%***Outputfilename ** row/x-coord ***column/y-coord *** glob and net data included from input data\n')

    for grid in config['outgrids']:
        ostr.append((grid['name'] + " " +
            " ".join(map(str, grid['location'])) +
            " " + str(grid['outglobnet']) + "\n"))

    ostr.append("%******** 3.) METHODS ENERGY BALANCE COMPONENTS ********************************\n")

    ostr.append('{methodinisnow}    %1=surface maps 2=start with initial snow cover.  methodinisnow\n')
    ostr.append('{methodsnowalbedo}    %1=constant for surface types, >2=alb generated.  methodsnowalbedo, 6=zongo\n')
    ostr.append('{methodglobal}    %1=direct and diffuse not separated, 2=separated.  methodglobal\n')
    ostr.append('{methodlonginstation}    %1=longin from net,glob,ref (Tsurf=0),2=meas,3-6=from paramet. methodlonginstation\n')
    ostr.append('{methodlongin}    %1=longin constant, 2=spatially variable. methodlongin\n')
    ostr.append('{methodsurftempglac}    %1=surftemp=0, 2=iteration 3=measurement+(decrease height), 4=snowmodel.  methodsurftempglac\n')

    ostr.append('%********************* TURBULENCE OPTION\n')
    ostr.append('{methodturbul}    %1=turbulence accord. to Escher-Vetter, 2=Ambach 3=stabil.  methodturbul\n')
    ostr.append('{method_z0Te}    %1=z0T/z0w fixed ratio 2=according to Andreas (1987).  method_z0Te\n')
    ostr.append('{methodiceheat}    %1=no ice heat flux 2=ice heat flux.  methodiceheat\n')
    ostr.append('{methodnegbal}    %1=neglected 2=neg energy balance stored to retard melt.  methodnegbal\n')

    ostr.append('%********* SCALING ********************************\n')
    ostr.append('{scalingyes}    %V-A scaling yes=1, no=0.  scalingyes\n')
    ostr.append('{gamma}    %gamma in V-A scaling.  gamma\n')
    ostr.append('{c_coefficient}    %coefficient in V-A scaling.  c_coefficient\n')

    ostr.append('%********* 4.) NAMES OF INPUT FILES ********************************\n')
    ostr.append('{namedgm}    %name of Digital Terrain Model.  namedgm\n')
    ostr.append('{namedgmdrain}    %name of DTM with drainage basin.  namedgmdrain\n')
    ostr.append('{namedgmglac}    %name of DTM glacier.  namedgmglac\n')
    ostr.append('{namedgmslope}    %name of DTM slope.  namedgmslope\n')
    ostr.append('{namedgmaspect}    %name of DTM aspect.  namedgmaspec\n')
    ostr.append('{namedgmskyview}    %name of DTM sky view factor.  namedgmskyview\n')
    ostr.append('{namedgmfirn}    %name of DTM firnarea.  namedgmfirn\n')
    ostr.append('{nameinitialsnow}   %name of DTM initial snow cover.  nameinitialsnow \n')
    ostr.append('{nameklima}    %name of climate data file.  nameklima\n')

    ostr.append('%********* 5.) GRID INFORMATION***************************************\n')
    ostr.append('{laenge}    %geographical longitude [degree].  laenge\n')
    ostr.append('{breite}    %latitude.  breite\n')
    ostr.append('{reflongitude}    %longitude time refers to.  reflongitude\n')
    ostr.append('{rowclim}    %row in DTM where climate station is located.   rowclim\n')
    ostr.append('{colclim}    %column of climate station.  colclim\n')
    ostr.append('{climoutsideyes}  {heightclim}    %take this elevation for AWS yes/no.  climoutsideyes  heightclim\n')
    ostr.append('{gridsize}    %gridsize in m.  gridsize\n')
    ostr.append('{timestep}    %time step in hours.  timestep\n')
    ostr.append('%********* 6.) CLIMATE DATA ******************************************\n')
    ostr.append('{formatclimdata}    %1=midnight time is 0, 2=time is 24, 3=24 but previous day.  formatclimdata\n')
    ostr.append('{maxcol}    %number of columns in climate file.  maxcol\n')
    ostr.append('{coltemp}    %columns in climate input file: temperature.  coltemp\n')
    ostr.append('{colhum}    %column containing relative humidity.  colhum\n')
    ostr.append('{colwind}    %column wind speed [m/s].  colwind\n')
    ostr.append('{colglob}    %global radiation.  colglob\n')
    ostr.append('{colref}    %reflected shortwave radiation.  colref\n')
    ostr.append('{colnet}    %net radiation.  colnet\n')
    ostr.append('{collongin}    %longwave incoming radiation.  collongin\n')
    ostr.append('{collongout}    %longwave outgoing radiation.  collongout\n')
    ostr.append('{colprec}    %precipitation.  colprec\n')
    ostr.append('{colcloud}    %cloud cover (number of eigths).  colcloud\n')
    ostr.append('{coltempgradvarying}    %time variant lapse rate (neg=decrease).  coltempgradvarying\n')
    ostr.append('{coldis}    %column of discharge data.  coldis\n')

    ostr.append('%********** CORRECTIONS TO INPUT ********************************\n')
    ostr.append('{ERAtempshift}    %add this to ERA temp to get to elevationstation.  ERAtempshift\n')
    ostr.append('{ERAwindshift}    %add this to ERA wind to get to elevationstation.  ERAwindshift\n')

    ostr.append('%********** 7.) LAPSE RATE / SCENARIOS ********************************\n')
    ostr.append('{methodtempinterpol}    %1=const lapse rate 2=variable 2AWS 3=grid.  methodtempinterpol\n')
    ostr.append('{tempgrad}    %temperature change with elevation [degree/100m].  tempgrad\n')
    ostr.append('{tempscenario}    %climate perturbation: temp + this amount.  tempscenario\n')
    ostr.append('{precscenario}    %climate perturbation: precip + this amount in percent.  precscenario\n')
    ostr.append('%on/off Jan   Feb   Mar   Apr   May   Jun   Jul   Aug   Sep   Oct   Nov   Dec\n')

    ostr.append((str(config["monthtempgradyes"]) + " " +
      " ".join(map(str, config["monthtempgrad"])) + "    %monthtempgrad(yes)\n"))

    ostr.append((str(config["monthtempscenyes"]) + " " +
      " ".join(map(str, config["monthtempscen"])) + "    %monthtempscen(yes)\n"))

    ostr.append((str(config["monthprecipscenyes"]) + " " +
      " ".join(map(str, config["monthprecipscen"])) + "    %monthprecipscen(yes)\n"))

    ostr.append("%******** 8.) SURFACE TYPE / ALBEDO ***********************************\n")
    ostr.append('{n_albfiles}    %number of transient surface type files\n')
    ostr.append('{albsnow}    %albedo for snow and firn (fixed value).  albsnow\n')
    ostr.append('{albslush}    %albedo for slush.  albslush\n')
    ostr.append('{albice}    %albedo for ice.  albice\n')
    ostr.append('{albfirn}    %albedo for firn (method 2).  albfirn\n')
    ostr.append('{albrock}    %albedo for rock outside glacier.  albrock\n')
    ostr.append('{albmin}    %minimum albedo for snow if generated.  albmin\n')
    ostr.append('{snowalbincrease}    %increase snowalb/100m elevation for 1. time. snowalbincrease\n')
    ostr.append('{albiceproz}    %decrease of ice albedo with elevation.  albiceproz\n')
    ostr.append('{ndstart}    %number of days since snow fall at start.  ndstart\n')

    ostr.append('%******** 9.) RADIATION *******************************************\n')
    ostr.append('{split}    %number of shade calculation per time step.  split\n')
    ostr.append('{prozdiffuse}    %percent diffuse radiation of global radiation.  prozdiffuse\n')
    ostr.append('{trans}    %transmissivity.  trans\n')
    ostr.append('{ratio}    %first ratio of global radiation and direct rad.  ratio\n')
    ostr.append('{ratiodir2dir}    %first ratio of direct and clear-sky direct rad.  ratiodir2dir\n')
    ostr.append('{surftemplapserate}    %decrease in surftemp with height if longout meas.  surftemplapserate\n')
    ostr.append('{directfromfile}    %direct radiation read from file = 1.  directfromfile\n')
    ostr.append('{pathdirectfile}    %Path for direct files.  pathdirectfile\n')
    ostr.append('{daysdirect}    %files only exist every number of days defined here.  daysdirect\n')
    ostr.append('{slopestation}    %0=slope at climate station is set to 0.  slopestation\n')

    ostr.append('%******** 10.) TURBULENCE ***********************************************\n')
    ostr.append('{iterstep}    %step for surface temp lowering for iteration.  iterstep\n')
    ostr.append('{z0wice}    %roughness length for wind for ice in m   .0027.  z0wice\n')
    ostr.append('{dividerz0T}    %z0Temp is zow divided by this value.  dividerz0T\n')
    ostr.append('{dividerz0snow}    %z0snow is z0wice divided by this value.  dividerz0snow\n')
    ostr.append('{z0proz}    %increase of z0 with decreasing elevation.  z0proz\n')
    ostr.append('{icez0min:.10f}    %min z0w ice.  icez0min\n')
    ostr.append('{icez0max}    %max z0w ice.  icez0max\n')

    ostr.append('%********** 11.) PRECIPITATION *******************************************\n')
    ostr.append('{methodprecipinterpol}    %1=lapse rate 2=scale AWS precip with index map 3=read grids.  methodprecipinterpol\n')
    ostr.append('{precgrad}    %precipitation change with elevation [%/100m].  precgrad\n')
    ostr.append('{precgradhigh} {precgradelev}    %precipitation change with elevation beyond certain elevation.  precgradhigh precgradelev\n')
    ostr.append('{preccorr}    %35 precipitation correction, caused by losses.  preccorr\n')
    ostr.append('{snowmultiplierglacier}    %snow precip is multiplied by this factor.  snowmultiplierglacier\n')
    ostr.append('{snowmultiplierrock}    %snow precip is multiplied by this factor.  snowmultiplierrock\n')
    ostr.append('{threshtemp}    %threshold temperature rain/snow precipitation.  threshtemp\n')
    ostr.append('{onlyglacieryes}    %0=if massbal calculations for whole drainage basin, 1=only glacier.  onlyglacieryes\n')
    ostr.append('{glacierpart}    %percentage of glacierization.  glacierpart\n')

    ostr.append('%************* 13.) DISCHARGE STARTING VALUES**********************\n')
    ostr.append('{nameqcalc}     %name of discharge output file.  nameqcalc\n')
    ostr.append('{nodis}    %nodata value of discharge file.  nodis\n')
    ostr.append('{firnkons}    %storage constant k for firn.  firnkons\n')
    ostr.append('{snowkons}    %storage constant k for snow.  snowkons\n')
    ostr.append('{icekons}    %storage constant k for ice.  icekons\n')
    ostr.append('{rockkons}    %storage constant k for rock(outside glacier non-snowcovered.  icekons\n')

    ostr.append('%************* 13.) DISCHARGE STARTING VALUES**********************\n')
    ostr.append('{qfirnstart}    %start value for firn discharge (previous time step).  qfirnstart\n')
    ostr.append('{qsnowstart}    %start value for snow discharge (m3/s).  qsnowstart\n')
    ostr.append('{qicestart}    %start value for ice discharge.  qicestart\n')
    ostr.append('{qrockstart}    %start value for rock discharge (outside glacier non-snowcovered).  qicestart\n')
    ostr.append('{qground}    %groundwater discharge[m3].  qground\n')
    ostr.append('{jdstartr2diff}    %difference between start of calculation and start r2.  jdstartr2diff\n')

    ostr.append('%%%%%%%%%%%% 15.) OPTIMIZATION %%%%%%%%%%%%%%%%%%%%%\n')
    ostr.append('{disyesopt}    %optimization run for k-values = 1; simulation=0.  disyesopt\n')
    ostr.append('{optkA}    %1. parameter to optimize.  optkA\n')
    ostr.append('{startopt1}    %startvalue of 1. parameter to optimize.  startopt1\n')
    ostr.append('{stepopt1}    %step length.  stepopt1\n')
    ostr.append('{anzahlopt1}    %number of steps no.1  anzahlopt1\n')
    ostr.append('{optkB}    %2. parameter to optimize.  optkB\n')
    ostr.append('{startopt2}    %startvalue of 2. parameter.  startopt2\n')
    ostr.append('{stepopt2}    %steplength no.2 of optimal r2.  stepopt2\n')
    ostr.append('{anzahlopt2}    %number of steps no.2.  anzahlopt2\n')
    ostr.append('{namematrix}    %name of r2-outputfile.  namematrix\n')
    
    ostr.append('%============ 16.) SNOW MODEL by C. Tijm-Reijmer 2/2005 ========================\n')
    ostr.append('{percolationyes}    %0=no percolation, 1=percolation+refreezing in snowlayer.  percolationyes\n')
    ostr.append('{slushformationyes}    %0=no slush, 1=meltwater accumulation in snowlayer.  slushformationyes\n')
    ostr.append('{densificationyes}    %0=no densification, 1=densific. of dry snow due to aging.  densificationyes\n')
    ostr.append('{wetstartyes}    %0=dry start, 1=wet start.  wetstartyes\n')
    ostr.append('{ndepths}    %maximum number of vertical layers.  ndepths\n')
    ostr.append('{factinter}    %number of subtimesteps for interpolation per main timestep 8.  factinter\n')

    ostr.append('%----------------------------\n')
    ostr.append('{thicknessfirst}    %layer thickness of first layer (m snow).  thicknessfirst\n')
    ostr.append('{thicknessdeep}    %layer thickness at deepest layer (m snow).  thicknessdeep\n')
    ostr.append('{depthdeep}    %maximum depth model (m).  depthdeep\n')
    ostr.append('{denssnow}    %density of fresh snowfall kg/m3.  denssnow\n')
    ostr.append('{irrwatercontyes}    %0=constant irreducible water content, 1=density dep. Schneider, 2= density dep. Coleou.  irrwatercontyes\n')
    ostr.append('{irrwatercont}    %fraction of space irreducible filled with water.  irrwatercont\n')

    ostr.append('%---- Output ----------\n')
    ostr.append('{factsubsurfout}    %factor for subsurf output, 1=every hour, 24=once per day at midnight.  factsubsurfout\n')
    ostr.append('{offsetsubsurfout}    %offfsetfactor for subsurf output to make print at noon possible.  offsetsubsurfout\n')
    ostr.append('%runoffyes superyes   wateryes   surfwateryes slushyes   coldsnowyes   coldtotyes.      for grid output\n')
    ostr.append('{runoffyes} {superyes} {wateryes} {surfwateryes} {slushyes} {coldsnowyes} {coldtotyes}\n')

    ostr.append('%========================================================\n')
    ostr.append('%   17.) TEMPERATURE INDEX METHOD\n')
    ostr.append('%========================================================\n')
    ostr.append('{ddmethod}    %which temp index method (1,2 or 3).  ddmethod\n')
    ostr.append('{DDFice}    %degree day factor for ice (only simple DDF method 1).  DDFice\n')
    ostr.append('{DDFsnow}    %degree day factor for snow (only simple DDF method 1).  DDFsnow\n')
    ostr.append('%---------------------------------------------------\n')
    ostr.append('{meltfactor}    %meltfactor (only for modified temp index method 2 or 3).  meltfactor\n')
    ostr.append('{radfactorice}    %radiation melt factor for ice.  radfactorice\n')
    ostr.append('{radfactorsnow}    %radiation melt factor for snow.  radfactorsnow\n')
    ostr.append('{debrisfactor}    %factor to reduce melt over debris.  debrisfactor\n')
    ostr.append('%******* 18.) OUTPUT STAKES **************************************\n')
    ostr.append('{coordinatesyes}    %1=stake locations given in local coordinates (x,y), 2=as 1 but center, 3=row/col.  coordinatesyes\n')

    for stake in config["stake_coords"]:
        ostr.append((" ".join(map(str, stake)) + "\n"))

    

    ostr = "".join(ostr)

    ostr = ostr.format(**config)
    return ostr
