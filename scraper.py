import requests
import time
import json
import pandas as pd
import numpy as np
from pandas import DataFrame

id_dict = {"875":"dice2win","11604":"luck100win","11988":"PoolTogether","12889":"tkncom","13024":"MT6","11720":"Trust-Dice","12441":"Play-Royal-ETH","10714":"TossCoin","12432":"SportX","636":"All-For-One-VfSE-Lottery","10399":"Playtowinio","12847":"Virtue-Poker","12327":"smartrouletteio","783":"CasinoFair","24":"Edgeless","12324":"Paradise-Slots","10235":"DSlot","11730":"Crypto-Lottery","11914":"EtherWin-X300","12949":"8coins","12411":"Native-Gaming","11909":"Dicether","13172":"GetTheBid","13020":"SimpleLotto","12211":"Okdice","12729":"Space-Lottery","13057":"ETH-Game","212":"CoinFlip","12176":"ERC-BET","12105":"InstaLottos","12131":"People's-Casino","10878":"IntuitionToETH","12390":"EtherDie","12222":"FlipStreak","11457":"LOTEO","1465":"A21","10295":"Russian-Roulette","479":"LuckyBlock","12962":"FLIP","11135":"EthexBet","10338":"HotLot","861":"Wesley-Boumans","11247":"P3XRoll","10019":"luck100","287":"Luckyone-casino","921":"ethroll","11100":"Alpha-Play","12638":"Herocoin","10911":"Etheroulette","1154":"Bear-Escape","12353":"Versus-Trade","1119":"Ethereum-Auction","287":"Luckyone-casino","10930":"E25","921":"ethroll","12560":"6114","10725":"Goat-Clash","12011":"4SGaming","11586":"Spinwin","12804":"playNumbers","11300":"DSG","1525":"PowerEther","10615":"M%C3%B6bius-Russian-Roulette","11100":"Alpha-Play","10763":"PLinc-Hub","11272":"Someones-win-but-someone-dies","11692":"PLincSlots","12638":"Herocoin","12052":"Guess-game-ETH","1222":"ZethrGame","12165":"betbeb","10791":"Megaballio","12073":"Lucky-Strike","51":"Crypto-Sportz","10786":"Etherdiceio","12852":"Ticketh","10694":"Lucky-Stars","37":"FairGrounds","10905":"Mr-Crypto","10":"Etheroll","931":"FCK","11054":"OneBullet","898":"Fire-Lotto","12096":"YOLOrekt","1483":"DGAlphaWolf","176":"Daily-Fantasy-Sports","912":"OOGROLL","12202":"WhiteBetting","960":"Ultimate-Pyramid","1210":"Greed-for-Charity","10914":"GalaxyETH","10009":"The-Blockchain-Lottery","1529":"ETHGG","1392":"Jan-Pon-War","978":"ETHSZ","1000":"Ethnite","898":"Fire-Lotto","1084":"CryptoRockPaperScissor","1096":"DailyDivs-VIP","957":"Break-Blockeggs","1040":"F3D-Go","74":"Etherlottery","1038":"Stargate","12693":"WheelWin-ETH","1036":"EtherLottery","1423":"0xgame","912":"OOGROLL","825":"SmartDice","10243":"Burstbet","82":"Etherjackpot","10914":"GalaxyETH","12707":"EthCasinoClub","1035":"SingChina","10009":"The-Blockchain-Lottery","1529":"ETHGG","11322":"Xether","168":"CryptoWager","54":"WinSome","304":"1-Finney-Quiz","13191":"ETH2X-Multiplayer-Roulette-Gambling-Platform","1000":"Ethnite","1069":"EtheRate","10632":"7-Fun","11822":"Be-First-Lotto","12962":"FLIP","11423":"FairPlay","1400":"Qiulot3D","8":"AceBusters","12043":"MegaEther","1037":"Ether-Derby","425":"QIULOT","10957":"GetETH-BET","12559":"Lottoshi","12853":"Square-Queue","655":"%E5%9D%97%E7%8C%9C%E4%B8%96%E7%95%8C%E6%9D%AF","12942":"Mythical-Token","10092":"DoubleCoin","1536":"All-For-1","11410":"PLAYFUN","10034":"ALLBET","12021":"%E5%8C%BA%E5%9D%97%E9%BE%99%E8%99%8E%E6%96%97","12717":"TomorrowsPrice","224":"CryptoJackpot","12460":"ERCWIN","12942":"Mythical-Token","1217":"Fairdapp-Bank-Simulator","10914":"GalaxyETH","1265":"Chanceeth","1529":"ETHGG","10240":"5coins","10284":"Quasar-X","1000":"Ethnite","1079":"All-for-the-winner","962":"win777","10700":"Countdown3D","12559":"Lottoshi","11103":"MyEherGames","10239":"Wagerwar","12853":"Square-Queue","11045":"Find-The-Rabbit","141":"OurRoulette","1457":"abcLotto","11963":"EJackpot","203":"Coinrace","10009":"The-Blockchain-Lottery","1072":"Trey","1536":"All-For-1","10182":"Hit-100-million","12444":"Rock-Paper-Scissors","973":"The-Last","1078":"LuckyETH","12163":"Degens","792":"dicerollapp-Fast-Fair-Ethereum-Gaming-Dice-Roll","10821":"Luck-Vegas","12962":"FLIP","1310":"P3Daily","8":"AceBusters","10132":"JadeZ-Games","1086":"4EVER","10453":"CoinBattle","10578":"ACEDICE","12037":"Ethflipper","10005":"XPOT","1400":"Qiulot3D","12431":"BETTA","10179":"WCG-Ice-wolf-poker","1081":"LottoPI","320":"Etherwow","13196":"KingTiger","10294":"SuperDice","1294":"BOOSTO-Prelaunch","1342":"Getco8","1028":"Game-of-Bull-and-Bear","243":"LuckyETH","1513":"LuckyDay","1138":"Donut-Chain","10193":"MONOPOLY","990":"ETHlus-the-first-service-where-you-can-sell-your-cryptocurrency-higher-than-its-market-value","10925":"CrazyBet","1455":"WCG-poker","248":"Bet%C3%90app","916":"lasthero","12732":"Ethsnakes","958":"CryptoDice","10698":"Mega-Billion-Lottery","1023":"%E5%B9%B8%E8%BF%90%E9%AA%B0%E5%AD%90","620":"Jungle-Scratch","1288":"War-of-Eth","982":"NoBull","1314":"Dragon-Treasure","10289":"KeepGuess","10134":"Temple-of-ETH","12039":"ServBet","290":"EtherHilo","10690":"willwin","12125":"Aloss","1340":"HashBet","12981":"Potluck","10145":"WCG-GUN","10109":"Rush-Hour","1411":"Pipot","10556":"ETHWINS","12898":"Cryptogame","1291":"MilFold","10947":"Cryptodragons","12196":"BitSwing","13155":"3Duel","1102":"Wall-Street-Market","1799":"godgame","10971":"4OutOf5","46":"The-Ethereum-Lottery","186":"BillionTix","979":"FairDapp-Infinity","1283":"DreamGame","823":"The-Ethereum-Lottery","35":"SportCrypt","10915":"Fluky","1267":"Etherbet","13127":"ezerio","1114":"Luckynum","10973":"Tomodice","11001":"Luck100","55":"Ethdice","11333":"CrypToss","11689":"Sunday-Lottery","11519":"Winy","1357":"Unified-Bet","10238":"QuickAward","10416":"PiggyBank-ETH","11349":"SmartLotteryGame","10322":"GORGONA-Roulette","10290":"DissHacker","11188":"SoPoW","11783":"3Duel","11307":"D2Wbet","10597":"Black-or-White-balloons","1022":"LuckyBuddy","1398":"In-The-Middle","279":"EthJackpot","326":"DappSoccer","1264":"ETHBOX","10557":"Clash-Hash","703":"%E4%BB%A5%E5%A4%AA%E6%89%91%E5%85%8B","1160":"Blockgame","1041":"Ethertote","10282":"Pluto-Commy-Lotto","12135":"HyperFair","1327":"MagicSoda","1030":"Lucky-Ether","1441":"Brave3D","12449":"smartlotto","100":"To-The-Moon","1308":"GCIwin","971":"Pandemica","1089":"WizardContract","11261":"DragonTiger","12388":"deFight","11697":"%E7%BB%8F%E5%85%B8%E7%99%BE%E5%AE%B6%E4%B9%90ETH","1408":"Infinite-Stars","10099":"%E4%BB%A5%E5%A4%AA%E5%AE%88%E6%8A%A4%E7%A5%9E","10096":"Run-Away","10993":"Kryptium","1169":"Russian-roulette","1029":"Raffle-ETH-Everyday","267":"Last-Flip-Wins-Low-Risk-Bag","12177":"ETH-Magician","1214":"DGMonster","12998":"Red-Ball"}
dict_len = len(id_dict)
null = ""
false = False

def save2df(r, row_list):
    r_dict = eval(r)
    contract_list = []
    for contract in r_dict["contracts"]:
        contract_list.append(contract["address"])

    temp_list = [r_dict["id"], r_dict["title"], r_dict["platform"], r_dict["category"], r_dict["publish_date"], contract_list]
    row_list.append(temp_list)
    return

def ScrapeData(dict, save_path):
        i = 1
        e = 0
        row_list = []
        
        for key in dict:
                randsleep = np.random.randint(low = 1, high = 3, size = 1)
                time.sleep(randsleep)

                headers = {
                    "Accept": "application/json, text/plain, */*",
                    "Referer": "https://dapp.review/dapp/614/Mega-Crypto-Polis-ETH",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
                }
                try:
                        r = requests.get('https://dapp.review/api/dapp/' + key, headers = headers, timeout = 30).text
                except:
                        print("connection error")
                        e += 1
                        continue

                try:
                        save2df(r, row_list)
                        print(f"{i}/{dict_len} DApp collected: {dict[key]}")
                        i = i + 1
                except:
                        print("error occurred.")
                        e = e + 1

        row_nparray = np.array(row_list)
        columns = ["id", "name", "platform", "cate", "publish_date", "contract"]
        df = pd.DataFrame(data = row_nparray, index = None, columns= columns)
        df.to_csv(save_path)
        print(f"{i} files scrapped, {e} failed.")

if __name__ == '__main__':
        ScrapeData(id_dict, './eth_gamble.csv')

