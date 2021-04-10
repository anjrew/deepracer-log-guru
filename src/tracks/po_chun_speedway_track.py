from src.tracks.track import Track
import src.personalize.configuration.personal_track_annotations as config


class PoChunSpeedwayTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Po-Chun Speedway"
        self._ui_description = "Po-Chun Speedway is a short track (68.68m) featuring a simple oval track paired with a dragstrip, and single hairpin. It is named in honor of the 2020 AWS DeepRacer League Champion from NCTU CGI Taiwan."
        self._ui_length_in_m = 68.68  # metres
        self._ui_width_in_cm = 107  # centimetres   # TODO
        self._world_name = "penbay_open"
        self._track_sector_dividers = [60, 90, 120, 153, 183]
        self._annotations = config.po_chun_speedway_annotations
        self._track_width = 1.066

        self._track_waypoints = [(-0.5438075065612793, -4.263250946998596), (-0.2424324005842209, -4.263250946998596),
                                 (0.058941951021552086, -4.263245105743408), (0.36031660437583923, -4.2632399797439575),
                                 (0.6616914868354797, -4.263237953186035), (0.963066667318337, -4.263237953186035),
                                 (1.2644420266151428, -4.263239026069641), (1.5658175349235535, -4.26324188709259),
                                 (1.8671924471855164, -4.263247013092041), (2.168567419052124, -4.263249039649963),
                                 (2.469942569732666, -4.263240933418274), (2.7713170051574707, -4.263220906257629),
                                 (3.072692036628723, -4.263198018074036), (3.374067544937134, -4.263236045837402),
                                 (3.675445079803467, -4.26334810256958), (3.976821541786194, -4.263386845588684),
                                 (4.27818751335144, -4.262967109680176), (4.579564571380615, -4.263054966926575),
                                 (4.880862474441528, -4.2593196630477905), (5.182199954986572, -4.255808472633362),
                                 (5.4835405349731445, -4.2602540254592896), (5.784820556640625, -4.267787456512451),
                                 (6.086097478866577, -4.27549409866333), (6.387416839599609, -4.2812405824661255),
                                 (6.688783645629883, -4.283218502998352), (6.990134000778198, -4.279719114303589),
                                 (7.291311502456665, -4.268986463546753), (7.592015504837036, -4.24904203414917),
                                 (7.891724348068237, -4.217547416687012), (8.18955373764038, -4.171620488166809),
                                 (8.484011173248291, -4.1076260805130005), (8.772565364837646, -4.020909070968628),
                                 (9.050934791564941, -3.9057544469833374), (9.31207799911499, -3.755754590034485),
                                 (9.545350074768066, -3.565456509590149), (9.737494945526123, -3.333828926086426),
                                 (9.877556800842285, -3.067478060722351), (9.962692260742188, -2.7787269353866577),
                                 (9.998307704925537, -2.4796690940856934), (9.993433952331543, -2.178444504737854),
                                 (9.956905841827393, -1.8793534636497498), (9.894974708557129, -1.5845664739608765),
                                 (9.813337802886963, -1.294617474079132), (9.661679744720459, -1.0340088605880737),
                                 (9.488976955413818, -0.7871880680322647), (9.28974962234497, -0.5612570866942406),
                                 (9.061550617218018, -0.36473871022462845), (8.805681228637695, -0.2060214877128601),
                                 (8.528502464294434, -0.08825819194316864), (8.238834857940683, -0.005477815866472724),
                                 (7.9439074993133545, 0.05643086135387421), (7.648383855819702, 0.1154988557100296),
                                 (7.356605052947998, 0.1906125396490097), (7.075538396835327, 0.29877113550901413),
                                 (6.815032005310059, 0.449687831569463), (6.583379507064819, 0.6420481652021408),
                                 (6.383110046386719, 0.8670095801353455), (6.211615562438965, 1.114708036184311),
                                 (6.064267873764038, 1.3775370121002197), (5.9365739822387695, 1.6504955291748047),
                                 (5.824730634689331, 1.930329442024231), (5.725836992263794, 2.215011954307556),
                                 (5.637604475021362, 2.503180980682373), (5.55827260017395, 2.7939260005950928),
                                 (5.486449480056763, 3.086618423461914), (5.4212236404418945, 3.3808475732803345),
                                 (5.360888957977295, 3.676126003265381), (5.307810306549072, 3.9728164672851562),
                                 (5.255915641784668, 4.269661903381348), (5.255915641784668, 4.269661903381348),
                                 (5.171812057495117, 4.558959007263184), (5.057467460632324, 4.837637901306152),
                                 (4.908321857452393, 5.099258661270142), (4.719554424285889, 5.333714485168457),
                                 (4.487942934036255, 5.525609016418457), (4.2155985832214355, 5.65233850479126),
                                 (3.9176909923553467, 5.687243938446045), (3.626256585121155, 5.6165759563446045),
                                 (3.373347520828247, 5.454691410064697), (3.172053098678589, 5.23124885559082),
                                 (3.0192744731903076, 4.971868991851807), (2.9074225425720215, 4.692229509353638),
                                 (2.8290610313415527, 4.401329517364502), (2.7656580209732056, 4.1068384647369385),
                                 (2.6942299604415894, 3.8140534162521362), (2.624626040458679, 3.5208264589309692),
                                 (2.5562684535980225, 3.2273060083389282), (2.487966477870941, 2.933772921562195),
                                 (2.417782425880432, 2.640684962272644), (2.3434759974479675, 2.3486180305480957),
                                 (2.263619542121887, 2.0580199360847473), (2.1779080033302307, 1.769095003604889),
                                 (2.086897075176239, 1.481793999671936), (1.9914774298667908, 1.195925533771515),
                                 (1.8925195336341858, 0.9112615883350372), (1.7909629940986633, 0.6275114417076111),
                                 (1.6771830320358276, 0.34851986169815063), (1.5420934557914734, 0.07920094579458237),
                                 (1.375698298215866, -0.17132550477981567), (1.154587984085083, -0.3748939111828804),
                                 (0.8861891627311707, -0.5099374107085168), (0.5929704010486603, -0.5773696657270193),
                                 (0.2924389988183975, -0.5975138358771801),
                                 (-0.008872425183653831, -0.5930791702121496),
                                 (-0.3100501596927643, -0.5822000745683908), (-0.6113669276237488, -0.5763594638556242),
                                 (-0.9126869142055511, -0.5706923473626375), (-1.2135509848594666, -0.5553900022059679),
                                 (-1.5122569799423218, -0.5155553366057575), (-1.8066700100898743, -0.4516452308744192),
                                 (-2.0904905200004578, -0.3511328548192978),
                                 (-2.3476184606552124, -0.19540660828351974),
                                 (-2.543960928916931, 0.031185656785964966), (-2.6494204998016357, 0.31214994937181473),
                                 (-2.6782190799713135, 0.6116668581962585), (-2.661974549293518, 0.9124709963798523),
                                 (-2.622704029083252, 1.2112460136413574), (-2.5733546018600464, 1.5085490345954895),
                                 (-2.522086977958679, 1.8055314421653748), (-2.4744099378585815, 2.10310697555542),
                                 (-2.4343894720077515, 2.4018020629882812), (-2.4045780301094055, 2.7017359733581543),
                                 (-2.4071930646896362, 3.0029375553131104), (-2.421003043651581, 3.303991436958313),
                                 (-2.441774010658264, 3.6046409606933594), (-2.4724985361099243, 3.904436469078064),
                                 (-2.5109124779701233, 4.203347444534302), (-2.557044506072998, 4.501156568527222),
                                 (-2.612808108329773, 4.797319650650024), (-2.6757819652557373, 5.092035531997681),
                                 (-2.7473304271698, 5.384776592254639), (-2.8280030488967896, 5.675145626068115),
                                 (-2.9156925678253174, 5.9634740352630615), (-3.0483371019363403, 6.233566045761108),
                                 (-3.206257462501526, 6.490138053894043), (-3.387305974960327, 6.7309410572052),
                                 (-3.5930325984954834, 6.950990915298462), (-3.824325919151306, 7.14389705657959),
                                 (-4.080339550971985, 7.302426338195801), (-4.358352899551392, 7.417964458465576),
                                 (-4.651947021484375, 7.484472274780273), (-4.952653408050537, 7.498128652572632),
                                 (-5.251113176345825, 7.458754539489746), (-5.538994550704956, 7.370548963546753),
                                 (-5.810213565826416, 7.239671945571899), (-6.061072587966919, 7.0729734897613525),
                                 (-6.2898008823394775, 6.876953363418579), (-6.495967149734497, 6.657280921936035),
                                 (-6.6798639297485325, 6.418627977371219), (-6.8422024250030535, 6.164793014526364),
                                 (-6.983914613723755, 5.898880958557129), (-7.105918884277344, 5.623551368713379),
                                 (-7.208332538604736, 5.340780973434448), (-7.291143894195557, 5.050683975219727),
                                 (-7.365557909011841, 4.7574474811553955), (-7.44334602355957, 4.465471506118774),
                                 (-7.52450966835022, 4.1747565269470215), (-7.60904860496521, 3.8853025436401367),
                                 (-7.696946382522583, 3.597102999687195), (-7.785883665084839, 3.3092925548553467),
                                 (-7.874215602874756, 3.0212559700012207), (-7.96194291114807, 2.7329950332641637),
                                 (-8.049065351486206, 2.4445085525512695), (-8.135598421096802, 2.155803084373474),
                                 (-8.22207498550415, 1.867075502872467), (-8.308757066726685, 1.5784239768981934),
                                 (-8.395602464675903, 1.2898319959640503), (-8.482460498809814, 1.001244992017746),
                                 (-8.569319248199463, 0.7126579582691193), (-8.65617847442627, 0.42407093942165375),
                                 (-8.743041515350342, 0.1354851396754384), (-8.830611228942871, -0.1528868685127236),
                                 (-8.917747020721436, -0.4413904547691345), (-9.004613399505615, -0.729975163936615),
                                 (-9.09135913848877, -1.018596351146698), (-9.177855491638184, -1.3072919845581055),
                                 (-9.264797687530518, -1.5958539843559265), (-9.352763652801514, -1.8841055035591125),
                                 (-9.440656185150146, -2.17237651348114), (-9.525533676147461, -2.4615434408187866),
                                 (-9.614251613616943, -2.749564051628113), (-9.702064514160156, -3.0378609895706177),
                                 (-9.78519344329834, -3.327538013458252), (-9.859961986541748, -3.6194756031036377),
                                 (-9.922293663024902, -3.9143035411834717), (-9.963254451751709, -4.21279764175415),
                                 (-9.988624572753906, -4.513084173202515), (-9.999826908111572, -4.8142006397247314),
                                 (-9.991546630859375, -5.115410566329956), (-9.960739612579346, -5.415127992630005),
                                 (-9.905710220336914, -5.711353302001953), (-9.823229789733887, -6.001063823699951),
                                 (-9.707994937896729, -6.279352903366089), (-9.55672550201416, -6.539675712585449),
                                 (-9.365952491760254, -6.7725489139556885), (-9.134821891784668, -6.965120553970337),
                                 (-8.881346225738525, -7.127945423126221), (-8.612974643707275, -7.264806509017944),
                                 (-8.331972599029548, -7.373393058776853), (-8.040998458862305, -7.451314449310303),
                                 (-7.742873907089233, -7.494183540344238), (-7.441753149032593, -7.496646404266357),
                                 (-7.144059658050537, -7.451900005340576), (-6.859269618988037, -7.354599475860596),
                                 (-6.5987584590911865, -7.203993797302246), (-6.373180389404297, -7.004823684692383),
                                 (-6.188401937484741, -6.767185926437378), (-6.0442726612091064, -6.5028064250946045),
                                 (-5.911931037902832, -6.232149124145508), (-5.7734694480896, -5.9644670486450195),
                                 (-5.629935026168823, -5.69947361946106), (-5.4770660400390625, -5.439780950546265),
                                 (-5.311311721801753, -5.18811964988708), (-5.130865097045894, -4.946840524673457),
                                 (-4.927100419998169, -4.72498083114624), (-4.699373960494995, -4.527881145477295),
                                 (-4.442312002182007, -4.371398568153381), (-4.159760951995858, -4.267678976058963),
                                 (-3.8585125207901, -4.266657471656799), (-3.5574525594711304, -4.264110445976257),
                                 (-3.256335973739624, -4.262017488479614), (-2.9548726081848145, -4.262735486030579),
                                 (-2.6534165143966675, -4.263384461402893), (-2.3520240783691406, -4.26352596282959),
                                 (-2.0506725311279297, -4.263338088989258), (-1.7493119835853577, -4.26321804523468),
                                 (-1.447941541671753, -4.2631789445877075), (-1.1465629935264587, -4.263208985328674),
                                 (-0.8451843559741974, -4.263236999511719), (-0.5438075065612793, -4.263250946998596)]
