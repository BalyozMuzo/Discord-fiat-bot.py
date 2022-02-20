import discord
from discord.ext import commands
from discord_components import *
import requests
from pycoingecko import CoinGeckoAPI
import json

cg = CoinGeckoAPI()

client = commands.Bot(command_prefix = '!')
@client.event
async def on_ready():
    print('bot hazir')
      
@client.command()
async def price(ctx, coin1:str):
   for sayfa in range(20):
    data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page="+str(sayfa)+"&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d", headers={"accept":"application/json"}).text
    data = json.loads(data)
    

    for giris in data :  
         if giris["symbol"] == coin1:
           list24h=str("1 hour   :`%")+str(round(giris["price_change_percentage_1h_in_currency"],2))+str("`")+"\n"+str("24 hour :`%")+str(round(giris["price_change_percentage_24h_in_currency"],2))+str("`")+"\n"+str("7 days   :`%")+str(round(giris["price_change_percentage_7d_in_currency"],2))+str("`")+"\n"+str("30 days  :`%")+str(round(giris["price_change_percentage_30d_in_currency"],2))+str("`")
           listmcap =str(giris["name"])+str(" Price : ")+str(giris["current_price"])+str(" $")+"\n"+str("MarketCap :`")+str(giris["market_cap"])+str("` $$$")+"\n"+str("MarketCap Rank :# `")+str(giris["market_cap_rank"])+str("`")+"\n"+str("TotalVolume :`")+str(giris["total_volume"])+str("` USD")+"\n"+str("MaxSuply :`")+str(giris["max_supply"])+str("` ")+str(coin1.upper())+"\n"+str("TotalSupply :`")+str(giris["total_supply"])+str(" `")+str(coin1.upper())+"\n"+str("CirculatingSupply :`")+str("{:,}".format(giris["circulating_supply"]))+str(" `")+str(coin1.upper())
           coin1=giris["name"]+" ("+giris["symbol"]+")"
           embed = discord.Embed(title=coin1+" price : ",description=listmcap,color=0x9208ea,Timestamp=ctx.message.created_at)
           embed.set_thumbnail(url=giris["image"])     
           embed.add_field(name="Price changes :",value=list24h,inline=True)
           embed.set_footer(text=f"Requested by - {ctx.author}",icon_url=ctx.author.avatar_url)
           await ctx.send(embed=embed)
           print(giris["current_price"])
           return
           
client.run("TOKEN")
