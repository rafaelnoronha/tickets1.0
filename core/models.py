from django.db import models
from django.db import connection


UF_CHOICES = [
    ('RO', 'Rondônia'),
    ('AC', 'Acre'),
    ('AM', 'Amazonas'),
    ('RR', 'Roraima'),
    ('PA', 'Pará'),
    ('AP', 'Amapá'),
    ('TO', 'Tocantins'),
    ('MA', 'Maranhão'),
    ('PI', 'Piauí'),
    ('CE', 'Ceará'),
    ('RN', 'Rio Grande do Norte'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernambuco'),
    ('AL', 'Alagoas'),
    ('SE', 'Sergipe'),
    ('BA', 'Bahia'),
    ('MG', 'Minas Gerais'),
    ('ES', 'Espírito Santo'),
    ('RJ', 'Rio de Janeiro'),
    ('SP', 'São Paulo'),
    ('PR', 'Paraná'),
    ('SC', 'Santa Catarina'),
    ('RS', 'Rio Grande do Sul'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('GO', 'Goiás'),
    ('DF', 'Distrito Federal'),
]

PAISES_CHOISES = [
    ('0132', 'AFEGANISTAO'),
    ('0153', 'ALAND, ILHAS'),
    ('0175', 'ALBANIA, REPUBLICA  DA'),
    ('0200', 'CURACAO'),
    ('0230', 'ALEMANHA'),
    ('0310', 'BURKINA FASO'),
    ('0370', 'ANDORRA'),
    ('0400', 'ANGOLA'),
    ('0418', 'ANGUILLA'),
    ('0420', 'ANTARTICA'),
    ('0434', 'ANTIGUA E BARBUDA'),
    ('0531', 'ARABIA SAUDITA'),
    ('0590', 'ARGELIA'),
    ('0639', 'ARGENTINA'),
    ('0647', 'ARMENIA, REPUBLICA DA'),
    ('0655', 'ARUBA'),
    ('0698', 'AUSTRALIA'),
    ('0728', 'AUSTRIA'),
    ('0736', 'AZERBAIJAO, REPUBLICA DO'),
    ('0779', 'BAHAMAS, ILHAS'),
    ('0809', 'BAHREIN, ILHAS'),
    ('0817', 'BANGLADESH'),
    ('0833', 'BARBADOS'),
    ('0850', 'BELARUS, REPUBLICA DA'),
    ('0876', 'BELGICA'),
    ('0884', 'BELIZE'),
    ('0906', 'BERMUDAS'),
    ('0930', 'MIANMAR (BIRMANIA)'),
    ('0973', 'BOLIVIA, ESTADO PLURINACIONAL DA'),
    ('0981', 'BOSNIA-HERZEGOVINA (REPUBLICA DA)'),
    ('0990', 'BONAIRE'),
    ('1015', 'BOTSUANA'),
    ('1023', 'BOUVET, ILHA'),
    ('1058', 'BRASIL'),
    ('1082', 'BRUNEI'),
    ('1112', 'BULGARIA, REPUBLICA DA'),
    ('1155', 'BURUNDI'),
    ('1198', 'BUTAO'),
    ('1279', 'CABO VERDE, REPUBLICA DE'),
    ('1376', 'CAYMAN, ILHAS'),
    ('1414', 'CAMBOJA'),
    ('1457', 'CAMAROES'),
    ('1490', 'CANADA'),
    ('1504', 'GUERNSEY, ILHA DO CANAL (INCLUI ALDERNEY E SARK)'),
    ('1508', 'JERSEY, ILHA DO CANAL'),
    ('1538', 'CAZAQUISTAO, REPUBLICA DO'),
    ('1546', 'CATAR'),
    ('1589', 'CHILE'),
    ('1600', 'CHINA, REPUBLICA POPULAR'),
    ('1619', 'FORMOSA (TAIWAN)'),
    ('1635', 'CHIPRE'),
    ('1651', 'COCOS(KEELING),ILHAS'),
    ('1694', 'COLOMBIA'),
    ('1732', 'COMORES, ILHAS'),
    ('1775', 'CONGO'),
    ('1830', 'COOK, ILHAS'),
    ('1872', 'COREIA (DO NORTE), REP.POP.DEMOCRATICA'),
    ('1902', 'COREIA (DO SUL), REPUBLICA DA'),
    ('1937', 'COSTA DO MARFIM'),
    ('1953', 'CROACIA (REPUBLICA DA)'),
    ('1961', 'COSTA RICA'),
    ('1988', 'COVEITE'),
    ('1988', 'KUWAIT'),
    ('1996', 'CUBA'),
    ('2003', 'CURACAO'),
    ('2291', 'BENIN'),
    ('2321', 'DINAMARCA'),
    ('2356', 'DOMINICA,ILHA'),
    ('2399', 'EQUADOR'),
    ('2402', 'EGITO'),
    ('2437', 'ERITREIA'),
    ('2445', 'EMIRADOS ARABES UNIDOS'),
    ('2453', 'ESPANHA'),
    ('2461', 'ESLOVENIA, REPUBLICA DA'),
    ('2470', 'ESLOVACA, REPUBLICA'),
    ('2496', 'ESTADOS UNIDOS'),
    ('2518', 'ESTONIA, REPUBLICA DA'),
    ('2534', 'ETIOPIA'),
    ('2550', 'FALKLAND (ILHAS MALVINAS)'),
    ('2593', 'FEROE, ILHAS'),
    ('2674', 'FILIPINAS'),
    ('2712', 'FINLANDIA'),
    ('2755', 'FRANCA'),
    ('2810', 'GABAO'),
    ('2852', 'GAMBIA'),
    ('2895', 'GANA'),
    ('2917', 'GEORGIA, REPUBLICA DA'),
    ('2925', 'ILHAS GEORGIA DO SUL E SANDWICH DO SUL'),
    ('2933', 'GIBRALTAR'),
    ('2976', 'GRANADA'),
    ('3018', 'GRECIA'),
    ('3050', 'GROENLANDIA'),
    ('3093', 'GUADALUPE'),
    ('3131', 'GUAM'),
    ('3174', 'GUATEMALA'),
    ('3212', 'GUERNSEY, ILHA DO CANAL (INCLUI ALDERNEY E SARK)'),
    ('3255', 'GUIANA FRANCESA'),
    ('3298', 'GUINE'),
    ('3310', 'GUINE-EQUATORIAL'),
    ('3344', 'GUINE-BISSAU'),
    ('3379', 'GUIANA'),
    ('3417', 'HAITI'),
    ('3433', 'ILHA HEARD E ILHAS MCDONALD'),
    ('3450', 'HONDURAS'),
    ('3514', 'HONG KONG'),
    ('3557', 'HUNGRIA, REPUBLICA DA'),
    ('3573', 'IEMEN'),
    ('3595', 'MAN, ILHA DE'),
    ('3599', 'BONAIRE'),
    ('3611', 'INDIA'),
    ('3654', 'INDONESIA'),
    ('3697', 'IRAQUE'),
    ('3727', 'IRA, REPUBLICA ISLAMICA DO'),
    ('3751', 'IRLANDA'),
    ('3794', 'ISLANDIA'),
    ('3832', 'ISRAEL'),
    ('3867', 'ITALIA'),
    ('3913', 'JAMAICA'),
    ('3930', 'JERSEY, ILHA DO CANAL'),
    ('3999', 'JAPAO'),
    ('4030', 'JORDANIA'),
    ('4111', 'KIRIBATI'),
    ('4200', 'LAOS, REP.POP.DEMOCR.DO'),
    ('4260', 'LESOTO'),
    ('4278', 'LETONIA, REPUBLICA DA'),
    ('4316', 'LIBANO'),
    ('4340', 'LIBERIA'),
    ('4383', 'LIBIA'),
    ('4405', 'LIECHTENSTEIN'),
    ('4421', 'LITUANIA, REPUBLICA DA'),
    ('4456', 'LUXEMBURGO'),
    ('4472', 'MACAU'),
    ('4499', 'MACEDONIA, ANT.REP.IUGOSLAVA'),
    ('4499', 'MACEDONIA DO NORTE'),
    ('4502', 'MADAGASCAR'),
    ('4553', 'MALASIA'),
    ('4588', 'MALAVI'),
    ('4618', 'MALDIVAS'),
    ('4642', 'MALI'),
    ('4677', 'MALTA'),
    ('4723', 'MARIANAS DO NORTE'),
    ('4740', 'MARROCOS'),
    ('4766', 'MARSHALL,ILHAS'),
    ('4774', 'MARTINICA'),
    ('4855', 'MAURICIO'),
    ('4880', 'MAURITANIA'),
    ('4885', 'MAYOTTE (ILHAS FRANCESAS)'),
    ('4898', 'MAYOTTE (ILHAS FRANCESAS)'),
    ('4936', 'MEXICO'),
    ('4944', 'MOLDAVIA, REPUBLICA DA'),
    ('4952', 'MONACO'),
    ('4979', 'MONGOLIA'),
    ('4985', 'MONTENEGRO'),
    ('4995', 'MICRONESIA'),
    ('5010', 'MONTSERRAT,ILHAS'),
    ('5053', 'MOCAMBIQUE'),
    ('5070', 'NAMIBIA'),
    ('5088', 'NAURU'),
    ('5118', 'CHRISTMAS,ILHA (NAVIDAD)'),
    ('5177', 'NEPAL'),
    ('5215', 'NICARAGUA'),
    ('5258', 'NIGER'),
    ('5282', 'NIGERIA'),
    ('5312', 'NIUE,ILHA'),
    ('5355', 'NORFOLK,ILHA'),
    ('5380', 'NORUEGA'),
    ('5428', 'NOVA CALEDONIA'),
    ('5452', 'PAPUA NOVA GUINE'),
    ('5487', 'NOVA ZELANDIA'),
    ('5517', 'VANUATU'),
    ('5568', 'OMA'),
    ('5665', 'PACIFICO,ILHAS DO (POSSESSAO DOS EUA)'),
    ('5738', 'PAISES BAIXOS (HOLANDA)'),
    ('5754', 'PALAU'),
    ('5762', 'PAQUISTAO'),
    ('5780', 'PALESTINA'),
    ('5800', 'PANAMA'),
    ('5860', 'PARAGUAI'),
    ('5894', 'PERU'),
    ('5932', 'PITCAIRN,ILHA'),
    ('5991', 'POLINESIA FRANCESA'),
    ('6033', 'POLONIA, REPUBLICA DA'),
    ('6076', 'PORTUGAL'),
    ('6114', 'PORTO RICO'),
    ('6238', 'QUENIA'),
    ('6254', 'QUIRGUIZ, REPUBLICA'),
    ('6289', 'REINO UNIDO'),
    ('6408', 'REPUBLICA CENTRO-AFRICANA'),
    ('6475', 'REPUBLICA DOMINICANA'),
    ('6602', 'REUNIAO, ILHA'),
    ('6653', 'ZIMBABUE'),
    ('6700', 'ROMENIA'),
    ('6750', 'RUANDA'),
    ('6769', 'RUSSIA, FEDERACAO DA'),
    ('6777', 'SALOMAO, ILHAS'),
    ('6858', 'SAARA OCIDENTAL'),
    ('6874', 'EL SALVADOR'),
    ('6904', 'SAMOA'),
    ('6912', 'SAMOA AMERICANA'),
    ('6955', 'SAO CRISTOVAO E NEVES,ILHAS'),
    ('6939', 'SAO BARTOLOMEU'),
    ('6971', 'SAN MARINO'),
    ('6980', 'SAO MARTINHO, ILHA DE (PARTE FRANCESA)'),
    ('6998', 'SAO MARTINHO, ILHA DE (PARTE HOLANDESA)'),
    ('7005', 'SAO PEDRO E MIQUELON'),
    ('7056', 'SAO VICENTE E GRANADINAS'),
    ('7102', 'SANTA HELENA'),
    ('7153', 'SANTA LUCIA'),
    ('7200', 'SAO TOME E PRINCIPE, ILHAS'),
    ('7285', 'SENEGAL'),
    ('7315', 'SEYCHELLES'),
    ('7358', 'SERRA LEOA'),
    ('7370', 'SERVIA'),
    ('7412', 'CINGAPURA'),
    ('7447', 'SIRIA, REPUBLICA ARABE DA'),
    ('7480', 'SOMALIA'),
    ('7501', 'SRI LANKA'),
    ('7544', 'SUAZILANDIA'),
    ('7544', 'ESSUATINI'),
    ('7552', 'SVALBARD E JAN MAYERN'),
    ('7560', 'AFRICA DO SUL'),
    ('7595', 'SUDAO'),
    ('7600', 'SUDÃO DO SUL'),
    ('7641', 'SUECIA'),
    ('7676', 'SUICA'),
    ('7706', 'SURINAME'),
    ('7722', 'TADJIQUISTAO, REPUBLICA DO'),
    ('7765', 'TAILANDIA'),
    ('7803', 'TANZANIA, REP.UNIDA DA'),
    ('7811', 'TERRAS AUSTRAIS E ANTARTICAS FRANCESAS'),
    ('7820', 'TERRITORIO BRIT.OC.INDICO'),
    ('7838', 'DJIBUTI'),
    ('7889', 'CHADE'),
    ('7919', 'TCHECA, REPUBLICA'),
    ('7951', 'TIMOR LESTE'),
    ('8001', 'TOGO'),
    ('8052', 'TOQUELAU,ILHAS'),
    ('8109', 'TONGA'),
    ('8150', 'TRINIDAD E TOBAGO'),
    ('8206', 'TUNISIA'),
    ('8230', 'TURCAS E CAICOS,ILHAS'),
    ('8249', 'TURCOMENISTAO, REPUBLICA DO'),
    ('8273', 'TURQUIA'),
    ('8281', 'TUVALU'),
    ('8311', 'UCRANIA'),
    ('8338', 'UGANDA'),
    ('8451', 'URUGUAI'),
    ('8478', 'UZBEQUISTAO, REPUBLICA DO'),
    ('8486', 'VATICANO, EST.DA CIDADE DO'),
    ('8508', 'VENEZUELA'),
    ('8583', 'VIETNA'),
    ('8630', 'VIRGENS,ILHAS (BRITANICAS)'),
    ('8664', 'VIRGENS,ILHAS (E.U.A.)'),
    ('8702', 'FIJI'),
    ('8753', 'WALLIS E FUTUNA, ILHAS'),
    ('8885', 'CONGO, REPUBLICA DEMOCRATICA DO'),
    ('8907', 'ZAMBIA'),
]


class Base(models.Model):
    """
    Modelo padrão do sistema, herdado em quase todas as tabelas.
    """

    ativo = models.BooleanField(
        verbose_name='Ativo',
        default=True,
        help_text='Se o registro está ativo ou não',
    )

    data_cadastro = models.DateField(
        verbose_name='Data do cadastro',
        auto_now_add=True,
        help_text='Data da criação do registro',
    )

    hora_cadastro = models.TimeField(
        verbose_name='Hora do cadastro',
        auto_now_add=True,
        help_text='Hora da criação do registro',
    )

    class Meta:
        abstract = True
