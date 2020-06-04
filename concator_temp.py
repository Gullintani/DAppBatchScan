import pandas as pd
df1 = pd.read_csv('./eth_game.csv')
df2 = pd.read_csv('./eth_game2.csv')

df = pd.concat([df1[["id", "name", "platform", "cate", "publish_date", "contract"]], df2[["id", "name", "platform", "cate", "publish_date", "contract"]]], axis=0)
df.reset_index(drop=True, inplace=True)
df.to_csv("./game.csv")
print(df.shape)