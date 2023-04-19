
def linearPaddingHastads(cArray,nArray,aArray,bArray,e=11,eps=1/13):
	"""
	Performs Hastads attack on raw RSA with no padding.
	This is for RSA encryptions of the form: cArray[i] = pow(aArray[i]*msg + bArray[i],e,nArray[i])
	Where they are all encryptions of the same message.
	cArray = Ciphertext Array
	nArray = Modulus Array
	aArray = Array of 'slopes' for the linear padding
	bArray = Array of 'y-intercepts' for the linear padding
	e = public exponent
	"""
    if(len(cArray) == len(nArray) == len(aArray) == len(bArray) == e):
        for i in range(e):
            cArray[i] = Integer(cArray[i])
            nArray[i] = Integer(nArray[i])
            aArray[i] = Integer(aArray[i])
            bArray[i] = Integer(bArray[i])
        TArray = [-1]*e
        for i in range(e):
            arrayToCRT = [0]*e
            arrayToCRT[i] = 1
            TArray[i] = crt(arrayToCRT,nArray)
        P.<x> = PolynomialRing(Zmod(prod(nArray)))
        gArray = [-1]*e
        for i in range(e):
            gArray[i] = TArray[i]*(pow(aArray[i]*x + bArray[i],e) - cArray[i])
        g = sum(gArray)
        g = g.monic()
        # Use Sage's inbuilt coppersmith method
        roots = g.small_roots(epsilon=eps)
        if(len(roots)== 0):
            print("No Solutions found")
            return -1
        return roots[0]

    else:
        print("CiphertextArray, ModulusArray, and the linear padding arrays need to be of the same length," +
         "and the same size as the public exponent")
         
         
print(linearPaddingHastads([5726315526762276771502241852510580404907144923423723151520535017921034034552237955373157643352724265884406381294908072565380669325397880779320633094444633224831659070852777746944598095316136558627906988181554870085846766499215211553707914294868548004174367197222110993561019604930890825354444812504360723077895633218776825330501594227280864021387583805120196254101138956360614342191104646723953185400049399898228518141531823582554328901324161938981985525601136595410743177253865335812712205558226655414790943341409583928449384633081347879930148284783077292814366972240250643302325486805055106659518640493634873854272, 2054014161361812426464474754925858319593315117050057826796683642829120008611407980125909323759180686854255766640613312843245868454045811729587994929893181975729918128006735423042203865129878067529717168735407763591867887191334913208140202553354639178232147403214619678836361535882355649009534978943724653165050281148353418722881860892111465399308499150436718713435098387386116933035884948860018134973246180922312083595259328685340304744023471059647008504834598398399891507272941183856118419085669048813120579553961291465525185700982842010428563241497325452687757570420863047538966834417781094914378069825066624963867, 7743528979366204051675190969544431451791699507249403365302575605984298146081419799821441955179225453995031435641982002146268291420932830623351670374947317212935637207171093662998560036150044529060227570258292333498118881189585606214891420326387658738228197470679942855629549290049941442026776606286208760903759529419123334549531954387228601247638723006979301254454904873124108852474476806139046023707813059629764473733227995079746184315087964673181325559671827255572979306127102144458737248853839264435510587770254197573333502317452827920811460311987586205564069410198718800818409606144311481148302354316069522468958, 13628957571029901272647063015162905768718421418563539267701104053946233284000519834979635704476950521386460000594116553676464586698135729277821055690924065586783708497648568453036872370929643162822489980909628572524043504463908417839003752380453089349063226163684411549516241056175443652998931051421428814969280609679510780722132097328272219786656351424916456895306718496199866776733346993064179576719614693992687728856405806032194082630391286483076351529117933427288403212905631926815099834626496166645022840492516104521307039201310982897398224984226381808865798173110222465464712141587772576219583362148585496581208, 13201696986643845959677371662948115967447802226786186451785739762623410393548513150972922020163641474748363757837456026666731761246661735274913763831543626312615614008873618261381904459892647389171244686671221633145537658399355847691467233696214515425783864841237517124691277198785978952396516274784529650270772458251365565127378020702585082924969148323558263009670132210443932415641565479360759239679284475120243347681128028643642037929722792454059836297039281405926733901289515261307204888121552806894673178743281044582225390624702272048253183910069636921324038240760027105820702942522903957648750782459562356599142, 4749074192663116715046977614212763814173594221541352102399885387227742063593832926977809310204497231241023648395450331816823329965263214976072414995206386616129515606750799778020726609248387717697581746262147005946678262019400627195608391449537128829050188392615589426962123442483853869353443210708211946593377756557673225951638634912105888660045644830818188795153184998308051643302966068214473974158040711592293806418515259647835614831197989689093201226756034443492749864602172460766487047629798267837080493654764556844228320465932818792563893445341916734835823961996280635423983716204757222122832073236295515354681, 2842904887944195384427325924503651157122570233764644773064695534492811105043993786429302282037549689090901886612679417716947487383584332123607953783069486592534646248119577819451707755504430311001734585744016938060373473158987087873933978976406426697575265800179883422915996784304365582286042446290045332668739308319645158799476214450370055423181838699324917762000297373140166259251936259938734629741769865914577370955345907061492318122686073527094032756353082054512478536416259790314741427568671881886259003587265118481004809234449653973555868741839759403478508320324227942499787403959849326561998775838287620651723, 7472988788771994715098679409517602219004758690718908300424133082164962281867813316380669594846950863248644333674031199319939118379735418512446422477702161197412975966820057050661376514972637089191697104222884316654246477359554573060219318096806823894199948646179641429535747872632440618995048372019010899230127358872127990602654730441624939863653196314685071770004807336626474776741902979579645432293882935413537162448778559767549002795678502725149916120121173265219680077934991335888665177841102458749752335822746867622349051758496031213814442011841619674104425451338994306790056598724232005513901735268861530822337, 12566792808383963125811204849659677219471940348708583298510099182806105630228717067217519668253457854515889410110927600262168315179210178351619638516502579153419594480683854358868210673462095820334794593323863361551462029767324162721121085233044058189488941145394155667834044297237805544714405730600408262087785105736845721339557575398800737334132174083541877727851421459024216746744961404523186833872645918824098966091591985245013788979068434639532136334603266043547770149748472613243659983120357493458389091574599121275194551724652720631744157185254460911024322196883399089249941137023859623615093567198226990944676, 6781353772958528118951578580070290762103144903197856677518202418411175210507513867449564876238164663915858618237003141873865756367106321545038458547111486917210585978622641238438511093371039110748378033029922247702949009856323336982129336618381169539949159946623026066689556535714687611264814977983153893557071352975508622801139120843546353299431914570610662663263160975072633709256393561150568632459950697992018071344675241822429312614836224838922648334190191992994553900583410421020812839555062310610856256911100163522370253861883067310907490425167822258628193002586931045895534535291863190890850372808302846204515, 11854879722972904558786360997823341722421174202228584304943347487031075100214009198073585506102654317072512416899979601887904944167370025301498128941653895789800255246751514536362453408648106697067598175900181904322689575100177889378522699674794848016191397719779076655662416938542259536807610508599807388173646621598757117690039538585896604184020031154381180971985425853147922692510833285039672324667942962557165133724063370246801302992721229876682848456154201357137038118975236343428367322382865274935631722280829995422519431468192673204621372416684155808102660048652017915188467417157382572219283601004936509029296 ], [17469119309192678862710950803044523317212702488797693446763589381579815077793712501024764168893129185082711608175696500687044227915841768742858988680162386777414066823035580182490355467656274475873123177297495574707440554180975464432322998169136575282638313762442756996582062657015144914438368113245631956671045984726787546333588273678626415988916789383193309141915194618134410997175482208392221490264141471211032151107753755284157503145009267118553597584129369101074862022726452947207594810570611297959647348281636343757531228844020183415025267090406030800827365793692916644215814948838751493358552675251184673710199, 16874318665485634350198943566741124697292998884158765649809507657384057244850389565828048113140756263290170446142989770337196942517590512686325407432395341449156127011586130155399713580906397808761755509697770295643560364569832869564302819021539336450901575858946034194964977804909092003695104208551503213605795507780982234526369391790728233030399934358380974373940270546648721666150993774693962771754152293605209097417841304151518811323301010755185650639983504977607932670864562561241504330430854032499286196940112496065621213802464028576597807097759817796872492191132372562719701887221646334993634436383208182891391, 16513123327695759372252218348301409103739849913827438697878731023312580388674853621265855172378516315273809385762889170240552677123961382846179080101499041377487634332096343374171255519795373721404207976915121296203915889251668652658437922749498040974749809839900601139538220422043508160998302941357688412215924570444188767167120430427134891449984984110739959141667399978387111510912154637153184896679894465377954721440189276655888882879860270693658734012226152957871507902884938271625147459731984304726621099251814024552241775791830840518659537700802528177507382740326951098587323778286410961358987942282585497414833, 21289284495525201818520880283930101121056182301438651138381601813962313257994983605311674748227482996350398002937243612454560605294507935136955418133174568702166330439093789076568617458630716061290906641058495078419352136093116029999015805851127401442937811016029017046474397319634721946905817037723191044241049628272964125764497135189937061162251642886252648921664695895435787624413383262740261670072781061956690078265294218683737331227526058658361635385648942700485331500919203037870260050888167844201613077934416072500275298004334011547221759267962422489433801814583693307412150517272301832048797743820320452731737, 14387707309645927285103344011955402511572313872961187648951017087015870514375146840013047600112507103063920916459293897757969423464190775581710526881402525252161150257808731963361220070028421261884853897117743866829508576422613255287813032943027776309603747538170778363460707855505435894913351223156439189014217633718127133477135096857920836811292490510744594328881647001793637968845995389395862207118816803638936535636880631154031557212884078404225795889575046640429761114625226618111777928538162276022185130139292881455821996739758214020210990084823853749142767743912821113924617278312153243475932755081554575525693, 14843990753278206106117274439394355750039101622339964009916848173682541750159401486949742769042581822621506539883115537450883971221476125951083171962801488552059896398729829042898413266919921658791826487829268119864857013344190899750482052674944266524217280768920119634758544906812415538911286697264425783266138605688459092237987785232677777505554875699655442892337484306837452805365521445733424599808785913363315151122602737830092316553405196562532348139770956415679631043542562779204979543075852994745344417968752014804135700586078041729047690003517708222493605341779673946460219247175345185928917666013189706602459, 12231622199632309539584424453940623219078349786452692223048234115884125564241755976436870929777720138009450262237530205182139374914625033026856346414529471355749713692050300187119251782407796412645701192105787751092892434584285222565300193942410748509310936811873395760152939441135157697221177353905154634379674457410500550398938076804108439114363514581522938700986798954776751202736616871001180723310277214115476887180039862668906561933510598956144950997719173070684931209951461780640284194794082772669209152840866624907652776802696661130579701156950590192917471613716068024255780171322421531631243295393530669855611, 17883982766058249125329694396768073862955005062116673967233455132139395063330212835422313135573298371046558360061380696509313283864755082891127063549731909250045543796792001700604091966053782979041415103839535315045548910224425750976835856149790253848796223791768105052868115876009815124281039436680390394039227621538943394583165158895519804680956806119572528147411010049125897293098513079911849110859656570853739925470558849525040695208241585672950506760320276328970229615213372477681963871587413916470440068052085228982477113779624056467642239174965388209451660819378717466190259786001563131050339524283264776133431, 15588632637326336067308982159114857453538522941490595727706389505322366174703886627570026785429262979524891878794457632241009554014053165746450485406788805029152854545867151610539515103036593105099388615269976837552522150716159640375968439513436893626595406020952566823263384174090345924213144440824155224959717053838012763097078148864110898052584370701885478841384354334474869332276069863330953630089562891567962698960727685845853079304811993965981987542496878747004884320118732119996001538577593558465963259402405909661684869383822055317073975771444713724076728686707612509015771780928044702269843746521515383983563, 19543629536173164502778093682736406689686445942264381743487982395065682015423088229664165736977850627705588018142955080105510221624759049112982789704187242060205246804855805362913100365301650779267975841298492251158726700713258326075817062351324790915769630362629056987437084065381231323726381957770046125156504509430620805702093945687545663778923669432562176890616030575777173738875219713091480984001703907802827803850014527111698795845431271230740515149946801586033925249845546070589563001986936316585602761251837812706674601279582125898090201800204861580435631231469174973770247256789585483910089442695396975982809, 16617722405541826315174350641566104962055635007172479984307047698255653459877546065781857556438520812158706849580382309669335675531285806543772717330646634220951822836665217614043856715943961722703348944603471705337602722790120770257286665883644598486030952993318732042322926058400596856681577962786012454757914445977932376704878470113584414122110174241824834196476510616505541655965678728132532370925271619214255301746281138834600389680185309838083698484276309658953277707166998464258495414552540926489510352381802696896990757831809795985966697472578754381651280811405781986888917046721159091716646583076551221313403 ], [1956330959956767383483153409156229126131306053495463875787467905533634648443105279210605476951163494543008084355821504066602613828266976017594951533094227717234314196340255590263983487742656965167502755597067708342523528468946545215004167673329491130322097688576464572952619756078017174657704334154535792763121046386107147351264414883580754180819055638587558470509472005515693898717304640664482629446117815134043420877754162345635721197113091483925244324573659242608246954623055645728168894664813198706230674210096705272438359882077106463044521368163390743264025882255773179701316342958839396135260248241621546453438, 16286747639766057534439361292780583837504429552001983061192421204644468922459174557518667029969578290605834083648598495448006730418640128747387775291802159545726000705038159316982878606267124399365481719752257691851742015441913368723034366834358011847775559750730403668692691254094524002871216226768601483560008040419162553118027573962924221241743951097660409926946360358371350277446494544136579703529083987553418633595871319878860260047345494648501684954645582066657850255060631473858818762440696458112101463077564479411291834279600875030448595786007599787041293896183184995833996984700849823455530546730051577163745, 6656758688896512089801647353493235639009068086204001096167276188690860835249543009980884885595532424576838051376803643096302082318228756749278400264039336032801607152912695657276384187067505100874311079223741615164756975008736701039338790944607709573140524548703914193840274457114761892624052740519822167353409382105839638221735989289978455661646692860102941543620005585631289923083563371077830007312733100009527949604244864612072582275185385331657677536412893571765286441916241826467343293622377812228256750538541221873263631294791526351153152401833603318860175143075993336802536951805626673181774790649001211860188, 13316433106127924522031466796885748924459745777751310925344138941951338862011449802272428208493884243213500116559203039370240199317614947473189095136242315400521866066153158105499108535861875122572794371396347905658879487941889685620104980401745125604616076095708695419106238173005569809905654315972542514110888994910820055165429644789491404498639890755539095201102672952588038627891784125783244604843487404372335142915000694141394278212941037995755490592890003984865438869432746171443816651812274351996707509135917322867889294003501010369183438882138000541549222607551530946142727643945608937467128259779254826500093, 1513719511947159650592756184817911385783488115294947109390967558092681551626664371264077511551451850596367466264575910384183536253665098513392683047913081432387386946799379188472013225321990986158905468179524598342454015627215071449568793776206259764347129706089004655340979819884079740394024149721406116957688359582019398080563764634762012046232877878111419194411282602285197741249145826223889990817713572906646969314341240195892696407759112150761236347751048499149673885022451837254786043481515878466283015398637832251040041966550653769062529555847063826385267989847635091442093258967263924820089466631259564667364, 1112551973033265133396777101225647742787501337728058866353148616928504971801885654141359819058761028205235796562467397662235550100396512891343598264937475329487323394961672009060377676817801468073856128028826141889928180251030033655080368144607178239511787873638695108051845690295851097421598639523183880931760386877983747392871402736770204428618655531668074025900926517425403906552090112485806817529061026354882446007805784938092261081003670204103114089405517379443117205398756561871651759590985307429866747865916699819045934433834690018984941453419203778002932055120144724018934247404728362756104235086318145100994, 4049659551488328397863715629960201247009752801280492561502986263185458518125472190553248456041709168742956015716038815038049178360572703455629537737950838775938098366475012011211534154157878990363743649822891273764636147656392601661267585279941033408992967541645406536009107454386486559460276460557757418318388769901617392046824517687881528851586095567412910587713892769230489754886112512260141047826942102161979649824041337588820275962744573562694163369347938429338296117049877878101509213101543924277138100193064255181406263329158694180833832774883028745267431397303144352416874681390675268046439959665249498483450, 12509889356119664356776293469048911610241665849682697011239878991154816235040755637577414147754947675535217701696793022439925930852150003155792752428491998534323736163318488073344858245812209499701353562854277611835150868547618772359231036888446085861091877301390961061153476572926026411261822490941872341847025499347438477610690825292287698827072108057380424196358715693151109730948779028346166126417107206829410097616427860244505486299005485383179148815587367399442365840346005595341796107036468343273258452985640608067449169386390158896283766525937453053637391335723406299122024666539392736992319867570847897254867, 12554823486122096137582873124401107426025893568755431196445323002129083935224300820856403984541347061709712105194687619593761328603068167923169760840439161467223936885145497865505205729980340382742647506307181784520685101753115572196316398359431594484699954431348975575310776288963026025392766829059915622253757330460512473449461745895766034883793484296646919364461064506309575687508998057585978069741734304928638222329604546758766789146369752541146921173639880574359136239238656154580678577860998298522909801986658453169486667053043358179782251648579372781434611524788299538168283750294882883047464905950467979189147, 10892268797637757325350751330317943388751554155839297112130906249350347236499672614296138392603217650269724052762399107930848651148296256244786562254232960608165622780358156806248829707612129177041618281981093048784186248374057175355525628184453781874339740401943840978327173707411322743235233313543177302747856730149446334882014644667119366653726385409261393361553770326615143530321540636314640895099357099890991684176717234843478246321399975940840183229184549798799080772983226990311345876651914662728471442853329311540389944880347751047918463360590878609129978606818171095873499629827273916261669847976324461937711, 1793735977469503189617806625616343564303941718700191899407703556948331036921110230167699250838578932796731894522415261211685264148049040600490713437763264925378036820553096662461422871224790168148051190422769490049789309908418275436066752381707970289287409646924176160448165446597654303563533607860771722986746446253249706223091632065879519779982314975489104397754550516261131079038060623189902794886633294812807372469727574030788341247245483211397211864036344831220493108837850961454129005397568676158325972376075017160514626281437537429137535368903041862689413102801781184778241727142170489983836760749549955975169 ], [8755671518702475251100285837309656161454323943844472000828366378113847282063836362267353985362877902640196378290992646088333458986190878360048842072277784282599795434741863153651344989843720498546493914613090196226414322019036814149973509488561428595512128509382540081532439748657352271144040882108102744240297249075374318109137218071373818669135881200886257292090792852446264512320370183485797288190909004590946820750005609642267880187286144367538647141397613572256525800413229002443300917880361575167040661876881070250938053735609612376203174670771814163707634736202671864884637112321681242606048990208416069689359, 1189535513761477820075629612928449120690890206475248096030116055663630203409392436698223970275351565310707254965838196199198876126412807930514101124183951803552694165564337473015303943358953173354074603816330980213138039197105411313177858717536276341146290705091546039766226138900479277886238756990661380015330576542734901016242831389110407859556343510569141317927244973986213293987129736578848699898030259279685048139092528459784476660336008512316258031596707252356029696823665588462972509927348787162849845820142983715895267974036637852721660224830173244373365360155339038456027477976989111404433413637517114821207, 16102906457237216402434664131325715080231082052317994470077689932311015195375162782029026610926014896827340504355872939291455331424248768587571104621928186204761797608838628315828689759746779727604659046770577501207885796961065291233231318941631601481385470852124769894473787240588897075138736260106156863346983963439036165649605858321765315185851383149274982419219930125816679911011998342129654539666486944306607323912526743623406921582741077011165559939640712436539846010032745928345165121861065043260999265917989288572787399034385396077829977218866700277116430816421340743115057424086205002206714272880667959661664, 3859142786101450465172127481458767235222665420967138053220921158151288386371070937096966045397444934808900173901959053556810638035024874816435210512801077899549015417437548696844982554318283919080023205647720564016664376718921326096215529693155935933649262514645387779813448304746046193198018259997335223684249381200311600865003444472280118790637187864302274120180721434245294606278076974668538619597524926647755790191145921022713948785389959117494066820829004747353572652293717760794017507131941180410423129293519671337771854485212340480842140283563802565071268961439819705008158849692177471607313541327968694621566, 11238690756322717289347379482357507997784935483489920739385264224774879123061814598562739931987603254705557914698672743516045976607540683752828074953942411565554696938044062188076988465238696115154133123331838009557219604050942902869618183169158841929424230986396185257663451071196813605616025561889914793746869112376679361351461901351194877558068535502901095084666139779658094785414803715573694128100263488103758935975987671086543275647593969590823244097233310260631019130351642384414572341865014689246750374059104566711147299308804053057006103672871491727033518749960339110039020286874326312158685606441952039395881, 9590664018795464935288046615631546132051698156420604946949173825231414976313794484229317008618768372275713072433408817964728489156972256148589060869366505154119375038083783988451763484041586561435153965019297001195924473901341546780055613442584472836332376473500696081779583494007216265332224384759354845614459372207490916377977908866679876925509466930013127106181422918382981840884409865799352178926806042526995831415938543710920559217717579855867304632015860280324049433763298876104190983122993584389208195343341916025978054503344070020162548144109548148927161421551149571877368262892011734347056409840367685457806, 10878300531060542966362404100954047909586362714897491021748656416805063853186903403049170356616531360277055014206093954022773482382144263392221562179189076745506222261646987960621407061966018022486858793508589985860982319646979122652539269719998717623297650611267539834502240907421959057822280537466235195316132923474887174873190581487214030665196235003203272164918458149414697018686213304117050594202211289844600807651482862399727308902713665785427904527100651916081078172750680944616015742582767897760242717423216392164603494486050153444803763638598420503951508094997814874855240470478503213521020882512753867773150, 17861390338757355787610450994093833871105249925990532284641284264761973120253240638314894458457150269890445699866083693004022038777775604729723992782768211785043625867786782219632309312994999346227990586509308454636465309249419690689871764499106848206936925324443635357734885262513150349293710435167914238692724399023001465688155856444577622912944445680925012692697449431825496510429654078646546390716624497211754189820049265493337362562911387216532554300144569293431122736813734447667475458558913262865270779651853073080425202414654469136148346079611147216656792754532515142920783652655526213310621904911490198470854, 11562159938685783960079824415902325243344871847506322079608539030798368794411862994104401666069658027772216859947707636531744065226236353330326604026303282957699987530438441860390884744362811945457405705580949774014657815538023562961696640211748175964888623881939781612792524210835760821298376836804418739776752461988741979482057641402943703744471551512932023509615330324831866730518223631881763048974678049259951446916453377539832122574369116125497175557106437311894767435732588999679693436674827652080801348307564073366274659556705019880814401570849677681744561164671249834805824712637390618376877825693462277385601, 13744988625883135813876556683100181296572406062153608041326521736447681936347377986636503605152568609918359126673034766695990051344528107097047934339590093207055375729583227219468210439120346792501096311966925198523486697018751597636146879261050996199209086386849439626899898630542586482058113495015433353979890252277446083717329048091950740529995596358715952201304738840276106326922723705462955699114819141825719851183993935140819697049273142209971971046758765319756099689739135079110684577948882661507178897491551720873849250774482634639313014323444843211133764832197992396725552995596294535944189606891907590877545, 13608679173772887613742714489421453365727885678711396489027064136015155256415235051162749870095036467000531718484868601764938913678766256078299671698744623032499889274302606027222757025429685862690308772080677543814428142393331980913103978326777213195029958425739837897581953833916046322625497477644629198482121169609297035182474422517704166322833372187440003370069554163332962666059144448579946386337912216394506072130424455639914760514619178449972126774538156604267465000746843293235527192177831759368273254215617283432632427492831250727620041448089624758116841226424491718435356741589270591050290859997616305939000 ], 11))


