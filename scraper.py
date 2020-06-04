import requests
import time
import json
import pandas as pd
import numpy as np
from pandas import DataFrame

id_dict = {"317":"RigWars","198":"Turfpool","11295":"FightClub","191":"TheNextBlock","159":"CryptoKiddyToys","10183":"Crypto-Versus","923":"lucky9io","578":"Ether-Alligators-Farm","144":"CryptoCelebrity","116":"EtherPrincesses","199":"CryptoPokemon","12007":"CardMaker-CAKE-Town","313":"John-Orion-Young","1544":"CryptoCocktailBar","136":"Candy-Claims","1305":"WorldConquestETH","11136":"FIS","1080":"Hashrush","1743":"Kittie-Fight","218":"Ether-Japanese-Pornstars","271":"CryptoTreasure","521":"Ether-Anthills","10177":"Balloons3D","295":"Game-Of-Blocks","240":"CryptoSolarSystem","85":"CryptoMasterpieces","10166":"%E6%8E%98%E9%87%91%E4%B9%8B%E7%8E%8B","236":"CryptoPornstars","1747":"CryptoZigzag","1539":"Etharea","118":"CryptoGit","145":"CryptoMemes","192":"Ether-Cities","53":"Crypto-Sprites","227":"Ethopia","156":"9Nine","66":"Etherions","49":"CryptoCats","300":"MyLuckyRabbit","1637":"Crypto-And-Dragons","1552":"Block-Stack-Game","1615":"Etherlambos","743":"Parsec-Frontiers","111":"CryptoMinesPRO","12746":"Creepts","814":"ProofOfOnlyDividends","1542":"WorldCryptoWar","868":"Greedy-599","1726":"AddressWars","262":"Eth10k","161":"Chronos","251":"Humanity-Cards","1006":"HODL-Earth","1528":"TrumpBingo","233":"PotPotato","209":"CryptoAlchemyio","799":"CryptoStrikers","11400":"CreasureQuest","1404":"Virtual-Lander","713":"DopeRaider","269":"BURNUP","930":"Black-Pearl","11308":"Snarkart","11102":"FortuneCats","1334":"CryptoPepes","11060":"Castle-Buidl","182":"CryptoSportStars","228":"Ethernauts","252":"CryptoPhoenixes","230":"Ethergarden","241":"Crypto-Surprise","925":"%E4%BB%99%E5%A6%96%E7%BA%B7%E4%BA%89","1012":"Blockwar","10902":"KillFish","1062":"CryptoGol","95":"Ether-Basketball","11062":"Play0x","63":"Aethiaco","333":"Ether-Warship","10232":"%C3%A0-table-","447":"MyCryptoChamp","210":"EthKing","532":"pixoarena","1168":"Founder-Cards","952":"0xfair-[Rock%E2%80%93Paper%E2%80%93Scissors]","863":"Ethercards-Online-Trading-Card-Game","859":"Star-Cards","800":"MyFish","331":"SpaceWar","183":"Ether-Quest","1792":"CryptoPets","1721":"Ethernal-Cup","967":"Okami-PK","827":"CryptoHuskies","1815":"Immortal-Player-Characters-IPCs","223":"Own-the-Day","1098":"MillionEtherWords","220":"Crypto-3-kingdom","11466":"NumberBoard","88":"WorldCryptoCup","237":"CryptoNumismat","643":"OasisFootball","840":"ETHCity","1613":"CarWarscc","10264":"CryptoFlowers","937":"Star-Block","12786":"Adventureth","234":"CityMayor","1085":"%E7%86%8A%E7%8C%AB%E7%8E%AF%E7%90%83","936":"BATTLE-FESTIVAL","41":"Crypto-All-Stars","897":"Lucky8D","11632":"COPA-2018","10069":"CryptoFollowers","557":"GOT-Dragonfarm","642":"RigCraft","315":"Darkwinds","1410":"Hodl-St","207":"Cryptogs","1722":"HiPrecious","181":"Avocado's-MMO-Clicker","11642":"Battle-Racers","117":"Treethereum","1534":"CryptoElements","11213":"%E8%A8%98%E6%86%B6%E8%99%AB","263":"Cryptoleaders","549":"SnailFarm","948":"Zomo5D","11346":"TokenWarriors","638":"gladiethers","1817":"CryptoGolio","1543":"Hashworld","289":"CryptoFamous","11631":"Crypto-Anime","1083":"Rent-Control","963":"LandSecrets","10018":"WCG-photomaster","288":"PodgarIO","102":"50-Shades-of-Ether","1031":"Etherlife-Online","615":"Magic-Academy","810":"ExoPlanets","704":"Cryptocup","934":"Crypto-Santa","908":"Cryptic-Conjure","1117":"RotoHive","12418":"World-Domination-MEOW","1714":"EtherLoot","175":"CryptoWatches","11613":"CryptoNudis","879":"ScamDog","314":"CryptoCup","841":"EtherCreaturesio","99":"IAmCryptoRich","1064":"EtherWheels","1527":"Jockey-Club","10118":"CryptoBeasties","10133":"Freaking-Awesome-Blockchain-Games-FABG","926":"EtherMage","862":"Cryptostarz","1566":"CryptoPainting","285":"YTIcons","11944":"PickFlix","668":"Produce101","1660":"GeoEth","265":"Cryptotwitchtv","911":"Last-Unicorn","378":"BitVideoOne","757":"CryptoCanvas-BETA","12400":"LTR-Light-trail-rush","62":"Crypto-Tulips","197":"Crypto-Pepe-Market","838":"CryptoCanvas","318":"Ether-Tycoon","177":"CryptoElections","901":"CryptoTomatoes","1442":"PetCraft","637":"%E5%8A%A0%E5%AF%86%E5%BE%B7%E6%89%91","225":"ChainMonsters","276":"CryptoBallers","256":"Mooncatrescue","944":"SuperCard","1076":"CryptoFights","1769":"CryptoFeather","174":"CryptoSoccer","11566":"Marketing-Director","951":"GB-from-Goal-Bonanza","748":"Fantasy-Football-Fund","275":"WorldCup","58":"Cryptoplaces","1032":"Crypto-Super-Girlfriend","147":"Crypto-Burrito","11995":"Fantasy-Coiner","1403":"Blitch-Goons","211":"CryptoRentCar","11090":"CryptoCards","11474":"RichCat","924":"Token-Tycoon","213":"Cryptopinions","73":"CryptoCuddles","226":"CryptoEmojis","188":"Crypto-Dynasty","132":"Puppychain","869":"%E4%BB%A5%E5%A4%AA%E8%81%94%E7%9B%9F","1432":"Eth-Gods","943":"%E4%B8%80%E8%B5%B7%E6%9D%A5%E8%B5%9B%E9%A9%AC","253":"CryptoConquest","247":"EthPiranha","556":"Ethereum-Chicken","169":"BOMBSwin","167":"EtherVillains","920":"GuessEther","1421":"EthMonsters","124":"CryptoStamps","137":"CryptoPizza","639":"REPOP-WORLD","216":"CryptoCars","1698":"MyCryptons","79":"CryptoArts","10593":"Cryptower","10412":"CryptoBundle","1390":"Last-Trip","940":"Retro-Block-Rob-The-Bank","170":"Crypto-Kotaku","572":"ETH-Dinosaur-Farmer","153":"CryptoT","707":"cryptostrippers","80":"EmojiBlockchain","12279":"Delight","10936":"HitTheCrypto","711":"EtherMinewar","903":"Choose-your-Force-side","321":"%E5%90%8D%E4%BA%BA%E5%A0%82","11602":"Multiprizer","719":"DCup","791":"CryptoDeads","11373":"CryptoConstellations","151":"ETHMap","10023":"Cubego","10797":"%E6%AF%94%E7%89%B9%E5%B8%9D%E5%9B%BD","94":"S0lar-System-For-Sale","10279":"MyMillions","301":"EtherOnline","1109":"BlockMagic","10877":"HIPR","108":"BitGallery","172":"EtherAthletesio","329":"alchemygod","12180":"To-Be-A-King","894":"RatScam","876":"World-FOMO","217":"CryptoPlanet","205":"EtherPaint","6":"EtherRockets","616":"Ether-World-Cup-Lion","727":"EthDice","306":"CryptonsGame","613":"CryptoSpin","215":"Myhero9","909":"Crypto-Ninja","10841":"BM-Legend-%E5%8C%BA%E5%9D%97%E4%BC%A0%E5%A5%87","938":"MythWars","105":"Crypto-Colors","229":"Crypto-Poop-Game","163":"CryptoHoroscope","68":"CryptoSpinners"}

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
                
                r = requests.get('https://dapp.review/api/dapp/' + key, headers = headers).text
                
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
        ScrapeData(id_dict, './eth_game2.csv')

