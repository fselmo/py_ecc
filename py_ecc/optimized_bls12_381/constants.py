from py_ecc.fields import (
    optimized_bls12_381_FQ2 as FQ2,
)

#
# Ciphersuite BLS12381G2-SHA256-SSWU-RO paramters
#
ISO_3_A = FQ2([0, 240])
ISO_3_B = FQ2([1012, 1012])
ISO_3_Z = FQ2([-2, -1])
P_MINUS_9_DIV_16 = 1001205140483106588246484290269935788605945006208159541241399033561623546780709821462541004956387089373434649096260670658193992783731681621012512651314777238193313314641988297376025498093520728838658813979860931248214124593092835  # noqa: E501

EV1 = 1015919005498129635886032702454337503112659152043614931979881174103627376789972962005013361970813319613593700736144  # noqa: E501
EV2 = 1244231661155348484223428017511856347821538750986231559855759541903146219579071812422210818684355842447591283616181  # noqa: E501
EV3 = 1646015993121829755895883253076789309308090876275172350194834453434199515639474951814226234213676147507404483718679  # noqa: E501
EV4 = 1637752706019426886789797193293828301565549384974986623510918743054325021588194075665960171838131772227885159387073  # noqa: E501
ETAS = [FQ2([EV1, EV2]), FQ2([-EV2, EV1]), FQ2([EV3, EV4]), FQ2([-EV4, EV3])]

RV1 = 1028732146235106349975324479215795277384839936929757896155643118032610843298655225875571310552543014690878354869257  # noqa: E501
POSITIVE_EIGTH_ROOTS_OF_UNITY = (
    FQ2([1, 0]), FQ2([0, 1]), FQ2([RV1, RV1]), FQ2([RV1, -RV1]),
)

# X Numerator
ISO_3_K_1_0_VAL = 889424345604814976315064405719089812568196182208668418962679585805340366775741747653930584250892369786198727235542  # noqa: E501
ISO_3_K_1_0 = FQ2([ISO_3_K_1_0_VAL, ISO_3_K_1_0_VAL])  # noqa: E501
ISO_3_K_1_1 = FQ2([0, 2668273036814444928945193217157269437704588546626005256888038757416021100327225242961791752752677109358596181706522])  # noqa: E501
ISO_3_K_1_2 = FQ2([2668273036814444928945193217157269437704588546626005256888038757416021100327225242961791752752677109358596181706526, 1334136518407222464472596608578634718852294273313002628444019378708010550163612621480895876376338554679298090853261])  # noqa: E501
ISO_3_K_1_3 = FQ2([3557697382419259905260257622876359250272784728834673675850718343221361467102966990615722337003569479144794908942033, 0])  # noqa: E501
ISO_3_X_NUMERATOR = (ISO_3_K_1_0, ISO_3_K_1_1, ISO_3_K_1_2, ISO_3_K_1_3)

# X Denominator
ISO_3_K_2_0 = FQ2([0, 4002409555221667393417789825735904156556882819939007885332058136124031650490837864442687629129015664037894272559715])  # noqa: E501
ISO_3_K_2_1 = FQ2([12, 4002409555221667393417789825735904156556882819939007885332058136124031650490837864442687629129015664037894272559775])  # noqa: E501
ISO_3_K_2_2 = FQ2.one()
ISO_3_K_2_3 = FQ2.zero()
ISO_3_X_DENOMINATOR = (ISO_3_K_2_0, ISO_3_K_2_1, ISO_3_K_2_2, ISO_3_K_2_3)

# Y Numerator
ISO_3_K_3_0_VAL = 3261222600550988246488569487636662646083386001431784202863158481286248011511053074731078808919938689216061999863558  # noqa: E501
ISO_3_K_3_0 = FQ2([ISO_3_K_3_0_VAL, ISO_3_K_3_0_VAL])  # noqa: E501
ISO_3_K_3_1 = FQ2([0, 889424345604814976315064405719089812568196182208668418962679585805340366775741747653930584250892369786198727235518])  # noqa: E501
ISO_3_K_3_2 = FQ2([2668273036814444928945193217157269437704588546626005256888038757416021100327225242961791752752677109358596181706524, 1334136518407222464472596608578634718852294273313002628444019378708010550163612621480895876376338554679298090853263])  # noqa: E501
ISO_3_K_3_3 = FQ2([2816510427748580758331037284777117739799287910327449993381818688383577828123182200904113516794492504322962636245776, 0])  # noqa: E501
ISO_3_Y_NUMERATOR = (ISO_3_K_3_0, ISO_3_K_3_1, ISO_3_K_3_2, ISO_3_K_3_3)

# Y Denominator
ISO_3_K_4_0_VAL = 4002409555221667393417789825735904156556882819939007885332058136124031650490837864442687629129015664037894272559355  # noqa: E501
ISO_3_K_4_0 = FQ2([ISO_3_K_4_0_VAL, ISO_3_K_4_0_VAL])  # noqa: E501
ISO_3_K_4_1 = FQ2([0, 4002409555221667393417789825735904156556882819939007885332058136124031650490837864442687629129015664037894272559571])  # noqa: E501
ISO_3_K_4_2 = FQ2([18, 4002409555221667393417789825735904156556882819939007885332058136124031650490837864442687629129015664037894272559769])  # noqa: E501
ISO_3_K_4_3 = FQ2.one()
ISO_3_Y_DENOMINATOR = (ISO_3_K_4_0, ISO_3_K_4_1, ISO_3_K_4_2, ISO_3_K_4_3)

ISO_3_MAP_COEFFICIENTS = (ISO_3_X_NUMERATOR, ISO_3_X_DENOMINATOR, ISO_3_Y_NUMERATOR, ISO_3_Y_DENOMINATOR)  # noqa: E501

# h_eff from https://tools.ietf.org/html/draft-irtf-cfrg-hash-to-curve-06#section-8.7.2
H_EFF = 209869847837335686905080341498658477663839067235703451875306851526599783796572738804459333109033834234622528588876978987822447936461846631641690358257586228683615991308971558879306463436166481  # noqa: E501
