import requests
import argparse
import asciichartpy

API_KEY = "eeeeb065b82568309c4d4c7057836f9df5e1f7d79f9bb54c07efaa28a0d5375d"
#Should I read it from file? NVM
availableCoinList = ['0XBTC', '1ST', '1WO', 'AAC', 'ABCC', 'ABT', 'ABYSS', 'ACCN', 'ACE', 'ADA', 'ADB', 'ADH', 'ADI', 'ADL', 'ADT', 'ADX', 'AE', 'AEN', 'AERGO', 'AGI', 'AGVC', 'AID', 'AIDOC', 'AIT', 'AIX', 'ALIS', 'ALX', 'AMB', 'AMLT', 'AMM', 'AMN', 'AMO', 'ANKR', 'ANT', 'AOA', 'APIS', 'APPC', 'ARAW', 'ARBT', 'ARCT', 'ARN', 'ART', 'ARY', 'AST', 'ASTO', 'ATL', 'ATM', 'ATMI', 'ATS', 'AUC', 'AVH', 'AVT', 'AWC', 'AXPR', 'B2B', 'BAAS', 'BANCA', 'BAT', 'BAX', 'BBC', 'BBO', 'BCAP', 'BCDN', 'BCDT', 'BCH', 'BCPT', 'BDG', 'BEAT', 'BEE', 'BELA', 'BERRY', 'BETHER', 'BETR', 'BEZ', 'BFT', 'BGG', 'BIO', 'BITX', 'BIX', 'BKX', 'BLNM', 'BLOC', 'BLT', 'BLZ', 'BMC', 'BMH', 'BMX', 'BNK', 'BNN', 'BNT', 'BNTY', 'BOB', 'BOE', 'BOLT', 'BOLTT', 'BON', 'BOT', 'BOUTS', 'BOX', 'BPT', 'BPX', 'BQ', 'BQTX', 'BRAT', 'BRD', 'BSTN', 'BSV', 'BTC', 'BTCL', 'BTCM', 'BTCRED', 'BTM', 'BTMX', 'BTO', 'BTRN', 'BTU', 'BUBO', 'BUD', 'BWT', 'BZ', 'BZKY', 'BZNT', 'C20', 'CAG', 'CAN', 'CANDY', 'CAPP', 'CAR', 'CARAT', 'CARD', 'CBC', 'CBT', 'CCCX', 'CCL', 'CCO', 'CCRB', 'CCT', 'CDT', 'CDX', 'CEDEX', 'CEEK', 'CEL', 'CELR', 'CEN', 'CENNZ', 'CET', 'CHAT', 'CHP', 'CHSB', 'CHT', 'CHX', 'CJT', 'CL', 'CLN', 'CMCT', 'CMS', 'CMT', 'CND', 'CNN', 'CNX', 'COB', 'COFI', 'COIN', 'CONI', 'COSM', 'COT', 'COU', 'COV', 'COVA', 'CPAY', 'CPCH', 'CPT', 'CPY', 'CRB', 'CRDS', 'CRED', 'CREDO', 'CRO', 'CRPT', 'CRYC', 'CSEN', 'CSM', 'CSNO', 'CSP', 'CTXC', 'CUBE', 'CV', 'CVC', 'CVT', 'CXO', 'DACC', 'DADI', 'DAG', 'DAGT', 'DAI', 'DAN', 'DAOC', 'DAPS', 'DASH', 'DAT', 'DATA', 'DATX', 'DAV', 'DAX', 'DAY', 'DBET', 'DCN', 'DDD', 'DEB', 'DEC', 'DENT', 'DFXT', 'DGD', 'DGTX', 'DGX', 'DICE', 'DIG', 'DIO', 'DLT', 'DML', 'DMT', 'DNA', 'DNT', 'DOCK', 'DOGE', 'DOOH', 'DOV', 'DOW', 'DPY', 'DRG', 'DRGN', 'DROP', 'DRPU', 'DRT', 'DTH', 'DTR', 'DTRC', 'DTX', 'DXT', 'EARTH', 'EBC', 'EBTC', 'ECASH', 'ECHT', 'ECOM', 'ECTE', 'EDG', 'EDN', 'EDO', 'EDU', 'EGCC', 'EGT', 'EKO', 'EKT', 'ELEC', 'ELF', 'ELI', 'ELITE', 'ELIX', 'ELTCOIN', 'ELY', 'EMPH', 'ENGT', 'ENJ', 'ENTER', 'EOSDAC', 'EQUAL', 'ERC20', 'ERIS', 'ERO', 'ESS', 'EST', 'ESZ', 'ETBS', 'ETC', 'ETG', 'ETGP', 'ETH', 'ETHM', 'ETHOS', 'ETK', 'ETN', 'EURS', 'EVC', 'EVE', 'EVED', 'EVR', 'EVX', 'EXC', 'EXMR', 'EXRN', 'EXY', 'FACE', 'FAIRG', 'FAT', 'FDX', 'FDZ', 'FET', 'FLIK', 'FLIXX', 'FLOT', 'FLUZ', 'FND', 'FNTB', 'FOAM', 'FOTA', 'FOXT', 'FREC', 'FREE', 'FSN', 'FT', 'FTM', 'FTT', 'FTX', 'FUEL', 'FUN', 'FUNDZ', 'FXT', 'FYP', 'GAMB', 'GARD', 'GEM', 'GENE', 'GENS', 'GETX', 'GNO', 'GNT', 'GNX', 'GOOD', 'GRID', 'GRMD', 'GRX', 'GSC', 'GST', 'GTC', 'GTO', 'GUESS', 'GUP', 'GUSD', 'GVE', 'GVT', 'HAND', 'HB', 'HBT', 'HBZ', 'HEDG', 'HER', 'HERO', 'HGT', 'HIT', 'HKN', 'HMC', 'HMQ', 'HORSE', 'HPB', 'HPT', 'HQT', 'HQX', 'HSC', 'HST', 'HT', 'HUR', 'HVN', 'HYDRO', 'HYT', 'ICHX', 'ICN', 'ICON', 'IDEX', 'IDH', 'IDT', 'IDXM', 'IETH', 'IFT', 'IG', 'IHF', 'IHT', 'IMT', 'IND', 'ING', 'INS', 'INSTAR', 'INT', 'INVC', 'INX', 'INXT', 'IOST', 'IOTX', 'IPC', 'IPSX', 'IQN', 'ISR', 'ITC', 'ITL', 'ITT', 'IVY', 'IXT', 'J8T', 'JC', 'JET', 'JNT', 'JOINT', 'JSE', 'KAN', 'KBC', 'KCASH', 'KCS', 'KEY', 'KICK', 'KIN', 'KIND', 'KNC', 'KRL', 'KUE', 'KWH', 'LA', 'LALA', 'LAMB', 'LATX', 'LCS', 'LDC', 'LEDU', 'LEND', 'LEV', 'LGO', 'LIF', 'LIFE', 'LIKE', 'LINA', 'LINK', 'LION', 'LNC', 'LND', 'LOCI', 'LOCK', 'LOOM', 'LPT', 'LQDN', 'LRC', 'LST', 'LTC', 'LTO', 'LUC', 'LUN', 'LYM', 'M2O', 'MANA', 'MATIC', 'MBTX', 'MCO', 'MDA', 'MDCL', 'MDS', 'MEDX', 'MEE', 'MENLO', 'META', 'METAL', 'METM', 'MFG', 'MFT', 'MGO', 'MIC', 'MITH', 'MITX', 'MIXI', 'MKR', 'MLN', 'MNC', 'MNE', 'MNTP', 'MOAC', 'MOF', 'MOLK', 'MOT', 'MRK', 'MRPH', 'MTC', 'MTH', 'MTKN', 'MTRC', 'MTX', 'MVL', 'MWAT', 'MXAI', 'MXM', 'MYB', 'MYST', 'NANJ', 'NAS', 'NAVI', 'NBAI', 'NBC', 'NCASH', 'NCC', 'NCT', 'NEC', 'NEU', 'NEXO', 'NEXT', 'NGC', 'NIO', 'NMR', 'NOAH', 'NOBS', 'NOKU', 'NOX', 'NPER', 'NPX', 'NPXS', 'NRG', 'NRP', 'NTK', 'NULS', 'NXC', 'OAX', 'OCN', 'ODE', 'OIO', 'OKB', 'OLE', 'OLT', 'OMG', 'OMX', 'ONG', 'ONL', 'OPEN', 'OPT', 'ORBS', 'ORI', 'ORME', 'ORS', 'OSA', 'OST', 'PAL', 'PARETO', 'PASS', 'PAT', 'PAX', 'PAY', 'PCH', 'PCL', 'PCO', 'PFR', 'PHI', 'PIX', 'PKT', 'PLA', 'PLAY', 'PLBT', 'PLR', 'PLU', 'PMA', 'PMNT', 'PNT', 'POE', 'POLL', 'POLY', 'POWR', 'PPP', 'PPT', 'PRA', 'PRG', 'PRIX', 'PRO', 'PSM', 'PST', 'PTOY', 'PXG', 'PYLNT', 'PYN', 'QASH', 'QBIT', 'QCX', 'QKC', 'QNTU', 'QSP', 'QUANT', 'QUN', 'QUSD', 'R', 'RCN', 'RCT', 'RDC', 'RDD', 'REAL', 'REBL', 'REF', 'REM', 'REP', 'REQ', 'REX', 'RFR', 'RHOC', 'RIYA', 'RLC', 'RLX', 'RMESH', 'RNT', 'RNTB', 'ROBET', 'ROCK', 'ROX', 'RRC', 'RTE', 'RUFF', 'RVT', 'SAL', 'SALT', 'SAN', 'SCC', 'SCL', 'SCRL', 'SEAL', 'SEELE', 'SENC', 'SENT', 'SETH', 'SGN', 'SGR', 'SHE', 'SHIP', 'SHOW', 'SHP', 'SHPING', 'SKIN', 'SKM', 'SKRB', 'SLT', 'SMT', 'SNC', 'SNGLS', 'SNIP', 'SNM', 'SNOV', 'SNPC', 'SNS', 'SNT', 'SNTR', 'SNTVT', 'SNX', 'SOAR', 'SOC', 'SOLVE', 'SOMA', 'SPANK', 'SPF', 'SPHTX', 'SPT', 'SPX', 'SRCH', 'SRCOIN', 'SRN', 'SS', 'STAC', 'STACS', 'STAR', 'STASH', 'STC', 'STK', 'STORJ', 'STORM', 'STQ', 'STU', 'STX', 'SUB', 'SUR', 'SUSD', 'SVD', 'SWARM', 'SWC', 'SWFTC', 'SWT', 'SXDT', 'SXUT', 'TAAS', 'TBX', 'TCH', 'TCT', 'TDP', 'TDS', 'TEL', 'TEN', 'TFD', 'TFL', 'TFUEL', 'TGAME', 'TGT', 'THETA', 'THR', 'THRT', 'TIE', 'TIG', 'TIOX', 'TIX', 'TKN', 'TMT', 'TMTG', 'TNB', 'TNT', 'TOMO', 'TOPC', 'TRAC', 'TRAK', 'TRCT', 'TRDT', 'TRIO', 'TRST', 'TRUE', 'TSL', 'TTC', 'TTV', 'TUSD', 'UBC', 'UBEX', 'UBT', 'UCT', 'UDOO', 'UFR', 'UGAS', 'UGC', 'UKG', 'UP', 'UPP', 'UQC', 'USDC', 'USDS', 'USDT', 'USE', 'UTK', 'UTNP', 'UTT', 'UUU', 'VEE', 'VERI', 'VEST', 'VET', 'VIBE', 'VIDT', 'VIN', 'VIT', 'VITE', 'VIU', 'VME', 'VNX', 'VOISE', 'VRA', 'VRS', 'VSL', 'VZT', 'WAB', 'WABI', 'WAN', 'WAND', 'WAX', 'WBTC', 'WCOIN', 'WEB', 'WELL', 'WETH', 'WHEN', 'WINGS', 'WISH', 'WIZ', 'WPP', 'WPR', 'WRC', 'WT', 'WTC', 'WTL', 'WYS', 'X8X', 'XAUR', 'XBASE', 'XBB', 'XBL', 'XBX', 'XCD', 'XCLR', 'XDCE', 'XES', 'XET', 'XMX', 'XNG', 'XNK', 'XOV', 'XPAT', 'XUC', 'XYO', 'XZC', 'YEE', 'YOYOW', 'YUP', 'ZAP', 'ZCN', 'ZCO', 'ZEC', 'ZEON', 'ZIL', 'ZINC', 'ZIP', 'ZIPT', 'ZLA', 'ZMN', 'ZPR', 'ZRX', 'ZSC', 'ZT', 'ZXC']

def showCoinList():
    print(availableCoinList[:])

def argv():


    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fsym",nargs="+", help = "The crypto currency symbol (default: BTC)", default = "BTC")
    parser.add_argument("-d", "--histo", help = "Time unit. Can be minute, hour or day (default: minute)", default = "minute", choices=["minute", "hour", "day"])
  
    subparsers = parser.add_subparsers()
    parser_showtop20 = subparsers.add_parser("list", help="List all available coin")
    parser_showtop20.set_defaults(func=showCoinList)

    args = parser.parse_args()
    return args


if __name__ == "__main__":

    args = argv()

    if hasattr(args, "func") : 
        args.func()
        exit()


    histo = args.histo
    fsym = args.fsym
    tsym = "USD"
    
    if type(type(fsym) == "str"): fsym = [fsym]

    chart_config = {
        "offset" : 3,
        "height": 10,
        "colors": [
            asciichartpy.blue,
            asciichartpy.green,
            asciichartpy.red,
            asciichartpy.yellow,
            asciichartpy.magenta,
            asciichartpy.black,
            asciichartpy.cyan,
            asciichartpy.darkgray,
            asciichartpy.lightred,
            asciichartpy.lightgreen,
            asciichartpy.lightyellow,
            asciichartpy.lightblue,
            asciichartpy.lightmagenta,
            asciichartpy.white,
            asciichartpy.default,
        ]
    }

    data_list = []
    for sym in fsym:
        if sym not in availableCoinList:
            print("{} currency not valid".format(sym))
            exit()
        URL = "https://min-api.cryptocompare.com/data/v2/histo{}?fsym={}&tsym={}&limit=120&api_key={}".format(histo, sym, tsym, API_KEY)
        respond = requests.get(URL).json()

        data = respond["Data"]["Data"]
        average_list = [(x["low"] + x["high"]) / 2 for x in data]
        data_list.append(average_list)

    print(asciichartpy.plot(data_list, chart_config))





