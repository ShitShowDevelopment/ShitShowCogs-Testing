import discord

from redbot.core import commands
from aiohttp import ClientSession

class WaifuIM(commands.Cog):
        """
        Get images from Waifu.IM API
        """

        def __init__(self, bot):
                self.bot = bot
                self.session = ClientSession = ClientSession()
                
        async def cog_unload(self) -> None:
                self.session.close()
                
        
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        async def random(self, ctx):
                """
                Get a random waifu image
                """
                
                async with ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                url = 'https://api.waifu.im/search'
                                params = {
                                        'is_nsfw': 'false'
                                }
                                
                                data = await response.json()
                                for image in data['images']:
                                        
                                        image_url = image['url']
                                        image_tag = image['tags'][0]['name']
                                        image_description = image['description'][0]
                                
                                e = discord.Embed(description='{}'.format(image_description), color=discord.Color.blue())
                                e.add_field(name='Tag', value=image_tag, inline=True)
                                e.add_field(name='Direct Link', value='[Open in Browser][{}]'.format(image_url), inline=True)
                                e.set_footer(text='Requested by {}'.format(ctx.author.display_name, icon_url=ctx.author.avatar_url))
                
                                await ctx.send(embed=e)
                                
        
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        async def tag(self, *args: input, ctx):
                """
                Get a random waifu image by tag
                
                Available tags:
                
                        - waifu
                        - maid
                        - marin-kitagawa
                        - mori-calliope
                        - raiden-shogun
                        - oppai
                        - selfies
                        - uniform
                        - kamisato-ayaka
                """
                
                async with ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                url = 'https://api.waifu.im/search'
                                params = {
                                        'included_tags': '{}'.format(args),
                                        'is_nsfw': 'false'
                                }
                                
                                data = await response.json()
                                for image in data['images']:
                                        
                                        image_url = image['url']
                                        image_tag = image['tags'][0]['name']
                                        image_description = image['description'][0]
                                
                                e = discord.Embed(description='{}'.format(image_description), color=discord.Color.blue())
                                e.add_field(name='Tag', value=image_tag, inline=True)
                                e.add_field(name='Direct Link', value='[Open in Browser][{}]'.format(image_url), inline=True)
                                e.set_footer(text='Requested by {}'.format(ctx.author.display_name, icon_url=ctx.author.avatar_url))
                
                                await ctx.send(embed=e)
                                
                
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        async def gif(self, ctx):
                """
                Get a random waifu gif
                """
                
                async with ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                url = 'https://api.waifu.im/search'
                                params = {
                                        'gif': 'true',
                                        'is_nsfw': 'false'
                                }
                                
                                data = await response.json()
                                for image in data['images']:
                                        
                                        image_url = image['url']
                                        image_tag = image['tags'][0]['name']
                                        image_description = image['description'][0]
                                
                                e = discord.Embed(description='{}'.format(image_description), color=discord.Color.blue())
                                e.add_field(name='Tag', value=image_tag, inline=True)
                                e.add_field(name='Direct Link', value='[Open in Browser][{}]'.format(image_url), inline=True)
                                e.set_footer(text='Requested by {}'.format(ctx.author.display_name, icon_url=ctx.author.avatar_url))
                
                                await ctx.send(embed=e)
                                
                
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        async def dump(self, ctx):
                """
                Dump a bunch of random waifu images
                """
                
                async with ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                url = 'https://api.waifu.im/search'
                                params = {
                                        'many': 'true',
                                        'is_nsfw': 'false'
                                }
                                
                                data = await response.json()
                                for image in data['images']:
                                        
                                        image_url = image['url']
                                        image_tag = image['tags'][0]['name']
                                        image_description = image['description'][0]
                                
                                e = discord.Embed(description='{}'.format(image_description), color=discord.Color.blue())
                                e.add_field(name='Tag', value=image_tag, inline=True)
                                e.add_field(name='Direct Link', value='[Open in Browser][{}]'.format(image_url), inline=True)
                                e.set_footer(text='Requested by {}'.format(ctx.author.display_name, icon_url=ctx.author.avatar_url))
                
                                await ctx.send(embed=e)
                                
                
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        @commands.is_nsfw()
        async def nrandom(self, ctx):
                """
                Get a random nsfw waifu image
                """
                
                async with ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                url = 'https://api.waifu.im/search'
                                params = {
                                        'is_nsfw': 'true'
                                }
                                
                                data = await response.json()
                                for image in data['images']:
                                        
                                        image_url = image['url']
                                        image_tag = image['tags'][0]['name']
                                        image_description = image['description'][0]
                                
                                e = discord.Embed(description='{}'.format(image_description), color=discord.Color.blue())
                                e.add_field(name='Tag', value=image_tag, inline=True)
                                e.add_field(name='Direct Link', value='[Open in Browser][{}]'.format(image_url), inline=True)
                                e.set_footer(text='Requested by {}'.format(ctx.author.display_name, icon_url=ctx.author.avatar_url))
                
                                await ctx.send(embed=e)
                                
                                
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        async def ntag(self, *args: input, ctx):
                """
                Get a random nsfw waifu image by tag
                
                Available tags:
                
                        - waifu
                        - maid
                        - marin-kitagawa
                        - mori-calliope
                        - raiden-shogun
                        - oppai
                        - selfies
                        - uniform
                        - kamisato-ayaka
                        - ero
                        - ass
                        - hentai
                        - milf
                        - oral
                        - paizuri
                        - ecchi
                """
                
                async with ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                url = 'https://api.waifu.im/search'
                                params = {
                                        'included_tags': '{}'.format(args),
                                        'is_nsfw': 'true'
                                }
                                
                                data = await response.json()
                                for image in data['images']:
                                        
                                        image_url = image['url']
                                        image_tag = image['tags'][0]['name']
                                        image_description = image['description'][0]
                                
                                e = discord.Embed(description='{}'.format(image_description), color=discord.Color.blue())
                                e.add_field(name='Tag', value=image_tag, inline=True)
                                e.add_field(name='Direct Link', value='[Open in Browser][{}]'.format(image_url), inline=True)
                                e.set_footer(text='Requested by {}'.format(ctx.author.display_name, icon_url=ctx.author.avatar_url))
                
                                await ctx.send(embed=e)
                                
                
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        @commands.is_nsfw()
        async def ngif(self, ctx):
                """
                Get a random nsfw waifu gif
                """
                
                async with ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                url = 'https://api.waifu.im/search'
                                params = {
                                        'gif': 'true',
                                        'is_nsfw': 'true'
                                }
                                
                                data = await response.json()
                                for image in data['images']:
                                        
                                        image_url = image['url']
                                        image_tag = image['tags'][0]['name']
                                        image_description = image['description'][0]
                                
                                e = discord.Embed(description='{}'.format(image_description), color=discord.Color.blue())
                                e.add_field(name='Tag', value=image_tag, inline=True)
                                e.add_field(name='Direct Link', value='[Open in Browser][{}]'.format(image_url), inline=True)
                                e.set_footer(text='Requested by {}'.format(ctx.author.display_name, icon_url=ctx.author.avatar_url))
                
                                await ctx.send(embed=e)
                                
                
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        @commands.is_nsfw()
        async def ndump(self, ctx):
                """
                Dump a bunch of random nsfw waifu images
                """
                
                async with ClientSession() as cs:
                        async with cs.get(url, params=params) as response:
                                
                                url = 'https://api.waifu.im/search'
                                params = {
                                        'many': 'true',
                                        'is_nsfw': 'frue'
                                }
                                
                                data = await response.json()
                                for image in data['images']:
                                        
                                        image_url = image['url']
                                        image_tag = image['tags'][0]['name']
                                        image_description = image['description'][0]
                                
                                e = discord.Embed(description='{}'.format(image_description), color=discord.Color.blue())
                                e.add_field(name='Tag', value=image_tag, inline=True)
                                e.add_field(name='Direct Link', value='[Open in Browser][{}]'.format(image_url), inline=True)
                                e.set_footer(text='Requested by {}'.format(ctx.author.display_name, icon_url=ctx.author.avatar_url))
                
                                await ctx.send(embed=e)