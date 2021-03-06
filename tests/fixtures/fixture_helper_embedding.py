import pytest
from pandas import DataFrame, Series
from numpy import array


txt_embedding = array(object=[0.00758314, -0.04057033, -0.00845575, -0.0201159 , -0.04586999,
                              0.00332502, -0.02775823, 0.05767533, 0.01903247, 0.03476274,
                              0.0288773, 0.01474632, 0.01945396, 0.06630314, 0.00538672,
                              -0.06145713, 0.02847647, 0.02201235, 0.01512327, 0.01092324,
                              -0.02756501, -0.0146731, -0.04810513, 0.03719742, -0.04777365,
                              0.03280924, 0.02882422, -0.03204942, -0.0081224, 0.02308647,
                              0.0045365, 0.04588496, 0.01917128, -0.01691195, -0.03411499,
                              -0.02355643, 0.03457421, 0.06079525, 0.01134013, -0.0256399,
                              0.01656622, -0.01038705, 0.0019108, 0.04360494, -0.03415447,
                              -0.03132271, -0.06359578, -0.04616151, 0.01020301, -0.00383239,
                              0.00178631, 0.01948975, -0.00797849, -0.01432367, -0.02442688,
                              -0.0111033, 0.00066797, 0.04571526, 0.06387474, -0.06131545,
                              -0.00127492, -0.01002222, -0.00655129, -0.01218376, 0.04722051,
                              -0.00642149, -0.0166607, 0.04706095, 0.04420083, -0.02601354,
                              0.0429102, -0.01496367, -0.02334549, 0.01212279, 0.00313755,
                              0.00860441, -0.04005159, -0.01371381, -0.04751048, 0.02760688,
                              -0.0011906, 0.02950571, 0.00158412, -0.04669149, 0.0284379,
                              -0.00884089, -0.01114245, -0.00904193, -0.05149768, -0.00663298,
                              0.05271522, 0.02928685, 0.0183193, -0.01097659, 0.02640475,
                              0.03421823, -0.1005656, 0.03081645, 0.04703048, -0.07040734,
                              -0.00719515, 0.03408591, 0.00097035, -0.00635485, 0.04968446,
                              -0.02198714, 0.04040168, -0.02746148, -0.02843263, 0.01343115,
                              -0.00610855, 0.06178593, -0.053201, 0.0276937, -0.03345978,
                              -0.00384959, -0.02278716, -0.03210494, 0.00789723, -0.06849387,
                              -0.01190054, 0.04874492, 0.01333231, -0.03151828, -0.03521387,
                              -0.02135759, -0.01115576, 0.01746067, -0.00747863, -0.04274426,
                              -0.01890128, 0.03765129, 0.01552849, 0.00751918, -0.04222542,
                              -0.02344488, -0.00030352, 0.01945224, -0.01890132, 0.03586229,
                              -0.00761239, -0.04925669, 0.03902499, 0.01237207, -0.00436865,
                              -0.06513885, 0.04770683, -0.0248727, 0.00714635, 0.00493991,
                              -0.00476898, -0.06223728, -0.00819198, 0.05924197, 0.04572555,
                              -0.05532372, -0.01389807, 0.02363005, -0.04751568, 0.01907042,
                              -0.02062205, -0.02504202, -0.01751611, 0.00061957, -0.04214758,
                              0.03657511, 0.00146617, -0.02484869, -0.03620175, 0.02113057,
                              0.00363012, 0.03767145, -0.01445784, 0.00146022, 0.0053842,
                              0.02405698, 0.03366247, -0.01576108, -0.01141369, -0.02529302,
                              0.035368, 0.030894, 0.00799014, 0.0501894, 0.02414941,
                              -0.03408464, 0.01445474, 0.02026469, 0.04683231, 0.03186164,
                              -0.00308913, 0.04095811, 0.0169592, -0.04148015, 0.00781449,
                              -0.02519212, 0.01991121, 0.01382916, 0.03322474, -0.00910845,
                              -0.07917278, 0.02990782, -0.00710899, 0.06764561, -0.05500574,
                              -0.01203308, 0.015366, 0.07354325, -0.00275073, 0.01916755,
                              0.02431012, 0.01223235, -0.0258958, -0.01981302, 0.02886396,
                              -0.01649947, 0.03573903, -0.04861635, 0.00677212, 0.03731664,
                              -0.00951139, 0.02149275, 0.00315674, -0.01146175, -0.0604165,
                              -0.02736448, -0.04783745, -0.02419003, 0.01985179, -0.02635792,
                              -0.01749933, -0.01616568, 0.04799304, -0.00486107, 0.03171677,
                              -0.03115101, 0.04178676, 0.01354185, -0.0165856, 0.01951943,
                              0.01820265, -0.02280911, 0.0389671, 0.0147406, 0.02883588,
                              0.01974467, -0.00650628, 0.01476233, 0.06904877, 0.03851929,
                              -0.01922715, -0.03963495, -0.0353441, 0.01994822, 0.05804847,
                              -0.10085574, -0.00929191, -0.02958486, -0.00833572, 0.0167295,
                              0.00241323, 0.02921159, -0.03546868, 0.04339874, 0.00458352,
                              0.03397116, 0.0250503, -0.03110229, -0.06158547, 0.03378525,
                              -0.05939225, 0.00163813, 0.00483735, 0.01041586, -0.00393123,
                              -0.00635516, 0.01800226, -0.02445067, -0.01168606, 0.02967846,
                              0.00909537, -0.02525184, 0.02959577, -0.00033257, -0.01922241,
                              -0.02130704, -0.02949895, 0.03131862, -0.0213174, -0.03090941,
                              -0.01563229, -0.01220967, 0.00922212, 0.01583056, -0.00207409,
                              -0.05704996, -0.00778104, -0.0248047, -0.04250111, 0.02263043,
                              0.00323957, 0.02344864, -0.03393135, -0.0042594, -0.03711075,
                              -0.05232705, -0.01297588, -0.06625759, -0.00935159, -0.01759462,
                              -0.00544772, 0.0024143, -0.00031241, -0.00729154, 0.05996676,
                              0.01425733, -0.00080728, 0.04041239, -0.03183956, 0.0060545,
                              0.00795601, -0.00617029, 0.03501041, -0.01169345, 0.01789562,
                              -0.02771952, 0.02746708, 0.05457193, -0.00166946, 0.00154569,
                              0.04021206, -0.01076574, 0.0020091, -0.03641248, 0.04062159,
                              -0.00405266, -0.04164627, 0.04723762, 0.01668178, 0.03462238,
                              0.00343914, 0.03758804, -0.0132026, -0.00211929, -0.04948168,
                              0.00414115, 0.01536282, 0.02668345, -0.01728784, 0.01813574,
                              -0.04614314, -0.00243735, 0.04168972, -0.04828265, 0.02900025,
                              0.02122161, -0.09605484, -0.01395928, 0.00963391, -0.01023826,
                              -0.0103722, -0.00820821, -0.03856637, -0.01388204, -0.0357706,
                              0.045965, -0.00033578, 0.01750737, -0.00664709, -0.02229693,
                              -0.02710585, 0.01987903, 0.03663435, 0.04116853, 0.00066738,
                              0.03865723, -0.01823542, -0.00385344, -0.04032779, -0.04049299,
                              0.0426104, -0.03200926, 0.00149975, -0.00164341, -0.01842648,
                              0.00627622, -0.04602464, -0.01834469, 0.02989182, 0.01255792,
                              -0.03783658, -0.03546048, -0.00227639, 0.02234917, 0.01253872,
                              -0.05473012, -0.03277816, -0.01391243, -0.03055581, -0.03414805,
                              0.00336391, 0.02118487, -0.00464859, -0.02051366, 0.01323998,
                              -0.00029194, -0.03645249, -0.05189436, -0.00721411, 0.00712745,
                              -0.04860304, 0.04439571, 0.02148942, -0.03260552, 0.02838767,
                              -0.03227391, -0.045981, 0.03344128, 0.02872719, -0.03943035,
                              -0.01319124, 0.01472563, -0.02603606, -0.0542901, 0.00707678,
                              0.01829946, -0.02260772, 0.01199408, -0.0361863, 0.04971267,
                              0.00403225, -0.0316598, -0.0269701, 0.03957063, -0.02896645,
                              0.04823492, 0.03789385, 0.01485069, -0.01079337, -0.00838999,
                              0.0001779, -0.03335852, -0.0298346, -0.03093538, 0.06557158,
                              -0.03477367, 0.02511596, -0.03036967, -0.01768584, 0.01149249,
                              -0.02969097, 0.00502657, -0.02504776, -0.06024984, 0.00966673,
                              -0.04686657, 0.01226555, 0.02581723, 0.01185327, 0.02677502,
                              -0.00297509, -0.0072193, -0.04213062, -0.00281747, -0.01784628,
                              -0.06570877, -0.0241308, 0.01200529, 0.01394668, 0.07241575,
                              0.00188935, -0.01994508, 0.0271538, -0.04867116, -0.05321804,
                              0.05179474, 0.01507803, 0.00690233, 0.01534308, -0.04679571,
                              -0.03947869, -0.0151585, -0.03220543, 0.00798052, -0.02612437,
                              -0.02669903, -0.08919559, -0.02360603, -0.03486576, 0.00186345,
                              -0.02478751, -0.0112715, 0.01283347, -0.04524445, -0.01384772,
                              0.01315738, -0.01944361, -0.0176969, -0.04788768, 0.04008672,
                              -0.00764625, 0.0003055, -0.03715469, 0.07463777, 0.0800526,
                              -0.02798378, 0.02028813, -0.0392269, 0.02556495, -0.01068487,
                              -0.01225293, 0.03785187],
                      dtype='float32')

@pytest.fixture()
def df_embedding_mess():
    return DataFrame(data=[[0.15, 0.66, 0.78],
                           [0.34, 0.12, 0.03],
                           [0.49, 0.32, 0.77]],
                     columns=['cat', 'sat', 'mat'])


@pytest.fixture()
def df_embedding_clean():
    return DataFrame(data=[['cat', [0.15, 0.34, 0.49]],
                           ['sat', [0.66, 0.12, 0.32]],
                           ['mat', [0.78, 0.03, 0.77]]],
                     columns=['word', 'embedding'])


@pytest.fixture()
def vectors():
    return {'a': [0.10, 0.55, 0.68],
            'b': [0.37, 0.60, 0.91],
            'c': [None, 0.47, None],
            'd': [0.45, 0.59, 0.95, 0.66]}


@pytest.fixture()
def vectors_cos_sim():
    return 0.972877241875058


@pytest.fixture()
def series_cos_sim():
    return Series(data=[0.648909, 1.000000, 0.938497],
                  index=['cat', 'sat', 'mat'],
                  name='embedding')


@pytest.fixture()
def similar_words():
    return {'bow': ['mat']}


@pytest.fixture()
def content_embed():
    return {'id': 'foo',
            'details_html': '<p>The quick brown fox jumps over the lazy dog.</p> '
                            '<p>I am a sentence for which you would like to get its embedding</p>',
            'details': ['The quick brown fox jumps over the lazy dog.',
                        'I am a sentence for which you would like to get its embedding'],
            'embedding': txt_embedding}



