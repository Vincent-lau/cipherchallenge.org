lines = ["TELUUTRFETNEHIOYITBEPHNDAHEIOODRULTIERATEFREHAEDUGSIOAFDEIIELCGNESRPINEOEREOONRHFTODCRDVLSRVTDBTMMOSSANFNSRWTURAWTEERNOFGVPUHEHLOASTIEEAOOENXIHBTNREESTVARMEDHBLCCELROCSHNPICCTVVBUAESDADAMAATIDSNEATRESATMWROITDTEOAFUTOTEEILTIUSONGLROAAEALLEOFLTSHTNIRWTALNRDORNNEFSORTYONTFRIT",
         "HLEEDOERDOIGEWITNEEYOLIVMEDTTUDAREONDUTHGTISETTFBROSFNRTMRUTLKWGTODINUDOBYRFRDEOTTUTSEEEOVYEEEAHYAUATFDOTAIATRECIHFNHPAOUERSESELUPSHLSRTOWCGTOEUTOATRAOECEYVTEEEIADESMAWAETNAIHIEYSRLEMRITMTCHREIORNHETSTOPEEGMHIHAUATBALOFUNOHOISHCEOIRNSDGASBBOOHAESILEAIGAGEEFIWGTYHWUHTUERUTSH",
         "ELDEIONOEFNIIENHOSASNOUEIYTIHNETTSNFBSUEIHOSSIURDENLMDOHYOMREAASIWSTGMTNRAOOCMFIHLNAEDCARIWRRDTELNSGJERURNCSOEGTTLFCAATRIRELSSRIDOEEOSSIKNUTHNDTLTNRIBBAADSEHYETPPBOAMTHDNEGEPICNJCHFCIYPIUIREECTLSDEWODCTERFISETETDNNTGABOPGSENLAAODCBEDHTRMOELRSERRUUEVSTRWIDFTBASBOTTTAHWEAROLO",
         "RIBNCKGMFTTOCREEVTSEBNMRURHEEDSEESIOYLSIOEUOIOROUBTAOCNEACAADLTTNNDEOBEEANIUEYUCEEDCNOINICHMMTTEOYAAUWERODOLSTIIHEIYPROHLTVOUEEOISDPUOIOHLRHLAIAEADULOELPEPAAHNOHTARNUIIBCDTSHSETUAIHULALCNOOEFAWOANRENEHHREUVECFDOIDOTRWLRRTSLSAIVUTAEBIIHIAHEATSCCWESDETWIHNTEHETTUUOHHTEIDVTTER",
         "EOYBCSTTEHHNEEDTARTTODAUMAESGAEDMUURVEOXNSSFTNNMIEHNNOTETOSVBOLRHWEBUENTVDSRSCLEBGATSUSDOTOAIHLNSTNISHDOOALEEHONRSCPSTNITHISPDBNCSOESFTNEISEESEBIWTEWURETNYLTAADEUTDDNOCERUHAEDIELEMARINOCINSMODANFEWSISEEOCLELROEFCLDHIAATIHOEAWDERHLSETNACYANMHOAIHTFTAHACOEHAESLRTWKEODNLTEHHON",
         "BNQOATHHAELTNJBRNIHUTINLTZCTRNCOPESMAGFLOENTURESNLEDANENVNHEANIEIOSETRTHEHMFAACOARNIURIGUOESNEEETHDNTUOWPGAFCENGUSIEITESOEOSRTEBCEFRNHUTRFIIGSDASAHPATEDUERETDBERRTECINHEYSERRENDISSDETDMOCSSPRESGEIEUUPSERATHFERFBCEOACSMHSEFGQATEAETTLWTTOAVTEEFEPAOAOLASOEEETTOIEIINTFAYLOLEEFS"]


output = ""
for row in range(len(lines[0])):
	for line in lines:
		output += line[row]
print(output)